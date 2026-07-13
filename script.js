(() => {
  const root = document.documentElement;
  const year = document.querySelector('[data-year]');
  const workflow = document.querySelector('[data-workflow]');
  const reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)');

  if (year) year.textContent = String(new Date().getFullYear());

  if (reduceMotion.matches) {
    document.querySelectorAll('.reveal').forEach((element) => {
      element.classList.add('is-visible');
    });
    root.style.setProperty('--progress', '1');
    return;
  }

  const revealObserver = new IntersectionObserver(
    (entries, observer) => {
      entries.forEach((entry) => {
        if (!entry.isIntersecting) return;
        entry.target.classList.add('is-visible');
        observer.unobserve(entry.target);
      });
    },
    { rootMargin: '0px 0px -12% 0px', threshold: 0.12 },
  );

  document.querySelectorAll('.reveal').forEach((element) => revealObserver.observe(element));

  let frameRequested = false;

  const updateWorkflowProgress = () => {
    frameRequested = false;
    if (!workflow) return;

    const rect = workflow.getBoundingClientRect();
    const viewportAnchor = window.innerHeight * 0.58;
    const progress = Math.min(1, Math.max(0, (viewportAnchor - rect.top) / rect.height));
    root.style.setProperty('--progress', progress.toFixed(3));
  };

  const requestProgressUpdate = () => {
    if (frameRequested) return;
    frameRequested = true;
    window.requestAnimationFrame(updateWorkflowProgress);
  };

  window.addEventListener('scroll', requestProgressUpdate, { passive: true });
  window.addEventListener('resize', requestProgressUpdate);
  requestProgressUpdate();
})();
