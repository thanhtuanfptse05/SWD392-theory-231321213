# _generator/part5.py
# Part 5: 23 Mẫu Thiết Kế GoF & Trí Tuệ Nhân Tạo Tạo Sinh (GenAI) - Redesigned with Syntax Highlighting & Accordion

def get_part5_html():
    return r"""
<!-- ========================================== -->
<!-- PART 5 DIVIDER BANNER -->
<!-- ========================================== -->
<div id="part-5" class="part-divider-banner part-5-banner">
  <span class="part-badge-tag">Phần 5 &bull; Design Patterns &amp; GenAI</span>
  <h2 class="part-title">23 Mẫu Thiết Kế GoF &amp; Ứng Dụng GenAI Trong Kiến Trúc</h2>
  <p class="part-desc">
    Bộ bách khoa toàn thư đầy đủ 100% về 23 mẫu thiết kế kinh điển của Gang of Four (Creational, Structural, Behavioral) với Intent, cấu trúc UML, thành phần Participants, ưu nhược điểm và mã nguồn minh họa chuẩn; kết hợp chuyên đề ứng dụng GenAI (ChatGPT, GitHub Copilot, PlantUML) trong thiết kế kiến trúc phần mềm hiện đại.
  </p>
</div>

<!-- ========================================== -->
<!-- CHUYÊN ĐỀ 1: 23 GOF DESIGN PATTERNS -->
<!-- ========================================== -->
<section id="gof-patterns" class="chapter-section">
  <div class="chapter-header">
    <div class="chapter-badge-row">
      <span class="chapter-badge">CHUYÊN ĐỀ GOF</span>
      <span class="chapter-lecturer-tag">Gang of Four &bull; 23 Reusable Design Patterns</span>
    </div>
    <h2 class="chapter-title">Toàn Bộ 23 Mẫu Thiết Kế Gang of Four (GoF Design Patterns)</h2>
    <div class="chapter-subtitle">Mục Đích, Cấu Trúc, Thành Phần, Ưu Nhược Điểm &amp; Mã Nguồn Mẫu Đã Định Dạng Cú Pháp</div>
  </div>

  <p>
    <strong>Design Pattern (Mẫu thiết kế)</strong> là giải pháp mẫu mực, đã được kiểm nghiệm thực tế qua hàng thập kỷ cho các bài toán thiết kế hướng đối tượng lặp đi lặp lại.
    Mẫu thiết kế giúp mã nguồn đạt tính <em>linh hoạt (Flexibility)</em>, <em>dễ tái sử dụng (Reusability)</em> và <em>giảm thiểu độ phụ thuộc (Decoupling)</em>.
  </p>

  <!-- ================= CREATIONAL ================= -->
  <h3 style="color: #0284c7; margin: 2.25rem 0 1rem; border-bottom: 2px solid #bae6fd; padding-bottom: 0.5rem; display: flex; align-items: center; gap: 0.5rem;">
    <span>🏭</span> Nhóm 1: Creational Patterns (Mẫu Khởi Tạo &bull; 5 Mẫu)
  </h3>
  <p style="color: var(--text-muted); margin-bottom: 1.5rem; font-size: 0.92rem;">Tập trung vào cơ chế tạo lập đối tượng một cách linh hoạt, tách rời phía Client khỏi logic khởi tạo trực tiếp qua từ khóa <code>new</code>.</p>

  <div class="card-grid">
    <!-- 1. Singleton -->
    <div class="card">
      <div class="card-title">1. Singleton Pattern</div>
      <div class="card-content">
        <span class="pattern-cat-tag cat-creational">Creational</span>
        <div class="concept-box" style="border-left-color: #0284c7; margin: 0.6rem 0;">
          <div class="concept-title" style="color: #0284c7;">🎯 Ý Định (Intent)</div>
          <p style="font-size: 0.88rem;">Đảm bảo một lớp chỉ có <em>duy nhất một thể hiện (Instance)</em> trong suốt vòng đời ứng dụng và cung cấp một điểm truy cập toàn cục tới thể hiện đó.</p>
        </div>
        <p style="font-size: 0.85rem; margin-bottom: 0.4rem;"><strong>👥 Participants:</strong> <code>SingletonClass</code>.</p>
        <p style="font-size: 0.85rem; margin-bottom: 0.6rem;"><strong>💡 Use Cases:</strong> Database Connection Pool, Logger, Configuration Manager, Thread Pool.</p>

        <details class="code-accordion">
          <summary><span>💻 Xem mã nguồn Java minh họa</span> <span class="toggle-icon">▼</span></summary>
          <div class="code-block">
            <div class="code-header">
              <div class="code-header-left">
                <div class="code-dots"><span class="code-dot dot-red"></span><span class="code-dot dot-yellow"></span><span class="code-dot dot-green"></span></div>
                <span class="code-lang-tag">Java &bull; Thread-Safe Singleton</span>
              </div>
              <button class="code-copy-btn" onclick="copyCode(this)">📋 Sao chép</button>
            </div>
            <pre class="code-body"><code><span class="kwd">public class</span> <span class="typ">DatabaseConnection</span> {
    <span class="kwd">private static volatile</span> <span class="typ">DatabaseConnection</span> instance;

    <span class="com">// Private constructor ngăn chặn tạo instance từ bên ngoài</span>
    <span class="kwd">private</span> <span class="fn">DatabaseConnection</span>() { }

    <span class="com">// Double-Checked Locking đảm bảo thread-safe hiệu năng cao</span>
    <span class="kwd">public static</span> <span class="typ">DatabaseConnection</span> <span class="fn">getInstance</span>() {
        <span class="kwd">if</span> (instance == <span class="kwd">null</span>) {
            <span class="kwd">synchronized</span> (<span class="typ">DatabaseConnection</span>.<span class="kwd">class</span>) {
                <span class="kwd">if</span> (instance == <span class="kwd">null</span>) {
                    instance = <span class="kwd">new</span> <span class="typ">DatabaseConnection</span>();
                }
            }
        }
        <span class="kwd">return</span> instance;
    }
}</code></pre>
          </div>
        </details>
      </div>
    </div>

    <!-- 2. Factory Method -->
    <div class="card">
      <div class="card-title">2. Factory Method Pattern</div>
      <div class="card-content">
        <span class="pattern-cat-tag cat-creational">Creational</span>
        <div class="concept-box" style="border-left-color: #0284c7; margin: 0.6rem 0;">
          <div class="concept-title" style="color: #0284c7;">🎯 Ý Định (Intent)</div>
          <p style="font-size: 0.88rem;">Định nghĩa một giao diện để tạo lập đối tượng, nhưng để các <em>lớp con (Subclasses) quyết định lớp cụ thể nào sẽ được khởi tạo</em>.</p>
        </div>
        <p style="font-size: 0.85rem; margin-bottom: 0.4rem;"><strong>👥 Participants:</strong> <code>Product</code>, <code>ConcreteProduct</code>, <code>Creator</code>, <code>ConcreteCreator</code>.</p>
        <p style="font-size: 0.85rem; margin-bottom: 0.6rem;"><strong>💡 Use Cases:</strong> Hệ thống vẽ Dialog đa nền tảng (WindowsDialog, MacDialog, HTMLDialog).</p>

        <details class="code-accordion">
          <summary><span>💻 Xem mã nguồn Java minh họa</span> <span class="toggle-icon">▼</span></summary>
          <div class="code-block">
            <div class="code-header">
              <div class="code-header-left">
                <div class="code-dots"><span class="code-dot dot-red"></span><span class="code-dot dot-yellow"></span><span class="code-dot dot-green"></span></div>
                <span class="code-lang-tag">Java &bull; Factory Method</span>
              </div>
              <button class="code-copy-btn" onclick="copyCode(this)">📋 Sao chép</button>
            </div>
            <pre class="code-body"><code><span class="kwd">public abstract class</span> <span class="typ">Dialog</span> {
    <span class="kwd">public void</span> <span class="fn">render</span>() {
        <span class="typ">Button</span> okBtn = <span class="fn">createButton</span>();
        okBtn.<span class="fn">onClick</span>();
    }
    <span class="com">// Factory Method được giao cho lớp con hiện thực</span>
    <span class="kwd">public abstract</span> <span class="typ">Button</span> <span class="fn">createButton</span>();
}

<span class="kwd">public class</span> <span class="typ">WindowsDialog</span> <span class="kwd">extends</span> <span class="typ">Dialog</span> {
    <span class="ann">@Override</span>
    <span class="kwd">public</span> <span class="typ">Button</span> <span class="fn">createButton</span>() {
        <span class="kwd">return new</span> <span class="typ">WindowsButton</span>();
    }
}</code></pre>
          </div>
        </details>
      </div>
    </div>

    <!-- 3. Abstract Factory -->
    <div class="card">
      <div class="card-title">3. Abstract Factory Pattern</div>
      <div class="card-content">
        <span class="pattern-cat-tag cat-creational">Creational</span>
        <div class="concept-box" style="border-left-color: #0284c7; margin: 0.6rem 0;">
          <div class="concept-title" style="color: #0284c7;">🎯 Ý Định (Intent)</div>
          <p style="font-size: 0.88rem;">Cung cấp giao diện tạo lập một <em>họ các đối tượng có liên quan hoặc phụ thuộc lẫn nhau</em> mà không cần chỉ định rõ các lớp cụ thể của chúng.</p>
        </div>
        <p style="font-size: 0.85rem; margin-bottom: 0.4rem;"><strong>👥 Participants:</strong> <code>AbstractFactory</code>, <code>ConcreteFactory</code>, <code>AbstractProduct</code>, <code>ConcreteProduct</code>.</p>
        <p style="font-size: 0.85rem; margin-bottom: 0.6rem;"><strong>💡 Use Cases:</strong> Bộ UI Toolkit (Button + Checkbox) cho Windows, Mac, Linux đồng nhất giao diện.</p>

        <details class="code-accordion">
          <summary><span>💻 Xem mã nguồn Java minh họa</span> <span class="toggle-icon">▼</span></summary>
          <div class="code-block">
            <div class="code-header">
              <div class="code-header-left">
                <div class="code-dots"><span class="code-dot dot-red"></span><span class="code-dot dot-yellow"></span><span class="code-dot dot-green"></span></div>
                <span class="code-lang-tag">Java &bull; Abstract Factory</span>
              </div>
              <button class="code-copy-btn" onclick="copyCode(this)">📋 Sao chép</button>
            </div>
            <pre class="code-body"><code><span class="kwd">public interface</span> <span class="typ">GUIFactory</span> {
    <span class="typ">Button</span> <span class="fn">createButton</span>();
    <span class="typ">Checkbox</span> <span class="fn">createCheckbox</span>();
}

<span class="kwd">public class</span> <span class="typ">WinFactory</span> <span class="kwd">implements</span> <span class="typ">GUIFactory</span> {
    <span class="kwd">public</span> <span class="typ">Button</span> <span class="fn">createButton</span>() { <span class="kwd">return new</span> <span class="typ">WinButton</span>(); }
    <span class="kwd">public</span> <span class="typ">Checkbox</span> <span class="fn">createCheckbox</span>() { <span class="kwd">return new</span> <span class="typ">WinCheckbox</span>(); }
}</code></pre>
          </div>
        </details>
      </div>
    </div>

    <!-- 4. Builder -->
    <div class="card">
      <div class="card-title">4. Builder Pattern</div>
      <div class="card-content">
        <span class="pattern-cat-tag cat-creational">Creational</span>
        <div class="concept-box" style="border-left-color: #0284c7; margin: 0.6rem 0;">
          <div class="concept-title" style="color: #0284c7;">🎯 Ý Định (Intent)</div>
          <p style="font-size: 0.88rem;">Tách rời quá trình <em>xây dựng một đối tượng phức tạp</em> khỏi biểu diễn của nó, cho phép cùng một quy trình có thể tạo ra các biến thể khác nhau.</p>
        </div>
        <p style="font-size: 0.85rem; margin-bottom: 0.4rem;"><strong>👥 Participants:</strong> <code>Builder</code>, <code>ConcreteBuilder</code>, <code>Director</code>, <code>Product</code>.</p>
        <p style="font-size: 0.85rem; margin-bottom: 0.6rem;"><strong>💡 Use Cases:</strong> Khởi tạo Order phức tạp có nhiều options, SQL Query Builder, Meal Builder.</p>

        <details class="code-accordion">
          <summary><span>💻 Xem mã nguồn Java minh họa</span> <span class="toggle-icon">▼</span></summary>
          <div class="code-block">
            <div class="code-header">
              <div class="code-header-left">
                <div class="code-dots"><span class="code-dot dot-red"></span><span class="code-dot dot-yellow"></span><span class="code-dot dot-green"></span></div>
                <span class="code-lang-tag">Java &bull; Builder Pattern</span>
              </div>
              <button class="code-copy-btn" onclick="copyCode(this)">📋 Sao chép</button>
            </div>
            <pre class="code-body"><code><span class="kwd">public class</span> <span class="typ">Order</span> {
    <span class="kwd">private</span> <span class="typ">String</span> id, payment, shipping;
    <span class="kwd">public static class</span> <span class="typ">Builder</span> {
        <span class="kwd">private</span> <span class="typ">Order</span> order = <span class="kwd">new</span> <span class="typ">Order</span>();
        <span class="kwd">public</span> <span class="typ">Builder</span> <span class="fn">setId</span>(<span class="typ">String</span> id) { order.id = id; <span class="kwd">return this</span>; }
        <span class="kwd">public</span> <span class="typ">Builder</span> <span class="fn">setPayment</span>(<span class="typ">String</span> p) { order.payment = p; <span class="kwd">return this</span>; }
        <span class="kwd">public</span> <span class="typ">Order</span> <span class="fn">build</span>() { <span class="kwd">return</span> order; }
    }
}
<span class="com">// Sử dụng Method Chaining:</span>
<span class="typ">Order</span> o = <span class="kwd">new</span> <span class="typ">Order</span>.<span class="typ">Builder</span>().<span class="fn">setId</span>(<span class="str">"ORD-1"</span>).<span class="fn">setPayment</span>(<span class="str">"MOMO"</span>).<span class="fn">build</span>();</code></pre>
          </div>
        </details>
      </div>
    </div>

    <!-- 5. Prototype -->
    <div class="card">
      <div class="card-title">5. Prototype Pattern</div>
      <div class="card-content">
        <span class="pattern-cat-tag cat-creational">Creational</span>
        <div class="concept-box" style="border-left-color: #0284c7; margin: 0.6rem 0;">
          <div class="concept-title" style="color: #0284c7;">🎯 Ý Định (Intent)</div>
          <p style="font-size: 0.88rem;">Chỉ định các loại đối tượng sẽ tạo bằng cách sử dụng một thể hiện mẫu (Prototype), và tạo đối tượng mới bằng cách <em>sao chép (Clone) thể hiện mẫu này</em>.</p>
        </div>
        <p style="font-size: 0.85rem; margin-bottom: 0.4rem;"><strong>👥 Participants:</strong> <code>Prototype</code>, <code>ConcretePrototype</code>, <code>Client</code>.</p>
        <p style="font-size: 0.85rem; margin-bottom: 0.6rem;"><strong>💡 Use Cases:</strong> Sinh hàng loạt quái vật trong game có chỉ số tương đồng, Clone đối tượng cấu hình nặng.</p>

        <details class="code-accordion">
          <summary><span>💻 Xem mã nguồn Java minh họa</span> <span class="toggle-icon">▼</span></summary>
          <div class="code-block">
            <div class="code-header">
              <div class="code-header-left">
                <div class="code-dots"><span class="code-dot dot-red"></span><span class="code-dot dot-yellow"></span><span class="code-dot dot-green"></span></div>
                <span class="code-lang-tag">Java &bull; Prototype Pattern</span>
              </div>
              <button class="code-copy-btn" onclick="copyCode(this)">📋 Sao chép</button>
            </div>
            <pre class="code-body"><code><span class="kwd">public interface</span> <span class="typ">Prototype</span> {
    <span class="typ">Prototype</span> <span class="fn">clone</span>();
}
<span class="kwd">public class</span> <span class="typ">Monster</span> <span class="kwd">implements</span> <span class="typ">Prototype</span> {
    <span class="kwd">private int</span> hp;
    <span class="kwd">public</span> <span class="fn">Monster</span>(<span class="kwd">int</span> hp) { <span class="kwd">this</span>.hp = hp; }
    <span class="ann">@Override</span>
    <span class="kwd">public</span> <span class="typ">Monster</span> <span class="fn">clone</span>() { <span class="kwd">return new</span> <span class="typ">Monster</span>(<span class="kwd">this</span>.hp); }
}</code></pre>
          </div>
        </details>
      </div>
    </div>
  </div>

  <!-- ================= STRUCTURAL ================= -->
  <h3 style="color: #4f46e5; margin: 3rem 0 1rem; border-bottom: 2px solid #c7d2fe; padding-bottom: 0.5rem; display: flex; align-items: center; gap: 0.5rem;">
    <span>🧱</span> Nhóm 2: Structural Patterns (Mẫu Cấu Trúc &bull; 7 Mẫu)
  </h3>
  <p style="color: var(--text-muted); margin-bottom: 1.5rem; font-size: 0.92rem;">Tập trung vào cách thức lắp ghép các lớp và đối tượng thành các cấu trúc lớn hơn, linh hoạt và độc lập hơn.</p>

  <div class="card-grid">
    <!-- 6. Adapter -->
    <div class="card">
      <div class="card-title">6. Adapter Pattern (Wrapper)</div>
      <div class="card-content">
        <span class="pattern-cat-tag cat-structural">Structural</span>
        <div class="concept-box" style="border-left-color: #4f46e5; margin: 0.6rem 0;">
          <div class="concept-title" style="color: #4f46e5;">🎯 Ý Định (Intent)</div>
          <p style="font-size: 0.88rem;">Chuyển đổi giao diện (Interface) của một lớp thành một giao diện khác mà Client mong đợi. Giúp các lớp không tương thích giao diện có thể làm việc được với nhau.</p>
        </div>
        <p style="font-size: 0.85rem; margin-bottom: 0.4rem;"><strong>👥 Participants:</strong> <code>Target</code>, <code>Adapter</code>, <code>Adaptee</code>, <code>Client</code>.</p>
        <p style="font-size: 0.85rem; margin-bottom: 0.6rem;"><strong>💡 Use Cases:</strong> Tích hợp thư viện thanh toán bên thứ ba (VNPay, ZaloPay), Legacy System Wrappers.</p>

        <details class="code-accordion">
          <summary><span>💻 Xem mã nguồn Java minh họa</span> <span class="toggle-icon">▼</span></summary>
          <div class="code-block">
            <div class="code-header">
              <div class="code-header-left">
                <div class="code-dots"><span class="code-dot dot-red"></span><span class="code-dot dot-yellow"></span><span class="code-dot dot-green"></span></div>
                <span class="code-lang-tag">Java &bull; Object Adapter</span>
              </div>
              <button class="code-copy-btn" onclick="copyCode(this)">📋 Sao chép</button>
            </div>
            <pre class="code-body"><code><span class="kwd">public interface</span> <span class="typ">PaymentProcessor</span> { <span class="kwd">void</span> <span class="fn">pay</span>(<span class="kwd">int</span> amount); }
<span class="kwd">public class</span> <span class="typ">VNPayLib</span> { <span class="kwd">public void</span> <span class="fn">chargeCustomer</span>(<span class="kwd">int</span> vnd) { } }

<span class="kwd">public class</span> <span class="typ">VNPayAdapter</span> <span class="kwd">implements</span> <span class="typ">PaymentProcessor</span> {
    <span class="kwd">private</span> <span class="typ">VNPayLib</span> vnPay = <span class="kwd">new</span> <span class="typ">VNPayLib</span>();
    <span class="ann">@Override</span>
    <span class="kwd">public void</span> <span class="fn">pay</span>(<span class="kwd">int</span> amount) {
        vnPay.<span class="fn">chargeCustomer</span>(amount);
    }
}</code></pre>
          </div>
        </details>
      </div>
    </div>

    <!-- 7. Bridge -->
    <div class="card">
      <div class="card-title">7. Bridge Pattern</div>
      <div class="card-content">
        <span class="pattern-cat-tag cat-structural">Structural</span>
        <div class="concept-box" style="border-left-color: #4f46e5; margin: 0.6rem 0;">
          <div class="concept-title" style="color: #4f46e5;">🎯 Ý Định (Intent)</div>
          <p style="font-size: 0.88rem;">Tách biệt phần <em>trừu tượng (Abstraction)</em> khỏi phần <em>hiện thực (Implementation)</em> của nó để cả hai có thể biến đổi độc lập với nhau.</p>
        </div>
        <p style="font-size: 0.85rem; margin-bottom: 0.4rem;"><strong>👥 Participants:</strong> <code>Abstraction</code>, <code>RefinedAbstraction</code>, <code>Implementor</code>, <code>ConcreteImplementor</code>.</p>
        <p style="font-size: 0.85rem; margin-bottom: 0.6rem;"><strong>💡 Use Cases:</strong> Phân lớp Hình học Shape kết nối với công cụ kết xuất đồ họa đa nền tảng DrawingAPI.</p>

        <details class="code-accordion">
          <summary><span>💻 Xem mã nguồn Java minh họa</span> <span class="toggle-icon">▼</span></summary>
          <div class="code-block">
            <div class="code-header">
              <div class="code-header-left">
                <div class="code-dots"><span class="code-dot dot-red"></span><span class="code-dot dot-yellow"></span><span class="code-dot dot-green"></span></div>
                <span class="code-lang-tag">Java &bull; Bridge Pattern</span>
              </div>
              <button class="code-copy-btn" onclick="copyCode(this)">📋 Sao chép</button>
            </div>
            <pre class="code-body"><code><span class="kwd">public interface</span> <span class="typ">DrawingAPI</span> { <span class="kwd">void</span> <span class="fn">drawCircle</span>(<span class="kwd">double</span> r); }
<span class="kwd">public abstract class</span> <span class="typ">Shape</span> {
    <span class="kwd">protected</span> <span class="typ">DrawingAPI</span> api; <span class="com">// Cầu nối Bridge</span>
    <span class="kwd">public</span> <span class="fn">Shape</span>(<span class="typ">DrawingAPI</span> api) { <span class="kwd">this</span>.api = api; }
    <span class="kwd">public abstract void</span> <span class="fn">draw</span>();
}</code></pre>
          </div>
        </details>
      </div>
    </div>

    <!-- 8. Composite -->
    <div class="card">
      <div class="card-title">8. Composite Pattern</div>
      <div class="card-content">
        <span class="pattern-cat-tag cat-structural">Structural</span>
        <div class="concept-box" style="border-left-color: #4f46e5; margin: 0.6rem 0;">
          <div class="concept-title" style="color: #4f46e5;">🎯 Ý Định (Intent)</div>
          <p style="font-size: 0.88rem;">Xây dựng các đối tượng theo <em>cấu trúc hình cây (Tree Structures)</em> để biểu diễn các cấp bậc Toàn thể &ndash; Bộ phận. Giúp Client xử lý đối tượng đơn lẻ và tập hợp đối tượng hoàn toàn đồng nhất.</p>
        </div>
        <p style="font-size: 0.85rem; margin-bottom: 0.4rem;"><strong>👥 Participants:</strong> <code>Component</code>, <code>Leaf</code>, <code>Composite</code>, <code>Client</code>.</p>
        <p style="font-size: 0.85rem; margin-bottom: 0.6rem;"><strong>💡 Use Cases:</strong> Cây thư mục hệ thống File/Folder, Cây danh mục phân cấp đa cấp trong FOS Catalog.</p>

        <details class="code-accordion">
          <summary><span>💻 Xem mã nguồn Java minh họa</span> <span class="toggle-icon">▼</span></summary>
          <div class="code-block">
            <div class="code-header">
              <div class="code-header-left">
                <div class="code-dots"><span class="code-dot dot-red"></span><span class="code-dot dot-yellow"></span><span class="code-dot dot-green"></span></div>
                <span class="code-lang-tag">Java &bull; Composite Pattern</span>
              </div>
              <button class="code-copy-btn" onclick="copyCode(this)">📋 Sao chép</button>
            </div>
            <pre class="code-body"><code><span class="kwd">public interface</span> <span class="typ">FileSystemNode</span> { <span class="kwd">int</span> <span class="fn">getSize</span>(); }
<span class="kwd">public class</span> <span class="typ">File</span> <span class="kwd">implements</span> <span class="typ">FileSystemNode</span> {
    <span class="kwd">private int</span> size;
    <span class="kwd">public int</span> <span class="fn">getSize</span>() { <span class="kwd">return</span> size; }
}
<span class="kwd">public class</span> <span class="typ">Folder</span> <span class="kwd">implements</span> <span class="typ">FileSystemNode</span> {
    <span class="kwd">private</span> <span class="typ">List</span>&lt;<span class="typ">FileSystemNode</span>&gt; children = <span class="kwd">new</span> <span class="typ">ArrayList</span>&lt;&gt;();
    <span class="kwd">public int</span> <span class="fn">getSize</span>() {
        <span class="kwd">return</span> children.<span class="fn">stream</span>().<span class="fn">mapToInt</span>(<span class="typ">FileSystemNode</span>::getSize).<span class="fn">sum</span>();
    }
}</code></pre>
          </div>
        </details>
      </div>
    </div>

    <!-- 9. Decorator -->
    <div class="card">
      <div class="card-title">9. Decorator Pattern (Wrapper)</div>
      <div class="card-content">
        <span class="pattern-cat-tag cat-structural">Structural</span>
        <div class="concept-box" style="border-left-color: #4f46e5; margin: 0.6rem 0;">
          <div class="concept-title" style="color: #4f46e5;">🎯 Ý Định (Intent)</div>
          <p style="font-size: 0.88rem;">Gắn thêm các trách nhiệm hoặc hành vi bổ sung cho một đối tượng một cách <em>động tại thời điểm chạy</em> mà không cần tạo lớp con kế thừa cứng nhắc.</p>
        </div>
        <p style="font-size: 0.85rem; margin-bottom: 0.4rem;"><strong>👥 Participants:</strong> <code>Component</code>, <code>ConcreteComponent</code>, <code>Decorator</code>, <code>ConcreteDecorator</code>.</p>
        <p style="font-size: 0.85rem; margin-bottom: 0.6rem;"><strong>💡 Use Cases:</strong> Thư viện Java I/O (<code>BufferedReader</code> bọc <code>FileReader</code>), Tính tiền đồ uống thêm Topping.</p>

        <details class="code-accordion">
          <summary><span>💻 Xem mã nguồn Java minh họa</span> <span class="toggle-icon">▼</span></summary>
          <div class="code-block">
            <div class="code-header">
              <div class="code-header-left">
                <div class="code-dots"><span class="code-dot dot-red"></span><span class="code-dot dot-yellow"></span><span class="code-dot dot-green"></span></div>
                <span class="code-lang-tag">Java &bull; Decorator Pattern</span>
              </div>
              <button class="code-copy-btn" onclick="copyCode(this)">📋 Sao chép</button>
            </div>
            <pre class="code-body"><code><span class="kwd">public interface</span> <span class="typ">Beverage</span> { <span class="kwd">double</span> <span class="fn">cost</span>(); }
<span class="kwd">public class</span> <span class="typ">Coffee</span> <span class="kwd">implements</span> <span class="typ">Beverage</span> { <span class="kwd">public double</span> <span class="fn">cost</span>() { <span class="kwd">return</span> <span class="num">20.0</span>; } }
<span class="kwd">public abstract class</span> <span class="typ">ToppingDecorator</span> <span class="kwd">implements</span> <span class="typ">Beverage</span> {
    <span class="kwd">protected</span> <span class="typ">Beverage</span> wrapped;
    <span class="kwd">public</span> <span class="fn">ToppingDecorator</span>(<span class="typ">Beverage</span> b) { <span class="kwd">this</span>.wrapped = b; }
}
<span class="kwd">public class</span> <span class="typ">Milk</span> <span class="kwd">extends</span> <span class="typ">ToppingDecorator</span> {
    <span class="kwd">public</span> <span class="fn">Milk</span>(<span class="typ">Beverage</span> b) { <span class="kwd">super</span>(b); }
    <span class="kwd">public double</span> <span class="fn">cost</span>() { <span class="kwd">return</span> wrapped.<span class="fn">cost</span>() + <span class="num">5.0</span>; }
}</code></pre>
          </div>
        </details>
      </div>
    </div>

    <!-- 10. Facade -->
    <div class="card">
      <div class="card-title">10. Facade Pattern</div>
      <div class="card-content">
        <span class="pattern-cat-tag cat-structural">Structural</span>
        <div class="concept-box" style="border-left-color: #4f46e5; margin: 0.6rem 0;">
          <div class="concept-title" style="color: #4f46e5;">🎯 Ý Định (Intent)</div>
          <p style="font-size: 0.88rem;">Cung cấp một giao diện cấp cao đồng nhất, đơn giản hóa để truy cập vào một tập hợp phức tạp gồm nhiều giao diện bên trong một hệ thống con (Subsystem).</p>
        </div>
        <p style="font-size: 0.85rem; margin-bottom: 0.4rem;"><strong>👥 Participants:</strong> <code>Facade</code>, <code>Subsystem Classes</code>, <code>Client</code>.</p>
        <p style="font-size: 0.85rem; margin-bottom: 0.6rem;"><strong>💡 Use Cases:</strong> Nút "Xem Phim" trên rạp hát tại gia, API Gateway gom nhiều microservices thành 1 endpoint.</p>
      </div>
    </div>

    <!-- 11. Flyweight -->
    <div class="card">
      <div class="card-title">11. Flyweight Pattern</div>
      <div class="card-content">
        <span class="pattern-cat-tag cat-structural">Structural</span>
        <div class="concept-box" style="border-left-color: #4f46e5; margin: 0.6rem 0;">
          <div class="concept-title" style="color: #4f46e5;">🎯 Ý Định (Intent)</div>
          <p style="font-size: 0.88rem;">Sử dụng kỹ thuật chia sẻ để hỗ trợ hiệu quả một số lượng cực lớn các đối tượng hạt mịn (Fine-grained objects), tiết kiệm bộ nhớ RAM.</p>
        </div>
        <p style="font-size: 0.85rem; margin-bottom: 0.4rem;"><strong>👥 Participants:</strong> <code>Flyweight</code>, <code>ConcreteFlyweight</code>, <code>FlyweightFactory</code>, <code>Client</code>.</p>
        <p style="font-size: 0.85rem; margin-bottom: 0.6rem;"><strong>💡 Use Cases:</strong> Trình soạn thảo văn bản lưu triệu ký tự font chữ, Rừng cây trong game 3D.</p>
      </div>
    </div>

    <!-- 12. Proxy -->
    <div class="card">
      <div class="card-title">12. Proxy Pattern</div>
      <div class="card-content">
        <span class="pattern-cat-tag cat-structural">Structural</span>
        <div class="concept-box" style="border-left-color: #4f46e5; margin: 0.6rem 0;">
          <div class="concept-title" style="color: #4f46e5;">🎯 Ý Định (Intent)</div>
          <p style="font-size: 0.88rem;">Cung cấp một đối tượng đại diện hoặc giữ chỗ (Surrogate/Placeholder) cho một đối tượng khác để <em>kiểm soát việc truy cập vào đối tượng đó</em>.</p>
        </div>
        <p style="font-size: 0.85rem; margin-bottom: 0.4rem;"><strong>👥 Participants:</strong> <code>Subject</code>, <code>RealSubject</code>, <code>Proxy</code>, <code>Client</code>.</p>
        <p style="font-size: 0.85rem; margin-bottom: 0.6rem;"><strong>💡 Use Cases:</strong> Remote Proxy (RMI/gRPC), Virtual Proxy (Lazy Loading ảnh), Protection Proxy (Check quyền).</p>
      </div>
    </div>
  </div>

  <!-- ================= BEHAVIORAL ================= -->
  <h3 style="color: #d97706; margin: 3rem 0 1rem; border-bottom: 2px solid #fde68a; padding-bottom: 0.5rem; display: flex; align-items: center; gap: 0.5rem;">
    <span>🧠</span> Nhóm 3: Behavioral Patterns (Mẫu Hành Vi &bull; 11 Mẫu)
  </h3>
  <p style="color: var(--text-muted); margin-bottom: 1.5rem; font-size: 0.92rem;">Tập trung vào các thuật toán, phân công trách nhiệm và cơ chế giao tiếp linh hoạt giữa các đối tượng.</p>

  <div class="card-grid">
    <!-- 13. Chain of Responsibility -->
    <div class="card">
      <div class="card-title">13. Chain of Responsibility</div>
      <div class="card-content">
        <span class="pattern-cat-tag cat-behavioral">Behavioral</span>
        <div class="concept-box" style="border-left-color: #d97706; margin: 0.6rem 0;">
          <div class="concept-title" style="color: #d97706;">🎯 Ý Định (Intent)</div>
          <p style="font-size: 0.88rem;">Tránh ghép nối chặt giữa bên gửi và bên nhận bằng cách nối các đối tượng nhận thành một chuỗi (Chain) và chuyển yêu cầu dọc theo chuỗi.</p>
        </div>
        <p style="font-size: 0.85rem; margin-bottom: 0.4rem;"><strong>👥 Participants:</strong> <code>Handler</code>, <code>ConcreteHandler</code>, <code>Client</code>.</p>
        <p style="font-size: 0.85rem; margin-bottom: 0.6rem;"><strong>💡 Use Cases:</strong> Middleware lọc HTTP Request (AuthFilter &rarr; CorsFilter &rarr; RateLimitFilter &rarr; Controller).</p>
      </div>
    </div>

    <!-- 14. Command -->
    <div class="card">
      <div class="card-title">14. Command Pattern</div>
      <div class="card-content">
        <span class="pattern-cat-tag cat-behavioral">Behavioral</span>
        <div class="concept-box" style="border-left-color: #d97706; margin: 0.6rem 0;">
          <div class="concept-title" style="color: #d97706;">🎯 Ý Định (Intent)</div>
          <p style="font-size: 0.88rem;">Đóng gói một yêu cầu dưới dạng đối tượng, cho phép tham số hóa các Client, xếp hàng yêu cầu (Queueing), ghi log và tính năng <strong>Undo / Redo</strong>.</p>
        </div>
        <p style="font-size: 0.85rem; margin-bottom: 0.4rem;"><strong>👥 Participants:</strong> <code>Command</code>, <code>ConcreteCommand</code>, <code>Invoker</code>, <code>Receiver</code>.</p>
        <p style="font-size: 0.85rem; margin-bottom: 0.6rem;"><strong>💡 Use Cases:</strong> Nút bấm GUI (Save, Print, Cut, Paste), Hàng đợi tác vụ bất đồng bộ Job Queue.</p>
      </div>
    </div>

    <!-- 15. Interpreter -->
    <div class="card">
      <div class="card-title">15. Interpreter Pattern</div>
      <div class="card-content">
        <span class="pattern-cat-tag cat-behavioral">Behavioral</span>
        <div class="concept-box" style="border-left-color: #d97706; margin: 0.6rem 0;">
          <div class="concept-title" style="color: #d97706;">🎯 Ý Định (Intent)</div>
          <p style="font-size: 0.88rem;">Định nghĩa biểu diễn ngữ pháp của một ngôn ngữ cùng trình thông dịch để đánh giá các câu trong ngôn ngữ đó.</p>
        </div>
        <p style="font-size: 0.85rem; margin-bottom: 0.4rem;"><strong>👥 Participants:</strong> <code>AbstractExpression</code>, <code>TerminalExpression</code>, <code>NonterminalExpression</code>, <code>Context</code>.</p>
        <p style="font-size: 0.85rem; margin-bottom: 0.6rem;"><strong>💡 Use Cases:</strong> Trình đánh giá biểu thức số học (SQL Parser, Regular Expressions AST).</p>
      </div>
    </div>

    <!-- 16. Iterator -->
    <div class="card">
      <div class="card-title">16. Iterator Pattern</div>
      <div class="card-content">
        <span class="pattern-cat-tag cat-behavioral">Behavioral</span>
        <div class="concept-box" style="border-left-color: #d97706; margin: 0.6rem 0;">
          <div class="concept-title" style="color: #d97706;">🎯 Ý Định (Intent)</div>
          <p style="font-size: 0.88rem;">Cung cấp phương thức truy cập tuần tự các phần tử của một đối tượng tập hợp mà <em>không để lộ cấu trúc bên trong của nó</em>.</p>
        </div>
        <p style="font-size: 0.85rem; margin-bottom: 0.4rem;"><strong>👥 Participants:</strong> <code>Iterator</code>, <code>ConcreteIterator</code>, <code>Aggregate</code>, <code>ConcreteAggregate</code>.</p>
        <p style="font-size: 0.85rem; margin-bottom: 0.6rem;"><strong>💡 Use Cases:</strong> Bộ lặp Java Collections (<code>List.iterator()</code>, <code>ResultSet.next()</code>).</p>
      </div>
    </div>

    <!-- 17. Mediator -->
    <div class="card">
      <div class="card-title">17. Mediator Pattern</div>
      <div class="card-content">
        <span class="pattern-cat-tag cat-behavioral">Behavioral</span>
        <div class="concept-box" style="border-left-color: #d97706; margin: 0.6rem 0;">
          <div class="concept-title" style="color: #d97706;">🎯 Ý Định (Intent)</div>
          <p style="font-size: 0.88rem;">Định nghĩa một đối tượng đóng gói cách thức một tập hợp các đối tượng tương tác, ngăn các đối tượng tham chiếu trực tiếp đến nhau.</p>
        </div>
        <p style="font-size: 0.85rem; margin-bottom: 0.4rem;"><strong>👥 Participants:</strong> <code>Mediator</code>, <code>ConcreteMediator</code>, <code>Colleague Classes</code>.</p>
        <p style="font-size: 0.85rem; margin-bottom: 0.6rem;"><strong>💡 Use Cases:</strong> Tháp không lưu điều phối máy bay, Hộp thoại DialogDirector quản lý các Form inputs.</p>
      </div>
    </div>

    <!-- 18. Memento -->
    <div class="card">
      <div class="card-title">18. Memento Pattern</div>
      <div class="card-content">
        <span class="pattern-cat-tag cat-behavioral">Behavioral</span>
        <div class="concept-box" style="border-left-color: #d97706; margin: 0.6rem 0;">
          <div class="concept-title" style="color: #d97706;">🎯 Ý Định (Intent)</div>
          <p style="font-size: 0.88rem;">Chụp lại và lưu trữ trạng thái nội bộ của một đối tượng để khôi phục lại sau đó mà không vi phạm tính đóng gói (Encapsulation).</p>
        </div>
        <p style="font-size: 0.85rem; margin-bottom: 0.4rem;"><strong>👥 Participants:</strong> <code>Originator</code>, <code>Memento</code>, <code>Caretaker</code>.</p>
        <p style="font-size: 0.85rem; margin-bottom: 0.6rem;"><strong>💡 Use Cases:</strong> Lưu snapshot màn chơi game, Lịch sử khôi phục văn bản trong Text Editor.</p>
      </div>
    </div>

    <!-- 19. Observer -->
    <div class="card">
      <div class="card-title">19. Observer Pattern (Publish/Subscribe)</div>
      <div class="card-content">
        <span class="pattern-cat-tag cat-behavioral">Behavioral</span>
        <div class="concept-box" style="border-left-color: #d97706; margin: 0.6rem 0;">
          <div class="concept-title" style="color: #d97706;">🎯 Ý Định (Intent)</div>
          <p style="font-size: 0.88rem;">Định nghĩa mối quan hệ một-nhiều (One-to-Many); khi Subject đổi trạng thái, <em>tất cả các Observers tự động được thông báo và cập nhật</em>.</p>
        </div>
        <p style="font-size: 0.85rem; margin-bottom: 0.4rem;"><strong>👥 Participants:</strong> <code>Subject</code>, <code>Observer</code>, <code>ConcreteSubject</code>, <code>ConcreteObserver</code>.</p>
        <p style="font-size: 0.85rem; margin-bottom: 0.6rem;"><strong>💡 Use Cases:</strong> Event Listener trong GUI, Bắn thông báo cập nhật trạng thái đơn hàng FOS Notification.</p>

        <details class="code-accordion">
          <summary><span>💻 Xem mã nguồn Java minh họa</span> <span class="toggle-icon">▼</span></summary>
          <div class="code-block">
            <div class="code-header">
              <div class="code-header-left">
                <div class="code-dots"><span class="code-dot dot-red"></span><span class="code-dot dot-yellow"></span><span class="code-dot dot-green"></span></div>
                <span class="code-lang-tag">Java &bull; Observer Pattern</span>
              </div>
              <button class="code-copy-btn" onclick="copyCode(this)">📋 Sao chép</button>
            </div>
            <pre class="code-body"><code><span class="kwd">public interface</span> <span class="typ">Observer</span> { <span class="kwd">void</span> <span class="fn">update</span>(<span class="typ">String</span> status); }

<span class="kwd">public class</span> <span class="typ">OrderSubject</span> {
    <span class="kwd">private</span> <span class="typ">List</span>&lt;<span class="typ">Observer</span>&gt; observers = <span class="kwd">new</span> <span class="typ">ArrayList</span>&lt;&gt;();
    <span class="kwd">public void</span> <span class="fn">attach</span>(<span class="typ">Observer</span> o) { observers.<span class="fn">add</span>(o); }
    <span class="kwd">public void</span> <span class="fn">notifyAll</span>(<span class="typ">String</span> status) {
        <span class="kwd">for</span> (<span class="typ">Observer</span> o : observers) o.<span class="fn">update</span>(status);
    }
}</code></pre>
          </div>
        </details>
      </div>
    </div>

    <!-- 20. State -->
    <div class="card">
      <div class="card-title">20. State Pattern</div>
      <div class="card-content">
        <span class="pattern-cat-tag cat-behavioral">Behavioral</span>
        <div class="concept-box" style="border-left-color: #d97706; margin: 0.6rem 0;">
          <div class="concept-title" style="color: #d97706;">🎯 Ý Định (Intent)</div>
          <p style="font-size: 0.88rem;">Cho phép một đối tượng thay đổi hành vi của nó khi trạng thái nội bộ của nó thay đổi. Triệt tiêu hoàn toàn khối switch-case / if-else kiểm tra trạng thái.</p>
        </div>
        <p style="font-size: 0.85rem; margin-bottom: 0.4rem;"><strong>👥 Participants:</strong> <code>Context</code>, <code>State</code>, <code>ConcreteState</code>.</p>
        <p style="font-size: 0.85rem; margin-bottom: 0.6rem;"><strong>💡 Use Cases:</strong> Quản lý trạng thái kết nối TCPConnection, Trạng thái đơn hàng FOS Order State.</p>

        <details class="code-accordion">
          <summary><span>💻 Xem mã nguồn Java minh họa</span> <span class="toggle-icon">▼</span></summary>
          <div class="code-block">
            <div class="code-header">
              <div class="code-header-left">
                <div class="code-dots"><span class="code-dot dot-red"></span><span class="code-dot dot-yellow"></span><span class="code-dot dot-green"></span></div>
                <span class="code-lang-tag">Java &bull; State Pattern</span>
              </div>
              <button class="code-copy-btn" onclick="copyCode(this)">📋 Sao chép</button>
            </div>
            <pre class="code-body"><code><span class="kwd">public interface</span> <span class="typ">OrderState</span> { <span class="kwd">void</span> <span class="fn">next</span>(<span class="typ">OrderContext</span> ctx); }
<span class="kwd">public class</span> <span class="typ">PendingState</span> <span class="kwd">implements</span> <span class="typ">OrderState</span> {
    <span class="kwd">public void</span> <span class="fn">next</span>(<span class="typ">OrderContext</span> ctx) { ctx.<span class="fn">setState</span>(<span class="kwd">new</span> <span class="typ">ShippingState</span>()); }
}</code></pre>
          </div>
        </details>
      </div>
    </div>

    <!-- 21. Strategy -->
    <div class="card">
      <div class="card-title">21. Strategy Pattern</div>
      <div class="card-content">
        <span class="pattern-cat-tag cat-behavioral">Behavioral</span>
        <div class="concept-box" style="border-left-color: #d97706; margin: 0.6rem 0;">
          <div class="concept-title" style="color: #d97706;">🎯 Ý Định (Intent)</div>
          <p style="font-size: 0.88rem;">Định nghĩa một họ thuật toán, đóng gói từng thuật toán lại và làm cho chúng <em>có thể hoán đổi cho nhau tại thời điểm chạy</em>.</p>
        </div>
        <p style="font-size: 0.85rem; margin-bottom: 0.4rem;"><strong>👥 Participants:</strong> <code>Strategy</code>, <code>ConcreteStrategy</code>, <code>Context</code>.</p>
        <p style="font-size: 0.85rem; margin-bottom: 0.6rem;"><strong>💡 Use Cases:</strong> Cổng thanh toán FOS (MomoStrategy, ZaloPayStrategy, CardStrategy), Thuật toán nén file.</p>

        <details class="code-accordion">
          <summary><span>💻 Xem mã nguồn Java minh họa</span> <span class="toggle-icon">▼</span></summary>
          <div class="code-block">
            <div class="code-header">
              <div class="code-header-left">
                <div class="code-dots"><span class="code-dot dot-red"></span><span class="code-dot dot-yellow"></span><span class="code-dot dot-green"></span></div>
                <span class="code-lang-tag">Java &bull; Strategy Pattern</span>
              </div>
              <button class="code-copy-btn" onclick="copyCode(this)">📋 Sao chép</button>
            </div>
            <pre class="code-body"><code><span class="kwd">public interface</span> <span class="typ">PaymentStrategy</span> { <span class="kwd">void</span> <span class="fn">pay</span>(<span class="kwd">int</span> amount); }
<span class="kwd">public class</span> <span class="typ">MomoPayment</span> <span class="kwd">implements</span> <span class="typ">PaymentStrategy</span> {
    <span class="kwd">public void</span> <span class="fn">pay</span>(<span class="kwd">int</span> amount) { System.out.<span class="fn">println</span>(<span class="str">"Trả qua Momo: "</span> + amount); }
}
<span class="kwd">public class</span> <span class="typ">ShoppingCart</span> {
    <span class="kwd">private</span> <span class="typ">PaymentStrategy</span> strategy;
    <span class="kwd">public void</span> <span class="fn">setPaymentStrategy</span>(<span class="typ">PaymentStrategy</span> s) { <span class="kwd">this</span>.strategy = s; }
    <span class="kwd">public void</span> <span class="fn">checkout</span>(<span class="kwd">int</span> total) { strategy.<span class="fn">pay</span>(total); }
}</code></pre>
          </div>
        </details>
      </div>
    </div>

    <!-- 22. Template Method -->
    <div class="card">
      <div class="card-title">22. Template Method Pattern</div>
      <div class="card-content">
        <span class="pattern-cat-tag cat-behavioral">Behavioral</span>
        <div class="concept-box" style="border-left-color: #d97706; margin: 0.6rem 0;">
          <div class="concept-title" style="color: #d97706;">🎯 Ý Định (Intent)</div>
          <p style="font-size: 0.88rem;">Định nghĩa bộ khung của thuật toán trong một thao tác, trì hoãn một số bước cho lớp con triển khai chi tiết mà không thay đổi cấu trúc tổng thể.</p>
        </div>
        <p style="font-size: 0.85rem; margin-bottom: 0.4rem;"><strong>👥 Participants:</strong> <code>AbstractClass</code>, <code>ConcreteClass</code>.</p>
        <p style="font-size: 0.85rem; margin-bottom: 0.6rem;"><strong>💡 Use Cases:</strong> Khung xử lý DataMiner (Đọc file &rarr; Bóc tách &rarr; Xử lý dữ liệu &rarr; Xuất báo cáo).</p>
      </div>
    </div>

    <!-- 23. Visitor -->
    <div class="card">
      <div class="card-title">23. Visitor Pattern</div>
      <div class="card-content">
        <span class="pattern-cat-tag cat-behavioral">Behavioral</span>
        <div class="concept-box" style="border-left-color: #d97706; margin: 0.6rem 0;">
          <div class="concept-title" style="color: #d97706;">🎯 Ý Định (Intent)</div>
          <p style="font-size: 0.88rem;">Đại diện cho thao tác được thực hiện trên các phần tử của cấu trúc đối tượng, cho phép định nghĩa thao tác mới mà không cần sửa đổi lớp của các phần tử đó.</p>
        </div>
        <p style="font-size: 0.85rem; margin-bottom: 0.4rem;"><strong>👥 Participants:</strong> <code>Visitor</code>, <code>ConcreteVisitor</code>, <code>Element</code>, <code>ConcreteElement</code>.</p>
        <p style="font-size: 0.85rem; margin-bottom: 0.6rem;"><strong>💡 Use Cases:</strong> Xuất dữ liệu sang XML/JSON/PDF từ cùng một cây đối tượng AST trong Compiler.</p>
      </div>
    </div>
  </div>
</section>

<!-- ========================================== -->
<!-- CHUYÊN ĐỀ 2: GENAI TRONG THIẾT KẾ PHẦN MỀM -->
<!-- ========================================== -->
<section id="genai-architecture" class="chapter-section">
  <div class="chapter-header">
    <div class="chapter-badge-row">
      <span class="chapter-badge">CHUYÊN ĐỀ AI</span>
      <span class="chapter-lecturer-tag">SWD392_GenAI &bull; Next-Gen Software Engineering</span>
    </div>
    <h2 class="chapter-title">Ứng Dụng Generative AI Trong Kiến Trúc &amp; Thiết Kế Phần Mềm</h2>
    <div class="chapter-subtitle">Prompt Engineering, PlantUML Auto-generation, Architecture Tradeoffs &amp; Copilot</div>
  </div>

  <div class="card-grid">
    <div class="card">
      <div class="card-title">🤖 1. Bộ Công Cụ Trợ Lý AI Then Chốt</div>
      <div class="card-content">
        <ul style="padding-left: 1.2rem;">
          <li><strong>ChatGPT / LLM</strong>: Đóng vai trò cố vấn kiến trúc sư (Architect Assistant), phân tích yêu cầu SRS, gợi ý Actor &amp; Use Case, đề xuất phong cách kiến trúc phù hợp.</li>
          <li><strong>PlantUML</strong>: Chuyển đổi mã mô tả văn bản (Text-to-Diagram) thành biểu đồ kiến trúc sắc nét một cách tức thì.</li>
          <li><strong>GitHub Copilot</strong>: Tự động sinh mã nguồn (Boilerplate code) cho tầng Service, DAO, Interface, Entity và hiện thực các mẫu Design Patterns.</li>
        </ul>
      </div>
    </div>

    <div class="card">
      <div class="card-title">💬 2. Kỹ Thuật Viết Prompt Chuẩn Cho Use Case</div>
      <div class="card-content">
        <p>Khai thác ChatGPT để bóc tách Actor &amp; Use Case từ bản mô tả bài toán:</p>
        <div class="code-block">
          <div class="code-header">
            <div class="code-header-left">
              <div class="code-dots"><span class="code-dot dot-red"></span><span class="code-dot dot-yellow"></span><span class="code-dot dot-green"></span></div>
              <span class="code-lang-tag">ChatGPT Prompt Template</span>
            </div>
            <button class="code-copy-btn" onclick="copyCode(this)">📋 Sao chép</button>
          </div>
          <pre class="code-body"><code>"Là một chuyên gia thiết kế kiến trúc phần mềm (Software Architect),
tôi cần thiết kế hệ thống quản lý thư viện số với các tính năng:
- Độc giả: tìm kiếm sách, mượn sách, trả sách, gia hạn.
- Thủ thư: quản lý đầu sách, phân loại, kiểm kê, duyệt thẻ.
Hãy giúp tôi:
1. Xác định Primary Actors và Secondary Actors.
2. Danh sách các Use Cases chính (viết theo quy tắc Động từ + Danh từ).
3. Viết mã nguồn PlantUML để sinh biểu đồ Use Case hoàn chỉnh."</code></pre>
        </div>
      </div>
    </div>

    <div class="card">
      <div class="card-title">📐 3. Tự Động Sinh Mã Biểu Đồ Với PlantUML</div>
      <div class="card-content">
        <p>Mẫu mã PlantUML do AI sinh ra cho Kiến trúc 3 tầng:</p>
        <div class="code-block">
          <div class="code-header">
            <div class="code-header-left">
              <div class="code-dots"><span class="code-dot dot-red"></span><span class="code-dot dot-yellow"></span><span class="code-dot dot-green"></span></div>
              <span class="code-lang-tag">PlantUML Code</span>
            </div>
            <button class="code-copy-btn" onclick="copyCode(this)">📋 Sao chép</button>
          </div>
          <pre class="code-body"><code>@startuml
package "Presentation Layer" {
    [Web Controller]
    [Mobile REST API]
}
package "Business Logic Layer" {
    [OrderService]
    [PaymentService]
}
package "Data Access Layer" {
    [OrderDAO]
    [AccountDAO]
}
database "PostgreSQL" {
    [Tables]
}
[Web Controller] --> [OrderService]
[OrderService] --> [OrderDAO]
[OrderDAO] --> [Tables]
@enduml</code></pre>
        </div>
      </div>
    </div>
  </div>

  <div class="topic-card">
    <div class="topic-title">⚡ Sử Dụng AI Để Lựa Chọn Kiến Trúc Thích Hợp (Case Study: Food Delivery System)</div>
    <p>
      Bài toán: <em>Thiết kế hệ thống giao đồ ăn trực tuyến (Online Food Delivery System) với các yêu cầu: Lưu lượng cao vào giờ cao điểm, cập nhật vị trí shipper thời gian thực (Real-time GPS), tích hợp nhiều cổng thanh toán số, độ trễ đặt hàng cực thấp.</em>
    </p>

    <div class="table-wrap">
      <table class="styled-table">
        <thead>
          <tr>
            <th>Yêu Cầu Bài Toán</th>
            <th>Khuyến Nghị Kiến Trúc Từ AI</th>
            <th>Lý Do Kỹ Thuật &amp; Đánh Đổi</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>Hệ thống đơn hàng &amp; Giỏ hàng</td>
            <td><strong>Microservices Architecture</strong></td>
            <td>Cho phép scale độc lập các service chịu tải đột biến vào bữa trưa/tối mà không ảnh hưởng toàn hệ thống.</td>
          </tr>
          <tr>
            <td>Theo dõi vị trí Shipper Realtime</td>
            <td><strong>Event-Driven &amp; WebSocket</strong></td>
            <td>Truyền tọa độ GPS liên tục độ trễ thấp qua Kafka/Redis Pub-Sub thay vì cơ chế Polling HTTP gây nghẽn server.</td>
          </tr>
          <tr>
            <td>Tích hợp đa dạng cổng thanh toán</td>
            <td><strong>Strategy + Factory Pattern</strong></td>
            <td>Dễ dàng thêm ví mới (Apple Pay, ShopeePay) mà không phải sửa đổi luồng thanh toán hiện tại.</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>

  <div class="callout callout-important">
    <div class="callout-title">⚠️ Nguyên Tắc Cốt Tử: AI Là Trợ Lý, Không Phải Người Thay Thế Kiến Trúc Sư!</div>
    <ul style="padding-left: 1.2rem;">
      <li>Các mô hình AI có thể tạo ra các giả định sai lầm (Hallucinations) về ranh giới hệ thống hoặc bỏ qua các ràng buộc vật lý, bảo mật đặc thù.</li>
      <li>Mọi mã nguồn, biểu đồ và quyết định kiến trúc do AI đề xuất <strong>bắt buộc phải được kiến trúc sư con người thẩm định, phê duyệt và chịu trách nhiệm kỹ thuật</strong>.</li>
    </ul>
  </div>
</section>
"""
