# _generator/part1.py
# Part 1: Tổng Quan & Nền Tảng Thiết Kế Phần Mềm (Chương 1 - 5)

def get_part1_html():
    return r"""
<!-- ========================================== -->
<!-- PART 1 DIVIDER BANNER -->
<!-- ========================================== -->
<div id="part-1" class="part-divider-banner part-1-banner">
  <span class="part-badge-tag">Phần 1 &bull; Nền Tảng Cốt Lõi</span>
  <h2 class="part-title">Tổng Quan & Nền Tảng Thiết Kế Phần Mềm</h2>
  <p class="part-desc">
    Khám phá các nguyên lý nền tảng của mô hình hóa phần mềm hướng đối tượng (OO Modeling), hệ thống ký hiệu chuẩn UML 2.5.1, các mô hình vòng đời phát triển phần mềm (Waterfall, Prototyping, Spiral, RUP), các khái niệm thiết kế kiến trúc then chốt (Information Hiding, Encapsulation, Concurrency) và phương pháp luận COMET độc quyền của Hassan Gomaa.
  </p>
</div>

<!-- ========================================== -->
<!-- CHƯƠNG 1 -->
<!-- ========================================== -->
<section id="ch01" class="chapter-section">
  <div class="chapter-header">
    <div class="chapter-badge-row">
      <span class="chapter-badge">CHƯƠNG 01</span>
      <span class="chapter-lecturer-tag">SWD392 &bull; Hassan Gomaa Edition</span>
    </div>
    <h2 class="chapter-title">Giới Thiệu Thiết Kế & Mô Hình Hóa Phần Mềm</h2>
    <div class="chapter-subtitle">Software Modeling, OO Methods, Architecture & Multiple Views</div>
  </div>

  <div class="card-grid">
    <div class="card">
      <div class="card-title">🎯 1. Bản Chất Của Mô Hình Hóa Phần Mềm</div>
      <div class="card-content">
        <p><strong>Mô hình hóa (Software Modeling)</strong> là quá trình thiết kế các ứng dụng phần mềm trước khi viết mã nguồn thực tế (Coding). Mô hình là một bản trừu tượng hóa có cấu trúc của hệ thống, giúp các kỹ sư:</p>
        <ul style="padding-left: 1.2rem; margin-top: 0.5rem;">
          <li>Phân tích yêu cầu và hành vi hệ thống trước khi hiện thực.</li>
          <li>Giảm thiểu rủi ro kiến trúc và chi phí sửa lỗi ở giai đoạn muộn.</li>
          <li>Định hướng và làm kim chỉ nam cho việc triển khai code phía sau.</li>
          <li>Ngôn ngữ đồ họa như <strong>UML</strong> giúp các bên liên quan (Stakeholders) dễ dàng giao tiếp và thống nhất góc nhìn.</li>
        </ul>
      </div>
    </div>

    <div class="card">
      <div class="card-title">💎 2. Phương Pháp Hướng Đối Tượng & UML</div>
      <div class="card-content">
        <p>Các phương pháp hướng đối tượng giải quyết bài toán sống còn về <em>khả năng sửa đổi (Modifiability)</em>, <em>khả năng thích ứng (Adaptation)</em> và <em>tiến hóa (Evolution)</em> của hệ thống thông qua 3 trụ cột:</p>
        <ul style="padding-left: 1.2rem; margin-top: 0.5rem;">
          <li><strong>Che giấu thông tin (Information Hiding)</strong>: Đóng gói chi tiết hiện thực bên trong.</li>
          <li><strong>Lớp & Đối tượng (Classes & Objects)</strong>: Khuôn mẫu và thể hiện cụ thể.</li>
          <li><strong>Kế thừa (Inheritance)</strong>: Tái sử dụng cấu trúc và hành vi.</li>
          <li><strong>UML (Unified Modeling Language)</strong>: Ngôn ngữ mô hình hóa đồ họa chuẩn hóa quốc tế (chuẩn ISO/IEC 19505, phiên bản hiện hành UML 2.5.1).</li>
        </ul>
      </div>
    </div>

    <div class="card">
      <div class="card-title">🏛️ 3. Thiết Kế Kiến Trúc Phần Mềm</div>
      <div class="card-content">
        <p>Thường được gọi là <strong>Thiết Kế Cấp Cao (High-Level Design)</strong>:</p>
        <ul style="padding-left: 1.2rem; margin-top: 0.5rem;">
          <li>Mô tả cách thức <strong>phân rã hệ thống phần mềm thành các hệ thống con (Subsystems)</strong> độc lập tương đối.</li>
          <li>Thiết lập hợp đồng giao tiếp (Interfaces & Connectors) giữa các hệ thống con.</li>
          <li>Trực tiếp định hình và thỏa mãn các <strong>thuộc tính chất lượng (Software Quality Attributes)</strong> như hiệu năng, khả năng mở rộng, tính sẵn sàng và bảo mật.</li>
          <li>Là tiền đề bắt buộc cho Thiết kế chi tiết (Detailed Design) và Phân rã thành Modules/Components.</li>
        </ul>
      </div>
    </div>
  </div>

  <div class="topic-card">
    <div class="topic-title">📚 4 Khái Niệm Phân Biệt Cốt Lõi Trong Thiết Kế</div>
    <div class="table-wrap">
      <table class="styled-table">
        <thead>
          <tr>
            <th>Thuật Ngữ</th>
            <th>Bản Chất & Định Nghĩa</th>
            <th>Ví Dụ Thực Tế</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Software Design Notation</strong> (Ký hiệu thiết kế)</td>
            <td>Ngôn ngữ đồ họa hoặc văn bản dùng để biểu diễn các thành phần và quan hệ trong thiết kế.</td>
            <td>Biểu đồ lớp UML (Class Diagram), Biểu đồ tuần tự (Sequence Diagram), Biểu đồ trạng thái.</td>
          </tr>
          <tr>
            <td><strong>Software Design Concept</strong> (Khái niệm thiết kế)</td>
            <td>Ý tưởng căn bản, triết lý nền tảng được áp dụng xuyên suốt khi xây dựng hệ thống.</td>
            <td>Che giấu thông tin (Information Hiding), Đóng gói (Encapsulation), Trừu tượng hóa dữ liệu (Data Abstraction).</td>
          </tr>
          <tr>
            <td><strong>Software Design Strategy</strong> (Chiến lược thiết kế)</td>
            <td>Kế hoạch và định hướng tổng thể để phát triển một bản thiết kế phần mềm.</td>
            <td>Phân rã hướng đối tượng (Object-Oriented Decomposition), Phân tầng kiến trúc (Layered Architecture).</td>
          </tr>
          <tr>
            <td><strong>Software Structuring Criteria</strong> (Tiêu chí cấu trúc hóa)</td>
            <td>Các quy tắc kinh nghiệm (Heuristics) hoặc hướng dẫn cụ thể giúp kiến trúc sư phân rã hệ thống thành các đối tượng/thành phần.</td>
            <td>Tiêu chí cấu trúc hóa đối tượng (Object Structuring Criteria: Boundary, Entity, Control).</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>

  <!-- SVG Diagram 1: Multiple Views of Software Architecture -->
  <div class="diagram-card">
    <div class="svg-container">
      <svg viewBox="0 0 880 320" xmlns="http://www.w3.org/2000/svg" style="font-family: 'Plus Jakarta Sans', sans-serif;">
        <rect width="880" height="320" rx="14" fill="#ffffff" stroke="#e2e8f0" stroke-width="2"/>
        <text x="440" y="32" text-anchor="middle" font-size="16" font-weight="800" fill="#0f172a">7 GÓC NHÌN KIẾN TRÚC PHẦN MỀM TRONG PHƯƠNG PHÁP COMET (MULTIPLE VIEWS)</text>
        
        <!-- Center Hub -->
        <rect x="360" y="125" width="160" height="70" rx="10" fill="#2563eb" stroke="#1d4ed8" stroke-width="2"/>
        <text x="440" y="155" text-anchor="middle" font-size="14" font-weight="800" fill="#ffffff">SOFTWARE</text>
        <text x="440" y="175" text-anchor="middle" font-size="13" font-weight="700" fill="#ffffff">ARCHITECTURE</text>
        
        <!-- View Nodes -->
        <!-- 1. Use Case View -->
        <rect x="40" y="60" width="180" height="50" rx="8" fill="#e0f2fe" stroke="#0284c7" stroke-width="1.5"/>
        <text x="130" y="82" text-anchor="middle" font-size="12" font-weight="700" fill="#0369a1">1. Use Case View</text>
        <text x="130" y="98" text-anchor="middle" font-size="10.5" fill="#475569">Use Case Diagrams</text>
        <line x1="220" y1="85" x2="360" y2="140" stroke="#0284c7" stroke-width="1.5" stroke-dasharray="4,4"/>

        <!-- 2. Static View -->
        <rect x="40" y="135" width="180" height="50" rx="8" fill="#eef2ff" stroke="#4f46e5" stroke-width="1.5"/>
        <text x="130" y="157" text-anchor="middle" font-size="12" font-weight="700" fill="#4338ca">2. Static View</text>
        <text x="130" y="173" text-anchor="middle" font-size="10.5" fill="#475569">Class Diagrams</text>
        <line x1="220" y1="160" x2="360" y2="160" stroke="#4f46e5" stroke-width="1.5"/>

        <!-- 3. Dynamic Interaction View -->
        <rect x="40" y="210" width="180" height="50" rx="8" fill="#d1fae5" stroke="#059669" stroke-width="1.5"/>
        <text x="130" y="232" text-anchor="middle" font-size="12" font-weight="700" fill="#047857">3. Dynamic Interaction</text>
        <text x="130" y="248" text-anchor="middle" font-size="10.5" fill="#475569">Sequence / Comm Diag</text>
        <line x1="220" y1="235" x2="360" y2="180" stroke="#059669" stroke-width="1.5" stroke-dasharray="4,4"/>

        <!-- 4. Dynamic State Machine View -->
        <rect x="660" y="60" width="180" height="50" rx="8" fill="#fef3c7" stroke="#d97706" stroke-width="1.5"/>
        <text x="750" y="82" text-anchor="middle" font-size="12" font-weight="700" fill="#b45309">4. State Machine View</text>
        <text x="750" y="98" text-anchor="middle" font-size="10.5" fill="#475569">Statecharts (FSM)</text>
        <line x1="660" y1="85" x2="520" y2="140" stroke="#d97706" stroke-width="1.5" stroke-dasharray="4,4"/>

        <!-- 5. Structural Component View -->
        <rect x="660" y="135" width="180" height="50" rx="8" fill="#ede9fe" stroke="#7c3aed" stroke-width="1.5"/>
        <text x="750" y="157" text-anchor="middle" font-size="12" font-weight="700" fill="#6d28d9">5. Structural Component</text>
        <text x="750" y="173" text-anchor="middle" font-size="10.5" fill="#475569">Structured Class Diag</text>
        <line x1="660" y1="160" x2="520" y2="160" stroke="#7c3aed" stroke-width="1.5"/>

        <!-- 6. Dynamic Concurrent View -->
        <rect x="660" y="210" width="180" height="50" rx="8" fill="#fee2e2" stroke="#dc2626" stroke-width="1.5"/>
        <text x="750" y="232" text-anchor="middle" font-size="12" font-weight="700" fill="#b91c1c">6. Concurrent View</text>
        <text x="750" y="248" text-anchor="middle" font-size="10.5" fill="#475569">Concurrent Comm Diag</text>
        <line x1="660" y1="235" x2="520" y2="180" stroke="#dc2626" stroke-width="1.5" stroke-dasharray="4,4"/>

        <!-- 7. Deployment View (Bottom) -->
        <rect x="350" y="245" width="180" height="48" rx="8" fill="#f1f5f9" stroke="#64748b" stroke-width="1.5"/>
        <text x="440" y="266" text-anchor="middle" font-size="12" font-weight="700" fill="#334155">7. Deployment View</text>
        <text x="440" y="282" text-anchor="middle" font-size="10.5" fill="#64748b">Deployment Diagrams</text>
        <line x1="440" y1="195" x2="440" y2="245" stroke="#64748b" stroke-width="1.5"/>
      </svg>
    </div>
    <div class="diagram-caption">Sơ đồ 1.1: 7 Góc nhìn đa chiều (Multiple Views) của Kiến trúc phần mềm theo phương pháp COMET</div>
  </div>
</section>

<!-- ========================================== -->
<!-- CHƯƠNG 2 -->
<!-- ========================================== -->
<section id="ch02" class="chapter-section">
  <div class="chapter-header">
    <div class="chapter-badge-row">
      <span class="chapter-badge">CHƯƠNG 02</span>
      <span class="chapter-lecturer-tag">UML Standard 2.5.1</span>
    </div>
    <h2 class="chapter-title">Tổng Quan Hệ Thống Ký Hiệu Chuẩn UML</h2>
    <div class="chapter-subtitle">UML Diagrams, Relationships, Visibility, Stereotypes & Constraints</div>
  </div>

  <div class="card-grid">
    <div class="card">
      <div class="card-title">👥 Use Case & Actor</div>
      <div class="card-content">
        <p><strong>Actor</strong>: Đại diện cho một vai trò của người dùng bên ngoài, hệ thống ngoài, hoặc thiết bị I/O/Timer tương tác với hệ thống. Luôn nằm <em>ngoài phạm vi hệ thống</em>.</p>
        <p><strong>Use Case</strong>: Định nghĩa một chuỗi tương tác hoàn chỉnh giữa tác nhân và hệ thống, mang lại một kết quả có giá trị cho tác nhân.</p>
      </div>
    </div>

    <div class="card">
      <div class="card-title">📦 Classes vs Objects</div>
      <div class="card-content">
        <p>Để phân biệt giữa <strong>Lớp</strong> (kiểu dữ liệu) và <strong>Đối tượng</strong> (thể hiện cụ thể):</p>
        <ul style="padding-left: 1.2rem;">
          <li>Tên đối tượng luôn được <u>gạch chân</u> trong biểu đồ UML.</li>
          <li>Cú pháp đầy đủ: <code><u>tênĐốiTượng : TênLớp</u></code> (Ví dụ: <code><u>currentAccount : Account</u></code>).</li>
          <li>Đối tượng ẩn danh: <code><u>: Account</u></code>.</li>
        </ul>
      </div>
    </div>

    <div class="card">
      <div class="card-title">👁️ Mức Độ Hiển Thị (Visibility)</div>
      <div class="card-content">
        <ul style="padding-left: 1.2rem;">
          <li><code>+</code> <strong>Public</strong>: Phần tử có thể truy cập tự do từ bất kỳ đâu bên ngoài lớp.</li>
          <li><code>-</code> <strong>Private</strong>: Chỉ có thể truy cập từ bên trong chính lớp định nghĩa nó (che giấu hoàn toàn).</li>
          <li><code>#</code> <strong>Protected</strong>: Truy cập được bên trong lớp định nghĩa và tất cả các lớp con kế thừa từ nó.</li>
          <li><code>~</code> <strong>Package</strong>: Truy cập được bởi các lớp nằm cùng gói (Package).</li>
        </ul>
      </div>
    </div>
  </div>

  <div class="topic-card">
    <div class="topic-title">🔗 Các Quan Hệ Cốt Lõi Trên Biểu Đồ Lớp (Class Relationships)</div>
    <div class="table-wrap">
      <table class="styled-table">
        <thead>
          <tr>
            <th>Quan Hệ</th>
            <th>Ký Hiệu Đồ Họa</th>
            <th>Bản Chất Ngữ Nghĩa</th>
            <th>Bội Số (Multiplicity) & Quy Tắc Vòng Đời</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Association</strong> (Liên kết)</td>
            <td>Đường nối liền nét (có thể có mũi tên điều hướng).</td>
            <td>Quan hệ cấu trúc tĩnh giữa 2 hay nhiều lớp. Thể hiện một lớp "biết" hoặc "làm việc với" lớp kia.</td>
            <td><code>1</code>, <code>0..1</code>, <code>*</code> hoặc <code>0..*</code>, <code>1..*</code>. Thể hiện số lượng instance tham gia.</td>
          </tr>
          <tr>
            <td><strong>Aggregation</strong> (Thu gom / Tụ hợp)</td>
            <td>Hình thoi <strong>rỗng</strong> ở phía lớp Toàn thể (Whole).</td>
            <td>Quan hệ Toàn thể / Bộ phận (Whole/Part) lỏng lẻo. Bộ phận có thể tồn tại độc lập khi Toàn thể bị hủy.</td>
            <td>Ví dụ: <code>Department</code> và <code>Employee</code>. Phòng ban giải tán, nhân viên vẫn tồn tại.</td>
          </tr>
          <tr>
            <td><strong>Composition</strong> (Hợp thành / Cấu thành)</td>
            <td>Hình thoi <strong>đặc</strong> ở phía lớp Toàn thể (Whole).</td>
            <td>Quan hệ Toàn thể / Bộ phận chặt chẽ. Bộ phận được sinh ra, sống và <em>chết cùng</em> với Toàn thể.</td>
            <td>Ví dụ: <code>Order</code> và <code>OrderItem</code>. Đơn hàng bị xóa thì các dòng hàng chi tiết lập tức bị hủy.</td>
          </tr>
          <tr>
            <td><strong>Generalization</strong> (Kế thừa / Tổng quát hóa)</td>
            <td>Đường liền nét với <strong>tam giác rỗng</strong> trỏ về phía Lớp cha (Superclass).</td>
            <td>Quan hệ "Is-a" (Là một). Lớp con kế thừa toàn bộ thuộc tính và phương thức của lớp cha, đồng thời có thể mở rộng.</td>
            <td>Ví dụ: <code>SavingsAccount</code> là một <code>Account</code>.</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>

  <div class="callout callout-info">
    <div class="callout-title">🛠️ 3 Cơ Chế Mở Rộng Của UML (UML Extension Mechanisms)</div>
    <ul style="padding-left: 1.2rem;">
      <li><strong>Stereotypes (&laquo;stereotype&raquo;)</strong>: Định nghĩa một khối xây dựng mới phái sinh từ phần tử UML có sẵn để biểu diễn mục đích chuyên biệt (Ví dụ: <code>&laquo;entity&raquo;</code>, <code>&laquo;boundary&raquo;</code>, <code>&laquo;control&raquo;</code>, <code>&laquo;subsystem&raquo;</code>).</li>
      <li><strong>Tagged Values ({tag = value})</strong>: Bổ sung thuộc tính mới có cấu trúc vào phần tử mô hình (Ví dụ: <code>{version = 2.1, author = "Gomaa"}</code>).</li>
      <li><strong>Constraints ({constraint})</strong>: Đặc tả điều kiện logic hoặc quy tắc ràng buộc nghiệp vụ phải luôn đúng (Ví dụ: <code>{balance &gt;= 0}</code>, <code>{ordered}</code>).</li>
    </ul>
  </div>
</section>

<!-- ========================================== -->
<!-- CHƯƠNG 3 -->
<!-- ========================================== -->
<section id="ch03" class="chapter-section">
  <div class="chapter-header">
    <div class="chapter-badge-row">
      <span class="chapter-badge">CHƯƠNG 03</span>
      <span class="chapter-lecturer-tag">Software Engineering Processes</span>
    </div>
    <h2 class="chapter-title">Mô Hình Vòng Đời & Quy Trình Phát Triển Phần Mềm</h2>
    <div class="chapter-subtitle">Waterfall, Prototyping, Incremental, Spiral, RUP & V&V</div>
  </div>

  <div class="card-grid">
    <div class="card">
      <div class="card-title">🌊 Mô Hình Thác Nước (Waterfall Model)</div>
      <div class="card-content">
        <p>Mô hình tuần tự tuyến tính kinh điển:</p>
        <ul style="padding-left: 1.2rem;">
          <li><strong>Quy trình</strong>: Phân tích yêu cầu &rarr; Thiết kế hệ thống &rarr; Hiện thực (Code) &rarr; Tích hợp & Kiểm thử &rarr; Vận hành & Bảo trì.</li>
          <li><strong>Hạn chế chí mạng</strong>: Thiếu tính lặp thực tế, không cho phép phản hồi sớm từ người dùng, rủi ro phát hiện lỗi kiến trúc quá muộn ở khâu kiểm thử.</li>
          <li><strong>Cải tiến</strong>: Waterfall có vòng lặp phản hồi (Iteration between adjacent phases).</li>
        </ul>
      </div>
    </div>

    <div class="card">
      <div class="card-title">🧪 Tạo Bản Mẫu Thử Nghiệm (Prototyping)</div>
      <div class="card-content">
        <p><strong>Throwaway Prototyping (Bản mẫu bỏ đi)</strong>:</p>
        <ul style="padding-left: 1.2rem;">
          <li><em>Requirements Prototyping</em>: Xây dựng giao diện nhanh nhằm chốt chính xác yêu cầu mơ hồ từ người dùng, sau đó vứt bỏ mã nguồn tạm.</li>
          <li><em>Architectural Prototyping</em>: Thử nghiệm giải pháp kỹ thuật, đánh giá hiệu năng chịu tải, kết nối phần cứng trước khi chốt kiến trúc.</li>
          <li><strong>Evolutionary Prototyping</strong>: Bản mẫu được giữ lại và phát triển dần thành sản phẩm hoàn chỉnh thông qua các phân đoạn gia tăng (Incremental).</li>
        </ul>
      </div>
    </div>

    <div class="card">
      <div class="card-title">🌀 Mô Hình Xoắn Ốc (Spiral Model - Boehm)</div>
      <div class="card-content">
        <p>Quy trình lặp có định hướng <strong>quản trị rủi ro (Risk-Driven)</strong> gồm 4 góc phần tư:</p>
        <ol style="padding-left: 1.2rem;">
          <li><strong>Q1</strong>: Xác định mục tiêu, giải pháp thay thế và ràng buộc.</li>
          <li><strong>Q2</strong>: Đánh giá phương án thay thế, nhận diện và giải quyết rủi ro (Tạo prototype).</li>
          <li><strong>Q3</strong>: Phát triển và thẩm định sản phẩm mức kế tiếp.</li>
          <li><strong>Q4</strong>: Lập kế hoạch chi tiết cho chu kỳ xoắn ốc tiếp theo.</li>
        </ol>
      </div>
    </div>
  </div>

  <div class="topic-card">
    <div class="topic-title">🏢 Quy Trình Hợp Nhất (Rational Unified Process - RUP)</div>
    <p>RUP (còn gọi là Unified Software Development Process - USDP) gồm <strong>4 Pha theo chiều ngang</strong> và <strong>5 Luồng công việc cốt lõi (Core Workflows) theo chiều dọc</strong>:</p>
    
    <div class="table-wrap">
      <table class="styled-table">
        <thead>
          <tr>
            <th>4 Pha Vòng Đời (Phases)</th>
            <th>Mục Tiêu Trọng Tâm</th>
            <th>Sản Phẩm Bàn Giao Cốt Lõi (Milestone)</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>1. Inception</strong> (Khởi tạo)</td>
            <td>Xác định phạm vi dự án, xây dựng Business Case, ước tính chi phí và rủi ro sơ bộ.</td>
            <td>Cột mốc Mục tiêu Vòng đời (Lifecycle Objectives Milestone).</td>
          </tr>
          <tr>
            <td><strong>2. Elaboration</strong> (Chi tiết hóa)</td>
            <td>Nắm bắt phần lớn yêu cầu (Use Cases), thiết lập <strong>Kiến trúc cơ sở (Architectural Baseline)</strong>, loại bỏ rủi ro lớn nhất.</td>
            <td>Cột mốc Kiến trúc Vòng đời (Lifecycle Architecture Milestone).</td>
          </tr>
          <tr>
            <td><strong>3. Construction</strong> (Xây dựng)</td>
            <td>Lập trình, tích hợp hàng loạt tính năng theo các phân đoạn gia tăng, hoàn thiện phần còn lại của hệ thống.</td>
            <td>Cột mốc Năng lực Vận hành Ban đầu (Initial Operational Capability).</td>
          </tr>
          <tr>
            <td><strong>4. Transition</strong> (Chuyển giao)</td>
            <td>Triển khai sản phẩm cho người dùng cuối, thử nghiệm Beta, đào tạo, tinh chỉnh lỗi thực tế.</td>
            <td>Cột mốc Phát hành Sản phẩm Hoàn chỉnh (Product Release Milestone).</td>
          </tr>
        </tbody>
      </table>
    </div>

    <div class="concept-box" style="margin-top: 1rem;">
      <div class="concept-title">⚖️ Phân Biệt Kiểm Định (Verification) vs Thẩm Định (Validation) - V&V</div>
      <ul style="padding-left: 1.2rem;">
        <li><strong>Verification (Kiểm định)</strong>: <em>"Are we building the product right?"</em> (Chúng ta có đang xây dựng sản phẩm đúng cách không?) &mdash; Đảm bảo mỗi giai đoạn thỏa mãn chính xác các đặc tả kỹ thuật đặt ra từ giai đoạn trước đó (Code khớp Design, Design khớp SRS).</li>
        <li><strong>Validation (Thẩm định)</strong>: <em>"Are we building the right product?"</em> (Chúng ta có đang xây dựng đúng sản phẩm khách hàng cần không?) &mdash; Đảm bảo phần mềm khi hoàn thành đáp ứng trọn vẹn mong đợi và nhu cầu thực tế của người dùng cuối.</li>
      </ul>
    </div>
  </div>
</section>

<!-- ========================================== -->
<!-- CHƯƠNG 4 -->
<!-- ========================================== -->
<section id="ch04" class="chapter-section">
  <div class="chapter-header">
    <div class="chapter-badge-row">
      <span class="chapter-badge">CHƯƠNG 04</span>
      <span class="chapter-lecturer-tag">Core Principles</span>
    </div>
    <h2 class="chapter-title">Khái Niệm Cốt Lõi Về Thiết Kế & Kiến Trúc Phần Mềm</h2>
    <div class="chapter-subtitle">Information Hiding, Concurrency, Classical Problems & Patterns Hierarchy</div>
  </div>

  <div class="card-grid">
    <div class="card">
      <div class="card-title">🛡️ Information Hiding & Encapsulation</div>
      <div class="card-content">
        <p><strong>Che giấu thông tin (David Parnas)</strong> là nguyên tắc căn bản nhất:</p>
        <ul style="padding-left: 1.2rem;">
          <li>Xác định những chi tiết dễ thay đổi (cấu trúc dữ liệu, thuật toán nội bộ, giao tiếp phần cứng) và giấu kín trong đối tượng.</li>
          <li>Khi nội bộ đối tượng thay đổi, <em>không có đối tượng nào khác bị ảnh hưởng</em>.</li>
          <li><strong>Data Abstraction</strong>: Lớp che giấu cấu trúc lưu trữ (mảng, con trỏ) và chỉ cung cấp giao diện thao tác (Ví dụ: Lớp <code>Stack</code> với các phương thức <code>push()</code>, <code>pop()</code>).</li>
        </ul>
      </div>
    </div>

    <div class="card">
      <div class="card-title">⚡ Ứng Dụng Tuần Tự vs Tương Tranh</div>
      <div class="card-content">
        <ul style="padding-left: 1.2rem;">
          <li><strong>Sequential Application</strong>: Chỉ có 1 luồng điều khiển (Single thread of control). Chỉ hỗ trợ truyền thông báo đồng bộ dạng gọi hàm/thủ tục (Call/Return).</li>
          <li><strong>Concurrent Application</strong>: Có nhiều đối tượng tương tranh (Active Objects / Threads / Tasks), mỗi đối tượng có luồng điều khiển độc lập và thực thi song song bất đồng bộ.</li>
          <li>Hỗ trợ cả thông điệp đồng bộ (chờ phản hồi) và bất đồng bộ (gửi qua hàng đợi buffer rồi tiếp tục chạy).</li>
        </ul>
      </div>
    </div>

    <div class="card">
      <div class="card-title">🧩 Thành Phần & Đầu Nối (Components & Connectors)</div>
      <div class="card-content">
        <ul style="padding-left: 1.2rem;">
          <li><strong>Component</strong>: Đơn vị phần mềm đóng gói, cung cấp giao diện cung cấp (Provided Interface) và yêu cầu (Required Interface).</li>
          <li><strong>Connector</strong>: Thực thể trung gian đóng gói giao thức truyền thông giữa hai hay nhiều components (ví dụ: RPC connector, Message Queue connector, Pipe connector).</li>
        </ul>
      </div>
    </div>
  </div>

  <div class="topic-card">
    <div class="topic-title">⚠️ 3 Bài Toán Tương Tranh Kinh Điển Trong Hệ Thống Thực Tế</div>
    <div class="card-grid">
      <div class="concept-box" style="border-left-color: #ef4444;">
        <div class="concept-title">1. Bài toán loại trừ lẫn nhau (Mutual Exclusion)</div>
        <p>Xảy ra khi nhiều tác vụ đồng thời muốn truy cập vào cùng một <em>tài nguyên dùng chung (Shared Resource / Critical Section)</em> như biến nhớ toàn cục hoặc thiết bị phần cứng. Nếu không khóa, dữ liệu sẽ bị xung đột và mất tính toàn vẹn (Race Condition). Giải pháp: Dùng <code>Mutex</code> hoặc <code>Semaphore</code>.</p>
      </div>

      <div class="concept-box" style="border-left-color: #f59e0b;">
        <div class="concept-title">2. Bài toán đồng bộ hóa (Synchronization)</div>
        <p>Xảy ra khi hai tác vụ cần phối hợp nhịp nhàng theo trình tự thời gian (Ví dụ: Tác vụ B chỉ được phép chạy sau khi tác vụ A hoàn tất một thao tác chuẩn bị). Giải pháp: Đồng bộ thông qua tín hiệu sự kiện (Event Signaling: <code>wait()</code> / <code>signal()</code>).</p>
      </div>

      <div class="concept-box" style="border-left-color: #10b981;">
        <div class="concept-title">3. Bài toán Sản xuất / Tiêu thụ (Producer / Consumer)</div>
        <p>Tác vụ Producer sinh dữ liệu và đưa vào hàng đợi đệm (Message Buffer); tác vụ Consumer lấy dữ liệu ra xử lý. Cần cơ chế khóa để Buffer rỗng thì Consumer phải chờ, Buffer đầy thì Producer phải dừng ghi (Inter-Process Communication - IPC).</p>
      </div>
    </div>
  </div>

  <div class="topic-card">
    <div class="topic-title">📐 Phân Cấp Các Mẫu Tái Sử Dụng (Patterns Hierarchy)</div>
    <div class="table-wrap">
      <table class="styled-table">
        <thead>
          <tr>
            <th>Cấp Độ Mẫu</th>
            <th>Quy Mô & Phạm Vi Áp Dụng</th>
            <th>Ví Dụ Tiêu Biểu</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Architectural Patterns</strong> (Mẫu kiến trúc)</td>
            <td>Cấp cao nhất, định hình cấu trúc vĩ mô toàn hệ thống và các hệ thống con.</td>
            <td>Layered Pattern, Client/Server, Broker, Model-View-Controller (MVC), Pipe &amp; Filter.</td>
          </tr>
          <tr>
            <td><strong>Design Patterns</strong> (Mẫu thiết kế)</td>
            <td>Cấp trung bình, giải quyết bài toán tương tác giữa một nhóm nhỏ các đối tượng cộng tác.</td>
            <td>23 mẫu GoF (Singleton, Factory, Observer, Strategy, Decorator, Adapter).</td>
          </tr>
          <tr>
            <td><strong>Analysis Patterns</strong> (Mẫu phân tích)</td>
            <td>Mẫu khái niệm lặp lại trong mô hình phân tích tĩnh miền nghiệp vụ.</td>
            <td>Account-Transaction pattern, Party-Role pattern trong tài chính.</td>
          </tr>
          <tr>
            <td><strong>Product Line Patterns</strong> (Mẫu dòng sản phẩm)</td>
            <td>Tập trung vào miền ứng dụng cụ thể, quản lý các điểm biến thể (Variability).</td>
            <td>Mẫu hệ thống điều khiển ô tô (Automotive Software Architecture).</td>
          </tr>
          <tr>
            <td><strong>Idioms</strong> (Mẫu đặc thù ngôn ngữ)</td>
            <td>Cấp thấp nhất, giải pháp hiện thực cụ thể dựa trên tính năng của từng ngôn ngữ lập trình.</td>
            <td>RAII trong C++, Double-Checked Locking trong Java, Context Manager trong Python.</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</section>

<!-- ========================================== -->
<!-- CHƯƠNG 5 -->
<!-- ========================================== -->
<section id="ch05" class="chapter-section">
  <div class="chapter-header">
    <div class="chapter-badge-row">
      <span class="chapter-badge">CHƯƠNG 05</span>
      <span class="chapter-lecturer-tag">COMET Methodology</span>
    </div>
    <h2 class="chapter-title">Tổng Quan Phương Pháp Mô Hình Hóa & Thiết Kế COMET</h2>
    <div class="chapter-subtitle">Collaborative Object Modeling and Architectural Design Method</div>
  </div>

  <div class="topic-card">
    <div class="topic-title">🚀 Phương Pháp COMET Là Gì?</div>
    <p>
      <strong>COMET</strong> là viết tắt của <em>Collaborative Object Modeling and Architectural Design Method</em> do Giáo sư <strong>Hassan Gomaa</strong> sáng lập.
      Công thức định nghĩa bản chất:
    </p>
    <div style="text-align: center; margin: 1rem 0;">
      <code style="font-size: 1.15rem; padding: 0.5rem 1.5rem; background: var(--bg-surface-subtle); border-radius: var(--radius-md); font-weight: 700; border: 1.5px solid var(--accent-primary);">
        COMET = UML (Hệ thống ký hiệu chuẩn) + METHOD (Trình tự phương pháp luận lặp hướng Use Case)
      </code>
    </div>
    <p>
      COMET kết nối chặt chẽ 3 giai đoạn: <strong>Mô hình hóa yêu cầu (Requirements) &rarr; Mô hình hóa phân tích (Analysis) &rarr; Mô hình hóa thiết kế (Design)</strong>.
    </p>
  </div>

  <div class="card-grid">
    <div class="card">
      <div class="card-title">🔍 Analysis vs Design (Phân Tích vs Thiết Kế)</div>
      <div class="card-content">
        <ul style="padding-left: 1.2rem;">
          <li><strong>Analysis (Phân tích)</strong>: Là hành vi <em>Decomposition (Phân rã)</em> &mdash; Bẻ nhỏ bài toán miền vấn đề (Problem Domain) để thấu hiểu sâu sắc bản chất hệ thống cần làm gì.</li>
          <li><strong>Design (Thiết kế)</strong>: Là hành vi <em>Synthesis (Tổng hợp)</em> &mdash; Ghép nối các giải pháp miền giải thuật (Solution Domain) thành kiến trúc phần mềm vận hành trên môi trường thực tế.</li>
        </ul>
      </div>
    </div>

    <div class="card">
      <div class="card-title">🏗️ Phân Kỳ Xây Dựng & Kiểm Thử Gia Tăng</div>
      <div class="card-content">
        <ul style="padding-left: 1.2rem;">
          <li><strong>Incremental Software Construction</strong>: Chọn từng tập con Use Case để thiết kế chi tiết, code và Unit Test.</li>
          <li><strong>Incremental Integration Testing</strong>: Kiểm thử tích hợp (White-box testing) giao diện giữa các đối tượng tham gia Use Case.</li>
          <li><strong>System Testing</strong>: Kiểm thử chức năng toàn diện (Black-box testing) dựa trên kịch bản Use Case chuẩn bàn giao khách hàng.</li>
        </ul>
      </div>
    </div>
  </div>

  <!-- SVG Diagram 2: COMET Iterative Life Cycle -->
  <div class="diagram-card">
    <div class="svg-container">
      <svg viewBox="0 0 880 260" xmlns="http://www.w3.org/2000/svg" style="font-family: 'Plus Jakarta Sans', sans-serif;">
        <rect width="880" height="260" rx="14" fill="#ffffff" stroke="#e2e8f0" stroke-width="2"/>
        <text x="440" y="30" text-anchor="middle" font-size="15" font-weight="800" fill="#0f172a">CHU TRÌNH PHÁT TRIỂN PHẦN MỀM HƯỚNG USE CASE TRONG PHƯƠNG PHÁP COMET</text>
        
        <!-- Step 1: Requirements -->
        <rect x="30" y="70" width="145" height="110" rx="8" fill="#e0f2fe" stroke="#0284c7" stroke-width="1.8"/>
        <text x="102" y="98" text-anchor="middle" font-size="12" font-weight="800" fill="#0369a1">1. REQUIREMENTS</text>
        <text x="102" y="118" text-anchor="middle" font-size="11" font-weight="600" fill="#0f172a">Use Case Model</text>
        <text x="102" y="136" text-anchor="middle" font-size="10" fill="#475569">- Actors & UCs</text>
        <text x="102" y="152" text-anchor="middle" font-size="10" fill="#475569">- Nonfunctional Req</text>

        <!-- Arrow 1 -> 2 -->
        <path d="M 175 125 L 200 125" stroke="#0284c7" stroke-width="2.5" marker-end="url(#arrowBlue)"/>

        <!-- Step 2: Analysis -->
        <rect x="205" y="70" width="145" height="110" rx="8" fill="#eef2ff" stroke="#4f46e5" stroke-width="1.8"/>
        <text x="277" y="98" text-anchor="middle" font-size="12" font-weight="800" fill="#4338ca">2. ANALYSIS</text>
        <text x="277" y="118" text-anchor="middle" font-size="11" font-weight="600" fill="#0f172a">Problem Domain</text>
        <text x="277" y="136" text-anchor="middle" font-size="10" fill="#475569">- Static Modeling</text>
        <text x="277" y="152" text-anchor="middle" font-size="10" fill="#475569">- Dynamic Interaction</text>
        <text x="277" y="168" text-anchor="middle" font-size="10" fill="#475569">- State Machines</text>

        <!-- Arrow 2 -> 3 -->
        <path d="M 350 125 L 375 125" stroke="#4f46e5" stroke-width="2.5"/>

        <!-- Step 3: Design -->
        <rect x="380" y="70" width="145" height="110" rx="8" fill="#d1fae5" stroke="#059669" stroke-width="1.8"/>
        <text x="452" y="98" text-anchor="middle" font-size="12" font-weight="800" fill="#047857">3. DESIGN</text>
        <text x="452" y="118" text-anchor="middle" font-size="11" font-weight="600" fill="#0f172a">Solution Domain</text>
        <text x="452" y="136" text-anchor="middle" font-size="10" fill="#475569">- Subsystem Structuring</text>
        <text x="452" y="152" text-anchor="middle" font-size="10" fill="#475569">- Architectural Patterns</text>
        <text x="452" y="168" text-anchor="middle" font-size="10" fill="#475569">- Class Interfaces</text>

        <!-- Arrow 3 -> 4 -->
        <path d="M 525 125 L 550 125" stroke="#059669" stroke-width="2.5"/>

        <!-- Step 4: Construction -->
        <rect x="555" y="70" width="145" height="110" rx="8" fill="#fef3c7" stroke="#d97706" stroke-width="1.8"/>
        <text x="627" y="98" text-anchor="middle" font-size="12" font-weight="800" fill="#b45309">4. CONSTRUCTION</text>
        <text x="627" y="118" text-anchor="middle" font-size="11" font-weight="600" fill="#0f172a">Phased Increment</text>
        <text x="627" y="136" text-anchor="middle" font-size="10" fill="#475569">- Detailed Design</text>
        <text x="627" y="152" text-anchor="middle" font-size="10" fill="#475569">- Coding & Unit Test</text>
        <text x="627" y="168" text-anchor="middle" font-size="10" fill="#475569">- Subset Selection</text>

        <!-- Arrow 4 -> 5 -->
        <path d="M 700 125 L 725 125" stroke="#d97706" stroke-width="2.5"/>

        <!-- Step 5: Testing -->
        <rect x="730" y="70" width="125" height="110" rx="8" fill="#fee2e2" stroke="#dc2626" stroke-width="1.8"/>
        <text x="792" y="98" text-anchor="middle" font-size="12" font-weight="800" fill="#b91c1c">5. TESTING</text>
        <text x="792" y="118" text-anchor="middle" font-size="11" font-weight="600" fill="#0f172a">Integration & Sys</text>
        <text x="792" y="136" text-anchor="middle" font-size="10" fill="#475569">- White-box Interf</text>
        <text x="792" y="152" text-anchor="middle" font-size="10" fill="#475569">- Black-box System</text>

        <!-- Feedback Loop -->
        <path d="M 792 180 L 792 220 L 102 220 L 102 180" fill="none" stroke="#64748b" stroke-width="2" stroke-dasharray="6,4"/>
        <text x="440" y="212" text-anchor="middle" font-size="11" font-weight="700" fill="#475569">VÒNG LẶP PHẢN HỒI GIA TĂNG LIÊN TỤC (ITERATIVE INCREMENTAL FEEDBACK)</text>
      </svg>
    </div>
    <div class="diagram-caption">Sơ đồ 5.1: Chu trình vòng đời phần mềm hướng Use Case trong phương pháp COMET</div>
  </div>
</section>
"""

