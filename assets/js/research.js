/* Shared behavior. No framework, network service or HTML content injection. */
(() => {
  'use strict';
  const root = document.querySelector('.aix-research');
  const storageKey = 'aix-research-language';
  const params = new URLSearchParams(location.search);
  let saved;
  try { saved = localStorage.getItem(storageKey); } catch (_) { /* file/private mode */ }
  let language = ['en', 'ko'].includes(params.get('lang')) ? params.get('lang') : saved === 'ko' ? 'ko' : 'en';
  const isEmbedded = params.get('embed') === '1';
  if (isEmbedded) root.classList.add('embedded');
  function applyLanguage(lang) {
    language = lang;
    document.documentElement.lang = lang;
    root.querySelectorAll('[data-lang]').forEach(node => { node.hidden = node.dataset.lang !== lang; });
    root.querySelectorAll('[data-language]').forEach(button => button.setAttribute('aria-pressed', String(button.dataset.language === lang)));
    root.querySelectorAll('[data-alt-en]').forEach(img => { img.alt = img.dataset[lang === 'ko' ? 'altKo' : 'altEn']; });
    root.querySelectorAll('[data-label-en]').forEach(node => node.setAttribute('aria-label', node.dataset[lang === 'ko' ? 'labelKo' : 'labelEn']));
    root.querySelectorAll('a[data-local]').forEach(link => {
      const url = new URL(link.getAttribute('href'), location.href);
      url.searchParams.set('lang', lang);
      if (isEmbedded) url.searchParams.set('embed', '1');
      link.setAttribute('href', url.pathname.split('/').pop() + url.search + url.hash);
    });
    try { localStorage.setItem(storageKey, lang); } catch (_) { /* optional persistence */ }
    try {
      const url = new URL(location.href); url.searchParams.set('lang', lang);
      history.replaceState(null, '', url);
    } catch (_) { /* direct file access may disallow history writes */ }
  }
  root.querySelectorAll('[data-language]').forEach(button => button.addEventListener('click', () => applyLanguage(button.dataset.language)));
  const menu = root.querySelector('.mobile-menu');
  const nav = root.querySelector('.js-nav');
  if (menu && nav) {
    nav.classList.remove('open');
    menu.setAttribute('aria-expanded', 'false');
    menu.addEventListener('click', () => {
      const opened = nav.classList.toggle('open'); menu.setAttribute('aria-expanded', String(opened));
    });
  }
  const frames = new Map([...root.querySelectorAll('figure[data-demo]')].map(figure => [figure, figure.querySelector('.media-frame')]));
  function playback(figure, playing) {
    const frame = frames.get(figure);
    const image = frame.querySelector('img');
    const video = frame.querySelector('video');
    const button = frame.querySelector('[data-play]');
    if (!button) return;
    if (video) {
      if (playing) video.play().catch(() => { if (video.paused) playback(figure, false); });
      else video.pause();
    } else image.src = playing ? button.dataset.play : image.dataset.poster;
    button.setAttribute('aria-pressed', String(playing));
    button.dataset.labelEn = playing ? 'Stop' : 'Play';
    button.dataset.labelKo = playing ? '정지' : '재생';
    button.setAttribute('aria-label', language === 'ko' ? button.dataset.labelKo : button.dataset.labelEn);
    button.querySelector('[data-icon-play]').style.display = playing ? 'none' : '';
    button.querySelector('[data-icon-stop]').style.display = playing ? '' : 'none';
  }
  root.querySelectorAll('[data-play]').forEach(button => {
    const figure = button.closest('figure');
    button.addEventListener('click', () => {
      figure.dataset.resume = 'false';
      playback(figure, button.getAttribute('aria-pressed') !== 'true');
    });
  });
  document.addEventListener('visibilitychange', () => {
    root.querySelectorAll('figure[data-demo]').forEach(figure => {
      if (document.hidden) {
        figure.dataset.resume = frames.get(figure).querySelector('[data-play]').getAttribute('aria-pressed');
        playback(figure, false);
      } else if (figure.dataset.resume === 'true') { playback(figure, true); }
    });
  });
  const modal = root.querySelector('dialog');
  let expandedFigure = null;
  if (modal) {
    root.querySelectorAll('[data-enlarge]').forEach(button => button.addEventListener('click', () => {
      if (modal.open) { modal.close(); return; }
      expandedFigure = button.closest('figure');
      const frame = frames.get(expandedFigure);
      expandedFigure.style.minHeight = expandedFigure.offsetHeight + 'px';
      modal.querySelector('img').hidden = true;
      modal.append(frame);
      modal.showModal();
      playback(expandedFigure, frame.querySelector('[data-play]').getAttribute('aria-pressed') === 'true');
    }));
    modal.querySelector('button').addEventListener('click', () => modal.close());
    modal.addEventListener('click', event => { if (event.target === modal) modal.close(); });
    modal.addEventListener('close', () => {
      if (!expandedFigure) return;
      const figure = expandedFigure;
      const frame = frames.get(figure);
      figure.prepend(frame);
      figure.style.minHeight = '';
      expandedFigure = null;
      playback(figure, frame.querySelector('[data-play]').getAttribute('aria-pressed') === 'true');
    });
  }
  applyLanguage(language);
  root.querySelectorAll('figure[data-demo]').forEach(figure => playback(figure, true));
})();
