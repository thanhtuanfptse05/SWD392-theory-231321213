# _generator/layout.py
# Layout structure for index.html

from styles import get_css
from part1 import get_part1_html
from part2 import get_part2_html
from part3 import get_part3_html
from part4 import get_part4_html
from part5 import get_part5_html
from tools_and_quiz import get_tools_and_quiz_html
from scripts import get_js

def build_full_html():
    css = get_css()
    part1_html = get_part1_html()
    part2_html = get_part2_html()
    part3_html = get_part3_html()
    part4_html = get_part4_html()
    part5_html = get_part5_html()
    tools_html = get_tools_and_quiz_html()
    js = get_js()

    template = r"""<!DOCTYPE html>
<html lang="vi" data-theme="light">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>SWD392 Master Study Guide &bull; Cẩm Nang Toàn Diện Kiến Trúc & Thiết Kế Phần Mềm</title>
  
  <!-- Google Fonts -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;500;600;700&family=Outfit:wght@500;600;700;800&family=Plus+Jakarta+Sans:wght@400;500;600;700&display=swap" rel="stylesheet">
  
  <!-- KaTeX Math Engine -->
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.css">
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.js"></script>
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/contrib/auto-render.min.js"></script>

  <style>
/* [[CSS_INJECTION]] */
  </style>
</head>
<body>

  <!-- Reading Progress Bar -->
  <div id="progressBar"></div>

  <!-- Master Sticky Header -->
  <header class="master-header">
    <div class="header-left">
      <button class="nav-toggle-btn" onclick="toggleMobileNav()" title="Mở danh mục điều hướng">☰</button>
      <a href="#" class="brand-badge">
        <div class="brand-icon">S</div>
        <div>
          <div class="brand-title">SWD392 Master Guide</div>
          <div class="brand-subtitle">Software Architecture &amp; Design &bull; Hassan Gomaa</div>
        </div>
      </a>
    </div>

    <div class="header-center">
      <div class="search-box">
        <span class="search-icon">🔍</span>
        <input type="text" id="searchInput" class="search-input" placeholder="Tìm kiếm nhanh khái niệm, UML, chương học, bài toán...">
        <button id="searchClearBtn" class="search-clear-btn" onclick="clearSearch()" title="Xóa từ khóa">✕</button>
        <span class="search-shortcut">Ctrl + K</span>
      </div>
    </div>

    <div class="header-right">
      <button id="themeToggleBtn" class="theme-toggle-btn" onclick="toggleTheme()" title="Chuyển chế độ Sáng / Tối">
        🌙
      </button>
    </div>
  </header>

  <div class="app-container">
    <!-- Master Left Sidebar -->
    <aside id="masterSidebar" class="master-sidebar">
      <div class="sidebar-heading">Mục Lục Toàn Bộ Khóa Học</div>

      <!-- Part 1 Navigation -->
      <div class="nav-part-group">
        <div class="nav-part-header part-1-header">
          <span>🔵 PHẦN 1: TỔNG QUAN & NỀN TẢNG</span>
        </div>
        <ul class="nav-list">
          <li class="nav-item">
            <a href="#ch01" class="nav-link">
              <span class="nav-ch-badge">Ch 01</span>
              <span>Giới Thiệu & Mô Hình Hóa</span>
            </a>
          </li>
          <li class="nav-item">
            <a href="#ch02" class="nav-link">
              <span class="nav-ch-badge">Ch 02</span>
              <span>Tổng Quan Ký Hiệu UML</span>
            </a>
          </li>
          <li class="nav-item">
            <a href="#ch03" class="nav-link">
              <span class="nav-ch-badge">Ch 03</span>
              <span>Vòng Đời & Quy Trình Phần Mềm</span>
            </a>
          </li>
          <li class="nav-item">
            <a href="#ch04" class="nav-link">
              <span class="nav-ch-badge">Ch 04</span>
              <span>Khái Niệm Cốt Lõi Kiến Trúc</span>
            </a>
          </li>
          <li class="nav-item">
            <a href="#ch05" class="nav-link">
              <span class="nav-ch-badge">Ch 05</span>
              <span>Phương Pháp Luận COMET</span>
            </a>
          </li>
        </ul>
      </div>

      <!-- Part 2 Navigation -->
      <div class="nav-part-group">
        <div class="nav-part-header part-2-header">
          <span>🟣 PHẦN 2: PHÂN TÍCH VỚI UML</span>
        </div>
        <ul class="nav-list">
          <li class="nav-item">
            <a href="#ch06" class="nav-link">
              <span class="nav-ch-badge">Ch 06</span>
              <span>Mô Hình Hóa Use Case</span>
            </a>
          </li>
          <li class="nav-item">
            <a href="#ch07" class="nav-link">
              <span class="nav-ch-badge">Ch 07</span>
              <span>Mô Hình Hóa Tĩnh (Static)</span>
            </a>
          </li>
          <li class="nav-item">
            <a href="#ch08" class="nav-link">
              <span class="nav-ch-badge">Ch 08</span>
              <span>Cấu Trúc Hóa Lớp & Đối Tượng</span>
            </a>
          </li>
          <li class="nav-item">
            <a href="#ch09-11" class="nav-link">
              <span class="nav-ch-badge">Ch 09-11</span>
              <span>Mô Hình Hóa Động (Dynamic)</span>
            </a>
          </li>
        </ul>
      </div>

      <!-- Part 3 Navigation -->
      <div class="nav-part-group">
        <div class="nav-part-header part-3-header">
          <span>🟢 PHẦN 3: THIẾT KẾ KIẾN TRÚC</span>
        </div>
        <ul class="nav-list">
          <li class="nav-item">
            <a href="#ch12" class="nav-link">
              <span class="nav-ch-badge">Ch 12</span>
              <span>Tổng Quan Kiến Trúc Phần Mềm</span>
            </a>
          </li>
          <li class="nav-item">
            <a href="#ch13" class="nav-link">
              <span class="nav-ch-badge">Ch 13</span>
              <span>Thiết Kế Phân Rã Subsystems</span>
            </a>
          </li>
          <li class="nav-item">
            <a href="#ch14" class="nav-link">
              <span class="nav-ch-badge">Ch 14</span>
              <span>Kiến Trúc Hướng Đối Tượng</span>
            </a>
          </li>
          <li class="nav-item">
            <a href="#ch15" class="nav-link">
              <span class="nav-ch-badge">Ch 15</span>
              <span>Kiến Trúc Client / Server & ORM</span>
            </a>
          </li>
          <li class="nav-item">
            <a href="#ch16" class="nav-link">
              <span class="nav-ch-badge">Ch 16</span>
              <span>Kiến Trúc Hướng Dịch Vụ SOA</span>
            </a>
          </li>
          <li class="nav-item">
            <a href="#ch17" class="nav-link">
              <span class="nav-ch-badge">Ch 17</span>
              <span>Kiến Trúc Thành Phần (CBD)</span>
            </a>
          </li>
          <li class="nav-item">
            <a href="#ch18" class="nav-link">
              <span class="nav-ch-badge">Ch 18</span>
              <span>Kiến Trúc Thời Gian Thực & RMA</span>
            </a>
          </li>
        </ul>
      </div>

      <!-- Part 4 Navigation -->
      <div class="nav-part-group">
        <div class="nav-part-header part-4-header">
          <span>🟠 PHẦN 4: CHẤT LƯỢNG & CASE STUDIES</span>
        </div>
        <ul class="nav-list">
          <li class="nav-item">
            <a href="#ch20" class="nav-link">
              <span class="nav-ch-badge">Ch 20</span>
              <span>Thuộc Tính Chất Lượng Phần Mềm</span>
            </a>
          </li>
          <li class="nav-item">
            <a href="#ch21" class="nav-link">
              <span class="nav-ch-badge">Ch 21</span>
              <span>Case Study 1: Hệ Thống ATM</span>
            </a>
          </li>
          <li class="nav-item">
            <a href="#ch22" class="nav-link">
              <span class="nav-ch-badge">Ch 22</span>
              <span>Case Study 2: Mua Sắm SOA</span>
            </a>
          </li>
          <li class="nav-item">
            <a href="#ch23" class="nav-link">
              <span class="nav-ch-badge">Ch 23</span>
              <span>Case Study 3: Giám Sát Cấp Cứu</span>
            </a>
          </li>
          <li class="nav-item">
            <a href="#ch24" class="nav-link">
              <span class="nav-ch-badge">Ch 24</span>
              <span>Case Study 4: Xe Tự Hành AGV</span>
            </a>
          </li>
          <li class="nav-item">
            <a href="#case-study-fos" class="nav-link">
              <span class="nav-ch-badge">FOS RDS</span>
              <span>Case Study Đồ Án FreshFood</span>
            </a>
          </li>
        </ul>
      </div>

      <!-- Part 5 Navigation -->
      <div class="nav-part-group">
        <div class="nav-part-header part-5-header">
          <span>🟪 PHẦN 5: PATTERNS & GENAI</span>
        </div>
        <ul class="nav-list">
          <li class="nav-item">
            <a href="#gof-patterns" class="nav-link">
              <span class="nav-ch-badge">GoF</span>
              <span>23 Mẫu Thiết Kế Gang of Four</span>
            </a>
          </li>
          <li class="nav-item">
            <a href="#genai-architecture" class="nav-link">
              <span class="nav-ch-badge">GenAI</span>
              <span>Ứng Dụng AI Trong Thiết Kế</span>
            </a>
          </li>
        </ul>
      </div>

      <!-- Interactive Tools Link -->
      <div class="nav-part-group">
        <div class="nav-part-header" style="background: var(--bg-surface-subtle); color: var(--accent-primary);">
          <span>⚡ CÔNG CỤ & QUIZ TRẮC NGHIỆM</span>
        </div>
        <ul class="nav-list">
          <li class="nav-item">
            <a href="#tool-pattern-explorer" class="nav-link">
              <span class="nav-ch-badge">Tool 1</span>
              <span>Tra Cứu 23 GoF Patterns</span>
            </a>
          </li>
          <li class="nav-item">
            <a href="#tool-arch-comparator" class="nav-link">
              <span class="nav-ch-badge">Tool 2</span>
              <span>So Sánh Đánh Đổi Kiến Trúc</span>
            </a>
          </li>
          <li class="nav-item">
            <a href="#tool-metrics-calc" class="nav-link">
              <span class="nav-ch-badge">Tool 3</span>
              <span>Tính Sẵn Sàng & Schedulability</span>
            </a>
          </li>
          <li class="nav-item">
            <a href="#tool-quiz" class="nav-link">
              <span class="nav-ch-badge">Quiz</span>
              <span>Đề Thi Trắc Nghiệm 25 Câu</span>
            </a>
          </li>
        </ul>
      </div>
    </aside>

    <!-- Mobile Drawer Overlay -->
    <div id="drawerOverlay" class="drawer-overlay" onclick="toggleMobileNav()"></div>

    <!-- Master Main Content -->
    <main class="master-main">
      <!-- Hero Banner -->
      <div class="hero-banner">
        <div class="hero-tag">🎓 ĐẠI HỌC FPT &bull; SWD392 SOFTWARE ARCHITECTURE &amp; DESIGN</div>
        <h1 class="hero-title">Cẩm Nang Toàn Diện Kiến Trúc &amp; Thiết Kế Phần Mềm</h1>
        <p class="hero-desc">
          Tài liệu tổng hợp học tập và ôn thi chuyên sâu <strong>chuẩn 100% nội dung học phần SWD392</strong> theo giáo trình quốc tế của <em>Giáo sư Hassan Gomaa</em>. 
          Tích hợp đầy đủ lý thuyết 24 bài giảng, hệ thống ký hiệu UML 2.5.1, phân tích Use Case &amp; Statechart, kiến trúc Client/Server, SOA, CBD, Real-Time, 23 mẫu thiết kế Gang of Four (GoF), công nghệ GenAI hiện đại và 5 Case Studies thực chiến.
        </p>

        <div class="hero-stats-grid">
          <div class="hero-stat-card">
            <div class="hero-stat-value" style="color: #0284c7;">24</div>
            <div class="hero-stat-label">Chương Học &amp; Slide Đầy Đủ</div>
          </div>
          <div class="hero-stat-card">
            <div class="hero-stat-value" style="color: #4f46e5;">23</div>
            <div class="hero-stat-label">Mẫu Thiết Kế GoF Patterns</div>
          </div>
          <div class="hero-stat-card">
            <div class="hero-stat-value" style="color: #059669;">5</div>
            <div class="hero-stat-label">Nghiên Cứu Điển Hình (Case Studies)</div>
          </div>
          <div class="hero-stat-card">
            <div class="hero-stat-value" style="color: #d97706;">50+</div>
            <div class="hero-stat-label">Sơ Đồ SVG &amp; Công Thức KaTeX</div>
          </div>
          <div class="hero-stat-card">
            <div class="hero-stat-value" style="color: #7c3aed;">25</div>
            <div class="hero-stat-label">Câu Hỏi Quiz Chấm Điểm Tức Thì</div>
          </div>
        </div>

        <div class="quick-jumps-row">
          <span class="quick-jump-label">Truy cập nhanh:</span>
          <a href="#part-1" class="quick-pill">Phần 1: Tổng Quan (Ch 1-5)</a>
          <a href="#part-2" class="quick-pill">Phần 2: Mô Hình Hóa UML (Ch 6-11)</a>
          <a href="#part-3" class="quick-pill">Phần 3: Thiết Kế Kiến Trúc (Ch 12-18)</a>
          <a href="#part-4" class="quick-pill">Phần 4: Case Studies (Ch 20-24 &amp; FOS)</a>
          <a href="#gof-patterns" class="quick-pill">23 GoF Patterns</a>
          <a href="#genai-architecture" class="quick-pill">GenAI trong Thiết Kế</a>
          <a href="#tool-quiz" class="quick-pill" style="border-color: #10b981; color: #059669;">Làm Quiz Trắc Nghiệm 📝</a>
        </div>
      </div>

      <!-- Parts Content -->
<!-- [[PART1_INJECTION]] -->
<!-- [[PART2_INJECTION]] -->
<!-- [[PART3_INJECTION]] -->
<!-- [[PART4_INJECTION]] -->
<!-- [[PART5_INJECTION]] -->
<!-- [[TOOLS_INJECTION]] -->

      <!-- Master Footer -->
      <footer style="margin-top: 4rem; padding-top: 2rem; border-top: 1px solid var(--border-color); text-align: center; font-size: 0.88rem; color: var(--text-muted);">
        <p style="margin-bottom: 0.5rem;">
          <strong>SWD392 Master Study Guide</strong> &bull; Kiến Trúc &amp; Thiết Kế Phần Mềm
        </p>
        <p style="margin-bottom: 0.5rem;">
          Dựa trên giáo trình chuẩn mực <em>"Software Modeling and Design: UML, Use Cases, Patterns, and Software Architectures"</em> &mdash; GS. Hassan Gomaa (Cambridge University Press).
        </p>
        <p>
          Hệ thống được thiết kế theo chuẩn Zero-Build Monolithic SPA, giao diện Light/Dark Mode tương thích hoàn toàn trên mọi trình duyệt hiện đại.
        </p>
      </footer>
    </main>
  </div>

  <!-- Floating Action Dock -->
  <div class="floating-dock">
    <button id="scrollTopBtn" class="scroll-top-btn" onclick="scrollToTop()" title="Cuộn lên đầu trang">⬆</button>
  </div>

  <!-- Client-side Scripts -->
  <script>
/* [[JS_INJECTION]] */
  </script>
</body>
</html>
"""

    return template.replace('/* [[CSS_INJECTION]] */', css) \
                   .replace('<!-- [[PART1_INJECTION]] -->', part1_html) \
                   .replace('<!-- [[PART2_INJECTION]] -->', part2_html) \
                   .replace('<!-- [[PART3_INJECTION]] -->', part3_html) \
                   .replace('<!-- [[PART4_INJECTION]] -->', part4_html) \
                   .replace('<!-- [[PART5_INJECTION]] -->', part5_html) \
                   .replace('<!-- [[TOOLS_INJECTION]] -->', tools_html) \
                   .replace('/* [[JS_INJECTION]] */', js)

