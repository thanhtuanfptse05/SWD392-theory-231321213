# _generator/part4.py
# Part 4: Thuộc Tính Chất Lượng & Các Nghiên Cứu Điển Hình Thực Tế (Chương 20 - 24 & Case Studies)

def get_part4_html():
    return r"""
<!-- ========================================== -->
<!-- PART 4 DIVIDER BANNER -->
<!-- ========================================== -->
<div id="part-4" class="part-divider-banner part-4-banner">
  <span class="part-badge-tag">Phần 4 &bull; Chất Lượng & Thực Chiến</span>
  <h2 class="part-title">Thuộc Tính Chất Lượng & Nghiên Cứu Điển Hình (Case Studies)</h2>
  <p class="part-desc">
    Chinh phục các tiêu chuẩn đánh giá thuộc tính chất lượng phần mềm (Ch 20) và mổ xẻ chi tiết 5 hệ thống nghiên cứu điển hình kinh điển trong giáo trình: Hệ thống ngân hàng ATM Client/Server (Ch 21), Hệ thống mua sắm trực tuyến SOA (Ch 22), Hệ thống giám sát cấp cứu CBD (Ch 23), Hệ thống xe tự hành AGV thời gian thực (Ch 24), và Đồ án đặc tả kiến trúc toàn diện FreshFood Online System (FOS).
  </p>
</div>

<!-- ========================================== -->
<!-- CHƯƠNG 20 -->
<!-- ========================================== -->
<section id="ch20" class="chapter-section">
  <div class="chapter-header">
    <div class="chapter-badge-row">
      <span class="chapter-badge">CHƯƠNG 20</span>
      <span class="chapter-lecturer-tag">Quality Attributes & Tradeoffs</span>
    </div>
    <h2 class="chapter-title">Thuộc Tính Chất Lượng Phần Mềm (Software Quality Attributes)</h2>
    <div class="chapter-subtitle">Non-functional Requirements, Metrics & Tradeoff Analysis</div>
  </div>

  <div class="card-grid">
    <div class="card">
      <div class="card-title">🔧 Maintainability & Modifiability</div>
      <div class="card-content">
        <ul style="padding-left: 1.2rem;">
          <li><strong>Maintainability (Khả năng bảo trì)</strong>: Mức độ dễ dàng sửa chữa lỗi sót lại sau khi phần mềm đã vận hành thực tế, giải quyết vấn đề hiệu năng phát sinh trong môi trường production, và thích nghi với các thay đổi nghiệp vụ.</li>
          <li><strong>Modifiability (Khả năng sửa đổi)</strong>: Khả năng mở rộng, thêm bớt tính năng mà không phá vỡ cấu trúc có sẵn nhờ kiến trúc phân tầng, phân rã lỏng lẻo và áp dụng triệt để nguyên lý che giấu thông tin.</li>
        </ul>
      </div>
    </div>

    <div class="card">
      <div class="card-title">🧪 Testability & Traceability</div>
      <div class="card-content">
        <ul style="padding-left: 1.2rem;">
          <li><strong>Testability (Khả năng kiểm thử)</strong>: Mức độ dễ dàng lập kịch bản và thực thi kiểm thử. Hỗ trợ tốt nhờ tính đóng gói, giao diện rõ ràng và mức độ phụ thuộc thấp (Low Coupling).</li>
          <li><strong>Traceability (Khả năng truy vết)</strong>: Khả năng liên kết và đối chiếu hai chiều: Mỗi dòng code phải truy ngược về một quyết định thiết kế, mỗi quyết định thiết kế phải truy về một yêu cầu Use Case trong tài liệu SRS ban đầu.</li>
        </ul>
      </div>
    </div>

    <div class="card">
      <div class="card-title">⚡ Performance, Scalability & Security</div>
      <div class="card-content">
        <ul style="padding-left: 1.2rem;">
          <li><strong>Performance (Hiệu năng)</strong>: Đo bằng thông lượng (Throughput) và thời gian phản hồi (Response Time $R = S + W$).</li>
          <li><strong>Scalability (Khả năng co giãn)</strong>: Năng lực đáp ứng khi khối lượng công việc tăng lên (Vertical Scaling: Tăng RAM/CPU; Horizontal Scaling: Thêm node server).</li>
          <li><strong>Security (Bảo mật)</strong>: Đảm bảo 3 tiêu chí CIA (Confidentiality, Integrity, Availability).</li>
        </ul>
      </div>
    </div>
  </div>

  <div class="topic-card">
    <div class="topic-title">📐 Công Thức Tính Tính Sẵn Sàng (System Availability Formula)</div>
    <p>
      Tính sẵn sàng (Availability) là tỷ lệ phần trăm thời gian hệ thống hoạt động ổn định và sẵn sàng phục vụ người dùng. 
      Được tính toán dựa trên hai đại lượng thống kê:
    </p>
    <ul style="padding-left: 1.2rem; margin-bottom: 0.85rem;">
      <li><strong>MTTF (Mean Time To Failure)</strong>: Thời gian hoạt động trung bình giữa các lần gặp sự cố hỏng hóc.</li>
      <li><strong>MTTR (Mean Time To Repair)</strong>: Thời gian trung bình để đội ngũ kỹ thuật khắc phục sự cố và phục hồi hệ thống.</li>
    </ul>

    <div style="text-align: center; margin: 1.25rem 0; font-size: 1.3rem;">
      $$A = \frac{\text{MTTF}}{\text{MTTF} + \text{MTTR}} \times 100\%$$
    </div>

    <div class="callout callout-info">
      <div class="callout-title">💡 Tiêu Chuẩn "Năm Con Số Chín" (The Five Nines - 99.999% Availability)</div>
      <p>
        Trong các hệ thống viễn thông và tài chính ngân hàng, tiêu chuẩn <strong>99.999%</strong> đồng nghĩa với việc tổng thời gian hệ thống ngừng hoạt động (Downtime) cho phép <strong>không được vượt quá 5.26 phút trong suốt một năm</strong>!
      </p>
    </div>
  </div>

  <div class="topic-card">
    <div class="topic-title">⚖️ Ma Trận Đánh Đổi Thuộc Tính Chất Lượng (Quality Attribute Tradeoffs)</div>
    <div class="table-wrap">
      <table class="styled-table">
        <thead>
          <tr>
            <th>Quyết Định Kiến Trúc</th>
            <th>Thuộc Tính Được Tối Ưu (Ưu Điểm)</th>
            <th>Thuộc Tính Bị Ảnh Hưởng Tiêu Cực (Nhược Điểm / Chi Phí Đánh Đổi)</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>Chia nhỏ thành nhiều Microservices phân tán</td>
            <td><strong>Modifiability, Scalability, Autonomy</strong> (Các đội nhóm code và deploy độc lập).</td>
            <td><strong>Performance</strong> (Tăng độ trễ mạng Network Latency) &amp; <strong>Complexity</strong> (Khó giám sát, khó đồng bộ dữ liệu ACID).</td>
          </tr>
          <tr>
            <td>Thêm lớp mã hóa toàn bộ dữ liệu &amp; xác thực đa yếu tố</td>
            <td><strong>Security</strong> (Bảo vệ thông tin người dùng an toàn tối đa).</td>
            <td><strong>Performance</strong> (Tăng thời gian CPU giải mã và xử lý giao dịch).</td>
          </tr>
          <tr>
            <td>Sử dụng cơ chế Caching dữ liệu tại RAM (Redis)</td>
            <td><strong>Performance, Response Time</strong> (Truy vấn dữ liệu gần như tức thời).</td>
            <td><strong>Data Consistency</strong> (Rủi ro người dùng đọc phải dữ liệu cũ Stale Data khi database nguồn thay đổi).</td>
          </tr>
          <tr>
            <td>Ghi log kiểm toán chi tiết (Audit Logging)</td>
            <td><strong>Traceability, Security</strong> (Dễ điều tra gian lận và tìm nguồn lỗi).</td>
            <td><strong>Performance, Storage</strong> (Tốn dung lượng đĩa và làm chậm I/O ghi đĩa).</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</section>

<!-- ========================================== -->
<!-- CHƯƠNG 21 -->
<!-- ========================================== -->
<section id="ch21" class="chapter-section">
  <div class="chapter-header">
    <div class="chapter-badge-row">
      <span class="chapter-badge">CHƯƠNG 21</span>
      <span class="chapter-lecturer-tag">Case Study 1</span>
    </div>
    <h2 class="chapter-title">Hệ Thống Ngân Hàng Tự Động ATM (Banking System Case Study)</h2>
    <div class="chapter-subtitle">Client/Server Architecture, ATM Statechart, Database Schema & PIN Rules</div>
  </div>

  <div class="topic-card">
    <div class="topic-title">🏦 Bài Toán Nghiệp Vụ Cốt Lõi</div>
    <p>
      Một ngân hàng triển khai hàng loạt cây ATM phân tán địa lý kết nối qua mạng diện rộng (WAN) về máy chủ ngân hàng tập trung (Bank Server). 
      Mỗi cây ATM trang bị 4 thiết bị I/O: <em>Đầu đọc thẻ (Card Reader), Máy nhả tiền mặt (Cash Dispenser), Bàn phím/Màn hình (Keyboard/Display), và Máy in biên lai (Receipt Printer)</em>.
    </p>
    <div class="callout callout-warning">
      <div class="callout-title">🔒 Quy Tắc Nghiệp Vụ Xác Thực Mã PIN (PIN Validation Rule)</div>
      <ul style="padding-left: 1.2rem;">
        <li>Khách hàng được phép nhập mã PIN tối đa <strong>3 lần</strong>.</li>
        <li>Nếu lần thứ 3 nhập sai, thẻ ATM sẽ bị máy <strong>tịch thu (Confiscate Card)</strong> ngay lập tức để bảo vệ tài khoản.</li>
        <li>Các thẻ hết hạn (Expired) hoặc bị báo mất/trộm (Lost/Stolen) cũng bị tịch thu lập tức khi đưa vào đầu đọc thẻ.</li>
      </ul>
    </div>
  </div>

  <div class="card-grid">
    <div class="card">
      <div class="card-title">💻 ATM Client Subsystem</div>
      <div class="card-content">
        <p>Phân rã thành các đối tượng đóng gói trên máy ATM:</p>
        <ul style="padding-left: 1.2rem;">
          <li><code>CardReaderInterface</code>: Đối tượng biên đọc dải từ / chip.</li>
          <li><code>CashDispenserInterface</code>: Đối tượng biên ra lệnh đếm và nhả tiền.</li>
          <li><code>ReceiptPrinterInterface</code>: Đối tượng biên in hóa đơn.</li>
          <li><code>ATMControl</code>: Đối tượng điều khiển phụ thuộc trạng thái (State-dependent control), thực thi ATM Statechart.</li>
          <li><code>BankServerProxy</code>: Đối tượng đại diện (Proxy) đóng gói kết nối mạng gửi thông điệp tới Bank Server.</li>
        </ul>
      </div>
    </div>

    <div class="card">
      <div class="card-title">🖥️ Bank Service Subsystem</div>
      <div class="card-content">
        <p>Thành phần xử lý phía máy chủ trung tâm:</p>
        <ul style="padding-left: 1.2rem;">
          <li><code>BankService</code>: Cung cấp các thao tác xử lý giao dịch.</li>
          <li><code>BankCoordinator</code>: Điều phối xác thực và phân loại tài khoản.</li>
          <li><code>DebitCard</code>, <code>Account</code>, <code>CheckingAccount</code>, <code>SavingsAccount</code>: Các thực thể ánh xạ xuống cơ sở dữ liệu quan hệ.</li>
          <li><code>DatabaseWrapper</code>: Đóng gói các câu lệnh SQL truy vấn và cập nhật số dư.</li>
        </ul>
      </div>
    </div>
  </div>
</section>

<!-- ========================================== -->
<!-- CHƯƠNG 22 -->
<!-- ========================================== -->
<section id="ch22" class="chapter-section">
  <div class="chapter-header">
    <div class="chapter-badge-row">
      <span class="chapter-badge">CHƯƠNG 22</span>
      <span class="chapter-lecturer-tag">Case Study 2</span>
    </div>
    <h2 class="chapter-title">Hệ Thống Mua Sắm Trực Tuyến (Online Shopping System SOA Case Study)</h2>
    <div class="chapter-subtitle">Service-Oriented Architecture, Autonomous Services & Coordinator Objects</div>
  </div>

  <p>
    Nghiên cứu điển hình kiến trúc SOA trên nền tảng Web phân tán cao. 
    Hệ thống phân rã thành các dịch vụ độc lập tự trị, cộng tác thông qua các đối tượng môi giới (Object Brokers) và điều phối viên (Coordinator Objects):
  </p>

  <div class="card-grid">
    <div class="card">
      <div class="card-title">📚 Catalog Service</div>
      <div class="card-content">
        <p>Quản trị danh mục sản phẩm của các nhà cung cấp (Suppliers). Cho phép khách hàng tìm kiếm, lọc theo thể loại và xem chi tiết mặt hàng.</p>
      </div>
    </div>

    <div class="card">
      <div class="card-title">📦 Inventory Service</div>
      <div class="card-content">
        <p>Quản lý số lượng hàng tồn kho. Thực hiện kiểm tra tính khả dụng và <em>tạm giữ (Hold/Reserve inventory)</em> khi khách hàng đặt đơn.</p>
      </div>
    </div>

    <div class="card">
      <div class="card-title">💳 Credit Card Service</div>
      <div class="card-content">
        <p>Kết nối cổng thanh toán đối tác bên ngoài để xác thực hạn mức tín dụng và thực hiện trừ tiền an toàn.</p>
      </div>
    </div>

    <div class="card">
      <div class="card-title">🚚 Delivery Order Service</div>
      <div class="card-content">
        <p>Quản lý đơn vận chuyển, kết nối với nhà xe/đơn vị giao vận, theo dõi hành trình và cập nhật trạng thái đơn hàng.</p>
      </div>
    </div>

    <div class="card">
      <div class="card-title">📧 Email Notification Service</div>
      <div class="card-content">
        <p>Dịch vụ phi đồng bộ bắn email thông báo xác nhận đơn hàng, hóa đơn điện tử và thông tin giao hàng tới khách hàng.</p>
      </div>
    </div>

    <div class="card">
      <div class="card-title">🎯 Order Coordinator</div>
      <div class="card-content">
        <p>Điều phối viên trung tâm quản lý luồng giao dịch đặt hàng tổng hợp: Gọi Catalog &rarr; Khóa kho Inventory &rarr; Trừ tiền CreditCard &rarr; Tạo vận đơn Delivery &rarr; Bắn Email.</p>
      </div>
    </div>
  </div>
</section>

<!-- ========================================== -->
<!-- CHƯƠNG 23 -->
<!-- ========================================== -->
<section id="ch23" class="chapter-section">
  <div class="chapter-header">
    <div class="chapter-badge-row">
      <span class="chapter-badge">CHƯƠNG 23</span>
      <span class="chapter-lecturer-tag">Case Study 3</span>
    </div>
    <h2 class="chapter-title">Hệ Thống Giám Sát Cấp Cứu (Emergency Monitoring System CBD)</h2>
    <div class="chapter-subtitle">Component-Based Architecture, Remote Monitoring Nodes & Alarm Management</div>
  </div>

  <div class="topic-card">
    <div class="topic-title">🚨 Bài Toán Giám Sát Phân Tán</div>
    <p>
      Hệ thống bao gồm nhiều <strong>Trạm giám sát từ xa (Remote Monitoring Stations)</strong> đặt tại hiện trường để đo đạc các chỉ số an toàn (nhiệt độ, nồng độ khí độc, bức xạ) và một <strong>Trung tâm giám sát tập trung (Central Monitoring Station)</strong> nơi các kỹ thuật viên vận hành theo dõi và xử lý cảnh báo.
    </p>

    <div class="card-grid">
      <div class="concept-box">
        <div class="concept-title">Monitoring Sensor Component</div>
        <p>Thành phần đóng gói tại trạm từ xa thu thập dữ liệu cảm biến định kỳ và truyền dữ liệu thô về trung tâm.</p>
      </div>
      <div class="concept-box">
        <div class="concept-title">Alarm Filter Component</div>
        <p>Phân tích ngưỡng cảm biến. Nếu chỉ số vượt mức an toàn, tạo lập bản ghi cảnh báo (Alarm) và gửi tín hiệu ưu tiên cao về trung tâm.</p>
      </div>
      <div class="concept-box">
        <div class="concept-title">Operator Presentation Component</div>
        <p>Hiển thị bảng điều khiển danh sách các cảnh báo nổi bật (Active Alarms) để nhân viên bấm xác nhận (Acknowledge alarm).</p>
      </div>
    </div>
  </div>
</section>

<!-- ========================================== -->
<!-- CHƯƠNG 24 -->
<!-- ========================================== -->
<section id="ch24" class="chapter-section">
  <div class="chapter-header">
    <div class="chapter-badge-row">
      <span class="chapter-badge">CHƯƠNG 24</span>
      <span class="chapter-lecturer-tag">Case Study 4</span>
    </div>
    <h2 class="chapter-title">Hệ Thống Xe Tự Hành Nhà Xưởng (Automated Guided Vehicle - AGV)</h2>
    <div class="chapter-subtitle">Real-Time Concurrent Architecture, Sensors, Actuators & Motion Statechart</div>
  </div>

  <div class="topic-card">
    <div class="topic-title">🤖 Đặc Tính Kỹ Thuật Của Xe Tự Hành AGV</div>
    <p>
      Xe tự hành AGV di chuyển trên đường ray khép kín trong nhà máy thông minh theo chiều kim đồng hồ, dừng đón và trả hàng tại các trạm sản xuất:
    </p>
    <ul style="padding-left: 1.2rem;">
      <li>Nhận lệnh di chuyển (Move Commands) từ <strong>Hệ Thống Giám Sát Nhà Xưởng (Supervisory System)</strong>.</li>
      <li>Gửi phản hồi (Acks) khi bắt đầu chạy, khi đi ngang qua một trạm và khi dừng hẳn tại trạm đích.</li>
      <li>Gửi trạng thái hoạt động định kỳ mỗi <strong>30 giây</strong> về <strong>Hệ Thống Màn Hình Hiển Thị (Display System)</strong>.</li>
      <li><strong>Cảm biến đến (Arrival Sensor)</strong>: Thiết bị đầu vào kích hoạt theo ngắt sự kiện (Event-driven input device).</li>
      <li><strong>Động cơ kéo (Motor) &amp; Cánh tay cơ khí (Arm)</strong>: Các thiết bị chấp hành thụ động (Passive output devices).</li>
    </ul>
  </div>

  <div class="card-grid">
    <div class="card">
      <div class="card-title">🎯 Sensor Interface Task</div>
      <div class="card-content">
        <p>Tác vụ tương tranh hướng sự kiện (Event-driven task), đón nhận tín hiệu ngắt ngay khi xe chạm cảm biến dừng tại trạm và gửi thông điệp báo hiệu cho Tác vụ điều khiển.</p>
      </div>
    </div>

    <div class="card">
      <div class="card-title">⚙️ AGV Motion Control Task</div>
      <div class="card-content">
        <p>Tác vụ tương tranh lõi thực thi Máy trạng thái chuyển động của xe (Moving, Stopping, ArrivedAtStation), phối hợp điều khiển động cơ và cánh tay xếp dỡ hàng hóa.</p>
      </div>
    </div>

    <div class="card">
      <div class="card-title">📡 Supervisory Comm Task</div>
      <div class="card-content">
        <p>Quản trị kênh truyền thông bất đồng bộ hai chiều (Bidirectional asynchronous communication) với máy chủ điều hành nhà máy.</p>
      </div>
    </div>
  </div>
</section>

<!-- ========================================== -->
<!-- CASE STUDY TOÀN DIỆN: FRESHFOOD ONLINE SYSTEM (FOS) -->
<!-- ========================================== -->
<section id="case-study-fos" class="chapter-section">
  <div class="chapter-header">
    <div class="chapter-badge-row">
      <span class="chapter-badge">CASE STUDY ĐỒ ÁN TOÀN DIỆN</span>
      <span class="chapter-lecturer-tag">SWD392 RDS Document &bull; FreshFood Online System (FOS)</span>
    </div>
    <h2 class="chapter-title">Đặc Tả Yêu Cầu & Thiết Kế Hệ Thống FreshFood Online System (FOS)</h2>
    <div class="chapter-subtitle">3-Tier Web & Mobile, Microservices Architecture, Database ERD & Pattern Integration</div>
  </div>

  <div class="topic-card">
    <div class="topic-title">🥗 Giới Thiệu Dự Án Thực Tế FOS (FreshFood Online System)</div>
    <p>
      Hệ thống FOS là nền tảng thương mại điện tử chuyên cung cấp thực phẩm tươi sống sạch, kết nối trực tiếp Người tiêu dùng (Customers), 
      Nhà cung cấp nông trại (Suppliers/Sellers), Đội ngũ tài xế giao hàng (Delivery Drivers), và Bộ máy Quản trị viên (Admins/Moderators).
    </p>

    <div class="table-wrap">
      <table class="styled-table">
        <thead>
          <tr>
            <th>Phân Hệ / Module</th>
            <th>Trách Nhiệm Kiến Trúc</th>
            <th>Mẫu Thiết Kế (Design Patterns) Áp Dụng</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>User &amp; Auth Service</strong></td>
            <td>Quản lý tài khoản, đăng ký, đăng nhập bảo mật qua JWT (JSON Web Token) &amp; OAuth2 (Google/Facebook).</td>
            <td><strong>Singleton</strong> (Database Connection Pool) &amp; <strong>Proxy</strong> (API Security Filter).</td>
          </tr>
          <tr>
            <td><strong>Product Catalog &amp; Search</strong></td>
            <td>Quản lý hàng ngàn mặt hàng rau củ quả tươi sống, danh mục theo mùa, hỗ trợ tìm kiếm và lọc giá nhanh.</td>
            <td><strong>Composite Pattern</strong> (Cây danh mục danh mục cha &ndash; con) &amp; <strong>Iterator</strong>.</td>
          </tr>
          <tr>
            <td><strong>Order &amp; Cart Management</strong></td>
            <td>Quản lý giỏ hàng tạm, tính toán giá trị đơn, áp mã giảm giá và chuyển trạng thái đơn hàng.</td>
            <td><strong>State Pattern</strong> (Đơn hàng: <em>Pending &rarr; Confirmed &rarr; Packaging &rarr; Shipping &rarr; Delivered</em>).</td>
          </tr>
          <tr>
            <td><strong>Payment Gateway Service</strong></td>
            <td>Tích hợp đa dạng các cổng thanh toán số: Thẻ ngân hàng nội địa, Visa/MasterCard, Ví MoMo, VNPay, COD.</td>
            <td><strong>Factory Method</strong> &amp; <strong>Strategy Pattern</strong> (Đóng gói linh hoạt các thuật toán thanh toán).</td>
          </tr>
          <tr>
            <td><strong>Notification Service</strong></td>
            <td>Bắn thông báo đẩy thời gian thực (Push notification) về điện thoại và email khi đơn hàng thay đổi trạng thái.</td>
            <td><strong>Observer Pattern</strong> (Lắng nghe sự kiện OrderStatusChanged từ Message Queue).</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>

  <!-- SVG Diagram: FOS Architecture -->
  <div class="diagram-card">
    <div class="svg-container">
      <svg viewBox="0 0 880 280" xmlns="http://www.w3.org/2000/svg" style="font-family: 'Plus Jakarta Sans', sans-serif;">
        <rect width="880" height="280" rx="14" fill="#ffffff" stroke="#e2e8f0" stroke-width="2"/>
        <text x="440" y="28" text-anchor="middle" font-size="15" font-weight="800" fill="#0f172a">KIẾN TRÚC TỔNG THỂ HỆ THỐNG FRESHFOOD ONLINE SYSTEM (FOS RDS ARCHITECTURE)</text>
        
        <!-- Clients -->
        <rect x="30" y="60" width="160" height="50" rx="8" fill="#e0f2fe" stroke="#0284c7" stroke-width="1.8"/>
        <text x="110" y="85" text-anchor="middle" font-size="12" font-weight="700" fill="#0369a1">Web Client</text>
        <text x="110" y="100" text-anchor="middle" font-size="10" fill="#475569">React.js / Next.js</text>

        <rect x="30" y="130" width="160" height="50" rx="8" fill="#e0f2fe" stroke="#0284c7" stroke-width="1.8"/>
        <text x="110" y="155" text-anchor="middle" font-size="12" font-weight="700" fill="#0369a1">Mobile App</text>
        <text x="110" y="170" text-anchor="middle" font-size="10" fill="#475569">Flutter / React Native</text>

        <!-- API Gateway -->
        <rect x="250" y="60" width="140" height="150" rx="10" fill="#fef3c7" stroke="#d97706" stroke-width="2"/>
        <text x="320" y="95" text-anchor="middle" font-size="13" font-weight="800" fill="#b45309">API GATEWAY</text>
        <text x="320" y="120" text-anchor="middle" font-size="10.5" fill="#475569">- JWT Auth Filter</text>
        <text x="320" y="140" text-anchor="middle" font-size="10.5" fill="#475569">- Rate Limiter</text>
        <text x="320" y="160" text-anchor="middle" font-size="10.5" fill="#475569">- SSL Termination</text>
        <text x="320" y="180" text-anchor="middle" font-size="10.5" fill="#475569">- Reverse Proxy</text>

        <!-- Connectors Client -> Gateway -->
        <line x1="190" y1="85" x2="250" y2="110" stroke="#0284c7" stroke-width="2"/>
        <line x1="190" y1="155" x2="250" y2="140" stroke="#0284c7" stroke-width="2"/>

        <!-- Microservices Grid -->
        <rect x="450" y="55" width="170" height="42" rx="6" fill="#eef2ff" stroke="#4f46e5" stroke-width="1.5"/>
        <text x="535" y="80" text-anchor="middle" font-size="11.5" font-weight="700" fill="#4338ca">User &amp; Auth Service</text>

        <rect x="450" y="105" width="170" height="42" rx="6" fill="#eef2ff" stroke="#4f46e5" stroke-width="1.5"/>
        <text x="535" y="130" text-anchor="middle" font-size="11.5" font-weight="700" fill="#4338ca">Product Catalog Svc</text>

        <rect x="450" y="155" width="170" height="42" rx="6" fill="#eef2ff" stroke="#4f46e5" stroke-width="1.5"/>
        <text x="535" y="180" text-anchor="middle" font-size="11.5" font-weight="700" fill="#4338ca">Order &amp; Cart Svc</text>

        <rect x="450" y="205" width="170" height="42" rx="6" fill="#eef2ff" stroke="#4f46e5" stroke-width="1.5"/>
        <text x="535" y="230" text-anchor="middle" font-size="11.5" font-weight="700" fill="#4338ca">Payment Gateway Svc</text>

        <!-- Gateway -> Services -->
        <line x1="390" y1="110" x2="450" y2="75" stroke="#d97706" stroke-width="1.5"/>
        <line x1="390" y1="125" x2="450" y2="125" stroke="#d97706" stroke-width="1.5"/>
        <line x1="390" y1="145" x2="450" y2="175" stroke="#d97706" stroke-width="1.5"/>
        <line x1="390" y1="165" x2="450" y2="225" stroke="#d97706" stroke-width="1.5"/>

        <!-- Message Broker / Databases -->
        <rect x="680" y="60" width="170" height="75" rx="8" fill="#d1fae5" stroke="#059669" stroke-width="2"/>
        <text x="765" y="90" text-anchor="middle" font-size="12" font-weight="800" fill="#047857">PostgreSQL Database</text>
        <text x="765" y="110" text-anchor="middle" font-size="10" fill="#475569">Relational ACID Stores</text>

        <rect x="680" y="150" width="170" height="75" rx="8" fill="#ede9fe" stroke="#7c3aed" stroke-width="2"/>
        <text x="765" y="180" text-anchor="middle" font-size="12" font-weight="800" fill="#6d28d9">Kafka / RabbitMQ</text>
        <text x="765" y="200" text-anchor="middle" font-size="10" fill="#475569">Async Event Streaming</text>

        <line x1="620" y1="100" x2="680" y2="100" stroke="#059669" stroke-width="1.5"/>
        <line x1="620" y1="180" x2="680" y2="180" stroke="#7c3aed" stroke-width="1.5"/>
      </svg>
    </div>
    <div class="diagram-caption">Sơ đồ 25.1: Sơ đồ kiến trúc giải pháp toàn diện cho đề án FreshFood Online System (FOS)</div>
  </div>
</section>
"""

