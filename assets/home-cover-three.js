/**
 * Home cover depth grid — Three.js r160 UMD (vendored)
 * Behind featured cover only; pointer-events none; outbound click unchanged.
 * Open-source: https://github.com/mrdoob/three.js
 * Note: r161+ dropped build/three.min.js; use assets/vendor/three.min.js
 */
(function () {
  "use strict";

  var THREE = window.THREE;
  var media = document.querySelector('[data-od-id="latest-video"]');
  var canvas = document.querySelector('[data-od-id="home-cover-three"]');
  if (!THREE || !media || !canvas) return;

  var reduceMotion = false;
  try {
    reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  } catch (_) {}

  var renderer;
  try {
    renderer = new THREE.WebGLRenderer({
      canvas: canvas,
      antialias: true,
      alpha: true,
      powerPreference: "low-power",
    });
  } catch (_) {
    media.classList.add("hero-media--no-webgl");
    return;
  }

  if (!renderer.getContext()) {
    media.classList.add("hero-media--no-webgl");
    renderer.dispose();
    return;
  }

  renderer.setClearColor(0x000000, 0);
  renderer.setPixelRatio(Math.min(window.devicePixelRatio || 1, 1.5));
  renderer.outputColorSpace = THREE.SRGBColorSpace;

  var scene = new THREE.Scene();
  var camera = new THREE.PerspectiveCamera(42, 1, 0.1, 60);
  camera.position.set(0, 3.6, 5.8);
  camera.lookAt(0, 0, 0);

  var root = new THREE.Group();
  scene.add(root);

  function tintGrid(helper, opacity) {
    var mats = Array.isArray(helper.material) ? helper.material : [helper.material];
    mats.forEach(function (m) {
      m.transparent = true;
      m.opacity = opacity;
      m.depthWrite = false;
    });
  }

  // Cobalt + muted lines — readable ring around inset cover
  var gridNear = new THREE.GridHelper(14, 28, 0x2f62f0, 0x7a8799);
  tintGrid(gridNear, 0.72);
  root.add(gridNear);

  var gridFar = new THREE.GridHelper(18, 18, 0x3d6ef5, 0x9aa5b4);
  gridFar.position.y = -0.35;
  tintGrid(gridFar, 0.45);
  root.add(gridFar);

  // Slight pitch so grid lines read in the exposed border, not only under cover
  root.rotation.x = -0.22;
  camera.position.set(0, 4.2, 5.2);
  camera.lookAt(0, -0.2, 0);

  var pointer = { x: 0, y: 0, tx: 0, ty: 0 };
  var running = false;
  var raf = 0;
  var disposed = false;

  function resize() {
    var w = media.clientWidth;
    var h = media.clientHeight;
    if (w < 2 || h < 2) return;
    renderer.setSize(w, h, false);
    camera.aspect = w / h;
    camera.updateProjectionMatrix();
  }

  function paint(t) {
    if (disposed) return;
    var time = (t || 0) * 0.001;
    pointer.x += (pointer.tx - pointer.x) * 0.08;
    pointer.y += (pointer.ty - pointer.y) * 0.08;

    root.rotation.x = -0.22 + pointer.y * 0.12;
    root.rotation.y = pointer.x * 0.18;
    if (!reduceMotion) {
      root.position.y = Math.sin(time * 0.35) * 0.04;
      gridNear.position.x = Math.sin(time * 0.12) * 0.08;
    }

    renderer.render(scene, camera);
  }

  function loop(t) {
    if (!running || disposed) return;
    paint(t);
    raf = window.requestAnimationFrame(loop);
  }

  function start() {
    if (running || disposed || reduceMotion) return;
    running = true;
    raf = window.requestAnimationFrame(loop);
  }

  function stop() {
    running = false;
    if (raf) window.cancelAnimationFrame(raf);
    raf = 0;
  }

  function onPointer(e) {
    var rect = media.getBoundingClientRect();
    if (!rect.width || !rect.height) return;
    pointer.tx = ((e.clientX - rect.left) / rect.width) * 2 - 1;
    pointer.ty = -(((e.clientY - rect.top) / rect.height) * 2 - 1);
  }

  function onLeave() {
    pointer.tx = 0;
    pointer.ty = 0;
  }

  function onVisibility() {
    if (document.hidden) stop();
    else if (!reduceMotion) start();
    else paint(0);
  }

  var ro = null;
  if (typeof ResizeObserver !== "undefined") {
    ro = new ResizeObserver(function () {
      resize();
      paint(0);
    });
    ro.observe(media);
  } else {
    window.addEventListener("resize", function () {
      resize();
      paint(0);
    });
  }

  media.addEventListener("pointermove", onPointer, { passive: true });
  media.addEventListener("pointerleave", onLeave);
  document.addEventListener("visibilitychange", onVisibility);

  resize();
  paint(0);
  if (!reduceMotion && !document.hidden) start();

  window.addEventListener(
    "pagehide",
    function () {
      if (disposed) return;
      disposed = true;
      stop();
      document.removeEventListener("visibilitychange", onVisibility);
      media.removeEventListener("pointermove", onPointer);
      media.removeEventListener("pointerleave", onLeave);
      if (ro) ro.disconnect();
      gridNear.geometry.dispose();
      gridFar.geometry.dispose();
      var mats = []
        .concat(gridNear.material)
        .concat(gridFar.material)
        .filter(Boolean);
      mats.forEach(function (m) {
        if (m && m.dispose) m.dispose();
      });
      renderer.dispose();
    },
    { once: true }
  );
})();
