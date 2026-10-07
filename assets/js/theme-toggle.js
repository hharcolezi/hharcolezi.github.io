(() => {
  const STORAGE_KEY = 'hha-theme';
  const root = document.documentElement;
  const button = document.getElementById('theme-toggle');
  const media = window.matchMedia ? window.matchMedia('(prefers-color-scheme: dark)') : null;

  const storedTheme = () => {
    try {
      const value = window.localStorage.getItem(STORAGE_KEY);
      return value === 'dark' || value === 'light' ? value : null;
    } catch (_error) {
      return null;
    }
  };

  const updateMeta = (theme) => {
    const meta = document.getElementById('theme-color-meta') || document.querySelector('meta[name="theme-color"]');
    if (meta) meta.setAttribute('content', theme === 'dark' ? '#0b1120' : '#f7f9fc');
  };

  const updateButton = (theme) => {
    if (!button) return;
    const dark = theme === 'dark';
    button.setAttribute('aria-pressed', String(dark));
    button.setAttribute('aria-label', dark ? 'Switch to light theme' : 'Switch to dark theme');
    button.setAttribute('title', dark ? 'Switch to light theme' : 'Switch to dark theme');
  };

  const applyTheme = (theme, persist = false) => {
    const next = theme === 'dark' ? 'dark' : 'light';
    root.dataset.theme = next;
    root.style.colorScheme = next;
    updateMeta(next);
    updateButton(next);
    if (persist) {
      try {
        window.localStorage.setItem(STORAGE_KEY, next);
      } catch (_error) {
        // Storage may be disabled; the page still switches for this session.
      }
    }
  };

  applyTheme(root.dataset.theme || (media && media.matches ? 'dark' : 'light'));

  if (button) {
    button.addEventListener('click', () => {
      applyTheme(root.dataset.theme === 'dark' ? 'light' : 'dark', true);
    });
  }

  const onSystemChange = (event) => {
    if (!storedTheme()) applyTheme(event.matches ? 'dark' : 'light');
  };

  if (media) {
    if (media.addEventListener) media.addEventListener('change', onSystemChange);
    else if (media.addListener) media.addListener(onSystemChange);
  }
})();
