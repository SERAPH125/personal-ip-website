/* Shared interactions for content hub — outbound Douyin/B站/YouTube */
(function () {
  const seriesMeta = {
    agent: "Agent 实战",
    observe: "模型观察",
    aivideo: "AI 视频"
  };

  /* Real Douyin share links (南吴 NANWU) — covers scraped via ego-browser */
  const videos = [
    {
      id: "v1",
      title: "Codex 的 5 级用法：从一条指令到完整目标",
      platform: "douyin",
      platformLabel: "抖音",
      duration: "短视频",
      series: "Agent 实战",
      seriesSlug: "agent",
      cover: "assets/covers/codex-5levels.jpg",
      url: "https://v.douyin.com/YIaxfdnPQeQ/",
      hook: "生产系统，不只是 Token",
      desc: "18 天跑了 400 个任务后的分级法：第一级交指令，第五级交完整目标。真正拉开差距的是能否把 Codex 变成可持续工作的生产系统。"
    },
    {
      id: "v2",
      title: "Fable 5 来了：Mythos 戴上「安全锁」的版本",
      platform: "douyin",
      platformLabel: "抖音",
      duration: "短视频",
      series: "模型观察",
      seriesSlug: "observe",
      cover: "assets/covers/fable-5.jpg",
      url: "https://v.douyin.com/sAoQQVUBtaM/",
      hook: "同底模型，日常场景 95%",
      desc: "两个月前强到不敢公开发布的 Mythos，今天以 Fable 5 登场——戴上安全锁的同底模型，日常场景能力高度一致。"
    },
    {
      id: "v3",
      title: "AI 短片没代入感？两个分镜思维让画面自己说话",
      platform: "douyin",
      platformLabel: "抖音",
      duration: "短视频",
      series: "AI 视频",
      seriesSlug: "aivideo",
      cover: "assets/covers/ai-storyboard.jpg",
      url: "https://v.douyin.com/-Hud8DcvLYs/",
      hook: "角色一致 · 视角 · 提示词",
      desc: "角色一致性、视角选择、提示词优化——把 AI 短片代入感的核心逻辑讲清楚。"
    },
    {
      id: "v4",
      title: "Seedance 2.0 四种玩法，附提示词",
      platform: "douyin",
      platformLabel: "抖音",
      duration: "短视频",
      series: "AI 视频",
      seriesSlug: "aivideo",
      cover: "assets/covers/seedance-2.jpg",
      url: "https://v.douyin.com/zrrR1ARupU4/",
      hook: "多模态 · 唇同步 · 动作",
      desc: "一条讲透 Seedance 2.0：多模态参考、精准唇同步、流畅动作生成——零门槛做大片向工作流。"
    }
  ];

  window.HubData = { videos, seriesMeta };

  function qs(sel, root) {
    return (root || document).querySelector(sel);
  }
  function qsa(sel, root) {
    return Array.from((root || document).querySelectorAll(sel));
  }
  function esc(s) {
    return String(s || "").replace(/&/g, "&amp;").replace(/"/g, "&quot;").replace(/</g, "&lt;");
  }

  /* Mobile nav */
  const toggle = qs("[data-od-id='nav-toggle']");
  const links = qs("[data-od-id='nav-links']");
  if (toggle && links) {
    function setNavOpen(open) {
      links.classList.toggle("is-open", open);
      toggle.setAttribute("aria-expanded", open ? "true" : "false");
      toggle.setAttribute("aria-label", open ? "关闭菜单" : "打开菜单");
    }
    toggle.addEventListener("click", function () {
      setNavOpen(!links.classList.contains("is-open"));
    });
    links.addEventListener("click", function (event) {
      if (event.target.closest("a")) setNavOpen(false);
    });
  }

  /* Follow modal — focus return + basic trap */
  const backdrop = qs("[data-od-id='follow-modal']");
  let followReturnFocus = null;
  function focusablesIn(root) {
    return qsa("a[href], button:not([disabled]), [tabindex]:not([tabindex='-1'])", root).filter(function (el) {
      return !el.hasAttribute("disabled") && el.getAttribute("aria-hidden") !== "true";
    });
  }
  function openFollow() {
    if (!backdrop) return;
    followReturnFocus = document.activeElement;
    backdrop.classList.add("is-open");
    backdrop.setAttribute("aria-hidden", "false");
    const first = qs(".platform-link:not(.platform-link--pending)", backdrop) || qs(".platform-link", backdrop);
    if (first) first.focus();
  }
  function closeFollow() {
    if (!backdrop) return;
    backdrop.classList.remove("is-open");
    backdrop.setAttribute("aria-hidden", "true");
    if (followReturnFocus && typeof followReturnFocus.focus === "function") {
      followReturnFocus.focus();
    }
    followReturnFocus = null;
  }
  qsa("[data-action='follow']").forEach(function (el) {
    el.addEventListener("click", function (e) {
      e.preventDefault();
      openFollow();
    });
  });
  if (backdrop) {
    backdrop.addEventListener("click", function (e) {
      if (e.target === backdrop) closeFollow();
    });
    const closer = qs("[data-action='close-follow']", backdrop);
    if (closer) closer.addEventListener("click", closeFollow);
    document.addEventListener("keydown", function (e) {
      if (!backdrop.classList.contains("is-open")) return;
      if (e.key === "Escape") {
        closeFollow();
        return;
      }
      if (e.key !== "Tab") return;
      const nodes = focusablesIn(backdrop);
      if (!nodes.length) return;
      const first = nodes[0];
      const last = nodes[nodes.length - 1];
      if (e.shiftKey && document.activeElement === first) {
        e.preventDefault();
        last.focus();
      } else if (!e.shiftKey && document.activeElement === last) {
        e.preventDefault();
        first.focus();
      }
    });
  }

  /* Outbound toast + real link open */
  const toast = qs("[data-od-id='toast']");
  let toastTimer;
  function showToast(msg) {
    if (!toast) return;
    toast.textContent = msg;
    toast.classList.add("is-on");
    clearTimeout(toastTimer);
    toastTimer = setTimeout(function () {
      toast.classList.remove("is-on");
    }, 2200);
  }

  qsa("[data-platform-out]").forEach(function (el) {
    el.addEventListener("click", function (e) {
      const href = el.getAttribute("href");
      const name = el.getAttribute("data-platform-out");
      if (href && href !== "#" && !href.startsWith("javascript:")) {
        showToast("正在打开「" + name + "」…");
        closeFollow();
        return;
      }
      e.preventDefault();
      showToast("「" + name + "」链接暂不可用");
      closeFollow();
    });
  });

  function bindVideoOutbound(root) {
    qsa("[data-video-out]", root || document).forEach(function (el) {
      if (el.__hubVideoOutBound) return;
      el.__hubVideoOutBound = true;
      el.addEventListener("click", function (e) {
        const platform = el.getAttribute("data-video-out") || "平台";
        const title = el.getAttribute("data-video-title") || "该视频";
        const href = el.getAttribute("href");
        if (href && href !== "#" && !href.startsWith("javascript:")) {
          showToast("前往「" + platform + "」观看「" + title + "」");
          /* allow default: open real URL in new tab (target=_blank) */
          return;
        }
        e.preventDefault();
        showToast("「" + title + "」的「" + platform + "」链接暂不可用");
      });
    });
  }
  bindVideoOutbound();

  /* Cover load error → quiet fallback (no broken-image icon) */
  function bindCoverFallback(root) {
    qsa("[data-cover-fallback]", root || document).forEach(function (img) {
      if (img.__hubCoverBound) return;
      img.__hubCoverBound = true;
      img.addEventListener("error", function onErr() {
        img.removeEventListener("error", onErr);
        const shell = document.createElement("div");
        shell.className = "cover-fallback";
        shell.setAttribute("aria-hidden", "true");
        shell.textContent = "封面暂不可用";
        if (img.parentNode) img.parentNode.replaceChild(shell, img);
      });
    });
  }
  bindCoverFallback();

  /* Works filter — platform chips + optional ?series= slug */
  const grid = qs("[data-od-id='works-grid']");
  if (grid) {
    const chips = qsa("[data-filter]");
    const empty = qs("[data-od-id='filter-empty']");
    const banner = qs("[data-od-id='series-banner']");
    const bannerLabel = qs("[data-od-id='series-banner-label']");
    const params = new URLSearchParams(location.search);
    let platformFilter = params.get("platform") || "all";
    let seriesFilter = params.get("series") || "";
    if (seriesFilter && !seriesMeta[seriesFilter]) seriesFilter = "";

    function applyFilters() {
      let visible = 0;
      qsa("[data-platform]", grid).forEach(function (card) {
        const platformOk = platformFilter === "all" || card.getAttribute("data-platform") === platformFilter;
        const seriesOk = !seriesFilter || card.getAttribute("data-series") === seriesFilter;
        const show = platformOk && seriesOk;
        card.hidden = !show;
        if (show) visible += 1;
      });
      if (empty) empty.classList.toggle("is-visible", visible === 0);
      chips.forEach(function (c) {
        const active = c.getAttribute("data-filter") === platformFilter;
        c.classList.toggle("is-active", active);
        c.setAttribute("aria-pressed", active ? "true" : "false");
      });
      if (banner) {
        banner.classList.toggle("is-on", !!seriesFilter);
        if (bannerLabel && seriesFilter) bannerLabel.textContent = seriesMeta[seriesFilter] || seriesFilter;
      }
    }

    chips.forEach(function (chip) {
      chip.addEventListener("click", function () {
        platformFilter = chip.getAttribute("data-filter") || "all";
        applyFilters();
      });
    });

    const mo = new MutationObserver(function () {
      applyFilters();
    });
    mo.observe(grid, { childList: true });
    applyFilters();
  }

  /* Notes list — series chips + ?series= deep link
     When notes.html loads GSAP motion (`html.notes-gsap`), assets/notes-motion.js owns filter + intro. */
  const noteList = qs("[data-od-id='note-list']");
  if (noteList && !document.documentElement.classList.contains("notes-gsap")) {
    const noteChips = qsa("[data-note-filter]");
    const noteEmpty = qs("[data-od-id='notes-empty']");
    const noteCount = qs("[data-od-id='notes-count']");
    const noteParams = new URLSearchParams(location.search);
    let noteSeries = noteParams.get("series") || "all";
    const allowedNoteSeries = { all: true, agent: true, industry: true };
    if (!allowedNoteSeries[noteSeries]) noteSeries = "all";

    function applyNoteFilter() {
      let visible = 0;
      qsa("[data-note-series]", noteList).forEach(function (item) {
        const show = noteSeries === "all" || item.getAttribute("data-note-series") === noteSeries;
        item.hidden = !show;
        if (show) visible += 1;
      });
      if (noteEmpty) noteEmpty.classList.toggle("is-visible", visible === 0);
      if (noteCount) {
        noteCount.innerHTML = noteSeries === "all"
          ? "共 <strong>" + visible + "</strong> 篇"
          : "筛选结果 <strong>" + visible + "</strong> 篇";
      }
      noteChips.forEach(function (c) {
        const active = c.getAttribute("data-note-filter") === noteSeries;
        c.classList.toggle("is-active", active);
        c.setAttribute("aria-pressed", active ? "true" : "false");
      });
    }

    noteChips.forEach(function (chip) {
      chip.addEventListener("click", function () {
        noteSeries = chip.getAttribute("data-note-filter") || "all";
        const url = new URL(location.href);
        if (noteSeries === "all") url.searchParams.delete("series");
        else url.searchParams.set("series", noteSeries);
        history.replaceState(null, "", url.pathname + url.search + url.hash);
        applyNoteFilter();
      });
    });

    applyNoteFilter();
  }

  /* watch.html is retired (dead_file): no hydrate; site never links here */

  /* Render works grid — outbound to platform (no watch.html) */
  const worksMount = qs("[data-od-id='works-grid'][data-render='auto']");
  if (worksMount) {
    worksMount.innerHTML = videos
      .map(function (v) {
        const thumb = v.cover
          ? '<img class="video-cover" src="' + esc(v.cover) + '" alt="" width="640" height="360" loading="lazy" decoding="async" data-cover-fallback />'
          : '<div class="cover-fallback" aria-hidden="true">封面暂不可用</div>';
        return (
          '<a class="video-card" data-od-id="video-card-' +
          v.id +
          '" data-platform="' +
          v.platform +
          '" data-series="' +
          v.seriesSlug +
          '" href="' +
          esc(v.url) +
          '" target="_blank" rel="noopener noreferrer" data-video-out="' +
          esc(v.platformLabel) +
          '" data-video-title="' +
          esc(v.title) +
          '" aria-label="在' +
          esc(v.platformLabel) +
          "观看：" +
          esc(v.title) +
          '">' +
          '<div class="video-card__thumb">' +
          thumb +
          '<span class="out-badge">' +
          esc(v.platformLabel) +
          "</span></div>" +
          '<div class="video-card__body"><div class="video-card__title">' +
          esc(v.title) +
          "</div>" +
          '<div class="video-card__meta"><span class="platform-dot" data-p="' +
          v.platform +
          '"></span>' +
          esc(v.series) +
          " · " +
          esc(v.hook) +
          "</div></div></a>"
        );
      })
      .join("");
    bindVideoOutbound(worksMount);
    bindCoverFallback(worksMount);
  }
})();
