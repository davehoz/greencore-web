/* GreenCore Nutrition — Animaciones globales */

/* ── 1. Page-hero entrance (subpages) ───────────────────────────────────── */
document.addEventListener('DOMContentLoaded', function () {

  /* Animate .page-hero children on load */
  var pageHero = document.querySelector('.page-hero');
  if (pageHero) {
    var els = pageHero.querySelectorAll('h1, p, .tag-esg, .eyebrow');
    els.forEach(function (el, i) {
      el.style.opacity = '0';
      el.style.transform = 'translateY(20px)';
      el.style.transition = 'opacity 0.6s ease, transform 0.6s ease';
      el.style.transitionDelay = (i * 0.12) + 's';
      setTimeout(function () {
        el.style.opacity = '1';
        el.style.transform = 'translateY(0)';
      }, 30);
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
        /* Stagger siblings in the same parent */
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
  }, { threshold: 0.12 });

  targets.forEach(function (el) { observer.observe(el); });

});
