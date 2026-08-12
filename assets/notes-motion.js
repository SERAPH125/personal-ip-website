/**
 * notes.html motion — GSAP only (transform / autoAlpha).
 * Refs: gsap-performance + gsap.matchMedia (prefers-reduced-motion).
 * Open source: https://github.com/greensock/gsap
 */
(function () {
  if (typeof gsap === "undefined") {
    document.documentElement.classList.remove("notes-gsap");
    return;
  }

  const page = document.querySelector("[data-od-id='notes-page']");
  const noteList = document.querySelector("[data-od-id='note-list']");
  if (!page || !noteList) return;

  const hero = document.querySelector("[data-od-id='notes-hero']");
  const filters = document.querySelector("[data-od-id='notes-filters']");
  const noteEmpty = document.querySelector("[data-od-id='notes-empty']");
  const noteCount = document.querySelector("[data-od-id='notes-count']");
  const noteChips = Array.prototype.slice.call(
    document.querySelectorAll("[data-note-filter]")
  );
  const foot = document.querySelector("[data-od-id='notes-foot']");

  const allowed = { all: true, agent: true, industry: true };
  const params = new URLSearchParams(location.search);
  let noteSeries = params.get("series") || "all";
  if (!allowed[noteSeries]) noteSeries = "all";

  let filterTl = null;
  let reduceMotion = false;

  function items() {
    return Array.prototype.slice.call(noteList.querySelectorAll("[data-note-series]"));
  }

  function setAnimating(on) {
    document.documentElement.classList.toggle("notes-animating", !!on);
  }

  function updateChrome(visible) {
    if (noteEmpty) noteEmpty.classList.toggle("is-visible", visible === 0);
    if (noteCount) {
      noteCount.innerHTML =
        noteSeries === "all"
          ? "共 <strong>" + visible + "</strong> 篇"
          : "筛选结果 <strong>" + visible + "</strong> 篇";
    }
    noteChips.forEach(function (c) {
      const active = c.getAttribute("data-note-filter") === noteSeries;
      c.classList.toggle("is-active", active);
      c.setAttribute("aria-pressed", active ? "true" : "false");
    });
  }

  function applyInstant() {
    if (filterTl) {
      filterTl.kill();
      filterTl = null;
    }
    setAnimating(false);
    let visible = 0;
    items().forEach(function (item) {
      const show =
        noteSeries === "all" || item.getAttribute("data-note-series") === noteSeries;
      item.hidden = !show;
      gsap.set(item, { clearProps: "opacity,visibility,transform" });
      if (show) visible += 1;
    });
    if (noteEmpty) {
      gsap.set(noteEmpty, { clearProps: "opacity,visibility,transform" });
    }
    updateChrome(visible);
  }

  function applyFiltered(animate) {
    if (!animate || reduceMotion) {
      applyInstant();
      return;
    }

    if (filterTl) {
      filterTl.kill();
      filterTl = null;
    }

    const all = items();
    const toShow = [];
    const toHide = [];
    all.forEach(function (item) {
      const show =
        noteSeries === "all" || item.getAttribute("data-note-series") === noteSeries;
      if (show) toShow.push(item);
      else toHide.push(item);
    });

    const hideNow = toHide.filter(function (el) {
      return !el.hidden;
    });
    const reveal = toShow.filter(function (el) {
      return el.hidden;
    });
    const stay = toShow.filter(function (el) {
      return !el.hidden;
    });

    setAnimating(true);
    updateChrome(toShow.length);

    filterTl = gsap.timeline({
      defaults: { ease: "power2.out" },
      onComplete: function () {
        setAnimating(false);
        filterTl = null;
      },
    });

    if (hideNow.length) {
      filterTl.to(hideNow, {
        autoAlpha: 0,
        y: -8,
        duration: 0.22,
        stagger: 0.03,
        overwrite: "auto",
      });
      filterTl.add(function () {
        hideNow.forEach(function (el) {
          el.hidden = true;
          gsap.set(el, { clearProps: "opacity,visibility,transform" });
        });
      });
    } else {
      toHide.forEach(function (el) {
        el.hidden = true;
        gsap.set(el, { clearProps: "opacity,visibility,transform" });
      });
    }

    if (reveal.length) {
      filterTl.add(function () {
        reveal.forEach(function (el) {
          el.hidden = false;
        });
        gsap.set(reveal, { autoAlpha: 0, y: 12 });
      });
      filterTl.to(reveal, {
        autoAlpha: 1,
        y: 0,
        duration: 0.32,
        stagger: 0.05,
        overwrite: "auto",
        clearProps: "transform",
      });
    }

    if (stay.length) {
      filterTl.to(
        stay,
        {
          autoAlpha: 1,
          y: 0,
          duration: 0.2,
          overwrite: "auto",
          clearProps: "transform",
        },
        "<"
      );
    }

    if (noteEmpty) {
      if (toShow.length === 0) {
        filterTl.fromTo(
          noteEmpty,
          { autoAlpha: 0, y: 6 },
          { autoAlpha: 1, y: 0, duration: 0.28, clearProps: "transform" },
          "-=0.1"
        );
      } else {
        filterTl.set(noteEmpty, { clearProps: "opacity,visibility,transform" });
      }
    }

    if (!hideNow.length && !reveal.length && stay.length) {
      setAnimating(false);
    }
  }

  function syncUrl() {
    const url = new URL(location.href);
    if (noteSeries === "all") url.searchParams.delete("series");
    else url.searchParams.set("series", noteSeries);
    history.replaceState(null, "", url.pathname + url.search + url.hash);
  }

  noteChips.forEach(function (chip) {
    chip.addEventListener("click", function () {
      noteSeries = chip.getAttribute("data-note-filter") || "all";
      syncUrl();
      applyFiltered(true);
    });
  });

  const mm = gsap.matchMedia();

  mm.add(
    {
      isMotion: "(prefers-reduced-motion: no-preference)",
      isReduce: "(prefers-reduced-motion: reduce)",
    },
    function (context) {
      const motionOk = context.conditions.isMotion && !context.conditions.isReduce;
      reduceMotion = !motionOk;

      /* Initial series state without anim (deep link) */
      applyInstant();
      document.documentElement.classList.add("notes-motion-ready");

      if (!motionOk) {
        gsap.set(
          [hero, filters, noteList, foot].filter(Boolean),
          { clearProps: "opacity,visibility,transform" }
        );
        return function () {
          if (filterTl) {
            filterTl.kill();
            filterTl = null;
          }
          setAnimating(false);
          document.documentElement.classList.remove("notes-motion-ready");
        };
      }

      const heroCopy = hero
        ? hero.querySelector("[data-od-id='notes-hero-copy']") || hero
        : null;
      const heroBits = heroCopy
        ? Array.prototype.slice.call(heroCopy.children)
        : [];
      const cards = items().filter(function (el) {
        return !el.hidden;
      });

      gsap.set(heroBits, { autoAlpha: 0, y: 14 });
      if (filters) gsap.set(filters, { autoAlpha: 0, y: 10 });
      if (cards.length) gsap.set(cards, { autoAlpha: 0, y: 16 });
      if (foot) gsap.set(foot, { autoAlpha: 0, y: 8 });

      setAnimating(true);
      const intro = gsap.timeline({
        defaults: { ease: "power2.out" },
        onComplete: function () {
          setAnimating(false);
        },
      });

      if (heroBits.length) {
        intro.to(heroBits, {
          autoAlpha: 1,
          y: 0,
          duration: 0.4,
          stagger: 0.06,
          clearProps: "transform",
        });
      }
      if (filters) {
        intro.to(
          filters,
          { autoAlpha: 1, y: 0, duration: 0.32, clearProps: "transform" },
          "-=0.22"
        );
      }
      if (cards.length) {
        intro.to(
          cards,
          {
            autoAlpha: 1,
            y: 0,
            duration: 0.36,
            stagger: 0.07,
            clearProps: "transform",
          },
          "-=0.18"
        );
      }
      if (foot) {
        intro.to(
          foot,
          { autoAlpha: 1, y: 0, duration: 0.28, clearProps: "transform" },
          "-=0.16"
        );
      }

      return function () {
        intro.kill();
        if (filterTl) {
          filterTl.kill();
          filterTl = null;
        }
        setAnimating(false);
        document.documentElement.classList.remove("notes-motion-ready");
        gsap.set(
          [heroBits, filters, cards, foot].flat().filter(Boolean),
          { clearProps: "opacity,visibility,transform" }
        );
      };
    }
  );
})();
