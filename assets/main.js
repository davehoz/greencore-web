/* GreenCore Nutrition — Animaciones globales */

document.addEventListener('DOMContentLoaded', function () {

  /* ── 1. Page-hero entrance (subpages) ─────────────────────────────────── */
  var pageHero = document.querySelector('.page-hero');
  if (pageHero) {
    var heroEls = pageHero.querySelectorAll('h1, p, .tag-esg, .eyebrow');
    heroEls.forEach(function (el, i) {
      el.style.opacity = '0';
      el.style.transform = 'translateY(20px)';
      el.style.transition = 'opacity 0.6s ease, transform 0.6s ease';
      el.style.transitionDelay = (i * 0.12) + 's';
    });
    /* Double-rAF: ensure browser renders opacity:0 before triggering */
    requestAnimationFrame(function () {
      requestAnimationFrame(function () {
        heroEls.forEach(function (el) {
          el.style.opacity = '1';
          el.style.transform = 'translateY(0)';
        });
      });
    });
  }

  /* ── 2. Scroll-triggered fade-in ──────────────────────────────────────── */
  var targets = document.querySelectorAll(
    '.section-header, .pillar, .card, .blog-card, .testimonial, .stat, ' +
    '.cards-grid > *, .pillars > *, .blog-grid > *, .testimonials-grid > *'
  );

  targets.forEach(function (el) {
    el.style.opacity = '0';
    el.style.transform = 'translateY(20px)';
    el.style.transition = 'opacity 0.55s ease, transform 0.55s ease';
  });

  var observer = new IntersectionObserver(function (entries) {
    entries.forEach(function (entry) {
      if (entry.isIntersecting) {
        var parent = entry.target.parentElement;
        var siblings = Array.from(parent.children).filter(function (c) {
          return c.style.opacity === '0';
        });
        var idx = siblings.indexOf(entry.target);
        var delay = Math.min(idx * 0.08, 0.4);
        entry.target.style.transitionDelay = delay + 's';
        entry.target.style.opacity = '1';
        entry.target.style.transform = 'translateY(0)';
        observer.unobserve(entry.target);
      }
    });
  }, { threshold: 0.1 });

  /* Double-rAF: ensures browser paints opacity:0 before observation starts */
  requestAnimationFrame(function () {
    requestAnimationFrame(function () {
      targets.forEach(function (el) { observer.observe(el); });
    });
  });

});
