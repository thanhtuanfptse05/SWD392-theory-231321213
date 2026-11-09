# _generator/tools_and_quiz.py
# Interactive Tools & Multi-Chapter Quiz Engine

def get_tools_and_quiz_html():
    return r"""
<!-- ========================================== -->
<!-- TRUNG TÂM CÔNG CỤ TƯƠNG TÁC & ÔN TẬP QUIZ -->
<!-- ========================================== -->
<div id="interactive-tools" class="part-divider-banner part-5-banner" style="background: linear-gradient(135deg, #1e1b4b, #312e81); color: white; border-color: #4338ca;">
  <span class="part-badge-tag" style="background: #6366f1; color: white;">Interactive Suite</span>
  <h2 class="part-title" style="color: white;">Trung Tâm Công Cụ Mô Phỏng &amp; Đề Thi Trắc Nghiệm</h2>
  <p class="part-desc" style="color: #cbd5e1;">
    Thực hành tương tác trực quan với 4 module ứng dụng mini: Trình tra cứu 23 Mẫu thiết kế GoF, Bảng so sánh đánh đổi 5 phong cách kiến trúc, Bộ tính toán chỉ số chất lượng &amp; lập lịch thời gian thực RMA, và Hệ thống đề thi trắc nghiệm toàn diện 25 câu hỏi có chấm điểm tức thì.
  </p>
</div>

<!-- MODULE 1: GOF PATTERN EXPLORER -->
<section id="tool-pattern-explorer" class="interactive-tool-box">
  <div class="tool-header">
    <div class="tool-title">🔍 Module 1: Trình Tra Cứu Tương Tác 23 Mẫu Thiết Kế GoF</div>
    <div class="tool-desc">Lọc nhanh theo nhóm khởi tạo (Creational), cấu trúc (Structural), hành vi (Behavioral) và tìm kiếm theo từ khóa</div>
  </div>

  <div class="pattern-filter-tabs">
    <button class="filter-btn active" onclick="filterPatterns('all')">Tất Cả (23 Mẫu)</button>
    <button class="filter-btn" onclick="filterPatterns('creational')">Creational (5 Mẫu)</button>
    <button class="filter-btn" onclick="filterPatterns('structural')">Structural (7 Mẫu)</button>
    <button class="filter-btn" onclick="filterPatterns('behavioral')">Behavioral (11 Mẫu)</button>
    <input type="text" id="patternSearchInput" placeholder="Gõ tên pattern (ví dụ: Singleton, Observer, Factory)..." 
           style="flex: 1; min-width: 200px; height: 36px; padding: 0 0.85rem; border-radius: var(--radius-full); border: 1px solid var(--border-color); background: var(--bg-surface-subtle); color: var(--text-primary); font-size: 0.85rem;"
           oninput="searchPatterns(this.value)">
  </div>

  <div id="patternsGrid" class="patterns-grid">
    <!-- Populated dynamically via JS -->
  </div>
</section>

<!-- MODULE 2: ARCHITECTURE COMPARATOR -->
<section id="tool-arch-comparator" class="interactive-tool-box">
  <div class="tool-header">
    <div class="tool-title">⚖️ Module 2: Bảng So Sánh &amp; Phân Tích Đánh Đổi 5 Phong Cách Kiến Trúc</div>
    <div class="tool-desc">Nhấp chọn phong cách kiến trúc để xem thang điểm định lượng trên 5 tiêu chí chất lượng then chốt</div>
  </div>

  <div class="arch-select-row">
    <button class="arch-choice-btn active" onclick="selectArch('monolith')">1. Monolith (Đơn Khối)</button>
    <button class="arch-choice-btn" onclick="selectArch('client-server')">2. 3-Tier Client / Server</button>
    <button class="arch-choice-btn" onclick="selectArch('soa')">3. SOA (Hướng Dịch Vụ)</button>
    <button class="arch-choice-btn" onclick="selectArch('microservices')">4. Microservices (Vi Dịch Vụ)</button>
    <button class="arch-choice-btn" onclick="selectArch('realtime')">5. Real-Time Concurrent</button>
  </div>

  <div id="archDetailContainer" class="arch-detail-view">
    <!-- Populated dynamically via JS -->
  </div>
</section>

<!-- MODULE 3: METRICS & SCHEDULABILITY CALCULATOR -->
<section id="tool-metrics-calc" class="interactive-tool-box">
  <div class="tool-header">
    <div class="tool-title">🧮 Module 3: Bộ Tính Toán Chỉ Số Chất Lượng &amp; Lập Lịch RMA</div>
    <div class="tool-desc">Tính toán độ sẵn sàng hệ thống (Availability) và kiểm chứng cận trên lập lịch thời gian thực Rate Monotonic Analysis</div>
  </div>

  <div class="calc-grid">
    <!-- Tool A: Availability -->
    <div class="calc-card">
      <h4 style="margin-bottom: 0.5rem; color: #0284c7;">1. Tính Độ Sẵn Sàng (System Availability)</h4>
      <p style="font-size: 0.82rem; color: var(--text-muted); margin-bottom: 1rem;">Công thức: $A = \frac{\text{MTTF}}{\text{MTTF} + \text{MTTR}} \times 100\%$</p>
      
      <div class="calc-input-group">
        <label class="calc-label">MTTF (Giờ hoạt động không lỗi trung bình):</label>
        <input type="number" id="calcMTTF" class="calc-input" value="990">
      </div>
      <div class="calc-input-group">
        <label class="calc-label">MTTR (Giờ sửa chữa trung bình khi gặp lỗi):</label>
        <input type="number" id="calcMTTR" class="calc-input" value="10">
      </div>
      <button class="calc-btn" onclick="computeAvailability()">Tính Toán Tính Sẵn Sàng</button>
      <div id="availResult" class="calc-result-box" style="display:none;"></div>
    </div>

    <!-- Tool B: RMA Schedulability -->
    <div class="calc-card">
      <h4 style="margin-bottom: 0.5rem; color: #059669;">2. Kiểm Chứng Lập Lịch RMA (Real-Time RMA Bound)</h4>
      <p style="font-size: 0.82rem; color: var(--text-muted); margin-bottom: 1rem;">Cận trên Liu &amp; Layland: $U \le n(2^{1/n} - 1)$</p>
      
      <div class="calc-input-group">
        <label class="calc-label">Số lượng tác vụ định kỳ ($n$):</label>
        <input type="number" id="calcRMA_N" class="calc-input" value="3" min="1" max="10">
      </div>
      <div class="calc-input-group">
        <label class="calc-label">Tổng hệ số sử dụng CPU thực tế $U = \sum \frac{C_i}{T_i}$ (%):</label>
        <input type="number" id="calcRMA_U" class="calc-input" value="72" min="1" max="100">
      </div>
      <button class="calc-btn" style="background: #059669;" onclick="computeRMA()">Kiểm Chứng Schedulability</button>
      <div id="rmaResult" class="calc-result-box" style="display:none;"></div>
    </div>
  </div>
</section>

<!-- MODULE 4: MULTI-CHAPTER QUIZ -->
<section id="tool-quiz" class="interactive-tool-box">
  <div class="tool-header">
    <div class="tool-title">📝 Module 4: Hệ Thống Đề Thi Trắc Nghiệm Tổng Hợp 25 Câu Hỏi</div>
    <div class="tool-desc">Bộ đề trắc nghiệm chuẩn hóa kiểm tra toàn diện 100% kiến thức từ Chương 1 đến Chương 24, GoF Patterns và GenAI</div>
  </div>

  <div class="quiz-box">
    <div class="quiz-meta-row">
      <span>Câu hỏi số <strong id="quizQIndex" class="quiz-q-num">1</strong> / <span id="quizTotalQ">25</span></span>
      <span>Điểm số hiện tại: <strong id="quizScoreText" style="color: #10b981;">0 / 0</strong></span>
    </div>

    <div id="quizQuestionText" class="quiz-question-text">
      Đang tải câu hỏi...
    </div>

    <div id="quizOptionsList" class="quiz-options-list">
      <!-- Generated via JS -->
    </div>

    <div id="quizExplanation" class="quiz-explanation-box">
      <!-- Explanation text -->
    </div>

    <div class="quiz-footer-actions">
      <button class="filter-btn" onclick="restartQuiz()">Làm Lại Từ Đầu ↺</button>
      <button id="quizNextBtn" class="quiz-nav-btn" style="display: none;" onclick="nextQuestion()">Câu Tiếp Theo &rarr;</button>
    </div>
  </div>
</section>
"""

