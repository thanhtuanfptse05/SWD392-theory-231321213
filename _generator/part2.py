# _generator/part2.py
# Part 2: Mô Hình Hóa Phân Tích Hệ Thống Với UML (Chương 6 - 11)

def get_part2_html():
    return r"""
<!-- ========================================== -->
<!-- PART 2 DIVIDER BANNER -->
<!-- ========================================== -->
<div id="part-2" class="part-divider-banner part-2-banner">
  <span class="part-badge-tag">Phần 2 &bull; Phân Tích & Mô Hình Hóa</span>
  <h2 class="part-title">Mô Hình Hóa Phân Tích Hệ Thống Với UML</h2>
  <p class="part-desc">
    Đi sâu vào kỹ nghệ phân tích miền bài toán (Problem Domain): Khai thác và chuẩn hóa yêu cầu với Use Case Modeling (Ch 6), xây dựng mô hình tĩnh cấu trúc thực thể và ngữ cảnh hệ thống (Ch 7), phân loại đối tượng chuyên biệt theo 4 Stereotypes chuẩn COMET (Ch 8), và mô hình hóa hành vi động thông qua Biểu đồ giao tiếp, Biểu đồ tuần tự và Máy trạng thái hữu hạn Finite State Machines (Ch 9 - 11).
  </p>
</div>

<!-- ========================================== -->
<!-- CHƯƠNG 6 -->
<!-- ========================================== -->
<section id="ch06" class="chapter-section">
  <div class="chapter-header">
    <div class="chapter-badge-row">
      <span class="chapter-badge">CHƯƠNG 06</span>
      <span class="chapter-lecturer-tag">Requirements Engineering</span>
    </div>
    <h2 class="chapter-title">Mô Hình Hóa Use Case (Use Case Modeling)</h2>
    <div class="chapter-subtitle">Requirements Analysis, Actor Identification, Specs & Activity Diagrams</div>
  </div>

  <div class="card-grid">
    <div class="card">
      <div class="card-title">📦 Hệ Thống Dưới Dạng Hộp Đen (Black Box)</div>
      <div class="card-content">
        <p>Trong mô hình hóa yêu cầu, hệ thống được nhìn nhận như một <strong>chiếc hộp đen</strong>:</p>
        <ul style="padding-left: 1.2rem;">
          <li>Chỉ xem xét các đặc tính và phản hồi đối ngoại nhìn thấy từ phía người dùng.</li>
          <li>Tuyệt đối <em>không quan tâm đến kiến trúc nội bộ, database hay mã nguồn bên trong</em> ở bước này.</li>
          <li>Xác định ranh giới rõ ràng: Cái gì là trách nhiệm của hệ thống, cái gì thuộc môi trường bên ngoài.</li>
        </ul>
      </div>
    </div>

    <div class="card">
      <div class="card-title">🎭 Bản Chất Của Actor & Phân Loại</div>
      <div class="card-content">
        <p><strong>Actor</strong> đại diện cho vai trò (Role) của người dùng hoặc thực thể ngoài tương tác với hệ thống:</p>
        <ul style="padding-left: 1.2rem;">
          <li><strong>Primary Actor</strong>: Tác nhân chính, trực tiếp khởi tạo Use Case nhằm đạt được mục tiêu có giá trị (Ví dụ: Khách hàng rút tiền).</li>
          <li><strong>Secondary Actor</strong>: Tác nhân phụ, tham gia hỗ trợ hệ thống hoàn thành Use Case (Ví dụ: Hệ thống xác thực thẻ liên ngân hàng).</li>
          <li><strong>Non-Human Actors</strong>: Thiết bị I/O ngoài (Cảm biến quang, Đầu đọc thẻ), Bộ định thời (Timer clock), hoặc Hệ thống ngoài (External System).</li>
        </ul>
      </div>
    </div>

    <div class="card">
      <div class="card-title">⚡ Quy Tắc Đặt Tên & Nhận Diện Use Case</div>
      <div class="card-content">
        <ul style="padding-left: 1.2rem;">
          <li>Cú pháp chuẩn bắt buộc: <strong>[Động Từ] + [Danh Từ]</strong> (Verb + Noun). Ví dụ: <em>Withdraw Cash</em>, <em>Validate PIN</em>, <em>View Alarms</em>.</li>
          <li><strong>Tránh bẫy Functional Decomposition</strong>: Không bẻ vụn Use Case thành các thao tác nhỏ lẻ như "Nhập mật khẩu", "Bấm nút OK". Một Use Case phải mang lại giá trị trọn vẹn.</li>
        </ul>
      </div>
    </div>
  </div>

  <div class="topic-card">
    <div class="topic-title">📋 8 Tiêu Chí Vàng Đánh Giá Đặc Tả Yêu Cầu Phần Mềm (SRS Quality Criteria)</div>
    <div class="table-wrap">
      <table class="styled-table">
        <thead>
          <tr>
            <th>Tiêu Chí</th>
            <th>Ý Nghĩa & Mục Tiêu Kỹ Thuật</th>
            <th>Cách Thức Đảm Bảo Trong Dự Án</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>1. Correct (Chính xác)</strong></td>
            <td>Mọi yêu cầu ghi lại phải phản ánh đúng nhu cầu thực tế của khách hàng.</td>
            <td>Review và ký duyệt nghiệm thu cùng Product Owner / Stakeholder.</td>
          </tr>
          <tr>
            <td><strong>2. Complete (Đầy đủ)</strong></td>
            <td>Không bỏ sót chức năng, trường dữ liệu, kịch bản ngoại lệ hay thuộc tính chất lượng nào.</td>
            <td>Lập Ma trận bao phủ yêu cầu (Traceability Matrix).</td>
          </tr>
          <tr>
            <td><strong>3. Unambiguous (Không mơ hồ)</strong></td>
            <td>Mỗi câu từ chỉ có duy nhất một cách hiểu, không dùng từ ngữ cảm tính ("nhanh", "đẹp", "dễ dùng").</td>
            <td>Định lượng hóa yêu cầu bằng chỉ số đo lường cụ thể (ms, TPS, % uptime).</td>
          </tr>
          <tr>
            <td><strong>4. Consistent (Nhất quán)</strong></td>
            <td>Các yêu cầu không được mâu thuẫn hay triệt tiêu lẫn nhau về thuật ngữ, nghiệp vụ hay giao diện.</td>
            <td>Sử dụng từ điển thuật ngữ chung (Data Glossary).</td>
          </tr>
          <tr>
            <td><strong>5. Verifiable (Kiểm chứng được)</strong></td>
            <td>Mỗi yêu cầu đều có thể thiết kế được ca kiểm thử (Test Case) để xác nhận Đạt hoặc Không Đạt.</td>
            <td>Viết Acceptance Criteria đi kèm từng Use Case.</td>
          </tr>
          <tr>
            <td><strong>6. Understandable (Dễ hiểu)</strong></td>
            <td>Chuyên gia nghiệp vụ không chuyên về máy tính vẫn có thể đọc và hiểu thông suốt.</td>
            <td>Trình bày bằng ngôn ngữ tự nhiên kết hợp biểu đồ Use Case trực quan.</td>
          </tr>
          <tr>
            <td><strong>7. Modifiable (Dễ sửa đổi)</strong></td>
            <td>Cấu trúc tài liệu mạch lạc, có mục lục, đánh số thứ tự rõ ràng để dễ cập nhật.</td>
            <td>Định dạng module hóa từng Use Case riêng biệt.</td>
          </tr>
          <tr>
            <td><strong>8. Traceable (Truy vết được)</strong></td>
            <td>Mỗi yêu cầu có mã định danh duy nhất để truy vết xuôi tới Code và truy ngược về Business Goal.</td>
            <td>Đánh số mã định danh duy nhất (Ví dụ: <code>UC-ATM-001</code>).</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>

  <div class="topic-card">
    <div class="topic-title">📄 Cấu Trúc Khung Đặc Tả Use Case Chuẩn (Use Case Specification Schema)</div>
    <div class="card-grid">
      <div class="concept-box">
        <div class="concept-title">1. Header & Meta</div>
        <p><strong>Use Case Name</strong>: Tên động từ + danh từ.<br>
        <strong>ID</strong>: Mã định danh duy nhất.<br>
        <strong>Summary</strong>: Tóm tắt 1-2 câu về mục đích.<br>
        <strong>Actors</strong>: Primary &amp; Secondary actors.</p>
      </div>
      <div class="concept-box">
        <div class="concept-title">2. Pre & Post Conditions</div>
        <p><strong>Preconditions</strong>: Điều kiện bắt buộc phải đúng trước khi Use Case kích hoạt (Ví dụ: <em>Người dùng đã đăng nhập</em>).<br>
        <strong>Postconditions</strong>: Trạng thái hệ thống sau khi Use Case hoàn thành thành công (Ví dụ: <em>Tiền được nhả và số dư tài khoản bị trừ</em>).</p>
      </div>
      <div class="concept-box">
        <div class="concept-title">3. Flow of Events</div>
        <p><strong>Main Sequence</strong>: Chuỗi các bước tương tác tương hỗ tuần tự giữa Actor và System khi mọi thứ diễn ra suôn sẻ (Happy Path).<br>
        <strong>Alternative Sequences</strong>: Các nhánh rẽ xử lý lỗi hoặc kịch bản ngoại lệ (Ví dụ: <em>PIN sai, số dư không đủ, máy hết tiền</em>).</p>
      </div>
    </div>
  </div>

  <div class="callout callout-warning">
    <div class="callout-title">⚠️ Phân Biệt Tuyệt Đối: &laquo;include&raquo; vs &laquo;extend&raquo; vs Generalization</div>
    <ul style="padding-left: 1.2rem;">
      <li><code>&laquo;include&raquo;</code> (Bắt buộc): Use Case gốc <strong>luôn luôn</strong> gọi Use Case được include trong mọi kịch bản. Dùng để tái sử dụng một chuỗi tương tác dùng chung (Ví dụ: <em>Withdraw Cash</em> &rarr; <code>&laquo;include&raquo;</code> &rarr; <em>Validate PIN</em>). Mũi tên nét đứt trỏ từ Use Case gốc sang Use Case con.</li>
      <li><code>&laquo;extend&raquo;</code> (Tùy chọn có điều kiện): Use Case mở rộng chỉ được kích hoạt tại các điểm mở rộng (<strong>Extension Points</strong>) khi một điều kiện ngoại lệ xảy ra (Ví dụ: <em>Validate PIN</em> &larr; <code>&laquo;extend&raquo;</code> &larr; <em>Confiscate Card</em> khi nhập sai 3 lần). Mũi tên nét đứt trỏ <strong>ngược</strong> từ Use Case mở rộng về Use Case gốc!</li>
      <li><strong>Generalization</strong>: Kế thừa giữa các Use Case (hoặc giữa các Actor). Use Case con là một biến thể cụ thể của Use Case cha (Ví dụ: <em>Pay by Credit Card</em> kế thừa <em>Make Payment</em>).</li>
    </ul>
  </div>

  <!-- SVG Diagram: Use Case Diagram -->
  <div class="diagram-card">
    <div class="svg-container">
      <svg viewBox="0 0 850 300" xmlns="http://www.w3.org/2000/svg" style="font-family: 'Plus Jakarta Sans', sans-serif;">
        <rect width="850" height="300" rx="14" fill="#ffffff" stroke="#e2e8f0" stroke-width="2"/>
        <text x="425" y="28" text-anchor="middle" font-size="15" font-weight="800" fill="#0f172a">MÔ HÌNH HÓA QUAN HỆ USE CASE TRONG HỆ THỐNG ATM (COMET USE CASE MODEL)</text>
        
        <!-- System Boundary Box -->
        <rect x="220" y="45" width="410" height="240" rx="10" fill="#f8fafc" stroke="#94a3b8" stroke-width="1.8" stroke-dasharray="6,4"/>
        <text x="240" y="70" font-size="12" font-weight="800" fill="#64748b">ATM System Boundary</text>

        <!-- Primary Actor: Customer -->
        <circle cx="80" cy="115" r="16" fill="#e0f2fe" stroke="#0284c7" stroke-width="2"/>
        <line x1="80" y1="131" x2="80" y2="170" stroke="#0284c7" stroke-width="2"/>
        <line x1="55" y1="145" x2="105" y2="145" stroke="#0284c7" stroke-width="2"/>
        <line x1="80" y1="170" x2="60" y2="205" stroke="#0284c7" stroke-width="2"/>
        <line x1="80" y1="170" x2="100" y2="205" stroke="#0284c7" stroke-width="2"/>
        <text x="80" y="228" text-anchor="middle" font-size="12" font-weight="800" fill="#0369a1">ATM Customer</text>

        <!-- Secondary Actor: Bank Server -->
        <rect x="690" y="110" width="130" height="70" rx="8" fill="#eef2ff" stroke="#4f46e5" stroke-width="2"/>
        <text x="755" y="140" text-anchor="middle" font-size="12" font-weight="800" fill="#4338ca">&laquo;external system&raquo;</text>
        <text x="755" y="160" text-anchor="middle" font-size="13" font-weight="700" fill="#0f172a">Bank Server</text>

        <!-- Use Cases -->
        <!-- UC 1: Withdraw Cash -->
        <ellipse cx="330" cy="110" rx="80" ry="26" fill="#e0f2fe" stroke="#0284c7" stroke-width="1.8"/>
        <text x="330" y="115" text-anchor="middle" font-size="12" font-weight="700" fill="#0369a1">Withdraw Cash</text>
        <line x1="105" y1="135" x2="252" y2="115" stroke="#0284c7" stroke-width="1.8"/>

        <!-- UC 2: Validate PIN -->
        <ellipse cx="520" cy="110" rx="75" ry="25" fill="#f1f5f9" stroke="#475569" stroke-width="1.8"/>
        <text x="520" y="115" text-anchor="middle" font-size="12" font-weight="700" fill="#334155">Validate PIN</text>
        <!-- Include arrow -->
        <path d="M 410 110 L 445 110" stroke="#0284c7" stroke-width="1.8" stroke-dasharray="4,3"/>
        <polygon points="445,107 452,110 445,113" fill="#0284c7"/>
        <text x="430" y="100" text-anchor="middle" font-size="9.5" font-weight="700" fill="#0284c7">&laquo;include&raquo;</text>

        <!-- UC 3: Query Account -->
        <ellipse cx="330" cy="180" rx="75" ry="25" fill="#e0f2fe" stroke="#0284c7" stroke-width="1.8"/>
        <text x="330" y="185" text-anchor="middle" font-size="12" font-weight="700" fill="#0369a1">Query Account</text>
        <line x1="105" y1="155" x2="255" y2="180" stroke="#0284c7" stroke-width="1.8"/>

        <!-- UC 4: Confiscate Card -->
        <ellipse cx="520" cy="205" rx="75" ry="25" fill="#fee2e2" stroke="#dc2626" stroke-width="1.8"/>
        <text x="520" y="210" text-anchor="middle" font-size="11.5" font-weight="700" fill="#b91c1c">Confiscate Card</text>
        <!-- Extend arrow (points UP to Validate PIN) -->
        <path d="M 520 180 L 520 135" stroke="#dc2626" stroke-width="1.8" stroke-dasharray="4,3"/>
        <polygon points="517,142 520,135 523,142" fill="#dc2626"/>
        <text x="560" y="162" text-anchor="middle" font-size="9.5" font-weight="700" fill="#dc2626">&laquo;extend&raquo;</text>

        <!-- Connect to Secondary Actor -->
        <line x1="595" y1="110" x2="690" y2="140" stroke="#4f46e5" stroke-width="1.8"/>
        <line x1="405" y1="180" x2="690" y2="150" stroke="#4f46e5" stroke-width="1.8"/>
      </svg>
    </div>
    <div class="diagram-caption">Sơ đồ 6.1: Biểu đồ Use Case chuẩn thể hiện ranh giới hệ thống, quan hệ &laquo;include&raquo; và &laquo;extend&raquo;</div>
  </div>
</section>

<!-- ========================================== -->
<!-- CHƯƠNG 7 -->
<!-- ========================================== -->
<section id="ch07" class="chapter-section">
  <div class="chapter-header">
    <div class="chapter-badge-row">
      <span class="chapter-badge">CHƯƠNG 07</span>
      <span class="chapter-lecturer-tag">Structural Analysis</span>
    </div>
    <h2 class="chapter-title">Mô Hình Hóa Tĩnh (Static Modeling)</h2>
    <div class="chapter-subtitle">System Context, Stereotypes, Associations, Aggregation & Composition</div>
  </div>

  <div class="card-grid">
    <div class="card">
      <div class="card-title">🏛️ Bản Chất Của Mô Hình Tĩnh</div>
      <div class="card-content">
        <p>Mô hình tĩnh tập trung vào <strong>cấu trúc cấu thành không thay đổi theo thời gian</strong> của bài toán:</p>
        <ul style="padding-left: 1.2rem;">
          <li>Cấu trúc dữ liệu và thực thể thường ổn định và ít biến động hơn các chức năng nghiệp vụ cụ thể.</li>
          <li>Xác định các lớp thực thể (Entity Classes), các thuộc tính (Attributes) và mối liên kết logic giữa chúng.</li>
          <li>Được thể hiện thông qua <strong>Biểu đồ lớp UML (Class Diagram)</strong>.</li>
        </ul>
      </div>
    </div>

    <div class="card">
      <div class="card-title">🌐 Mô Hình Ngữ Cảnh Hệ Thống (Context Modeling)</div>
      <div class="card-content">
        <ul style="padding-left: 1.2rem;">
          <li><strong>System Context Class Diagram</strong>: Biểu diễn ranh giới giữa toàn bộ hệ thống (gồm cả phần cứng + phần mềm, đóng vai trò hộp đen) với môi trường bên ngoài.</li>
          <li><strong>Software System Context Diagram</strong>: Đặt phần mềm ở trung tâm; lúc này các thiết bị phần cứng (cảm biến, máy in thẻ, actuator) được xem là các thực thể bên ngoài tương tác với phần mềm.</li>
        </ul>
      </div>
    </div>

    <div class="card">
      <div class="card-title">🏷️ Phân Loại Stereotypes Trong COMET</div>
      <div class="card-content">
        <p>COMET phân nhóm các lớp thông qua Stereotypes chuẩn:</p>
        <ul style="padding-left: 1.2rem;">
          <li><code>&laquo;entity&raquo;</code>: Lớp thực thể lưu trữ dữ liệu bền vững (Persistent).</li>
          <li><code>&laquo;boundary&raquo;</code>: Lớp biên tương tác môi trường ngoài.</li>
          <li><code>&laquo;control&raquo;</code>: Lớp điều khiển, điều phối Use Case.</li>
          <li><code>&laquo;external user&raquo;</code>, <code>&laquo;external system&raquo;</code>, <code>&laquo;external I/O device&raquo;</code>, <code>&laquo;external timer&raquo;</code>.</li>
        </ul>
      </div>
    </div>
  </div>

  <div class="topic-card">
    <div class="topic-title">🔍 Chi Tiết Các Kiểu Liên Kết & Cấp Bậc Trong Biểu Đồ Lớp</div>
    <div class="table-wrap">
      <table class="styled-table">
        <thead>
          <tr>
            <th>Loại Liên Kết</th>
            <th>Mô Tả & Bản Chất Ngữ Nghĩa</th>
            <th>Ví Dụ Minh Họa</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Unary Association</strong> (Tự liên kết)</td>
            <td>Liên kết giữa một đối tượng của lớp này với một đối tượng khác thuộc <em>chính lớp đó</em>.</td>
            <td><code>Employee</code> <em>quản lý (is boss of)</em> <code>Employee</code>; <code>Person</code> <em>kết hôn với</em> <code>Person</code>.</td>
          </tr>
          <tr>
            <td><strong>Ternary Association</strong> (Liên kết tam nguyên)</td>
            <td>Mối liên kết đồng thời giữa 3 lớp độc lập với nhau.</td>
            <td><code>Buyer</code> đàm phán giá với <code>Seller</code> thông qua trung gian <code>Agent</code>.</td>
          </tr>
          <tr>
            <td><strong>Association Class</strong> (Lớp liên kết)</td>
            <td>Một lớp được tạo ra để lưu trữ các thuộc tính của chính mối quan hệ Many-to-Many (M:N) giữa hai lớp khác.</td>
            <td><code>Employee</code> làm việc trong <code>Project</code>; thuộc tính <code>hoursWorked</code> nằm trên Association Class <code>Assignment</code>.</td>
          </tr>
          <tr>
            <td><strong>Aggregation Hierarchy</strong> (Quan hệ Tụ hợp)</td>
            <td>Toàn thể / Bộ phận yếu. Part có thể tồn tại mà không cần Whole; Part có thể thuộc về nhiều Whole khác nhau.</td>
            <td><code>Pond</code> (Ao) và <code>Duck</code> (Vịt). Vịt có thể bay sang ao khác.</td>
          </tr>
          <tr>
            <td><strong>Composition Hierarchy</strong> (Quan hệ Hợp thành)</td>
            <td>Toàn thể / Bộ phận mạnh. Part <em>chỉ thuộc duy nhất một Whole</em>. Khi Whole bị hủy, Part bắt buộc bị hủy theo.</td>
            <td><code>Building</code> (Tòa nhà) và <code>Room</code> (Phòng). Tòa nhà sập thì các phòng không còn tồn tại.</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</section>

<!-- ========================================== -->
<!-- CHƯƠNG 8 -->
<!-- ========================================== -->
<section id="ch08" class="chapter-section">
  <div class="chapter-header">
    <div class="chapter-badge-row">
      <span class="chapter-badge">CHƯƠNG 08</span>
      <span class="chapter-lecturer-tag">COMET Taxonomy</span>
    </div>
    <h2 class="chapter-title">Cấu Trúc Hóa Lớp & Đối Tượng (Object & Class Structuring)</h2>
    <div class="chapter-subtitle">Boundary, Entity, Control, and Application Logic Classes</div>
  </div>

  <p>
    Trong phương pháp COMET, việc phân rã hệ thống thành các đối tượng không phải là hành động tùy tiện mà tuân theo 
    <strong>Bộ Tiêu Chí Cấu Trúc Hóa Đối Tượng (Object Structuring Criteria)</strong> với 4 nhóm Stereotype cốt lõi:
  </p>

  <div class="card-grid">
    <div class="card" style="border-top: 4px solid #0284c7;">
      <div class="card-title">1. Boundary Objects (&laquo;boundary&raquo;)</div>
      <div class="card-content">
        <p>Giao tiếp trực tiếp với tác nhân bên ngoài môi trường:</p>
        <ul style="padding-left: 1.2rem;">
          <li><strong>User Interaction Objects</strong>: Nhận input từ người dùng (bàn phím, chuột, touch) và hiển thị kết quả ra màn hình (GUI Window, Console).</li>
          <li><strong>Device I/O Objects</strong>: Giao tiếp với thiết bị phần cứng (Sensor Interface, Actuator Interface, Motor Interface).</li>
          <li><strong>Proxy Objects</strong>: Đại diện trung gian kết nối mạng với hệ thống bên ngoài (External System Proxy).</li>
          <li><strong>Timer Objects</strong>: Nhận xung nhịp định thời gian thực từ OS clock.</li>
        </ul>
      </div>
    </div>

    <div class="card" style="border-top: 4px solid #4f46e5;">
      <div class="card-title">2. Entity Objects (&laquo;entity&raquo;)</div>
      <div class="card-content">
        <p>Lưu trữ và quản trị dữ liệu dài hạn:</p>
        <ul style="padding-left: 1.2rem;">
          <li>Lưu trữ thông tin bền vững (Persistent) cần truy cập xuyên suốt phiên làm việc.</li>
          <li>Cung cấp các thao tác đóng gói để đọc, ghi, cập nhật trạng thái dữ liệu an toàn.</li>
          <li>Thường được ánh xạ xuống các bảng trong Cơ sở dữ liệu quan hệ (RDBMS).</li>
          <li>Ví dụ: <code>Account</code>, <code>Customer</code>, <code>AlarmRecord</code>, <code>ItemCatalog</code>.</li>
        </ul>
      </div>
    </div>

    <div class="card" style="border-top: 4px solid #d97706;">
      <div class="card-title">3. Control Objects (&laquo;control&raquo;)</div>
      <div class="card-content">
        <p>Đóng vai trò như <strong>Nhạc trưởng trong dàn nhạc (Orchestra Conductor)</strong>:</p>
        <ul style="padding-left: 1.2rem;">
          <li>Điều phối hành vi và thứ tự tương tác giữa các đối tượng trong một Use Case phức tạp.</li>
          <li><strong>State-dependent Control Objects</strong>: Hành vi thay đổi theo từng trạng thái cụ thể dựa trên Biểu đồ máy trạng thái (Statechart).</li>
          <li><strong>Timer Control Objects</strong>: Được kích hoạt định kỳ bởi xung clock để thực thi tác vụ lặp lại theo chu kỳ.</li>
        </ul>
      </div>
    </div>

    <div class="card" style="border-top: 4px solid #059669;">
      <div class="card-title">4. Application Logic Objects</div>
      <div class="card-content">
        <p>Chứa đựng logic xử lý chuyên biệt độc lập với dữ liệu:</p>
        <ul style="padding-left: 1.2rem;">
          <li><strong>Business Logic Objects</strong>: Đóng gói các quy tắc nghiệp vụ có thể thay đổi độc lập với dữ liệu Entity (Ví dụ: Tính thuế, tính lãi suất vay).</li>
          <li><strong>Algorithm Objects</strong>: Đóng gói thuật toán tính toán phức tạp, chuyên sâu (Ví dụ: Thuật toán định tuyến đường đi ngắn nhất của xe tự hành AGV, nén ảnh).</li>
          <li><strong>Service Objects</strong>: Cung cấp dịch vụ cho nhiều client gọi tới, không tự phát sinh yêu cầu.</li>
        </ul>
      </div>
    </div>
  </div>
</section>

<!-- ========================================== -->
<!-- CHƯƠNG 9 - 11 -->
<!-- ========================================== -->
<section id="ch09-11" class="chapter-section">
  <div class="chapter-header">
    <div class="chapter-badge-row">
      <span class="chapter-badge">CHƯƠNG 09 - 11</span>
      <span class="chapter-lecturer-tag">Behavioral Modeling</span>
    </div>
    <h2 class="chapter-title">Mô Hình Hóa Động (Dynamic Modeling)</h2>
    <div class="chapter-subtitle">Communication Diagrams, Sequence Diagrams & Finite State Machines (FSM)</div>
  </div>

  <div class="topic-card">
    <div class="topic-title">⚖️ So Sánh: Communication Diagram vs Sequence Diagram</div>
    <p>
      Cả hai đều là Biểu đồ tương tác (Interaction Diagrams) mô tả chuỗi thông điệp truyền qua lại giữa các đối tượng, 
      nhưng có mục đích sử dụng và triết lý hiển thị khác nhau:
    </p>

    <div class="table-wrap">
      <table class="styled-table">
        <thead>
          <tr>
            <th>Tiêu Chí So Sánh</th>
            <th>Communication Diagram (Biểu Đồ Giao Tiếp)</th>
            <th>Sequence Diagram (Biểu Đồ Tuần Tự)</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Trục hiển thị chính</strong></td>
            <td>Không gian mạng lưới (Network Topology). Thể hiện cách các đối tượng được kết nối trực tiếp với nhau.</td>
            <td>Trục thời gian chạy từ trên xuống dưới dọc theo đường sống (Lifelines).</td>
          </tr>
          <tr>
            <td><strong>Biểu diễn thứ tự</strong></td>
            <td>Sử dụng số thứ tự thông điệp phân cấp: <code>1</code>, <code>1.1</code>, <code>1.2</code>, <code>2</code>.</td>
            <td>Vị trí tương đối theo chiều dọc từ đỉnh xuống đáy.</td>
          </tr>
          <tr>
            <td><strong>Vòng lặp &amp; Rẽ nhánh</strong></td>
            <td>Biểu diễn ngắn gọn nhưng khó nhìn khi logic rẽ nhánh quá phức tạp.</td>
            <td>Rất trực quan với các khung tương tác (Combined Fragments: <code>alt</code>, <code>opt</code>, <code>loop</code>).</td>
          </tr>
          <tr>
            <td><strong>Vai trò trong COMET</strong></td>
            <td><strong>Được ưu tiên hàng đầu</strong> &mdash; vì các biểu đồ giao tiếp từng Use Case sẽ được ghép nối trực tiếp thành <em>Integrated Communication Diagram</em> định hình kiến trúc hệ thống ban đầu!</td>
            <td>Được dùng hỗ trợ khi phân tích các ca tương tác dài, phức tạp hoặc có logic rẽ nhánh sâu.</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>

  <div class="card-grid">
    <div class="card">
      <div class="card-title">🔄 Quy Trình 4 Bước Mô Hình Hóa Tương Tác Phi Trạng Thái</div>
      <div class="card-content">
        <p>Áp dụng cho các Use Case không phụ thuộc vào trạng thái trước đó (Stateless Dynamic Interaction):</p>
        <ol style="padding-left: 1.2rem;">
          <li><strong>Bước 1</strong>: Phân tích kịch bản Use Case Model chuẩn.</li>
          <li><strong>Bước 2</strong>: Xác định các đối tượng tham gia thực thi (Boundary objects nhận input, Entity objects lấy data, Service objects).</li>
          <li><strong>Bước 3</strong>: Xác định chuỗi thông điệp tuần tự trong kịch bản chính (Main Sequence).</li>
          <li><strong>Bước 4</strong>: Xác định chuỗi thông điệp cho các kịch bản ngoại lệ (Alternative Sequences).</li>
        </ol>
      </div>
    </div>

    <div class="card">
      <div class="card-title">⚙️ Máy Trạng Thái Hữu Hạn (Finite State Machines - FSM)</div>
      <div class="card-content">
        <p>Mô hình hóa hành vi nội tại của đối tượng điều khiển theo thời gian:</p>
        <ul style="padding-left: 1.2rem;">
          <li><strong>State (Trạng thái)</strong>: Đại diện cho một tình huống tồn tại trong một khoảng thời gian nhất định (Ví dụ: <em>WaitingForPIN</em>, <em>DispensingCash</em>).</li>
          <li><strong>Event (Sự kiện)</strong>: Biến cố xảy ra tức thời tại một thời điểm kích hoạt chuyển trạng thái (Ví dụ: <em>CardInserted</em>, <em>PINEntered</em>).</li>
          <li><strong>Guard Condition [Điều kiện]</strong>: Mệnh đề logic đặt trong ngoặc vuông <code>[Condition]</code>. Chuyển dịch chỉ diễn ra khi điều kiện đúng.</li>
        </ul>
      </div>
    </div>
  </div>

  <div class="topic-card">
    <div class="topic-title">⚡ 3 Loại Hành Động Đầu Ra Trong Biểu Đồ Trạng Thái (Output Actions)</div>
    <div class="card-grid">
      <div class="concept-box" style="border-left-color: #3b82f6;">
        <div class="concept-title">1. Transition Action (Hành động trên cung chuyển)</div>
        <p>Cú pháp: <code>Event [Guard] / Action</code>. Hành động được thực thi tức thời ngay khi sự kiện xảy ra và thỏa mãn điều kiện canh gác để chuyển trạng thái.</p>
      </div>

      <div class="concept-box" style="border-left-color: #10b981;">
        <div class="concept-title">2. Entry Action (Hành động khi vào trạng thái)</div>
        <p>Cú pháp: <code>entry / Action</code>. Được gọi tự động mỗi khi luồng điều khiển đi vào trạng thái. <em>Dùng tốt nhất khi có nhiều cung chuyển dịch khác nhau cùng đi vào một trạng thái và đòi hỏi cùng một hành động khởi tạo</em>.</p>
      </div>

      <div class="concept-box" style="border-left-color: #f59e0b;">
        <div class="concept-title">3. Exit Action (Hành động khi rời trạng thái)</div>
        <p>Cú pháp: <code>exit / Action</code>. Được gọi tự động mỗi khi trạng thái bị thoát ra ngoài. <em>Dùng tốt nhất khi có nhiều cung chuyển dịch đi ra khỏi trạng thái và đòi hỏi cùng một hành động dọn dẹp tài nguyên</em>.</p>
      </div>
    </div>
  </div>

  <!-- SVG Diagram: ATM Statechart -->
  <div class="diagram-card">
    <div class="svg-container">
      <svg viewBox="0 0 880 270" xmlns="http://www.w3.org/2000/svg" style="font-family: 'Plus Jakarta Sans', sans-serif;">
        <rect width="880" height="270" rx="14" fill="#ffffff" stroke="#e2e8f0" stroke-width="2"/>
        <text x="440" y="28" text-anchor="middle" font-size="15" font-weight="800" fill="#0f172a">BIỂU ĐỒ MÁY TRẠNG THÁI ATM CONTROL (FINITE STATE MACHINE WITH GUARDS & ACTIONS)</text>
        
        <!-- Initial State -->
        <circle cx="50" cy="130" r="12" fill="#0f172a"/>
        <line x1="62" y1="130" x2="110" y2="130" stroke="#0f172a" stroke-width="2"/>
        <polygon points="105,126 112,130 105,134" fill="#0f172a"/>

        <!-- State 1: Idle -->
        <rect x="115" y="100" width="130" height="60" rx="10" fill="#f1f5f9" stroke="#475569" stroke-width="2"/>
        <text x="180" y="125" text-anchor="middle" font-size="13" font-weight="800" fill="#0f172a">Idle</text>
        <text x="180" y="145" text-anchor="middle" font-size="10.5" fill="#64748b">entry/ PromptCard</text>

        <!-- Transition 1 -> 2 -->
        <line x1="245" y1="120" x2="310" y2="120" stroke="#0284c7" stroke-width="2"/>
        <polygon points="305,116 312,120 305,124" fill="#0284c7"/>
        <text x="277" y="112" text-anchor="middle" font-size="10" font-weight="700" fill="#0284c7">CardInserted</text>

        <!-- State 2: WaitingForPIN -->
        <rect x="315" y="100" width="155" height="60" rx="10" fill="#e0f2fe" stroke="#0284c7" stroke-width="2"/>
        <text x="392" y="125" text-anchor="middle" font-size="13" font-weight="800" fill="#0369a1">WaitingForPIN</text>
        <text x="392" y="145" text-anchor="middle" font-size="10.5" fill="#475569">entry/ PromptPIN</text>

        <!-- Transition 2 -> 3 (Valid) -->
        <line x1="470" y1="120" x2="535" y2="120" stroke="#059669" stroke-width="2"/>
        <polygon points="530,116 537,120 530,124" fill="#059669"/>
        <text x="502" y="112" text-anchor="middle" font-size="10" font-weight="700" fill="#059669">PINOk [valid]</text>

        <!-- State 3: TransactionSelection -->
        <rect x="540" y="100" width="165" height="60" rx="10" fill="#d1fae5" stroke="#059669" stroke-width="2"/>
        <text x="622" y="125" text-anchor="middle" font-size="12.5" font-weight="800" fill="#047857">TransactionSelection</text>
        <text x="622" y="145" text-anchor="middle" font-size="10.5" fill="#475569">entry/ ShowMenu</text>

        <!-- Transition 2 -> Self (Invalid < 3) -->
        <path d="M 370 100 C 370 50, 420 50, 420 100" fill="none" stroke="#d97706" stroke-width="2"/>
        <polygon points="416,92 420,100 424,92" fill="#d97706"/>
        <text x="395" y="44" text-anchor="middle" font-size="9.5" font-weight="700" fill="#d97706">PINInvalid [attempts &lt; 3] / Beep</text>

        <!-- Transition 2 -> Confiscate (Invalid == 3) -->
        <path d="M 392 160 L 392 210" stroke="#dc2626" stroke-width="2"/>
        <polygon points="388,202 392,210 396,202" fill="#dc2626"/>
        <text x="465" y="188" text-anchor="middle" font-size="9.5" font-weight="700" fill="#dc2626">PINInvalid [attempts == 3] / Confiscate</text>

        <rect x="330" y="210" width="125" height="42" rx="8" fill="#fee2e2" stroke="#dc2626" stroke-width="2"/>
        <text x="392" y="235" text-anchor="middle" font-size="11.5" font-weight="800" fill="#b91c1c">CardConfiscated</text>

        <!-- Return to Idle from Transaction Done -->
        <path d="M 705 130 L 760 130 L 760 250 L 180 250 L 180 160" fill="none" stroke="#64748b" stroke-width="1.8" stroke-dasharray="5,4"/>
        <polygon points="176,168 180,160 184,168" fill="#64748b"/>
        <text x="560" y="244" text-anchor="middle" font-size="10" font-weight="600" fill="#64748b">TransactionComplete / EjectCard</text>
      </svg>
    </div>
    <div class="diagram-caption">Sơ đồ 11.1: Máy trạng thái hữu hạn ATM Control với cơ chế đếm số lần sai mã PIN và hành động Entry</div>
  </div>
</section>
"""

