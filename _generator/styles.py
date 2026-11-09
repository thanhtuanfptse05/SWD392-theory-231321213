# _generator/styles.py
# System Design Tokens and CSS Rules matching design.md with modern UI polish

def get_css():
    return r"""
:root {
  --bg-body: #f8fafc;
  --bg-surface: #ffffff;
  --bg-surface-subtle: #f1f5f9;
  --bg-sidebar: #ffffff;
  --bg-header: rgba(255, 255, 255, 0.92);
  --bg-card: #ffffff;
  --bg-code: #0d1117;
  --text-primary: #0f172a;
  --text-secondary: #334155;
  --text-muted: #64748b;
  --border-color: #e2e8f0;
  --border-subtle: #f1f5f9;
  --accent-primary: #2563eb;
  --accent-hover: #1d4ed8;
  --accent-light: #eff6ff;
  --shadow-sm: 0 1px 2px rgba(15, 23, 42, 0.05);
  --shadow-md: 0 4px 6px -1px rgba(15, 23, 42, 0.07), 0 2px 4px -2px rgba(15, 23, 42, 0.05);
  --shadow-lg: 0 10px 15px -3px rgba(15, 23, 42, 0.08), 0 4px 6px -4px rgba(15, 23, 42, 0.04);
  --shadow-card: 0 2px 8px rgba(15, 23, 42, 0.04), 0 1px 2px rgba(15, 23, 42, 0.06);
  --shadow-hover: 0 12px 24px -4px rgba(15, 23, 42, 0.1), 0 4px 6px -2px rgba(15, 23, 42, 0.05);
  --radius-sm: 6px;
  --radius-md: 10px;
  --radius-lg: 16px;
  --radius-full: 9999px;

  --part1-color: #0284c7;
  --part1-bg: #f0f9ff;
  --part1-border: #bae6fd;

  --part2-color: #4f46e5;
  --part2-bg: #eef2ff;
  --part2-border: #c7d2fe;

  --part3-color: #059669;
  --part3-bg: #ecfdf5;
  --part3-border: #a7f3d0;

  --part4-color: #d97706;
  --part4-bg: #fffbeb;
  --part4-border: #fde68a;

  --part5-color: #7c3aed;
  --part5-bg: #f5f3ff;
  --part5-border: #ddd6fe;

  --success-color: #10b981;
  --warning-color: #f59e0b;
  --danger-color: #ef4444;
  --info-color: #3b82f6;
}

[data-theme="dark"] {
  --bg-body: #090d16;
  --bg-surface: #111827;
  --bg-surface-subtle: #1e293b;
  --bg-sidebar: #0f172a;
  --bg-header: rgba(15, 23, 42, 0.92);
  --bg-card: #131d2f;
  --bg-code: #070b12;
  --text-primary: #f8fafc;
  --text-secondary: #cbd5e1;
  --text-muted: #94a3b8;
  --border-color: #1e293b;
  --border-subtle: #172033;
  --accent-primary: #60a5fa;
  --accent-hover: #93c5fd;
  --accent-light: rgba(96, 165, 250, 0.15);
  --shadow-sm: 0 1px 3px rgba(0,0,0,0.3);
  --shadow-md: 0 4px 6px -1px rgba(0,0,0,0.4);
  --shadow-lg: 0 10px 20px -3px rgba(0,0,0,0.5);
  --shadow-card: 0 4px 12px rgba(0, 0, 0, 0.25);
  --shadow-hover: 0 14px 28px rgba(0, 0, 0, 0.4);

  --part1-bg: rgba(2, 132, 199, 0.12);
  --part1-border: rgba(2, 132, 199, 0.35);
  --part2-bg: rgba(79, 70, 229, 0.12);
  --part2-border: rgba(79, 70, 229, 0.35);
  --part3-bg: rgba(5, 150, 105, 0.12);
  --part3-border: rgba(5, 150, 105, 0.35);
  --part4-bg: rgba(217, 119, 6, 0.12);
  --part4-border: rgba(217, 119, 6, 0.35);
  --part5-bg: rgba(124, 58, 237, 0.12);
  --part5-border: rgba(124, 58, 237, 0.35);
}

* {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

html {
  scroll-behavior: smooth;
  font-size: 15px;
}

body {
  font-family: 'Plus Jakarta Sans', system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
  background-color: var(--bg-body);
  color: var(--text-secondary);
  line-height: 1.68;
  transition: background-color 0.25s ease, color 0.25s ease;
  overflow-x: hidden;
}

/* Typography */
h1, h2, h3, h4, h5, h6 {
  font-family: 'Outfit', sans-serif;
  color: var(--text-primary);
  font-weight: 700;
  line-height: 1.25;
  letter-spacing: -0.015em;
}

h1 { font-size: 2.25rem; font-weight: 800; }
h2 { font-size: 1.65rem; font-weight: 700; margin-bottom: 0.75rem; }
h3 { font-size: 1.25rem; font-weight: 600; margin-bottom: 0.5rem; }
h4 { font-size: 1.05rem; font-weight: 600; margin-bottom: 0.35rem; }

p { margin-bottom: 0.85rem; }
p:last-child { margin-bottom: 0; }

strong, b {
  color: var(--text-primary);
  font-weight: 600;
}

code, kbd, samp, pre {
  font-family: 'JetBrains Mono', monospace;
}

/* FIX: Inline Code ONLY - NEVER affect pre code */
:not(pre) > code {
  background: var(--bg-surface-subtle);
  color: var(--accent-primary);
  padding: 0.2em 0.45em;
  border-radius: var(--radius-sm);
  font-size: 0.88em;
  font-weight: 600;
  border: 1px solid var(--border-color);
  font-family: 'JetBrains Mono', monospace;
  word-break: break-word;
}

/* Code Block Component - Modern Terminal / VS Code Style */
.code-block {
  background: var(--bg-code);
  border-radius: var(--radius-md);
  margin: 1.25rem 0;
  overflow: hidden;
  border: 1px solid #30363d;
  box-shadow: 0 4px 16px rgba(0, 0, 0, 0.18);
}

.code-header {
  background: #161b22;
  padding: 0.6rem 1rem;
  display: flex;
  align-items: center;
  justify-content: space-between;
  border-bottom: 1px solid #30363d;
  font-size: 0.78rem;
  color: #8b949e;
  font-family: 'JetBrains Mono', monospace;
  user-select: none;
}

.code-header-left {
  display: flex;
  align-items: center;
  gap: 0.65rem;
}

.code-dots {
  display: flex;
  gap: 6px;
  align-items: center;
}

.code-dot {
  width: 10px;
  height: 10px;
  border-radius: 50%;
  display: inline-block;
}
.dot-red { background: #ff5f56; }
.dot-yellow { background: #ffbd2e; }
.dot-green { background: #27c93f; }

.code-lang-tag {
  color: #c9d1d9;
  font-weight: 600;
  font-size: 0.75rem;
}

.code-copy-btn {
  background: rgba(255, 255, 255, 0.08);
  border: 1px solid rgba(255, 255, 255, 0.15);
  color: #c9d1d9;
  padding: 0.25rem 0.65rem;
  border-radius: 4px;
  font-size: 0.72rem;
  cursor: pointer;
  transition: all 0.15s ease;
  display: flex;
  align-items: center;
  gap: 0.35rem;
}

.code-copy-btn:hover {
  background: rgba(255, 255, 255, 0.18);
  color: #ffffff;
  border-color: rgba(255, 255, 255, 0.3);
}

pre.code-body {
  padding: 1.1rem 1.25rem;
  margin: 0;
  overflow-x: auto;
  background: #0d1117 !important;
  line-height: 1.6;
}

/* CRITICAL FIX: reset pre code styles completely so NO white patches or boxes appear */
pre.code-body,
pre.code-body *,
pre.code-body code,
pre.code-body span {
  background: #0d1117 !important;
  border: none !important;
  box-shadow: none !important;
  outline: none !important;
}

pre.code-body code {
  color: #e6edf3 !important;
  padding: 0 !important;
  border-radius: 0 !important;
  font-size: 0.88rem;
  font-family: 'JetBrains Mono', monospace;
  white-space: pre;
  display: block;
}

/* Syntax Highlighting Colors */
.kwd { color: #ff7b72 !important; font-weight: 600; } /* Keywords */
.typ { color: #79c0ff !important; font-weight: 600; } /* Types / Classes */
.str { color: #a5d6ff !important; } /* Strings */
.com { color: #8b949e !important; font-style: italic; } /* Comments */
.fn  { color: #d2a8ff !important; } /* Methods */
.ann { color: #ffa657 !important; } /* Annotations / Stereotypes */
.num { color: #79c0ff !important; } /* Numbers */

/* Code Details / Accordion */
.code-accordion {
  margin-top: 1rem;
  border: 1px solid var(--border-color);
  border-radius: var(--radius-md);
  overflow: hidden;
  background: var(--bg-surface);
}

.code-accordion summary {
  padding: 0.65rem 1rem;
  background: var(--bg-surface-subtle);
  cursor: pointer;
  font-size: 0.82rem;
  font-weight: 700;
  color: var(--accent-primary);
  display: flex;
  align-items: center;
  justify-content: space-between;
  user-select: none;
  transition: background 0.15s ease;
}

.code-accordion summary:hover {
  background: #e2e8f0;
}

[data-theme="dark"] .code-accordion summary:hover {
  background: #334155;
}

.code-accordion[open] summary {
  border-bottom: 1px solid var(--border-color);
}

.code-accordion .code-block {
  margin: 0;
  border-radius: 0;
  border: none;
  box-shadow: none;
}

.toggle-icon {
  transition: transform 0.2s ease;
  display: inline-block;
  font-size: 0.75rem;
}

.code-accordion[open] .toggle-icon {
  transform: rotate(180deg);
}
  background: var(--border-color);
}

.code-accordion[open] summary {
  border-bottom: 1px solid var(--border-color);
}

/* Code Block Component - Modern Terminal / VS Code Style */
.code-block {
  background: var(--bg-code);
  border-radius: var(--radius-md);
  margin: 1.25rem 0;
  overflow: hidden;
  border: 1px solid #30363d;
  box-shadow: 0 4px 16px rgba(0, 0, 0, 0.18);
}

.code-header {
  background: #161b22;
  padding: 0.6rem 1rem;
  display: flex;
  align-items: center;
  justify-content: space-between;
  border-bottom: 1px solid #30363d;
  font-size: 0.78rem;
  color: #8b949e;
  font-family: 'JetBrains Mono', monospace;
  user-select: none;
}

.code-header-left {
  display: flex;
  align-items: center;
  gap: 0.65rem;
}

.code-dots {
  display: flex;
  gap: 6px;
  align-items: center;
}

.code-dot {
  width: 10px;
  height: 10px;
  border-radius: 50%;
  display: inline-block;
}
.dot-red { background: #ff5f56; }
.dot-yellow { background: #ffbd2e; }
.dot-green { background: #27c93f; }

.code-lang-tag {
  color: #c9d1d9;
  font-weight: 600;
  font-size: 0.75rem;
}

.code-copy-btn {
  background: rgba(255, 255, 255, 0.08);
  border: 1px solid rgba(255, 255, 255, 0.15);
  color: #c9d1d9;
  padding: 0.25rem 0.65rem;
  border-radius: 4px;
  font-size: 0.72rem;
  cursor: pointer;
  transition: all 0.15s ease;
  display: flex;
  align-items: center;
  gap: 0.35rem;
}

.code-copy-btn:hover {
  background: rgba(255, 255, 255, 0.18);
  color: #ffffff;
  border-color: rgba(255, 255, 255, 0.3);
}

pre.code-body {
  padding: 1.1rem 1.25rem;
  margin: 0;
  overflow-x: auto;
  background: transparent !important;
  line-height: 1.6;
}

/* CRITICAL FIX: reset pre code styles completely so NO white patches or boxes appear */
pre.code-body,
pre.code-body *,
pre.code-body code,
pre.code-body span {
  background: transparent !important;
  border: none !important;
  box-shadow: none !important;
  outline: none !important;
}

pre.code-body code {
  color: #e6edf3 !important;
  padding: 0 !important;
  border-radius: 0 !important;
  font-size: 0.88rem;
  font-family: 'JetBrains Mono', monospace;
  white-space: pre;
  display: block;
}

/* Syntax Highlighting Colors */
.kwd { color: #ff7b72 !important; font-weight: 600; } /* Keywords */
.typ { color: #79c0ff !important; font-weight: 600; } /* Types / Classes */
.str { color: #a5d6ff !important; } /* Strings */
.com { color: #8b949e !important; font-style: italic; } /* Comments */
.fn  { color: #d2a8ff !important; } /* Methods */
.ann { color: #ffa657 !important; } /* Annotations / Stereotypes */
.num { color: #79c0ff !important; } /* Numbers */

/* Code Details / Accordion */
.code-accordion {
  margin-top: 1rem;
  border: 1px solid var(--border-color);
  border-radius: var(--radius-md);
  overflow: hidden;
  background: var(--bg-surface);
}

.code-accordion summary {
  padding: 0.65rem 1rem;
  background: var(--bg-surface-subtle);
  cursor: pointer;
  font-size: 0.82rem;
  font-weight: 700;
  color: var(--accent-primary);
  display: flex;
  align-items: center;
  justify-content: space-between;
  user-select: none;
  transition: background 0.15s ease;
}

.code-accordion summary:hover {
  background: #e2e8f0;
}

[data-theme="dark"] .code-accordion summary:hover {
  background: #334155;
}

.code-accordion[open] summary {
  border-bottom: 1px solid var(--border-color);
}

.code-accordion .code-block {
  margin: 0;
  border-radius: 0;
  border: none;
  box-shadow: none;
}

.toggle-icon {
  transition: transform 0.2s ease;
  display: inline-block;
  font-size: 0.75rem;
}

.code-accordion[open] .toggle-icon {
  transform: rotate(180deg);
}
  background: var(--border-color);
}

.code-accordion[open] summary {
  border-bottom: 1px solid var(--border-color);
}

/* Progress bar */
#progressBar {
  position: fixed;
  top: 0;
  left: 0;
  height: 3.5px;
  background: linear-gradient(90deg, #2563eb, #7c3aed, #059669);
  z-index: 1000;
  width: 0%;
  transition: width 0.1s ease;
}

/* Master Sticky Header */
.master-header {
  position: sticky;
  top: 0;
  height: 64px;
  background: var(--bg-header);
  backdrop-filter: blur(12px);
  -webkit-backdrop-filter: blur(12px);
  border-bottom: 1px solid var(--border-color);
  z-index: 900;
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 0 1.5rem;
  transition: background-color 0.25s ease, border-color 0.25s ease;
}

.header-left {
  display: flex;
  align-items: center;
  gap: 1rem;
}

.nav-toggle-btn {
  display: none;
  background: transparent;
  border: 1px solid var(--border-color);
  color: var(--text-primary);
  border-radius: var(--radius-md);
  width: 38px;
  height: 38px;
  cursor: pointer;
  font-size: 1.2rem;
  align-items: center;
  justify-content: center;
  transition: all 0.2s;
}

.nav-toggle-btn:hover {
  background: var(--bg-surface-subtle);
}

.brand-badge {
  display: flex;
  align-items: center;
  gap: 0.75rem;
  text-decoration: none;
  color: inherit;
}

.brand-icon {
  width: 38px;
  height: 38px;
  background: linear-gradient(135deg, #2563eb, #7c3aed);
  color: white;
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: var(--radius-md);
  font-weight: 800;
  font-family: 'Outfit', sans-serif;
  font-size: 1.15rem;
  box-shadow: 0 4px 10px rgba(37, 99, 235, 0.3);
}

.brand-title {
  font-family: 'Outfit', sans-serif;
  font-weight: 700;
  font-size: 1.15rem;
  color: var(--text-primary);
  line-height: 1.1;
}

.brand-subtitle {
  font-size: 0.72rem;
  color: var(--text-muted);
  font-weight: 500;
  letter-spacing: 0.02em;
}

.header-center {
  flex: 1;
  max-width: 580px;
  margin: 0 1.5rem;
}

.search-box {
  position: relative;
  display: flex;
  align-items: center;
}

.search-input {
  width: 100%;
  height: 40px;
  padding: 0 4.2rem 0 2.4rem;
  background: var(--bg-surface-subtle);
  border: 1px solid var(--border-color);
  border-radius: var(--radius-full);
  color: var(--text-primary);
  font-size: 0.9rem;
  transition: all 0.2s ease;
  outline: none;
}

.search-input:focus {
  background: var(--bg-surface);
  border-color: var(--accent-primary);
  box-shadow: 0 0 0 3px rgba(37, 99, 235, 0.15);
}

.search-icon {
  position: absolute;
  left: 0.85rem;
  color: var(--text-muted);
  pointer-events: none;
  font-size: 0.95rem;
}

.search-shortcut {
  position: absolute;
  right: 0.75rem;
  font-size: 0.72rem;
  background: var(--bg-surface);
  border: 1px solid var(--border-color);
  padding: 0.15rem 0.45rem;
  border-radius: var(--radius-sm);
  color: var(--text-muted);
  pointer-events: none;
  font-family: 'JetBrains Mono', monospace;
  font-weight: 600;
}

.search-clear-btn {
  position: absolute;
  right: 2.5rem;
  background: transparent;
  border: none;
  color: var(--text-muted);
  cursor: pointer;
  font-size: 0.85rem;
  display: none;
  padding: 0.2rem;
}

.search-clear-btn:hover {
  color: var(--text-primary);
}

.header-right {
  display: flex;
  align-items: center;
  gap: 0.75rem;
}

.theme-toggle-btn {
  background: var(--bg-surface-subtle);
  border: 1px solid var(--border-color);
  color: var(--text-primary);
  width: 38px;
  height: 38px;
  border-radius: var(--radius-md);
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: all 0.2s;
  font-size: 1.05rem;
}

.theme-toggle-btn:hover {
  background: var(--bg-surface);
  border-color: var(--accent-primary);
  color: var(--accent-primary);
  transform: rotate(15deg);
}

/* App Container Layout */
.app-container {
  display: flex;
  min-height: calc(100vh - 64px);
  position: relative;
}

/* Master Sidebar */
.master-sidebar {
  width: 310px;
  background: var(--bg-sidebar);
  border-right: 1px solid var(--border-color);
  position: fixed;
  top: 64px;
  bottom: 0;
  left: 0;
  overflow-y: auto;
  padding: 1.25rem 0.85rem 3rem;
  z-index: 850;
  transition: transform 0.25s ease, background-color 0.25s ease, border-color 0.25s ease;
}

.master-sidebar::-webkit-scrollbar {
  width: 5px;
}
.master-sidebar::-webkit-scrollbar-track {
  background: transparent;
}
.master-sidebar::-webkit-scrollbar-thumb {
  background: var(--border-color);
  border-radius: 4px;
}

.sidebar-heading {
  font-size: 0.75rem;
  text-transform: uppercase;
  letter-spacing: 0.08em;
  color: var(--text-muted);
  padding: 0.5rem 0.75rem;
  font-weight: 700;
  margin-top: 0.5rem;
}

.nav-part-group {
  margin-bottom: 1.25rem;
}

.nav-part-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 0.5rem 0.75rem;
  border-radius: var(--radius-md);
  font-size: 0.8rem;
  font-weight: 700;
  cursor: pointer;
  user-select: none;
  transition: background-color 0.15s;
  text-transform: uppercase;
  letter-spacing: 0.03em;
}

.part-1-header { color: var(--part1-color); background: var(--part1-bg); border: 1px solid var(--part1-border); }
.part-2-header { color: var(--part2-color); background: var(--part2-bg); border: 1px solid var(--part2-border); }
.part-3-header { color: var(--part3-color); background: var(--part3-bg); border: 1px solid var(--part3-border); }
.part-4-header { color: var(--part4-color); background: var(--part4-bg); border: 1px solid var(--part4-border); }
.part-5-header { color: var(--part5-color); background: var(--part5-bg); border: 1px solid var(--part5-border); }

.nav-list {
  list-style: none;
  margin-top: 0.35rem;
}

.nav-item {
  margin-bottom: 0.15rem;
}

.nav-link {
  display: flex;
  align-items: center;
  gap: 0.6rem;
  padding: 0.45rem 0.75rem;
  color: var(--text-secondary);
  text-decoration: none;
  border-radius: var(--radius-sm);
  font-size: 0.85rem;
  font-weight: 500;
  transition: all 0.15s ease;
}

.nav-link:hover {
  background: var(--bg-surface-subtle);
  color: var(--accent-primary);
  transform: translateX(2px);
}

.nav-link.active {
  background: var(--accent-light);
  color: var(--accent-primary);
  font-weight: 700;
  border-left: 3px solid var(--accent-primary);
}

.nav-ch-badge {
  font-size: 0.72rem;
  font-weight: 700;
  padding: 0.1rem 0.4rem;
  border-radius: var(--radius-sm);
  background: var(--bg-surface-subtle);
  color: var(--text-muted);
  border: 1px solid var(--border-color);
  font-family: 'JetBrains Mono', monospace;
  white-space: nowrap;
}

.nav-link.active .nav-ch-badge {
  background: var(--accent-primary);
  color: white;
  border-color: var(--accent-primary);
}

/* Master Main Content Area */
.master-main {
  margin-left: 310px;
  flex: 1;
  padding: 2rem 3rem 6rem;
  max-width: 1340px;
  transition: margin-left 0.25s ease;
}

/* Hero Banner */
.hero-banner {
  background: var(--bg-surface);
  border: 1px solid var(--border-color);
  border-radius: var(--radius-lg);
  padding: 2.5rem;
  margin-bottom: 2.5rem;
  box-shadow: var(--shadow-card);
  position: relative;
  overflow: hidden;
}

.hero-banner::before {
  content: "";
  position: absolute;
  top: -80px;
  right: -80px;
  width: 280px;
  height: 280px;
  background: radial-gradient(circle, rgba(37, 99, 235, 0.1), transparent 70%);
  border-radius: 50%;
  pointer-events: none;
}

.hero-tag {
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  font-size: 0.78rem;
  font-weight: 700;
  color: var(--accent-primary);
  background: var(--accent-light);
  padding: 0.3rem 0.85rem;
  border-radius: var(--radius-full);
  margin-bottom: 1rem;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  border: 1px solid rgba(37, 99, 235, 0.2);
}

.hero-title {
  font-size: 2.4rem;
  font-weight: 800;
  margin-bottom: 0.75rem;
  line-height: 1.15;
}

.hero-desc {
  font-size: 1.05rem;
  color: var(--text-secondary);
  max-width: 880px;
  margin-bottom: 1.8rem;
  line-height: 1.6;
}

.hero-stats-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
  gap: 1rem;
  margin-bottom: 1.8rem;
}

.hero-stat-card {
  background: var(--bg-surface-subtle);
  border: 1px solid var(--border-color);
  border-radius: var(--radius-md);
  padding: 1.1rem 1.25rem;
  position: relative;
  overflow: hidden;
}

.hero-stat-card::before {
  content: "";
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  height: 3px;
  background: var(--accent-primary);
}

.hero-stat-value {
  font-size: 1.9rem;
  font-weight: 800;
  font-family: 'Outfit', sans-serif;
  color: var(--text-primary);
  line-height: 1;
  margin-bottom: 0.3rem;
}

.hero-stat-label {
  font-size: 0.8rem;
  color: var(--text-muted);
  font-weight: 500;
}

.quick-jumps-row {
  display: flex;
  align-items: center;
  flex-wrap: wrap;
  gap: 0.6rem;
}

.quick-jump-label {
  font-size: 0.82rem;
  font-weight: 700;
  color: var(--text-muted);
  margin-right: 0.3rem;
}

.quick-pill {
  font-size: 0.82rem;
  padding: 0.35rem 0.85rem;
  border-radius: var(--radius-full);
  background: var(--bg-surface-subtle);
  color: var(--text-secondary);
  text-decoration: none;
  border: 1px solid var(--border-color);
  font-weight: 600;
  transition: all 0.15s ease;
}

.quick-pill:hover {
  background: var(--accent-light);
  color: var(--accent-primary);
  border-color: var(--accent-primary);
  transform: translateY(-1px);
}

/* Part Divider Banner */
.part-divider-banner {
  border-radius: var(--radius-lg);
  padding: 2.25rem 2.5rem;
  margin: 3.5rem 0 2rem;
  position: relative;
  overflow: hidden;
  border: 1px solid;
}

.part-1-banner { background: var(--part1-bg); border-color: var(--part1-border); }
.part-2-banner { background: var(--part2-bg); border-color: var(--part2-border); }
.part-3-banner { background: var(--part3-bg); border-color: var(--part3-border); }
.part-4-banner { background: var(--part4-bg); border-color: var(--part4-border); }
.part-5-banner { background: var(--part5-bg); border-color: var(--part5-border); }

.part-badge-tag {
  display: inline-block;
  font-size: 0.75rem;
  font-weight: 800;
  text-transform: uppercase;
  letter-spacing: 0.08em;
  padding: 0.25rem 0.75rem;
  border-radius: var(--radius-sm);
  margin-bottom: 0.75rem;
}

.part-1-banner .part-badge-tag { background: #0284c7; color: white; }
.part-2-banner .part-badge-tag { background: #4f46e5; color: white; }
.part-3-banner .part-badge-tag { background: #059669; color: white; }
.part-4-banner .part-badge-tag { background: #d97706; color: white; }
.part-5-banner .part-badge-tag { background: #7c3aed; color: white; }

.part-title {
  font-size: 1.85rem;
  font-weight: 800;
  margin-bottom: 0.5rem;
}

.part-desc {
  font-size: 0.98rem;
  max-width: 900px;
  line-height: 1.6;
}

/* Chapter Sections */
.chapter-section {
  background: var(--bg-surface);
  border: 1px solid var(--border-color);
  border-radius: var(--radius-lg);
  padding: 2.5rem;
  margin-bottom: 3rem;
  box-shadow: var(--shadow-card);
  scroll-margin-top: 80px;
}

.chapter-header {
  border-bottom: 1px solid var(--border-color);
  padding-bottom: 1.25rem;
  margin-bottom: 1.75rem;
}

.chapter-badge-row {
  display: flex;
  align-items: center;
  gap: 0.75rem;
  margin-bottom: 0.6rem;
}

.chapter-badge {
  font-size: 0.75rem;
  font-weight: 800;
  font-family: 'JetBrains Mono', monospace;
  padding: 0.2rem 0.65rem;
  border-radius: var(--radius-sm);
  background: var(--bg-surface-subtle);
  color: var(--text-primary);
  border: 1px solid var(--border-color);
}

.chapter-lecturer-tag {
  font-size: 0.75rem;
  color: var(--text-muted);
  font-weight: 600;
}

.chapter-title {
  font-size: 1.75rem;
  font-weight: 800;
  line-height: 1.25;
  color: var(--text-primary);
}

.chapter-subtitle {
  font-size: 0.95rem;
  color: var(--text-muted);
  margin-top: 0.25rem;
}

/* Component Cards Grid */
.card-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(340px, 1fr));
  gap: 1.5rem;
  margin: 1.5rem 0;
}

.card {
  background: var(--bg-surface);
  border: 1px solid var(--border-color);
  border-radius: var(--radius-md);
  padding: 1.5rem;
  box-shadow: var(--shadow-card);
  transition: all 0.2s ease;
  display: flex;
  flex-direction: column;
}

.card:hover {
  border-color: #cbd5e1;
  box-shadow: var(--shadow-hover);
  transform: translateY(-2px);
}

.card-title {
  font-size: 1.15rem;
  font-weight: 700;
  color: var(--text-primary);
  margin-bottom: 0.75rem;
  display: flex;
  align-items: center;
  gap: 0.5rem;
  line-height: 1.3;
}

.card-content {
  font-size: 0.92rem;
  line-height: 1.6;
  flex: 1;
}

/* Topic Card */
.topic-card {
  background: var(--bg-surface);
  border: 1px solid var(--border-color);
  border-left: 4px solid var(--accent-primary);
  border-radius: var(--radius-md);
  padding: 1.5rem 1.75rem;
  margin: 1.5rem 0;
  box-shadow: var(--shadow-card);
}

.topic-title {
  font-size: 1.2rem;
  font-weight: 700;
  color: var(--text-primary);
  margin-bottom: 0.75rem;
}

/* Concept Box */
.concept-box {
  background: var(--bg-surface-subtle);
  border-radius: var(--radius-md);
  padding: 1.1rem 1.35rem;
  margin: 1rem 0;
  border-left: 3px solid var(--text-muted);
}

.concept-title {
  font-weight: 700;
  color: var(--text-primary);
  margin-bottom: 0.35rem;
  font-size: 0.98rem;
}

/* Callout Boxes */
.callout {
  padding: 1.2rem 1.5rem;
  border-radius: var(--radius-md);
  margin: 1.5rem 0;
  border-left: 4px solid;
  font-size: 0.92rem;
  line-height: 1.6;
}

.callout-title {
  font-weight: 700;
  font-size: 0.98rem;
  margin-bottom: 0.4rem;
  display: flex;
  align-items: center;
  gap: 0.45rem;
}

.callout-info {
  background: rgba(59, 130, 246, 0.08);
  border-color: #3b82f6;
  color: var(--text-secondary);
}
.callout-info .callout-title { color: #2563eb; }

.callout-tip {
  background: rgba(16, 185, 129, 0.08);
  border-color: #10b981;
  color: var(--text-secondary);
}
.callout-tip .callout-title { color: #059669; }

.callout-warning {
  background: rgba(245, 158, 11, 0.08);
  border-color: #f59e0b;
  color: var(--text-secondary);
}
.callout-warning .callout-title { color: #d97706; }

.callout-important {
  background: rgba(239, 68, 68, 0.08);
  border-color: #ef4444;
  color: var(--text-secondary);
}
.callout-important .callout-title { color: #dc2626; }

/* Styled Tables */
.table-wrap {
  width: 100%;
  overflow-x: auto;
  margin: 1.25rem 0;
  border: 1px solid var(--border-color);
  border-radius: var(--radius-md);
  box-shadow: var(--shadow-sm);
}

.styled-table {
  width: 100%;
  border-collapse: collapse;
  font-size: 0.9rem;
  text-align: left;
}

.styled-table th {
  background: var(--bg-surface-subtle);
  color: var(--text-primary);
  font-weight: 700;
  padding: 0.85rem 1.1rem;
  border-bottom: 2px solid var(--border-color);
  white-space: nowrap;
}

.styled-table td {
  padding: 0.85rem 1.1rem;
  border-bottom: 1px solid var(--border-color);
  color: var(--text-secondary);
  vertical-align: top;
}

.styled-table tr:last-child td {
  border-bottom: none;
}

.styled-table tr:hover td {
  background: rgba(37, 99, 235, 0.03);
}

/* Step Boxes */
.step-list {
  display: flex;
  flex-direction: column;
  gap: 0.85rem;
  margin: 1.25rem 0;
}

.step-item {
  display: flex;
  gap: 1.1rem;
  background: var(--bg-surface-subtle);
  border: 1px solid var(--border-color);
  border-radius: var(--radius-md);
  padding: 1.1rem 1.35rem;
  align-items: flex-start;
}

.step-num {
  width: 32px;
  height: 32px;
  background: var(--accent-primary);
  color: white;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: 800;
  font-size: 0.9rem;
  flex-shrink: 0;
}

.step-body {
  flex: 1;
}

.step-title {
  font-weight: 700;
  color: var(--text-primary);
  margin-bottom: 0.25rem;
  font-size: 0.98rem;
}

/* Diagram Cards & SVGs */
.diagram-card {
  background: var(--bg-surface-subtle);
  border: 1px solid var(--border-color);
  border-radius: var(--radius-md);
  padding: 1.75rem;
  margin: 1.75rem 0;
  text-align: center;
}

.diagram-caption {
  font-size: 0.88rem;
  color: var(--text-muted);
  font-weight: 600;
  margin-top: 0.85rem;
}

.svg-container {
  width: 100%;
  max-width: 900px;
  margin: 0 auto;
  display: flex;
  justify-content: center;
}

.svg-container svg {
  max-width: 100%;
  height: auto;
}

/* Interactive Tools */
.interactive-tool-box {
  background: var(--bg-surface);
  border: 2px solid var(--accent-primary);
  border-radius: var(--radius-lg);
  padding: 2.25rem;
  margin: 3rem 0;
  box-shadow: var(--shadow-md);
}

.tool-header {
  margin-bottom: 1.5rem;
}

.tool-title {
  font-size: 1.45rem;
  font-weight: 800;
  color: var(--text-primary);
  display: flex;
  align-items: center;
  gap: 0.6rem;
}

.tool-desc {
  font-size: 0.92rem;
  color: var(--text-secondary);
  margin-top: 0.25rem;
}

/* Pattern Explorer */
.pattern-filter-tabs {
  display: flex;
  gap: 0.5rem;
  flex-wrap: wrap;
  margin-bottom: 1.5rem;
}

.filter-btn {
  padding: 0.5rem 1.15rem;
  border-radius: var(--radius-full);
  background: var(--bg-surface-subtle);
  border: 1px solid var(--border-color);
  color: var(--text-secondary);
  font-size: 0.85rem;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.15s ease;
}

.filter-btn:hover {
  background: var(--border-color);
}

.filter-btn.active {
  background: var(--accent-primary);
  color: white;
  border-color: var(--accent-primary);
}

.patterns-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(320px, 1fr));
  gap: 1.25rem;
}

.pattern-card-item {
  background: var(--bg-surface);
  border: 1px solid var(--border-color);
  border-radius: var(--radius-md);
  padding: 1.35rem;
  cursor: pointer;
  box-shadow: var(--shadow-card);
  transition: all 0.2s ease;
  display: flex;
  flex-direction: column;
}

.pattern-card-item:hover {
  border-color: var(--accent-primary);
  box-shadow: var(--shadow-hover);
  transform: translateY(-2px);
}

.pattern-cat-tag {
  font-size: 0.72rem;
  font-weight: 800;
  text-transform: uppercase;
  padding: 0.2rem 0.55rem;
  border-radius: var(--radius-full);
  display: inline-block;
  margin-bottom: 0.5rem;
  letter-spacing: 0.05em;
  width: fit-content;
}

.cat-creational { background: #e0f2fe; color: #0284c7; border: 1px solid #bae6fd; }
.cat-structural { background: #eef2ff; color: #4f46e5; border: 1px solid #c7d2fe; }
.cat-behavioral { background: #fef3c7; color: #d97706; border: 1px solid #fde68a; }

/* Architecture Comparator */
.arch-select-row {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 0.75rem;
  margin-bottom: 1.5rem;
}

.arch-choice-btn {
  padding: 0.75rem 1rem;
  border-radius: var(--radius-md);
  border: 1px solid var(--border-color);
  background: var(--bg-surface-subtle);
  color: var(--text-primary);
  font-weight: 700;
  font-size: 0.9rem;
  cursor: pointer;
  text-align: center;
  transition: all 0.2s;
}

.arch-choice-btn:hover {
  border-color: var(--accent-primary);
}

.arch-choice-btn.active {
  background: var(--accent-light);
  border-color: var(--accent-primary);
  color: var(--accent-primary);
}

.arch-detail-view {
  background: var(--bg-surface-subtle);
  border: 1px solid var(--border-color);
  border-radius: var(--radius-md);
  padding: 1.75rem;
}

.metric-row {
  display: flex;
  align-items: center;
  margin-bottom: 0.75rem;
  gap: 1rem;
}

.metric-name {
  width: 150px;
  font-size: 0.85rem;
  font-weight: 600;
  color: var(--text-primary);
}

.metric-bar-bg {
  flex: 1;
  height: 10px;
  background: var(--border-color);
  border-radius: var(--radius-full);
  overflow: hidden;
}

.metric-bar-fill {
  height: 100%;
  border-radius: var(--radius-full);
  transition: width 0.4s ease;
}

.metric-score {
  width: 45px;
  font-size: 0.85rem;
  font-weight: 700;
  font-family: 'JetBrains Mono', monospace;
  text-align: right;
}

/* Calculator Tool */
.calc-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 1.5rem;
}

.calc-card {
  background: var(--bg-surface-subtle);
  border: 1px solid var(--border-color);
  border-radius: var(--radius-md);
  padding: 1.5rem;
}

.calc-input-group {
  margin-bottom: 0.85rem;
}

.calc-label {
  display: block;
  font-size: 0.82rem;
  font-weight: 600;
  color: var(--text-secondary);
  margin-bottom: 0.3rem;
}

.calc-input {
  width: 100%;
  height: 38px;
  padding: 0 0.75rem;
  background: var(--bg-surface);
  border: 1px solid var(--border-color);
  border-radius: var(--radius-sm);
  color: var(--text-primary);
  font-family: 'JetBrains Mono', monospace;
  font-size: 0.9rem;
}

.calc-btn {
  background: var(--accent-primary);
  color: white;
  border: none;
  padding: 0.55rem 1.35rem;
  border-radius: var(--radius-sm);
  font-weight: 600;
  font-size: 0.88rem;
  cursor: pointer;
  transition: background 0.15s;
}

.calc-btn:hover {
  background: var(--accent-hover);
}

.calc-result-box {
  margin-top: 1rem;
  padding: 0.85rem 1.1rem;
  background: var(--bg-surface);
  border: 1px dashed var(--accent-primary);
  border-radius: var(--radius-sm);
  font-size: 0.92rem;
  color: var(--text-primary);
  line-height: 1.6;
}

/* Quiz Engine */
.quiz-box {
  background: var(--bg-surface);
  border: 1px solid var(--border-color);
  border-radius: var(--radius-md);
  padding: 2rem;
  box-shadow: var(--shadow-card);
}

.quiz-meta-row {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 1.25rem;
  font-size: 0.85rem;
  color: var(--text-muted);
}

.quiz-q-num {
  font-weight: 700;
  color: var(--accent-primary);
  font-family: 'JetBrains Mono', monospace;
}

.quiz-question-text {
  font-size: 1.15rem;
  font-weight: 700;
  color: var(--text-primary);
  margin-bottom: 1.5rem;
  line-height: 1.45;
}

.quiz-options-list {
  display: flex;
  flex-direction: column;
  gap: 0.75rem;
  margin-bottom: 1.5rem;
}

.quiz-opt-btn {
  display: flex;
  align-items: center;
  gap: 0.85rem;
  padding: 0.95rem 1.2rem;
  background: var(--bg-surface-subtle);
  border: 1px solid var(--border-color);
  border-radius: var(--radius-md);
  color: var(--text-secondary);
  font-size: 0.92rem;
  font-weight: 500;
  cursor: pointer;
  text-align: left;
  transition: all 0.15s;
}

.quiz-opt-btn:hover:not(:disabled) {
  border-color: var(--accent-primary);
  background: var(--bg-surface);
  color: var(--text-primary);
}

.quiz-opt-key {
  width: 28px;
  height: 28px;
  border-radius: 50%;
  background: var(--bg-surface);
  border: 1px solid var(--border-color);
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: 700;
  font-size: 0.82rem;
  flex-shrink: 0;
}

.quiz-opt-btn.correct {
  background: rgba(16, 185, 129, 0.12);
  border-color: #10b981;
  color: #065f46;
  font-weight: 700;
}
.quiz-opt-btn.correct .quiz-opt-key {
  background: #10b981;
  color: white;
  border-color: #10b981;
}

.quiz-opt-btn.wrong {
  background: rgba(239, 68, 68, 0.12);
  border-color: #ef4444;
  color: #991b1b;
}
.quiz-opt-btn.wrong .quiz-opt-key {
  background: #ef4444;
  color: white;
  border-color: #ef4444;
}

.quiz-explanation-box {
  display: none;
  padding: 1.1rem 1.35rem;
  border-radius: var(--radius-md);
  background: var(--bg-surface-subtle);
  border-left: 4px solid var(--accent-primary);
  margin-bottom: 1.5rem;
  font-size: 0.9rem;
  line-height: 1.6;
}

.quiz-footer-actions {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.quiz-nav-btn {
  background: var(--accent-primary);
  color: white;
  border: none;
  padding: 0.6rem 1.5rem;
  border-radius: var(--radius-md);
  font-weight: 700;
  font-size: 0.9rem;
  cursor: pointer;
  transition: background 0.15s;
}

.quiz-nav-btn:hover {
  background: var(--accent-hover);
}

/* Floating Dock */
.floating-dock {
  position: fixed;
  bottom: 2rem;
  right: 2rem;
  display: flex;
  flex-direction: column;
  gap: 0.75rem;
  z-index: 800;
}

.scroll-top-btn {
  width: 44px;
  height: 44px;
  background: var(--accent-primary);
  color: white;
  border: none;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  box-shadow: 0 4px 12px rgba(37, 99, 235, 0.35);
  opacity: 0;
  transform: translateY(10px);
  pointer-events: none;
  transition: all 0.25s ease;
  font-size: 1.1rem;
}

.scroll-top-btn.visible {
  opacity: 1;
  transform: translateY(0);
  pointer-events: auto;
}

.scroll-top-btn:hover {
  background: var(--accent-hover);
  transform: translateY(-2px);
}

/* Mobile Drawer Overlay */
.drawer-overlay {
  display: none;
  position: fixed;
  inset: 0;
  background: rgba(0, 0, 0, 0.5);
  backdrop-filter: blur(4px);
  z-index: 840;
}

/* Responsive Media Queries */
@media (max-width: 1024px) {
  .master-sidebar {
    width: 270px;
  }
  .master-main {
    margin-left: 270px;
    padding: 1.75rem 2rem 5rem;
  }
}

@media (max-width: 768px) {
  .nav-toggle-btn {
    display: flex;
  }
  .master-sidebar {
    transform: translateX(-100%);
    width: 290px;
  }
  .master-sidebar.open {
    transform: translateX(0);
  }
  .drawer-overlay.open {
    display: block;
  }
  .master-main {
    margin-left: 0;
    padding: 1.25rem 1rem 5rem;
  }
  .header-center {
    display: none;
  }
  .hero-banner {
    padding: 1.5rem;
  }
  .hero-title {
    font-size: 1.75rem;
  }
  .chapter-section {
    padding: 1.5rem 1.25rem;
  }
  .card-grid {
    grid-template-columns: 1fr;
  }
}
"""
