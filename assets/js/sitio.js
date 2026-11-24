// ARCO · sitio web v2.0 — navegación adaptable y controles de video
(function () {
  'use strict';

  // Menú en celulares
  var btn = document.querySelector('.menu-btn');
  var nav = document.getElementById('menu-principal');
  if (btn && nav) {
    btn.addEventListener('click', function () {
      var abierto = nav.classList.toggle('abierto');
      btn.setAttribute('aria-expanded', abierto ? 'true' : 'false');
    });
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && nav.classList.contains('abierto')) {
        nav.classList.remove('abierto');
        btn.setAttribute('aria-expanded', 'false');
        btn.focus();
      }
    });
  }

  // Botones «Ver» y «Pantalla completa» asociados a un <video>.
  // Los videos usan preload="none": no se descarga nada hasta que la persona lo pide.
  function videoDe(el) {
    return document.getElementById(el.getAttribute('data-video'));
  }

  document.querySelectorAll('[data-accion="reproducir"]').forEach(function (b) {
    b.addEventListener('click', function (e) {
      var v = videoDe(b);
      if (!v) return; // sin JS o sin video, el enlace funciona como ancla normal
      e.preventDefault();
      v.scrollIntoView({ behavior: 'smooth', block: 'center' });
      var p = v.play();
      if (p && typeof p.catch === 'function') p.catch(function () { v.focus(); });
    });
  });

  document.querySelectorAll('[data-accion="pantalla"]').forEach(function (b) {
    var v = videoDe(b);
    var fs = v && (v.requestFullscreen || v.webkitRequestFullscreen || v.webkitEnterFullscreen);
    if (!fs) { b.hidden = true; return; }
    b.addEventListener('click', function () {
      try {
        var r = fs.call(v);
        if (r && typeof r.catch === 'function') r.catch(function () {});
        if (v.paused) { var p = v.play(); if (p && p.catch) p.catch(function () {}); }
      } catch (err) { /* el navegador no permite pantalla completa */ }
    });
  });

  // Al reproducir un video se pausa el otro
  var videos = document.querySelectorAll('video');
  videos.forEach(function (v) {
    v.addEventListener('play', function () {
      videos.forEach(function (o) { if (o !== v && !o.paused) o.pause(); });
    });
  });
})();
