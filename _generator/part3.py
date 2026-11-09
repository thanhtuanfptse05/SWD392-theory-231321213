# _generator/part3.py
# Part 3: Thiết Kế Kiến Trúc Phần Mềm Chuyên Sâu (Chương 12 - 18)

def get_part3_html():
    return r"""
<!-- ========================================== -->
<!-- PART 3 DIVIDER BANNER -->
<!-- ========================================== -->
<div id="part-3" class="part-divider-banner part-3-banner">
  <span class="part-badge-tag">Phần 3 &bull; Thiết Kế Kiến Trúc Chuyên Sâu</span>
  <h2 class="part-title">Thiết Kế Kiến Trúc Phần Mềm Chuyên Sâu</h2>
  <p class="part-desc">
    Làm chủ nghệ thuật thiết kế kiến trúc cấp cao: Từ tổng quan kiến trúc và đa góc nhìn (Ch 12), phân rã hệ thống con Subsystems dựa trên tích hợp biểu đồ giao tiếp (Ch 13), kiến trúc hướng đối tượng tuần tự (Ch 14), kiến trúc Client/Server đa tầng và ORM Database (Ch 15), kiến trúc hướng dịch vụ SOA và điều phối ESB (Ch 16), kiến trúc dựa trên thành phần CBD (Ch 17), đến kiến trúc tương tranh thời gian thực Concurrent & Real-Time với định luật lập lịch RMA (Ch 18).
  </p>
</div>

<!-- ========================================== -->
<!-- CHƯƠNG 12 -->
<!-- ========================================== -->
<section id="ch12" class="chapter-section">
  <div class="chapter-header">
    <div class="chapter-badge-row">
      <span class="chapter-badge">CHƯƠNG 12</span>
      <span class="chapter-lecturer-tag">Architecture Fundamentals</span>
    </div>
    <h2 class="chapter-title">Tổng Quan Kiến Trúc Phần Mềm (Software Architecture Overview)</h2>
    <div class="chapter-subtitle">Subsystems, Interfaces, Component-Based Perspective & Multiple Views</div>
  </div>

  <div class="card-grid">
    <div class="card">
      <div class="card-title">🏛️ Định Nghĩa Kiến Trúc Phần Mềm (Bass, Clements, Kazman)</div>
      <div class="card-content">
        <p>Kiến trúc phần mềm là tập hợp các cấu trúc của hệ thống, bao gồm:</p>
        <ul style="padding-left: 1.2rem;">
          <li>Các phần tử phần mềm (Software Elements / Subsystems / Components).</li>
          <li>Các thuộc tính có thể nhìn thấy từ bên ngoài (Externally Visible Properties) của các phần tử đó.</li>
          <li>Mối quan hệ và ràng buộc kết nối giữa các phần tử đó.</li>
          <li>Kiến trúc <strong>tách biệt cấu trúc tổng thể</strong> của hệ thống khỏi chi tiết nội bộ của từng phần tử.</li>
        </ul>
      </div>
    </div>

    <div class="card">
      <div class="card-title">🧩 Góc Nhìn Dựa Trên Thành Phần (Component-Based View)</div>
      <div class="card-content">
        <ul style="padding-left: 1.2rem;">
          <li>Mỗi <strong>Component</strong> là một đơn vị khép kín, độc lập và che giấu thông tin nội bộ.</li>
          <li>Component có thể là một đối tượng phức hợp (Composite Object) chứa nhiều đối tượng bên trong hoặc đối tượng đơn giản (Simple Object).</li>
          <li>Giao tiếp hoàn toàn thông qua <strong>Interface chuẩn</strong>. Tất cả thông tin cần thiết để giao tiếp đều được quy định trong Interface, tách rời hoàn toàn khỏi mã nguồn hiện thực.</li>
        </ul>
      </div>
    </div>

    <div class="card">
      <div class="card-title">📐 Thiết Kế Giao Diện Hợp Đồng (Contract-Based Interface)</div>
      <div class="card-content">
        <p>Giao diện tạo thành một <strong>bản hợp đồng ràng buộc (Contract)</strong> giữa bên cung cấp (Provider) và bên sử dụng (Consumer):</p>
        <ul style="padding-left: 1.2rem;">
          <li>Bên sử dụng chỉ cần biết tên hàm, tham số đầu vào và kiểu dữ liệu trả về.</li>
          <li>Bên cung cấp có thể thay đổi toàn bộ thuật toán bên trong mà không làm gián đoạn bên sử dụng.</li>
        </ul>
      </div>
    </div>
  </div>
</section>

<!-- ========================================== -->
<!-- CHƯƠNG 13 -->
<!-- ========================================== -->
<section id="ch13" class="chapter-section">
  <div class="chapter-header">
    <div class="chapter-badge-row">
      <span class="chapter-badge">CHƯƠNG 13</span>
      <span class="chapter-lecturer-tag">Subsystem Design</span>
    </div>
    <h2 class="chapter-title">Thiết Kế Phân Rã Hệ Thống Con (Subsystem Architectural Design)</h2>
    <div class="chapter-subtitle">Integrated Communication Diagrams & Subsystem Structuring Criteria</div>
  </div>

  <div class="topic-card">
    <div class="topic-title">🔄 Quá Trình Tổng Hợp: Integrated Communication Diagrams</div>
    <p>
      Làm thế nào để chuyển từ giai đoạn Phân Tích (Analysis) sang giai đoạn Thiết Kế (Design)? 
      Kiến trúc sư sử dụng phương pháp <strong>Ghép Nối Biểu Đồ Giao Tiếp (Integrated Communication Diagram)</strong>:
    </p>
    <div class="step-list">
      <div class="step-item">
        <div class="step-num">1</div>
        <div class="step-body">
          <div class="step-title">Thu thập biểu đồ giao tiếp từng Use Case</div>
          <p>Mỗi Use Case ở pha Dynamic Modeling đã sinh ra một biểu đồ giao tiếp chứa các đối tượng và luồng thông điệp cụ thể.</p>
        </div>
      </div>
      <div class="step-item">
        <div class="step-num">2</div>
        <div class="step-body">
          <div class="step-title">Hợp nhất lên sơ đồ tổng thể ban đầu</div>
          <p>Ghép tất cả các đối tượng và liên kết lên một sơ đồ chung, tạo nên kiến trúc phác thảo sơ khai của toàn bộ hệ thống.</p>
        </div>
      </div>
      <div class="step-item">
        <div class="step-num">3</div>
        <div class="step-body">
          <div class="step-title">Giảm thiểu độ phức tạp bằng Gom Thông Điệp (Message Aggregation)</div>
          <p>Nếu có quá nhiều thông điệp đơn lẻ giữa 2 đối tượng/hệ thống con, gom chúng thành một giao dịch cấp cao hoặc nhóm chức năng để sơ đồ thanh thoát.</p>
        </div>
      </div>
      <div class="step-item">
        <div class="step-num">4</div>
        <div class="step-body">
          <div class="step-title">Phân rã thành Subsystem Communication Diagrams</div>
          <p>Tạo sơ đồ giao tiếp mức cao giữa các Subsystem, sau đó vẽ sơ đồ giao tiếp chi tiết nội bộ bên trong từng Subsystem.</p>
        </div>
      </div>
    </div>
  </div>

  <div class="topic-card">
    <div class="topic-title">🏢 6 Tiêu Chí Cấu Trúc Hóa Hệ Thống Con (Subsystem Structuring Criteria)</div>
    <div class="table-wrap">
      <table class="styled-table">
        <thead>
          <tr>
            <th>Loại Subsystem</th>
            <th>Stereotype UML</th>
            <th>Trách Nhiệm Cốt Lõi</th>
            <th>Thành Phần Bên Trong</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>1. Client Subsystem</strong></td>
            <td><code>&laquo;subsystem&raquo;</code></td>
            <td>Bên gửi yêu cầu dịch vụ (Requester). Chủ động khởi tạo phiên tương tác.</td>
            <td>User Interaction, Control Subsystem, I/O Subsystem.</td>
          </tr>
          <tr>
            <td><strong>2. User Interaction Subsystem</strong></td>
            <td><code>&laquo;subsystem&raquo;</code></td>
            <td>Cung cấp giao diện đồ họa cho người dùng, đóng vai trò Client trong mô hình Client/Server.</td>
            <td>Tập hợp các GUI Windows/Screens, Local Cache Entity, Control objects điều hướng màn hình.</td>
          </tr>
          <tr>
            <td><strong>3. Service Subsystem</strong></td>
            <td><code>&laquo;subsystem&raquo;</code> / <code>&laquo;service&raquo;</code></td>
            <td>Cung cấp dịch vụ cho các Client; phản hồi yêu cầu nhưng <em>không tự khởi tạo yêu cầu mới</em>.</td>
            <td>Coordinator objects, Business Logic objects, Database Entity classes.</td>
          </tr>
          <tr>
            <td><strong>4. Control Subsystem</strong></td>
            <td><code>&laquo;subsystem&raquo;</code></td>
            <td>Kiểm soát và điều khiển một bộ phận vật lý hoặc luồng vận hành của hệ thống. Thường phụ thuộc trạng thái.</td>
            <td>State-dependent Control objects thực thi Statechart, Device Drivers.</td>
          </tr>
          <tr>
            <td><strong>5. Coordinator Subsystem</strong></td>
            <td><code>&laquo;subsystem&raquo;</code></td>
            <td>Điều phối sự cộng tác phức tạp giữa nhiều Service Subsystems hoặc Control Subsystems khác nhau.</td>
            <td>Orchestrator objects, Workflow Managers. Bắt buộc khi có nghiệp vụ phân tán đa dịch vụ.</td>
          </tr>
          <tr>
            <td><strong>6. Input / Output Subsystem</strong></td>
            <td><code>&laquo;subsystem&raquo;</code></td>
            <td>Thực hiện các thao tác vào/ra cảm biến và cơ cấu chấp hành thay mặt cho các Subsystem khác.</td>
            <td>Bộ đệm dữ liệu cảm biến, Event-driven input tasks, Actuator controllers.</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>

  <div class="concept-box">
    <div class="concept-title">💬 Quyết Định Về Giao Tiếp Thông Điệp Giữa Các Subsystems</div>
    <ul style="padding-left: 1.2rem;">
      <li><strong>Unidirectional (Đơn hướng)</strong>: Thông điệp truyền một chiều từ bên gửi sang bên nhận, không đòi hỏi phản hồi trực tiếp (thích hợp cho bắn sự kiện, logging).</li>
      <li><strong>Bidirectional (Song hướng)</strong>: Truyền hai chiều, bên gửi yêu cầu và bên nhận gửi lại kết quả trả lời (Request / Reply).</li>
      <li><strong>Synchronous (Đồng bộ)</strong>: Bên gửi tạm dừng thực thi (Blocked) để chờ phản hồi từ bên nhận trước khi tiếp tục.</li>
      <li><strong>Asynchronous (Bất đồng bộ)</strong>: Bên gửi đẩy thông điệp vào hàng đợi (Buffer) rồi tiếp tục thực thi ngay lập tức mà không chờ bên nhận.</li>
    </ul>
  </div>
</section>

<!-- ========================================== -->
<!-- CHƯƠNG 14 -->
<!-- ========================================== -->
<section id="ch14" class="chapter-section">
  <div class="chapter-header">
    <div class="chapter-badge-row">
      <span class="chapter-badge">CHƯƠNG 14</span>
      <span class="chapter-lecturer-tag">Object-Oriented Design</span>
    </div>
    <h2 class="chapter-title">Thiết Kế Kiến Trúc Hướng Đối Tượng (Object-Oriented Architectures)</h2>
    <div class="chapter-subtitle">Information Hiding Classes, Interfaces, Inheritance & Dynamic Binding</div>
  </div>

  <div class="card-grid">
    <div class="card">
      <div class="card-title">📦 Data Abstraction Classes</div>
      <div class="card-content">
        <p>Lớp trừu tượng hóa dữ liệu:</p>
        <ul style="padding-left: 1.2rem;">
          <li>Đóng gói cấu trúc lưu trữ nội bộ (Mảng động, Danh sách liên kết, Cây nhị phân, Bảng băm).</li>
          <li>Chỉ công khai các hàm nghiệp vụ thao tác an toàn (Ví dụ: Lớp <code>Stack</code> chỉ để lộ <code>push()</code>, <code>pop()</code>, <code>top()</code>, <code>isEmpty()</code>).</li>
          <li>Bảo vệ dữ liệu không bị truy cập trái phép hoặc làm hỏng cấu trúc.</li>
        </ul>
      </div>
    </div>

    <div class="card">
      <div class="card-title">⚙️ State-Machine Classes</div>
      <div class="card-content">
        <p>Hiện thực Máy trạng thái bằng lập trình hướng đối tượng:</p>
        <ul style="padding-left: 1.2rem;">
          <li>Đóng gói biến lưu trạng thái hiện tại (<code>currentState</code>).</li>
          <li>Sử dụng Bảng chuyển dịch trạng thái (State Transition Table) hoặc mẫu <strong>State Pattern</strong> (mỗi trạng thái là một lớp con cụ thể).</li>
          <li>Xử lý sự kiện đầu vào, kiểm tra điều kiện canh gác và kích hoạt hành vi tương ứng.</li>
        </ul>
      </div>
    </div>

    <div class="card">
      <div class="card-title">🎭 Polymorphism & Dynamic Binding</div>
      <div class="card-content">
        <ul style="padding-left: 1.2rem;">
          <li><strong>Polymorphism (Tính đa hình)</strong>: Khả năng cho phép các đối tượng thuộc các lớp khác nhau phản hồi cùng một lời gọi phương thức theo những cách riêng biệt.</li>
          <li><strong>Dynamic Binding (Ràng buộc động)</strong>: Trình biên dịch/máy ảo quyết định mã phương thức nào được thực thi tại <em>thời điểm chạy (Runtime)</em> dựa trên thể hiện thực tế của đối tượng, thay vì lúc biên dịch (Compile time).</li>
        </ul>
      </div>
    </div>
  </div>

  <div class="callout callout-tip">
    <div class="callout-title">💡 Mẫu Truyền Thông Trong Kiến Trúc Tuần Tự: Call / Return Pattern</div>
    <p>
      Trong kiến trúc phần mềm tuần tự (Sequential Architecture), toàn bộ chương trình chỉ vận hành trên một luồng duy nhất (Single thread). 
      Vì vậy, <strong>Call / Return (Gọi hàm / Trả về)</strong> là mẫu truyền thông duy nhất tồn tại giữa các đối tượng. Khi Object A gọi phương thức của Object B, luồng điều khiển được chuyển giao sang B, A bị khóa (Blocked) cho đến khi B thực thi xong và trả về giá trị (Return).
    </p>
  </div>
</section>

<!-- ========================================== -->
<!-- CHƯƠNG 15 -->
<!-- ========================================== -->
<section id="ch15" class="chapter-section">
  <div class="chapter-header">
    <div class="chapter-badge-row">
      <span class="chapter-badge">CHƯƠNG 15</span>
      <span class="chapter-lecturer-tag">Distributed Systems</span>
    </div>
    <h2 class="chapter-title">Thiết Kế Kiến Trúc Client / Server & ORM Database</h2>
    <div class="chapter-subtitle">Multi-tier Architectures, Middleware, Service Subsystems & Relational Mapping</div>
  </div>

  <div class="card-grid">
    <div class="card">
      <div class="card-title">💻 1. Multiple Client / Single Service</div>
      <div class="card-content">
        <p>Mô hình kinh điển và phổ biến nhất:</p>
        <ul style="padding-left: 1.2rem;">
          <li>Một Server duy nhất cung cấp dịch vụ trung tâm (Database server, File server).</li>
          <li>Nhiều Clients phân tán đồng thời kết nối và gửi yêu cầu.</li>
          <li>Ví dụ: Hệ thống ATM kết nối về máy chủ ngân hàng tập trung.</li>
        </ul>
      </div>
    </div>

    <div class="card">
      <div class="card-title">🌐 2. Multiple Client / Multiple Service</div>
      <div class="card-content">
        <p>Mô hình phân tán phức hợp:</p>
        <ul style="padding-left: 1.2rem;">
          <li>Khách hàng giao tiếp với nhiều dịch vụ khác nhau (Catalog, Payment, Shipping).</li>
          <li>Các Server cũng có thể đóng vai trò Client để gọi chéo lẫn nhau.</li>
          <li>Giao tiếp có thể diễn ra tuần tự hoặc đồng thời bất đồng bộ.</li>
        </ul>
      </div>
    </div>

    <div class="card">
      <div class="card-title">🏢 3. Multi-Tier Architectures (2-Tier vs 3-Tier vs N-Tier)</div>
      <div class="card-content">
        <ul style="padding-left: 1.2rem;">
          <li><strong>2-Tier Thick Client</strong>: UI + Toàn bộ Business Logic nằm trên máy Client; Server chỉ chứa RDBMS Database. Nhược điểm: Khó nâng cấp code, gánh nặng bảo trì.</li>
          <li><strong>2-Tier Thin Client</strong>: Client chỉ hiển thị màn hình (Terminal); toàn bộ logic và dữ liệu nằm ở Server.</li>
          <li><strong>3-Tier Standard</strong>: Tách biệt hoàn toàn 3 tầng: <em>Presentation Tier (UI/Web) &harr; Application / Business Logic Tier &harr; Data Tier (Database)</em>. Dễ mở rộng, bảo mật cao.</li>
        </ul>
      </div>
    </div>
  </div>

  <!-- SVG Diagram: 3-Tier Client Server -->
  <div class="diagram-card">
    <div class="svg-container">
      <svg viewBox="0 0 880 280" xmlns="http://www.w3.org/2000/svg" style="font-family: 'Plus Jakarta Sans', sans-serif;">
        <rect width="880" height="280" rx="14" fill="#ffffff" stroke="#e2e8f0" stroke-width="2"/>
        <text x="440" y="30" text-anchor="middle" font-size="15" font-weight="800" fill="#0f172a">KIẾN TRÚC PHÂN TẦNG CLIENT / SERVER ĐA TẦNG (3-TIER ARCHITECTURE WITH MIDDLEWARE)</text>
        
        <!-- Tier 1: Presentation -->
        <rect x="40" y="70" width="220" height="150" rx="10" fill="#e0f2fe" stroke="#0284c7" stroke-width="2"/>
        <text x="150" y="98" text-anchor="middle" font-size="13" font-weight="800" fill="#0369a1">TIER 1: PRESENTATION</text>
        <rect x="60" y="115" width="180" height="40" rx="6" fill="#ffffff" stroke="#0284c7" stroke-width="1.2"/>
        <text x="150" y="140" text-anchor="middle" font-size="11.5" font-weight="700" fill="#0f172a">Web Browser / Mobile App</text>
        <text x="150" y="185" text-anchor="middle" font-size="10.5" fill="#475569">HTML5 / React / Flutter UI</text>
        <text x="150" y="202" text-anchor="middle" font-size="10" fill="#64748b">(Thin Client Layer)</text>

        <!-- Connector 1 <-> 2 -->
        <path d="M 260 145 L 325 145" stroke="#0284c7" stroke-width="2.5" marker-end="url(#arrow)"/>
        <path d="M 325 155 L 260 155" stroke="#0284c7" stroke-width="2.5"/>
        <text x="292" y="135" text-anchor="middle" font-size="9.5" font-weight="700" fill="#0284c7">HTTPS / JSON</text>

        <!-- Tier 2: Business Logic -->
        <rect x="330" y="70" width="220" height="150" rx="10" fill="#eef2ff" stroke="#4f46e5" stroke-width="2"/>
        <text x="440" y="98" text-anchor="middle" font-size="13" font-weight="800" fill="#4338ca">TIER 2: APPLICATION</text>
        <rect x="350" y="115" width="180" height="40" rx="6" fill="#ffffff" stroke="#4f46e5" stroke-width="1.2"/>
        <text x="440" y="140" text-anchor="middle" font-size="11.5" font-weight="700" fill="#0f172a">Business Logic Server</text>
        <text x="440" y="185" text-anchor="middle" font-size="10.5" fill="#475569">Coordinator &amp; Services</text>
        <text x="440" y="202" text-anchor="middle" font-size="10" fill="#64748b">Spring Boot / .NET Core</text>

        <!-- Connector 2 <-> 3 -->
        <path d="M 550 145 L 615 145" stroke="#4f46e5" stroke-width="2.5"/>
        <path d="M 615 155 L 550 155" stroke="#4f46e5" stroke-width="2.5"/>
        <text x="582" y="135" text-anchor="middle" font-size="9.5" font-weight="700" fill="#4f46e5">JDBC / ORM</text>

        <!-- Tier 3: Database -->
        <rect x="620" y="70" width="220" height="150" rx="10" fill="#d1fae5" stroke="#059669" stroke-width="2"/>
        <text x="730" y="98" text-anchor="middle" font-size="13" font-weight="800" fill="#047857">TIER 3: DATA STORE</text>
        <!-- DB Cylinder representation -->
        <rect x="650" y="115" width="160" height="40" rx="6" fill="#ffffff" stroke="#059669" stroke-width="1.2"/>
        <text x="730" y="140" text-anchor="middle" font-size="11.5" font-weight="700" fill="#0f172a">Relational Database</text>
        <text x="730" y="185" text-anchor="middle" font-size="10.5" fill="#475569">PostgreSQL / Oracle / SQL</text>
        <text x="730" y="202" text-anchor="middle" font-size="10" fill="#64748b">(ACID Storage Layer)</text>

        <rect x="180" y="240" width="520" height="28" rx="6" fill="#f1f5f9" stroke="#94a3b8" stroke-width="1"/>
        <text x="440" y="259" text-anchor="middle" font-size="10.5" font-weight="600" fill="#475569">MIDDLEWARE ENGINES: RPC &bull; Java RMI &bull; Message Broker (RabbitMQ/Kafka) &bull; ORB</text>
      </svg>
    </div>
    <div class="diagram-caption">Sơ đồ 15.1: Kiến trúc Client/Server 3 tầng chuẩn mực với lớp phần mềm trung gian Middleware</div>
  </div>

  <div class="topic-card">
    <div class="topic-title">🗄️ Ánh Xạ Mô Hình Tĩnh Sang Cơ Sở Dữ Liệu Quan Hệ (ORM Design Rules)</div>
    <div class="table-wrap">
      <table class="styled-table">
        <thead>
          <tr>
            <th>Phần Tử Mô Hình Hướng Đối Tượng</th>
            <th>Quy Tắc Chuyển Đổi Sang Bảng CSDL Quan Hệ</th>
            <th>Cơ Chế Khóa &amp; Ràng Buộc</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Entity Class</strong> (Lớp thực thể)</td>
            <td>Ánh xạ trực tiếp thành một <strong>Bảng (Table)</strong> trong CSDL.</td>
            <td>Chọn 1 thuộc tính duy nhất làm Khóa chính (<strong>Primary Key - PK</strong>).</td>
          </tr>
          <tr>
            <td><strong>Class Attributes</strong> (Thuộc tính lớp)</td>
            <td>Ánh xạ thành các <strong>Cột (Columns)</strong> tương ứng trong bảng.</td>
            <td>Chỉ định kiểu dữ liệu SQL (VARCHAR, INT, DECIMAL, BOOLEAN).</td>
          </tr>
          <tr>
            <td><strong>Quan hệ 1 : N (One-to-Many)</strong></td>
            <td>Đưa Khóa chính của bảng phía "1" sang làm <strong>Khóa ngoại (Foreign Key - FK)</strong> của bảng phía "N".</td>
            <td>Ví dụ: Cột <code>department_id</code> nằm trong bảng <code>Employee</code>.</td>
          </tr>
          <tr>
            <td><strong>Quan hệ M : N (Many-to-Many)</strong></td>
            <td>Bắt buộc tạo một <strong>Bảng trung gian (Junction Table / Associative Table)</strong>.</td>
            <td>Bảng trung gian chứa 2 cột FK trỏ về PK của 2 bảng gốc, kết hợp tạo thành Composite PK.</td>
          </tr>
          <tr>
            <td><strong>Kế Thừa: Single Table Strategy</strong></td>
            <td>Gom toàn bộ cha và các lớp con vào <em>duy nhất một bảng lớn</em>.</td>
            <td>Dùng cột phân biệt <strong>Discriminator Column</strong> (ví dụ: <code>account_type = 'SAVINGS'</code>).</td>
          </tr>
          <tr>
            <td><strong>Kế Thừa: Table per Subclass</strong></td>
            <td>Tạo bảng riêng cho lớp cha và từng lớp con. Bảng con dùng PK vừa làm PK vừa làm FK trỏ về cha.</td>
            <td>Truy vấn cần <code>JOIN</code> bảng cha và bảng con. Tối ưu chuẩn hóa dữ liệu.</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</section>

<!-- ========================================== -->
<!-- CHƯƠNG 16 -->
<!-- ========================================== -->
<section id="ch16" class="chapter-section">
  <div class="chapter-header">
    <div class="chapter-badge-row">
      <span class="chapter-badge">CHƯƠNG 16</span>
      <span class="chapter-lecturer-tag">Modern Enterprise Architecture</span>
    </div>
    <h2 class="chapter-title">Thiết Kế Kiến Trúc Hướng Dịch Vụ (Service-Oriented Architectures - SOA)</h2>
    <div class="chapter-subtitle">8 Design Principles, Broker Patterns, ESB, 2PC & Orchestration vs Choreography</div>
  </div>

  <div class="topic-card">
    <div class="topic-title">🌐 8 Nguyên Lý Vàng Trong Thiết Kế Dịch Vụ SOA (Erl's Principles)</div>
    <div class="card-grid">
      <div class="concept-box">
        <div class="concept-title">1. Loose Coupling (Khớp nối lỏng)</div>
        <p>Các dịch vụ giảm thiểu tối đa sự phụ thuộc lẫn nhau, cho phép nâng cấp độc lập.</p>
      </div>
      <div class="concept-box">
        <div class="concept-title">2. Service Contract (Hợp đồng dịch vụ)</div>
        <p>Giao tiếp thông qua bản mô tả chuẩn hóa chính thức (WSDL, OpenAPI/Swagger).</p>
      </div>
      <div class="concept-box">
        <div class="concept-title">3. Autonomy (Tính tự trị)</div>
        <p>Mỗi dịch vụ toàn quyền kiểm soát logic thực thi và dữ liệu của chính mình.</p>
      </div>
      <div class="concept-box">
        <div class="concept-title">4. Abstraction (Tính trừu tượng)</div>
        <p>Che giấu hoàn toàn công nghệ, ngôn ngữ lập trình và logic nội bộ bên trong.</p>
      </div>
      <div class="concept-box">
        <div class="concept-title">5. Reusability (Tính tái sử dụng)</div>
        <p>Dịch vụ được thiết kế tổng quát để phục vụ nhiều ứng dụng doanh nghiệp khác nhau.</p>
      </div>
      <div class="concept-box">
        <div class="concept-title">6. Composability (Tính có thể ghép nối)</div>
        <p>Dễ dàng lắp ghép nhiều dịch vụ nhỏ để tạo thành dịch vụ tổng hợp (Composite Service).</p>
      </div>
      <div class="concept-box">
        <div class="concept-title">7. Statelessness (Phi trạng thái)</div>
        <p>Dịch vụ không lưu trạng thái phiên của client giữa các lời gọi, tối ưu hóa khả năng mở rộng.</p>
      </div>
      <div class="concept-box">
        <div class="concept-title">8. Discoverability (Khả năng phát hiện)</div>
        <p>Dịch vụ công khai siêu dữ liệu giúp client tự động tìm kiếm qua Service Registry.</p>
      </div>
    </div>
  </div>

  <div class="topic-card">
    <div class="topic-title">🔄 3 Mẫu Môi Giới Kiến Trúc (Architectural Broker Patterns)</div>
    <ul style="padding-left: 1.2rem;">
      <li><strong>Matchmaker / Registry Broker</strong>: Hoạt động như trang vàng doanh nghiệp. Nhà cung cấp đăng ký dịch vụ (Publish); người dùng tra cứu địa chỉ (Lookup/Find) rồi tự liên lạc trực tiếp (Bind). Ví dụ: UDDI, Consul, Eureka.</li>
      <li><strong>Routing Broker</strong>: Tiếp nhận yêu cầu từ client, tự động phân tích và chuyển tiếp (Route) yêu cầu tới nhà cung cấp phù hợp nhất dựa trên tải hoặc quy tắc định tuyến (API Gateway, NGINX).</li>
      <li><strong>Subscription / Event Broker</strong>: Quản lý đăng ký kênh sự kiện (Topic). Khi có sự kiện mới, Broker sẽ bắn thông báo tới tất cả các bên đăng ký (Publish / Subscribe Pattern với Kafka, RabbitMQ).</li>
    </ul>
  </div>

  <div class="card-grid">
    <div class="card">
      <div class="card-title">⚖️ Giao Thức Cam Kết Hai Pha (Two-Phase Commit - 2PC)</div>
      <div class="card-content">
        <p>Đảm bảo tính nhất quán dữ liệu ACID phân tán:</p>
        <ul style="padding-left: 1.2rem;">
          <li><strong>Pha 1 (Prepare Phase)</strong>: Điều phối viên (Coordinator) gửi thông điệp <em>Prepare</em> tới tất cả các nút dịch vụ tham gia. Các nút khóa tài nguyên cục bộ và bỏ phiếu (Vote YES nếu sẵn sàng, Vote NO nếu lỗi).</li>
          <li><strong>Pha 2 (Commit Phase)</strong>: Nếu <em>tất cả 100% các nút đều vote YES</em>, Coordinator phát lệnh <strong>Global Commit</strong>. Nếu có dù chỉ một nút vote NO hoặc timeout, phát lệnh <strong>Global Abort/Rollback</strong>.</li>
        </ul>
      </div>
    </div>

    <div class="card">
      <div class="card-title">🎼 Orchestration vs Choreography (Điều Phối Dịch Vụ)</div>
      <div class="card-content">
        <ul style="padding-left: 1.2rem;">
          <li><strong>Orchestration (Hòa âm chỉ huy tập trung)</strong>: Có một bộ điều phối trung tâm (Orchestrator / Process Manager) đóng vai trò nhạc trưởng, ra lệnh tuần tự cho từng dịch vụ (Ví dụ: BPEL Engine, Camunda). Dễ kiểm soát quy trình nhưng tạo điểm nghẽn cổ chai.</li>
          <li><strong>Choreography (Vũ đạo phân tán tự do)</strong>: Không có nhạc trưởng. Mỗi dịch vụ tự lắng nghe sự kiện trên Event Bus và tự quyết định kích hoạt hành động tiếp theo. Tự do, phân tán cao nhưng khó theo dõi toàn cục luồng nghiệp vụ.</li>
        </ul>
      </div>
    </div>
  </div>
</section>

<!-- ========================================== -->
<!-- CHƯƠNG 17 -->
<!-- ========================================== -->
<section id="ch17" class="chapter-section">
  <div class="chapter-header">
    <div class="chapter-badge-row">
      <span class="chapter-badge">CHƯƠNG 17</span>
      <span class="chapter-lecturer-tag">Modular Engineering</span>
    </div>
    <h2 class="chapter-title">Thiết Kế Kiến Trúc Dựa Trên Thành Phần (Component-Based - CBD)</h2>
    <div class="chapter-subtitle">Composite Subsystems, Ports, Provided/Required Interfaces & Group Communication</div>
  </div>

  <div class="card-grid">
    <div class="card">
      <div class="card-title">📦 Composite Subsystems & Components</div>
      <div class="card-content">
        <p>Một <strong>Composite Subsystem</strong> là một thành phần đóng gói chứa các thành phần/đối tượng con bên trong:</p>
        <ul style="padding-left: 1.2rem;">
          <li>Đóng vai trò là thùng chứa logic lẫn vật lý (Container).</li>
          <li>Bản thân Subsystem không bổ sung thêm hành vi mà hành vi do các thành phần con cấu thành hiện thực.</li>
          <li>Có thể triển khai độc lập trên các nút phần cứng vật lý phân tán.</li>
        </ul>
      </div>
    </div>

    <div class="card">
      <div class="card-title">🔌 Ký Hiệu UML 2 Cho Ports & Interfaces</div>
      <div class="card-content">
        <ul style="padding-left: 1.2rem;">
          <li><strong>Port (Cổng)</strong>: Điểm tương tác ranh giới được vẽ bằng hình vuông nhỏ trên viền Component.</li>
          <li><strong>Provided Interface (Giao diện cung cấp)</strong>: Biểu diễn bằng hình que kẹo mút (<strong>Lollipop notation &bull;&ndash;</strong>) thể hiện dịch vụ mà component phục vụ cho bên ngoài.</li>
          <li><strong>Required Interface (Giao diện yêu cầu)</strong>: Biểu diễn bằng hình ổ cắm nửa vòng tròn (<strong>Socket notation &mdash;(</strong>) thể hiện dịch vụ mà component bắt buộc phải có để hoạt động.</li>
        </ul>
      </div>
    </div>

    <div class="card">
      <div class="card-title">📡 Các Mẫu Truyền Thông Nhóm (Group Message Patterns)</div>
      <div class="card-content">
        <ul style="padding-left: 1.2rem;">
          <li><strong>Broadcast</strong>: Gửi một thông điệp đồng loạt tới tất cả các nút trong mạng không phân biệt.</li>
          <li><strong>Multicast</strong>: Gửi thông điệp tới một nhóm cụ thể các thành phần quan tâm đã tham gia nhóm (Group Membership).</li>
          <li><strong>Publish / Subscribe</strong>: Phân tán dựa trên chủ đề (Topic-based) hoặc nội dung (Content-based), loại bỏ hoàn toàn sự phụ thuộc địa chỉ mạng giữa người gửi và người nhận.</li>
        </ul>
      </div>
    </div>
  </div>
</section>

<!-- ========================================== -->
<!-- CHƯƠNG 18 -->
<!-- ========================================== -->
<section id="ch18" class="chapter-section">
  <div class="chapter-header">
    <div class="chapter-badge-row">
      <span class="chapter-badge">CHƯƠNG 18</span>
      <span class="chapter-lecturer-tag">Real-Time & Embedded</span>
    </div>
    <h2 class="chapter-title">Thiết Kế Kiến Trúc Đồng Thời & Thời Gian Thực (Concurrent & Real-Time)</h2>
    <div class="chapter-subtitle">Task Structuring, Synchronization, Priority Inversion & Rate Monotonic Analysis (RMA)</div>
  </div>

  <div class="card-grid">
    <div class="card">
      <div class="card-title">⏱️ Phân Loại Hệ Thống Thời Gian Thực</div>
      <div class="card-content">
        <ul style="padding-left: 1.2rem;">
          <li><strong>Hard Real-Time (Thời gian thực cứng)</strong>: Nếu vi phạm Deadline (hạn chót hoàn thành) dù chỉ 1 mili-giây sẽ dẫn đến <em>thảm họa nguy hiểm tính mạng hoặc phá hủy toàn bộ hệ thống</em> (Túi khí ô tô, Hệ thống điều khiển thanh nhiên liệu hạt nhân, Máy thở y tế).</li>
          <li><strong>Soft Real-Time (Thời gian thực mềm)</strong>: Vi phạm deadline chỉ làm suy giảm chất lượng dịch vụ (QoS) nhưng không làm hỏng hệ thống (Live stream video bị giật khung hình, Voice over IP).</li>
          <li><strong>Firm Real-Time</strong>: Kết quả trả về sau deadline là vô giá trị, nhưng không gây ra thảm họa (Giao dịch chứng khoán realtime).</li>
        </ul>
      </div>
    </div>

    <div class="card">
      <div class="card-title">📥 Tiêu Chí Cấu Trúc Tác Vụ In / Out (I/O Tasks)</div>
      <div class="card-content">
        <ul style="padding-left: 1.2rem;">
          <li><strong>Event-driven I/O Task</strong>: Kích hoạt khi có ngắt phần cứng (Hardware Interrupt) từ cảm biến báo có sự kiện mới.</li>
          <li><strong>Periodic I/O Task</strong>: Quét (Poll) trạng thái cảm biến định kỳ theo khoảng thời gian cố định $\Delta t$ (Dùng cho cảm biến không có ngắt).</li>
          <li><strong>Demand-driven (Passive) I/O Task</strong>: Chỉ kích hoạt khi có yêu cầu xuất từ tác vụ khác (Ví dụ: Tác vụ in biên lai).</li>
        </ul>
      </div>
    </div>

    <div class="card">
      <div class="card-title">⚙️ Tiêu Chí Cấu Trúc Tác Vụ Nội Bộ (Internal Tasks)</div>
      <div class="card-content">
        <ul style="padding-left: 1.2rem;">
          <li><strong>Periodic Task</strong>: Tác vụ tính toán nội bộ chạy theo chu kỳ đều đặn (Ví dụ: Tính toán vị trí xe tự hành mỗi 50ms).</li>
          <li><strong>State-dependent Control Task</strong>: Tác vụ thực thi máy trạng thái hữu hạn điều khiển toàn bộ luồng vận hành.</li>
          <li><strong>Coordinator Task</strong>: Điều phối hàng đợi thông điệp giữa các tác vụ khác nhau.</li>
        </ul>
      </div>
    </div>
  </div>

  <div class="topic-card">
    <div class="topic-title">⚠️ Hiện Tượng Nghịch Đảo Độ Ưu Tiên (Priority Inversion) & Giải Pháp</div>
    <p>
      Hiện tượng nguy hiểm xảy ra khi một tác vụ ưu tiên cao ($Task_H$) bị chặn gián tiếp bởi một tác vụ ưu tiên thấp ($Task_L$) đang giữ khóa Mutex, trong khi một tác vụ ưu tiên trung bình ($Task_M$) lại cướp quyền CPU của $Task_L$, khiến $Task_H$ bị trễ hạn chót (từng suýt làm hỏng sứ mệnh tàu Mars Pathfinder của NASA năm 1997!).
    </p>
    <div class="callout callout-important">
      <div class="callout-title">🛡️ Giao Thức Kế Thừa Độ Ưu Tiên (Priority Inheritance Protocol)</div>
      <p>
        Khi $Task_H$ cố gắng truy cập Mutex đang bị $Task_L$ nắm giữ, $Task_L$ sẽ <strong>tạm thời được nâng độ ưu tiên lên bằng đúng mức của $Task_H$</strong>. Nhờ đó, $Task_M$ không thể cướp quyền $Task_L$ được nữa! $Task_L$ nhanh chóng chạy xong vùng tranh chấp, giải phóng Mutex và hạ về ưu tiên cũ, giúp $Task_H$ tiếp tục thực thi ngay lập tức.
      </p>
    </div>
  </div>

  <div class="topic-card">
    <div class="topic-title">📐 Định Luật Lập Lịch Rate Monotonic Analysis (RMA Schedulability Formula)</div>
    <p>
      Trong hệ thống thời gian thực với $n$ tác vụ định kỳ độc lập có chu kỳ $T_i$ và thời gian thực thi tối đa $C_i$, 
      thuật toán gán ưu tiên theo tần số (chu kỳ càng ngắn thì độ ưu tiên càng cao).
      Hệ thống đảm bảo <strong>chắc chắn 100% thỏa mãn mọi deadline</strong> nếu tổng hệ số sử dụng bộ vi xử lý (Processor Utilization) thỏa mãn công thức cận trên Liu &amp; Layland:
    </p>

    <div style="text-align: center; margin: 1.25rem 0; font-size: 1.3rem;">
      $$U = \sum_{i=1}^{n} \frac{C_i}{T_i} \le n \left( 2^{1/n} - 1 \right)$$
    </div>

    <div class="table-wrap">
      <table class="styled-table">
        <thead>
          <tr>
            <th>Số Lượng Tác Vụ ($n$)</th>
            <th>Công Thức Cận Trên $n(2^{1/n} - 1)$</th>
            <th>Ngưỡng Sử Dụng CPU Tối Đa An Toàn ($U_{bound}$)</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>$n = 1$</td>
            <td>$1 \times (2^1 - 1)$</td>
            <td><strong>$100.0\%$</strong></td>
          </tr>
          <tr>
            <td>$n = 2$</td>
            <td>$2 \times (2^{1/2} - 1) = 2 \times (\sqrt{2} - 1)$</td>
            <td><strong>$82.8\%$</strong></td>
          </tr>
          <tr>
            <td>$n = 3$</td>
            <td>$3 \times (2^{1/3} - 1)$</td>
            <td><strong>$78.0\%$</strong></td>
          </tr>
          <tr>
            <td>$n \to \infty$ (Vô hạn tác vụ)</td>
            <td>$\lim_{n \to \infty} n (2^{1/n} - 1) = \ln 2$</td>
            <td><strong>$\approx 69.3\%$</strong> (Ngưỡng an toàn tuyệt đối)</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</section>
"""

