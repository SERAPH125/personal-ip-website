/* Shared interactions for content hub — outbound Douyin/B站/YouTube */
(function () {
  const seriesMeta = {
    agent: "Agent 实战",
    observe: "模型观察",
    aivideo: "AI 视频",
    industry: "行业观察"
  };

  function qs(sel, root) {
    return (root || document).querySelector(sel);
  }
  function qsa(sel, root) {
    return Array.from((root || document).querySelectorAll(sel));
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
        return;
      }
      e.preventDefault();
      showToast("「" + name + "」链接暂不可用");
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

  /* Shared series filter — works and notes + shareable ?series= deep link */
  qsa("[data-series-filter-root]").forEach(function (filterRoot) {
    const chips = qsa("[data-series-filter]", filterRoot);
    const items = qsa("[data-filter-item]", filterRoot);
    const empty = qs("[data-filter-empty]", filterRoot);
    const resultCount = qs("[data-filter-count]", filterRoot);
    const unit = filterRoot.getAttribute("data-filter-unit") || "内容";
    const params = new URLSearchParams(location.search);
    let seriesFilter = params.get("series") || "all";
    if (seriesFilter !== "all" && !seriesMeta[seriesFilter]) seriesFilter = "all";
    if (!chips.some(function (chip) {
      return chip.getAttribute("data-series-filter") === seriesFilter;
    })) seriesFilter = "all";

    function applyFilters() {
      let visible = 0;
      items.forEach(function (item) {
        const show = seriesFilter === "all" || item.getAttribute("data-series") === seriesFilter;
        item.hidden = !show;
        if (show) visible += 1;
      });
      if (empty) empty.classList.toggle("is-visible", visible === 0);
      if (resultCount) {
        const label = seriesFilter === "all" ? "全部" : seriesMeta[seriesFilter];
        const measure = unit === "作品" ? " 条作品" : unit === "文章" ? " 篇文章" : " 条" + unit;
        resultCount.textContent = label + " · " + visible + measure;
      }
      chips.forEach(function (c) {
        const active = c.getAttribute("data-series-filter") === seriesFilter;
        c.classList.toggle("is-active", active);
        c.setAttribute("aria-pressed", active ? "true" : "false");
      });
    }

    chips.forEach(function (chip) {
      chip.addEventListener("click", function () {
        seriesFilter = chip.getAttribute("data-series-filter") || "all";
        const url = new URL(location.href);
        if (seriesFilter === "all") url.searchParams.delete("series");
        else url.searchParams.set("series", seriesFilter);
        history.replaceState(null, "", url.pathname + url.search + url.hash);
        applyFilters();
      });
    });
    applyFilters();
  });
})();
