# _generator/scripts.py
# Full Vanilla JavaScript Engine matching design.md - Raw String

def get_js():
    return r"""
// ==========================================
// 1. DATA STORES: 23 GOF PATTERNS
// ==========================================
const gofPatternsData = [
  // Creational (5)
  {
    name: "Singleton",
    cat: "creational",
    intent: "Đảm bảo một lớp chỉ có duy nhất một thể hiện và cung cấp điểm truy cập toàn cục.",
    useCase: "Database Connection Pool, Logger, Cấu hình hệ thống (Configuration Manager).",
    pros: "Kiểm soát truy cập tài nguyên duy nhất, tiết kiệm bộ nhớ.",
    cons: "Khó viết Unit Test (vi phạm Single Responsibility), tiềm ẩn điểm thắt cổ chai."
  },
  {
    name: "Factory Method",
    cat: "creational",
    intent: "Định nghĩa interface tạo đối tượng, để lớp con quyết định lớp cụ thể nào được khởi tạo.",
    useCase: "Hệ thống vẽ Dialog đa nền tảng (WindowsDialog, MacDialog, LinuxDialog).",
    pros: "Tuân thủ Open/Closed Principle, tách rời mã Client khỏi các lớp cụ thể.",
    cons: "Làm gia tăng số lượng lớp con trong hệ thống."
  },
  {
    name: "Abstract Factory",
    cat: "creational",
    intent: "Cung cấp giao diện tạo lập một họ các đối tượng có liên quan mà không chỉ định lớp cụ thể.",
    useCase: "Bộ UI Toolkit (Button + Checkbox + Scrollbar) cho Windows, Mac, Linux.",
    pros: "Đảm bảo tính tương thích tuyệt đối giữa các sản phẩm trong cùng một họ.",
    cons: "Khó khăn khi muốn bổ sung thêm sản phẩm mới vào họ sản phẩm."
  },
  {
    name: "Builder",
    cat: "creational",
    intent: "Tách quy trình xây dựng đối tượng phức tạp khỏi biểu diễn của nó.",
    useCase: "Tạo đối tượng Order, SQL Query Builder, Meal Builder trong nhà hàng.",
    pros: "Kiểm soát chi tiết từng bước xây dựng, loại bỏ Constructor quá nhiều tham số.",
    cons: "Tăng độ phức tạp mã nguồn do phải tạo thêm lớp Builder riêng biệt."
  },
  {
    name: "Prototype",
    cat: "creational",
    intent: "Tạo đối tượng mới bằng cách sao chép (Clone) một thể hiện mẫu có sẵn.",
    useCase: "Tạo nhân vật game (Quái vật lính hàng loạt với thuộc tính tương đồng).",
    pros: "Tối ưu hiệu năng khi chi phí tạo đối tượng bằng new quá tốn kém.",
    cons: "Khó khăn khi đối tượng có cấu trúc lồng nhau phức tạp (Deep Clone vs Shallow Clone)."
  },

  // Structural (7)
  {
    name: "Adapter",
    cat: "structural",
    intent: "Chuyển đổi giao diện của một lớp thành giao diện khác mà Client mong đợi.",
    useCase: "Tích hợp thư viện thanh toán bên thứ ba (VNPay, Momo) vào hệ thống hiện tại.",
    pros: "Tái sử dụng mã nguồn cũ mà không cần sửa đổi mã nguồn gốc.",
    cons: "Tăng độ phức tạp tổng thể do xuất hiện thêm lớp trung gian."
  },
  {
    name: "Bridge",
    cat: "structural",
    intent: "Tách phần trừu tượng (Abstraction) khỏi phần hiện thực (Implementation).",
    useCase: "Hình học Shape (Circle, Square) kết hợp với các công cụ vẽ DrawingAPI (OpenGL, DirectX).",
    pros: "Mở rộng 2 chiều độc lập, che giấu chi tiết hiện thực khỏi Client.",
    cons: "Cấu trúc mã trở nên phức tạp hơn đối với bài toán đơn giản."
  },
  {
    name: "Composite",
    cat: "structural",
    intent: "Tổ chức các đối tượng theo cấu trúc cây (Tree) biểu diễn phân cấp Toàn thể - Bộ phận.",
    useCase: "Hệ thống thư mục tập tin (File và Directory), Cây Menu đa cấp.",
    pros: "Client thao tác với đối tượng đơn và phức hợp hoàn toàn đồng nhất.",
    cons: "Khó giới hạn các kiểu đối tượng có thể thêm vào cấu trúc cây."
  },
  {
    name: "Decorator",
    cat: "structural",
    intent: "Gắn thêm trách nhiệm và hành vi mới cho đối tượng một cách động tại thời điểm chạy.",
    useCase: "Java I/O (BufferedReader bọc FileReader), Tính giá đồ uống thêm Topping.",
    pros: "Linh hoạt hơn kế thừa bội phần, tuân thủ nguyên lý Single Responsibility.",
    cons: "Tạo ra rất nhiều đối tượng nhỏ li ti bao bọc lồng nhau khó debug."
  },
  {
    name: "Facade",
    cat: "structural",
    intent: "Cung cấp một giao diện cấp cao đồng nhất, đơn giản hóa cho một hệ thống con phức tạp.",
    useCase: "Bộ điều khiển Rạp hát tại gia (Home Theater Facade), API Gateway rút gọn.",
    pros: "Giảm sự phụ thuộc của Client vào mạng lưới lớp rắc rối bên trong Subsystem.",
    cons: "Facade có nguy cơ trở thành một 'God Object' nắm quá nhiều quyền lực."
  },
  {
    name: "Flyweight",
    cat: "structural",
    intent: "Chia sẻ trạng thái dùng chung (Intrinsic) để hỗ trợ hiệu quả số lượng cực lớn đối tượng.",
    useCase: "Trình soạn thảo văn bản lưu trữ hàng triệu ký tự font chữ, Rừng cây trong game 3D.",
    pros: "Tiết kiệm đáng kể dung lượng bộ nhớ RAM của hệ thống.",
    cons: "Tăng thời gian tính toán CPU để ráp nối trạng thái ngoại lai (Extrinsic state)."
  },
  {
    name: "Proxy",
    cat: "structural",
    intent: "Cung cấp đối tượng đại diện để kiểm soát quyền truy cập tới đối tượng thực.",
    useCase: "Virtual Proxy (Lazy loading ảnh lớn), Protection Proxy (Check quyền Admin), Remote Proxy.",
    pros: "Kiểm soát vòng đời và bảo mật truy cập mà Client không hề hay biết.",
    cons: "Làm tăng độ trễ phản hồi qua thêm một lớp trung gian."
  },

  // Behavioral (11)
  {
    name: "Chain of Responsibility",
    cat: "behavioral",
    intent: "Chuyển yêu cầu dọc theo chuỗi các đối tượng xử lý cho đến khi có đối tượng giải quyết nó.",
    useCase: "Bộ lọc HTTP Filter Middleware (Auth -> Logging -> Cors -> RateLimit).",
    pros: "Giảm mức độ ghép nối giữa bên gửi và các bên nhận.",
    cons: "Không đảm bảo 100% yêu cầu sẽ được xử lý nếu đi hết chuỗi mà không khớp."
  },
  {
    name: "Command",
    cat: "behavioral",
    intent: "Đóng gói yêu cầu thành một đối tượng, cho phép xếp hàng, ghi log và hỗ trợ Undo/Redo.",
    useCase: "Nút bấm GUI Editor (Undo, Redo, Cut, Copy, Paste), Hàng đợi tác vụ Task Queue.",
    pros: "Tách biệt đối tượng kích hoạt thao tác (Invoker) khỏi đối tượng thực thi (Receiver).",
    cons: "Gia tăng số lượng lớp con Command cho từng thao tác nhỏ lẻ."
  },
  {
    name: "Interpreter",
    cat: "behavioral",
    intent: "Định nghĩa ngữ pháp cho một ngôn ngữ và bộ thông dịch để đánh giá các câu trong ngôn ngữ đó.",
    useCase: "Trình đánh giá biểu thức số học (Calculator Parser), Trình diễn giải SQL đơn giản.",
    pros: "Dễ dàng thay đổi và mở rộng ngữ pháp bằng cách thêm lớp Expression mới.",
    cons: "Hiệu năng rất chậm và kém khi cấu trúc ngữ pháp trở nên phức tạp."
  },
  {
    name: "Iterator",
    cat: "behavioral",
    intent: "Cung cấp cách truy cập tuần tự các phần tử của tập hợp mà không để lộ cấu trúc bên trong.",
    useCase: "Java Collections Iterator (List, Set, Map traversal).",
    pros: "Đơn giản hóa giao diện của tập hợp, hỗ trợ nhiều tiến trình duyệt đồng thời.",
    cons: "Có thể dư thừa đối với các cấu trúc dữ liệu đơn giản như mảng 1 chiều."
  },
  {
    name: "Mediator",
    cat: "behavioral",
    intent: "Định nghĩa đối tượng trung gian đóng gói cách thức giao tiếp giữa một tập hợp các đối tượng.",
    useCase: "Tháp kiểm soát không lưu sân bay, Hộp thoại Form (DialogDirector điều khiển các ô nhập).",
    pros: "Giảm phụ thuộc trực tiếp Many-to-Many thành One-to-Many.",
    cons: "Đối tượng Mediator có nguy cơ biến thành God Object cực kỳ phức tạp."
  },
  {
    name: "Memento",
    cat: "behavioral",
    intent: "Chụp lại và lưu trữ trạng thái nội bộ của đối tượng để khôi phục sau này mà không phá vỡ Encapsulation.",
    useCase: "Chức năng Snapshot màn chơi trong Game, Lịch sử khôi phục văn bản Text Editor.",
    pros: "Giữ nguyên vẹn tính bao bọc đóng gói của dữ liệu.",
    cons: "Tiêu tốn bộ nhớ RAM lớn nếu đối tượng lưu trữ trạng thái quá nặng và chụp liên tục."
  },
  {
    name: "Observer",
    cat: "behavioral",
    intent: "Xây dựng quan hệ 1-Nhiều; khi Subject đổi trạng thái, mọi Observers tự động được cập nhật.",
    useCase: "Event Listener trong GUI, Hệ thống bắn thông báo đơn hàng (FOS Notification).",
    pros: "Khớp nối lỏng tuyệt vời giữa bên phát tin và bên nhận tin.",
    cons: "Observers có thể bị rò rỉ bộ nhớ (Memory Leak) nếu quên hủy đăng ký (Deregister)."
  },
  {
    name: "State",
    cat: "behavioral",
    intent: "Cho phép đối tượng thay đổi hành vi khi trạng thái nội bộ thay đổi.",
    useCase: "Quy trình xử lý đơn hàng (Pending -> Shipping -> Delivered), Máy bán hàng tự động.",
    pros: "Triệt tiêu hoàn toàn khối lệnh if-else và switch-case rắc rối.",
    cons: "Làm gia tăng số lượng lớp con tương ứng với từng trạng thái."
  },
  {
    name: "Strategy",
    cat: "behavioral",
    intent: "Đóng gói một họ thuật toán và làm cho chúng có thể hoán đổi cho nhau tại thời điểm chạy.",
    useCase: "Các phương thức thanh toán trong FOS (Momo, ZaloPay, VNPay, CreditCard), Thuật toán sắp xếp.",
    pros: "Dễ dàng thêm thuật toán mới mà không sửa mã Client (Open/Closed Principle).",
    cons: "Client buộc phải hiểu sự khác biệt giữa các thuật toán để chọn Strategy phù hợp."
  },
  {
    name: "Template Method",
    cat: "behavioral",
    intent: "Định nghĩa khung thuật toán ở lớp cha, để lớp con triển khai chi tiết các bước cụ thể.",
    useCase: "Quy trình khai phá dữ liệu Data Mining (Đọc file -> Tiền xử lý -> Phân tích -> Xuất báo cáo).",
    pros: "Tái sử dụng mã nguồn tối đa ở lớp cha, kiểm soát luồng thực thi tổng thể.",
    cons: "Bị giới hạn bởi cấu trúc khung cố định do lớp cha áp đặt."
  },
  {
    name: "Visitor",
    cat: "behavioral",
    intent: "Định nghĩa thao tác mới trên cấu trúc đối tượng mà không cần sửa đổi các lớp của đối tượng đó.",
    useCase: "Trình biên dịch Compiler (Kiểm tra kiểu dữ liệu, Tối ưu mã, Sinh mã máy trên cây AST).",
    pros: "Dễ dàng bổ sung chức năng mới trên toàn bộ cấu trúc dữ liệu.",
    cons: "Rất khó khăn khi cấu trúc phần tử thường xuyên bổ sung thêm lớp mới."
  }
];

// ==========================================
// 2. DATA STORES: ARCHITECTURE STYLES
// ==========================================
const archStylesData = {
  "monolith": {
    name: "Monolithic Architecture (Đơn Khối)",
    desc: "Toàn bộ mã nguồn giao diện, nghiệp vụ và truy cập CSDL được đóng gói trong một tệp nhị phân duy nhất chạy trên một tiến trình.",
    scores: {
      scalability: 4,
      coupling: 2,
      latency: 9,
      resilience: 3,
      simplicity: 9
    },
    pros: "Cực kỳ dễ phát triển ban đầu, dễ kiểm thử toàn cục, độ trễ gọi hàm nội bộ (In-memory) gần như bằng 0.",
    cons: "Khó mở rộng theo chiều ngang, nghẽn cổ chai triển khai (Deploy toàn bộ khối), một lỗi nhỏ có thể đánh sập cả hệ thống."
  },
  "client-server": {
    name: "3-Tier Client / Server Architecture",
    desc: "Phân tách rõ ràng 3 tầng: Presentation Tier (Giao diện) ↔ Business Logic Tier (Máy chủ ứng dụng) ↔ Data Tier (CSDL RDBMS).",
    scores: {
      scalability: 7,
      coupling: 6,
      latency: 7,
      resilience: 6,
      simplicity: 7
    },
    pros: "Phân định rõ trách nhiệm, bảo mật dữ liệu cao (Client không chạm trực tiếp vào DB), dễ nâng cấp tầng giao diện.",
    cons: "Phát sinh chi phí truyền thông mạng giữa các tầng, tầng Business Logic có thể trở thành điểm nghẽn chịu tải."
  },
  "soa": {
    name: "Service-Oriented Architecture (SOA)",
    desc: "Kiến trúc tích hợp doanh nghiệp dựa trên các dịch vụ tự trị, kết nối qua trục truyền thông Enterprise Service Bus (ESB) và giao thức chuẩn SOAP/WSDL.",
    scores: {
      scalability: 8,
      coupling: 8,
      latency: 5,
      resilience: 7,
      simplicity: 5
    },
    pros: "Tái sử dụng dịch vụ cao giữa các phòng ban doanh nghiệp, hỗ trợ tốt các hệ thống kế thừa (Legacy Systems).",
    cons: "Trục ESB trung tâm có nguy cơ trở thành điểm thắt cổ chai và điểm lỗi duy nhất (Single Point of Failure), cấu hình giao thức SOAP/XML cồng kềnh."
  },
  "microservices": {
    name: "Microservices Architecture (Vi Dịch Vụ)",
    desc: "Phân rã hệ thống thành hàng chục dịch vụ nhỏ độc lập hoàn toàn, mỗi dịch vụ sở hữu cơ sở dữ liệu riêng (Database per Service) và giao tiếp qua REST/gRPC/Kafka.",
    scores: {
      scalability: 10,
      coupling: 9,
      latency: 6,
      resilience: 9,
      simplicity: 3
    },
    pros: "Khả năng mở rộng không giới hạn, các đội phát triển độc lập, triển khai CI/CD liên tục không gián đoạn.",
    cons: "Độ phức tạp vận hành cực cao (DevOps, Distributed Tracing), bài toán tính nhất quán dữ liệu ACID phân tán rất nan giải."
  },
  "realtime": {
    name: "Real-Time Concurrent Architecture",
    desc: "Kiến trúc hệ thống tương tranh đa tác vụ (Concurrent Tasks) với ràng buộc thời gian nghiêm ngặt, điều khiển theo ngắt sự kiện và chu kỳ định thời.",
    scores: {
      scalability: 5,
      coupling: 7,
      latency: 10,
      resilience: 8,
      simplicity: 4
    },
    pros: "Độ trễ xử lý cực thấp (micro-giây), phản hồi tất định (Deterministic timing), đảm bảo các giới hạn an toàn vật lý.",
    cons: "Rất khó debug các lỗi tranh chấp tương tranh (Race conditions, Deadlock, Priority Inversion), đòi hỏi phần cứng chuyên dụng."
  }
};

// ==========================================
// 3. DATA STORES: 25 MULTI-CHAPTER QUIZ QUESTIONS
// ==========================================
const quizQuestions = [
  {
    q: "Phương pháp luận COMET của Giáo sư Hassan Gomaa được định nghĩa dựa trên công thức cốt lõi nào?",
    opts: [
      "COMET = Waterfall + C++",
      "COMET = UML (Ký hiệu chuẩn) + METHOD (Trình tự lặp hướng Use Case)",
      "COMET = Agile + Scrum",
      "COMET = Microservices + Docker"
    ],
    ans: 1,
    ex: "COMET (Collaborative Object Modeling and Architectural Design Method) sử dụng ký hiệu UML kết hợp với phương pháp luận lặp hướng Use Case xuyên suốt từ Yêu cầu -> Phân tích -> Thiết kế."
  },
  {
    q: "Trong biểu đồ lớp UML, ký hiệu hình thoi ĐẶC biểu diễn mối quan hệ nào giữa hai lớp?",
    opts: [
      "Aggregation (Quan hệ tụ hợp)",
      "Generalization (Quan hệ kế thừa)",
      "Composition (Quan hệ hợp thành chặt chẽ)",
      "Dependency (Quan hệ phụ thuộc)"
    ],
    ans: 2,
    ex: "Hình thoi đặc thể hiện quan hệ Composition (Hợp thành). Lớp bộ phận (Part) sinh ra, sống và chết cùng với lớp toàn thể (Whole). Hình thoi rỗng là Aggregation."
  },
  {
    q: "Trong mô hình RUP (Rational Unified Process), cột mốc 'Kiến trúc cơ sở' (Architectural Baseline) được hoàn thiện ở cuối pha nào?",
    opts: [
      "Pha Inception (Khởi tạo)",
      "Pha Elaboration (Chi tiết hóa)",
      "Pha Construction (Xây dựng)",
      "Pha Transition (Chuyển giao)"
    ],
    ans: 1,
    ex: "Pha Elaboration có mục tiêu cốt lõi là giải quyết các rủi ro kỹ thuật lớn nhất và thiết lập một Kiến trúc cơ sở ổn định (Lifecycle Architecture Milestone) trước khi bước vào xây dựng hàng loạt."
  },
  {
    q: "Câu hỏi kinh điển: 'Are we building the product right?' liên quan đến hoạt động nào trong bảo đảm chất lượng phần mềm?",
    opts: [
      "Validation (Thẩm định)",
      "Verification (Kiểm định)",
      "Integration (Tích hợp)",
      "Deployment (Triển khai)"
    ],
    ans: 1,
    ex: "Verification kiểm tra xem sản phẩm có được xây dựng đúng theo đặc tả kỹ thuật không (Building the product right). Validation kiểm tra xem có xây dựng đúng sản phẩm khách hàng cần không (Building the right product)."
  },
  {
    q: "Hiện tượng nào xảy ra khi nhiều tác vụ đồng thời truy cập vào cùng một tài nguyên dùng chung dẫn đến dữ liệu bị sai lệch?",
    opts: [
      "Deadlock (Khóa chết)",
      "Race Condition do bài toán Mutual Exclusion",
      "Starvation (Đói tài nguyên)",
      "Thrashing"
    ],
    ans: 1,
    ex: "Bài toán loại trừ lẫn nhau (Mutual Exclusion) giải quyết hiện tượng Race Condition khi nhiều luồng cùng ghi vào vùng tranh chấp (Critical Section). Dùng Mutex hoặc Semaphore để khóa."
  },
  {
    q: "Trong quy tắc đặt tên Use Case chuẩn của UML, cấu trúc ngữ pháp bắt buộc phải là gì?",
    opts: [
      "[Tính Từ] + [Danh Từ]",
      "[Động Từ] + [Danh Từ] (Verb + Noun)",
      "[Danh Từ] + [Động Từ]",
      "Một cụm danh từ trừu tượng"
    ],
    ans: 1,
    ex: "Tên Use Case luôn được đặt theo cấu trúc [Động từ] + [Danh từ] (Ví dụ: Withdraw Cash, Validate PIN) để thể hiện rõ hành động mang lại giá trị có thể đo lường cho Actor."
  },
  {
    q: "Khi nào thì một Use Case A nên sử dụng quan hệ «extend» trỏ về Use Case B?",
    opts: [
      "Khi Use Case A luôn luôn bắt buộc phải thực thi trong B",
      "Khi Use Case A là một hành vi tùy chọn chỉ được kích hoạt tại điểm mở rộng (Extension Point) khi có điều kiện thỏa mãn",
      "Khi A kế thừa các thuộc tính của B",
      "Khi A và B chạy song song"
    ],
    ans: 1,
    ex: "«extend» thể hiện luồng mở rộng có điều kiện (Ví dụ: Confiscate Card mở rộng Validate PIN khi nhập sai mã PIN quá 3 lần). Nếu bắt buộc thực thi thì phải dùng «include»."
  },
  {
    q: "Trong phương pháp COMET, một đối tượng đóng vai trò 'nhạc trưởng' điều phối sự cộng tác của các đối tượng khác trong Use Case thuộc stereotype nào?",
    opts: [
      "«boundary»",
      "«entity»",
      "«control»",
      "«service»"
    ],
    ans: 2,
    ex: "Lớp «control» đóng vai trò như nhạc trưởng (Conductor), nắm giữ quyền kiểm soát và điều phối hành vi của các đối tượng biên và đối tượng thực thể."
  },
  {
    q: "Tại sao phương pháp COMET lại ưu tiên sử dụng Communication Diagram hơn Sequence Diagram trong pha phân tích?",
    opts: [
      "Vì Communication Diagram vẽ đẹp hơn",
      "Vì các Communication Diagram của từng Use Case có thể được ghép nối trực tiếp thành Integrated Communication Diagram để định hình kiến trúc ban đầu",
      "Vì Sequence Diagram không hỗ trợ vòng lặp",
      "Vì Communication Diagram biểu diễn trục thời gian rõ ràng hơn"
    ],
    ans: 1,
    ex: "COMET ưu tiên Communication Diagram vì nó thể hiện cấu trúc kết nối không gian giữa các đối tượng, cho phép ghép nối (Synthesize) trực tiếp thành bản thiết kế kiến trúc hệ thống ban đầu."
  },
  {
    q: "Trong biểu đồ máy trạng thái hữu hạn (FSM), hành động 'entry / Action' được kích hoạt khi nào?",
    opts: [
      "Khi chuẩn bị thoát khỏi trạng thái",
      "Tự động được thực thi mỗi khi luồng điều khiển chuyển vào trạng thái đó",
      "Chỉ khi có lỗi xảy ra",
      "Được thực thi liên tục trong suốt thời gian nằm ở trạng thái đó"
    ],
    ans: 1,
    ex: "Entry action là hành động tức thời được thực thi ngay khi bước vào trạng thái. Thích hợp khi có nhiều cung chuyển dịch cùng đi vào một trạng thái và đòi hỏi cùng một hành động khởi tạo."
  },
  {
    q: "Trong kiến trúc Client/Server 3 tầng chuẩn, tầng Application / Business Logic có trách nhiệm gì?",
    opts: [
      "Chỉ hiển thị giao diện HTML cho người dùng",
      "Chỉ lưu trữ các khối dữ liệu nhị phân trên đĩa cứng",
      "Đóng gói toàn bộ quy tắc nghiệp vụ, điều phối giao dịch và xử lý tính toán",
      "Quản lý driver phần cứng máy in"
    ],
    ans: 2,
    ex: "Tầng 2 (Application / Business Logic Tier) chứa các đối tượng nghiệp vụ, kiểm tra tính hợp lệ và điều phối giao dịch, tách rời hoàn toàn khỏi UI (Tầng 1) và Database (Tầng 3)."
  },
  {
    q: "Khi ánh xạ quan hệ Nhiều-Nhiều (M:N) giữa hai lớp thực thể sang CSDL quan hệ, giải pháp chuẩn là gì?",
    opts: [
      "Thêm cột khóa ngoại vào cả hai bảng",
      "Tạo một Bảng trung gian (Junction / Associative Table) chứa 2 khóa ngoại trỏ về khóa chính của 2 bảng gốc",
      "Gộp hai lớp thành một bảng duy nhất",
      "Không thể ánh xạ được"
    ],
    ans: 1,
    ex: "Quan hệ M:N bắt buộc phải được chuẩn hóa bằng cách tạo Bảng trung gian (Junction Table) chứa 2 khóa ngoại (FK) kết hợp làm khóa chính phức hợp (Composite PK)."
  },
  {
    q: "Trong 8 nguyên lý thiết kế dịch vụ SOA của Thomas Erl, nguyên lý 'Statelessness' mang lại lợi ích gì lớn nhất?",
    opts: [
      "Tối đa hóa khả năng mở rộng (Scalability) vì server không phải tốn RAM lưu trữ trạng thái phiên của Client",
      "Bảo mật tuyệt đối",
      "Giảm độ phức tạp mã nguồn",
      "Tăng tốc độ đọc đĩa cứng"
    ],
    ans: 0,
    ex: "Dịch vụ phi trạng thái (Statelessness) giúp bất kỳ server nào trong cụm cluster cũng có thể xử lý yêu cầu tiếp theo của client, giúp hệ thống dễ dàng mở rộng theo chiều ngang (Horizontal Scaling)."
  },
  {
    q: "Giao thức cam kết hai pha (Two-Phase Commit - 2PC) trong SOA được áp dụng để giải quyết bài toán gì?",
    opts: [
      "Tăng tốc độ tải trang web",
      "Đảm bảo tính toàn vẹn và nhất quán dữ liệu ACID trong các giao dịch phân tán qua nhiều dịch vụ",
      "Mã hóa đường truyền SSL",
      "Phát hiện lỗi phần cứng CPU"
    ],
    ans: 1,
    ex: "2PC là giao thức đồng thuận đảm bảo một giao dịch phân tán hoặc là được Commit trên tất cả các dịch vụ tham gia, hoặc là bị Rollback toàn bộ nếu có một dịch vụ gặp lỗi."
  },
  {
    q: "Trong ký hiệu UML 2 cho Kiến trúc thành phần (CBD), biểu tượng 'Lollipop' (lollipop notation) biểu diễn điều gì?",
    opts: [
      "Required Interface (Giao diện yêu cầu)",
      "Provided Interface (Giao diện cung cấp)",
      "Port vào/ra",
      "Connector nối dây"
    ],
    ans: 1,
    ex: "Hình que kẹo mút (Lollipop) biểu diễn Provided Interface - các thao tác và dịch vụ mà thành phần công khai phục vụ cho bên ngoài."
  },
  {
    q: "Hệ thống thời gian thực nào mà nếu vi phạm hạn chót (Deadline) sẽ dẫn đến thảm họa phá hủy hệ thống hoặc nguy hiểm tính mạng?",
    opts: [
      "Soft Real-Time System",
      "Hard Real-Time System",
      "Firm Real-Time System",
      "Batch Processing System"
    ],
    ans: 1,
    ex: "Hard Real-Time đòi hỏi tính tất định tuyệt đối; trễ hạn chót dù chỉ 1ms là xem như toàn bộ hệ thống thất bại (ví dụ: bung túi khí ô tô, điều khiển phản ứng hạt nhân)."
  },
  {
    q: "Hiện tượng Nghịch đảo độ ưu tiên (Priority Inversion) có thể được ngăn chặn hiệu quả nhất bằng kỹ thuật nào?",
    opts: [
      "Tắt toàn bộ ngắt hệ thống",
      "Priority Inheritance Protocol (Giao thức kế thừa độ ưu tiên)",
      "Tăng bộ nhớ RAM",
      "Chuyển sang ứng dụng tuần tự"
    ],
    ans: 1,
    ex: "Priority Inheritance Protocol tạm thời nâng độ ưu tiên của tác vụ đang giữ khóa Mutex lên bằng mức của tác vụ ưu tiên cao đang chờ, ngăn không cho các tác vụ trung bình cướp CPU."
  },
  {
    q: "Theo công thức định luật Rate Monotonic Analysis (RMA), cận trên an toàn tuyệt đối cho hệ thống có vô hạn tác vụ định kỳ là bao nhiêu?",
    opts: [
      "100%",
      "82.8%",
      "Khoảng 69.3% (ln 2)",
      "50%"
    ],
    ans: 2,
    ex: "Khi số lượng tác vụ n tiến tới vô cùng, cận trên giới hạn: lim n(2^(1/n) - 1) = ln 2 ≈ 0.693 (khoảng 69.3% tổng công suất CPU)."
  },
  {
    q: "Công thức tính hệ số sẵn sàng của hệ thống (System Availability) là gì?",
    opts: [
      "A = MTTR / MTTF",
      "A = MTTF / (MTTF + MTTR)",
      "A = (MTTF - MTTR) / MTTF",
      "A = MTTR / (MTTF - MTTR)"
    ],
    ans: 1,
    ex: "Hệ số sẵn sàng được tính theo công thức: A = MTTF / (MTTF + MTTR). Đây là tỷ lệ giữa thời gian hoạt động bình thường trên tổng thời gian vòng đời (thời gian chạy + thời gian sửa chữa)."
  },
  {
    q: "Trong Case Study ATM (Chương 21), điều gì sẽ xảy ra khi khách hàng nhập sai mã PIN lần thứ 3 liên tiếp?",
    opts: [
      "Máy tự động nhả thẻ ra",
      "Thẻ ATM bị hệ thống tịch thu (Confiscate Card) ngay lập tức",
      "Máy khóa bàn phím trong 5 phút",
      "Máy tự động gửi tin nhắn SMS cảnh báo"
    ],
    ans: 1,
    ex: "Quy tắc nghiệp vụ của ATM: Khách hàng được phép nhập mã PIN sai tối đa 2 lần; lần thứ 3 sai thì máy chuyển trạng thái sang Confiscate Card và nuốt thẻ vào khay an toàn."
  },
  {
    q: "Design Pattern nào thuộc nhóm Creational cho phép tạo đối tượng phức tạp từng bước một mà không cần một constructor dài dòng?",
    opts: [
      "Factory Method",
      "Builder Pattern",
      "Prototype",
      "Singleton"
    ],
    ans: 1,
    ex: "Builder Pattern giải quyết bài toán tạo lập các đối tượng phức tạp có nhiều tham số tùy chọn (Telescoping Constructor problem) bằng cách thiết lập từng thuộc tính qua các bước method chaining."
  },
  {
    q: "Khi một hệ thống cần hỗ trợ nhiều cổng thanh toán (Momo, ZaloPay, Thẻ tín dụng) có thể hoán đổi linh hoạt tại thời điểm chạy, mẫu thiết kế nào phù hợp nhất?",
    opts: [
      "Observer Pattern",
      "Strategy Pattern",
      "Decorator Pattern",
      "Flyweight Pattern"
    ],
    ans: 1,
    ex: "Strategy Pattern đóng gói từng thuật toán/phương thức thanh toán thành các lớp riêng biệt tuân thủ cùng một interface chung, cho phép Client hoán đổi thuật toán thanh toán tùy ý lúc runtime."
  },
  {
    q: "Mẫu thiết kế nào giúp gắn thêm hành vi cho một đối tượng một cách linh hoạt tại thời điểm chạy mà không cần kế thừa lớp (Ví dụ: Thêm Topping cho Cafe)?",
    opts: [
      "Adapter Pattern",
      "Decorator Pattern",
      "Facade Pattern",
      "Proxy Pattern"
    ],
    ans: 1,
    ex: "Decorator Pattern bao bọc (wrap) đối tượng gốc và bổ sung thêm các tính năng động mà không phá vỡ cấu trúc lớp ban đầu."
  },
  {
    q: "Trong chuyên đề GenAI (SWD392_GenAI), công cụ nào được dùng để sinh biểu đồ kiến trúc phần mềm tự động từ mô tả văn bản của AI?",
    opts: [
      "Adobe Photoshop",
      "PlantUML",
      "Microsoft Excel",
      "AutoCAD"
    ],
    ans: 1,
    ex: "PlantUML nhận mã kịch bản văn bản (Text-to-Diagram) do ChatGPT hoặc lập trình viên cung cấp để tự động vẽ thành các biểu đồ UML chuẩn xác."
  },
  {
    q: "Vai trò chuẩn mực nhất của Trí Tuệ Nhân Tạo (GenAI) trong quy trình thiết kế kiến trúc phần mềm là gì?",
    opts: [
      "Thay thế hoàn toàn vai trò của các kiến trúc sư phần mềm con người",
      "Đóng vai trò là trợ lý đắc lực hỗ trợ gợi ý ý tưởng, viết code mẫu và phân tích đánh đổi, nhưng bắt buộc phải có con người thẩm định",
      "Tự động nghiệm thu và triển khai sản phẩm trực tiếp lên production mà không cần test",
      "Chỉ dùng để vẽ hình minh họa cho đẹp"
    ],
    ans: 1,
    ex: "AI là một công cụ trợ lý hỗ trợ (Assistant), không thể thay thế kiến trúc sư con người. Mọi đề xuất kiến trúc của AI đều cần được kỹ sư thẩm định, kiểm chứng về tính an toàn và khả thi."
  }
];

// ==========================================
// 4. CLIENT LOGIC ENGINES
// ==========================================

// Global State
let currentQuizIdx = 0;
let userScore = 0;
let answeredCount = 0;
let currentPatternCat = 'all';

// Initialize on Load
document.addEventListener('DOMContentLoaded', () => {
  initTheme();
  renderPatterns();
  selectArch('monolith');
  renderQuizQuestion();
  initScrollSpy();
  initLiveSearch();
  renderMathSafe();
});

// Copy Code Helper
function copyCode(btn) {
  const codeBlock = btn.closest('.code-block');
  const codeElem = codeBlock.querySelector('pre.code-body code');
  if (codeElem) {
    const text = codeElem.innerText;
    navigator.clipboard.writeText(text).then(() => {
      const orig = btn.innerHTML;
      btn.innerHTML = '✓ Đã chép!';
      btn.style.color = '#10b981';
      setTimeout(() => {
        btn.innerHTML = orig;
        btn.style.color = '';
      }, 2000);
    });
  }
}

// Theme Management
function initTheme() {
  const savedTheme = localStorage.getItem('swd392_theme') || 'light';
  document.documentElement.setAttribute('data-theme', savedTheme);
  updateThemeIcon(savedTheme);
}

function toggleTheme() {
  const current = document.documentElement.getAttribute('data-theme') || 'light';
  const next = current === 'light' ? 'dark' : 'light';
  document.documentElement.setAttribute('data-theme', next);
  localStorage.setItem('swd392_theme', next);
  updateThemeIcon(next);
}

function updateThemeIcon(theme) {
  const btn = document.getElementById('themeToggleBtn');
  if (!btn) return;
  btn.innerHTML = theme === 'dark' ? '☀️' : '🌙';
  btn.setAttribute('title', theme === 'dark' ? 'Chuyển sang nền sáng' : 'Chuyển sang nền tối');
}

// Live Search Engine (Ctrl + K)
function initLiveSearch() {
  const searchInput = document.getElementById('searchInput');
  const clearBtn = document.getElementById('searchClearBtn');

  // Shortcut Ctrl + K
  window.addEventListener('keydown', (e) => {
    if ((e.ctrlKey || e.metaKey) && e.key.toLowerCase() === 'k') {
      e.preventDefault();
      searchInput.focus();
      searchInput.select();
    }
  });

  searchInput.addEventListener('input', () => {
    const q = searchInput.value.trim().toLowerCase();
    clearBtn.style.display = q ? 'block' : 'none';
    filterContent(q);
  });
}

function clearSearch() {
  const searchInput = document.getElementById('searchInput');
  searchInput.value = '';
  document.getElementById('searchClearBtn').style.display = 'none';
  filterContent('');
  searchInput.focus();
}

function filterContent(query) {
  const cards = document.querySelectorAll('.card, .topic-card, .concept-box');
  let matchCount = 0;

  cards.forEach(card => {
    if (!query) {
      card.style.display = '';
      return;
    }
    const text = card.textContent.toLowerCase();
    if (text.includes(query)) {
      card.style.display = '';
      matchCount++;
    } else {
      card.style.display = 'none';
    }
  });
}

// ScrollSpy & Progress Tracker
function initScrollSpy() {
  const progressBar = document.getElementById('progressBar');
  const scrollTopBtn = document.getElementById('scrollTopBtn');
  const sections = document.querySelectorAll('.chapter-section, .part-divider-banner');
  const navLinks = document.querySelectorAll('.nav-link');

  window.addEventListener('scroll', () => {
    // Progress Bar
    const scrollY = window.scrollY;
    const docHeight = document.documentElement.scrollHeight - window.innerHeight;
    const progress = docHeight > 0 ? (scrollY / docHeight) * 100 : 0;
    progressBar.style.width = progress + '%';

    // Scroll Top Button
    if (scrollY > 400) {
      scrollTopBtn.classList.add('visible');
    } else {
      scrollTopBtn.classList.remove('visible');
    }

    // ScrollSpy active link
    let currentId = '';
    sections.forEach(sec => {
      const top = sec.offsetTop - 120;
      if (scrollY >= top) {
        currentId = sec.getAttribute('id');
      }
    });

    if (currentId) {
      navLinks.forEach(link => {
        link.classList.remove('active');
        if (link.getAttribute('href') === '#' + currentId) {
          link.classList.add('active');
        }
      });
    }
  });
}

function scrollToTop() {
  window.scrollTo({ top: 0, behavior: 'smooth' });
}

function toggleMobileNav() {
  const sidebar = document.getElementById('masterSidebar');
  const overlay = document.getElementById('drawerOverlay');
  sidebar.classList.toggle('open');
  overlay.classList.toggle('open');
}

// Module 1: Pattern Explorer
function filterPatterns(cat) {
  currentPatternCat = cat;
  document.querySelectorAll('.filter-btn').forEach(btn => btn.classList.remove('active'));
  event.target.classList.add('active');
  renderPatterns();
}

function searchPatterns(term) {
  const t = term.trim().toLowerCase();
  renderPatterns(t);
}

function renderPatterns(searchTerm = '') {
  const grid = document.getElementById('patternsGrid');
  if (!grid) return;
  grid.innerHTML = '';

  const filtered = gofPatternsData.filter(p => {
    const matchCat = currentPatternCat === 'all' || p.cat === currentPatternCat;
    const matchSearch = !searchTerm || p.name.toLowerCase().includes(searchTerm) || p.intent.toLowerCase().includes(searchTerm);
    return matchCat && matchSearch;
  });

  if (filtered.length === 0) {
    grid.innerHTML = `<div style="grid-column: 1/-1; text-align: center; color: var(--text-muted); padding: 2rem;">Không tìm thấy pattern nào khớp với từ khóa.</div>`;
    return;
  }

  filtered.forEach(p => {
    const card = document.createElement('div');
    card.className = 'pattern-card-item';
    const tagClass = 'cat-' + p.cat;
    card.innerHTML = `
      <span class="pattern-cat-tag ${tagClass}">${p.cat}</span>
      <h4 style="margin: 0.25rem 0 0.5rem; font-size: 1.05rem;">${p.name} Pattern</h4>
      <p style="font-size: 0.85rem; color: var(--text-secondary); margin-bottom: 0.5rem;"><strong>Mục đích:</strong> ${p.intent}</p>
      <p style="font-size: 0.82rem; color: var(--text-muted); margin-bottom: 0.4rem;"><strong>Ứng dụng:</strong> ${p.useCase}</p>
      <div style="font-size: 0.8rem; color: #10b981; margin-top: auto;"><strong>Ưu điểm:</strong> ${p.pros}</div>
    `;
    grid.appendChild(card);
  });
}

// Module 2: Architecture Comparator
function selectArch(key) {
  document.querySelectorAll('.arch-choice-btn').forEach(btn => btn.classList.remove('active'));
  if (event && event.target && event.target.classList) {
    event.target.classList.add('active');
  }

  const data = archStylesData[key];
  const container = document.getElementById('archDetailContainer');
  if (!container || !data) return;

  container.innerHTML = `
    <h3 style="color: var(--accent-primary); margin-bottom: 0.4rem;">${data.name}</h3>
    <p style="font-size: 0.95rem; margin-bottom: 1.25rem; color: var(--text-secondary);">${data.desc}</p>
    
    <div style="margin-bottom: 1.5rem;">
      <div class="metric-row">
        <span class="metric-name">Khả năng mở rộng (Scale):</span>
        <div class="metric-bar-bg"><div class="metric-bar-fill" style="width: ${data.scores.scalability * 10}%; background: #0284c7;"></div></div>
        <span class="metric-score" style="color: #0284c7;">${data.scores.scalability}/10</span>
      </div>
      <div class="metric-row">
        <span class="metric-name">Khớp nối lỏng (Decoupling):</span>
        <div class="metric-bar-bg"><div class="metric-bar-fill" style="width: ${data.scores.coupling * 10}%; background: #4f46e5;"></div></div>
        <span class="metric-score" style="color: #4f46e5;">${data.scores.coupling}/10</span>
      </div>
      <div class="metric-row">
        <span class="metric-name">Độ trễ thấp (Latency):</span>
        <div class="metric-bar-bg"><div class="metric-bar-fill" style="width: ${data.scores.latency * 10}%; background: #059669;"></div></div>
        <span class="metric-score" style="color: #059669;">${data.scores.latency}/10</span>
      </div>
      <div class="metric-row">
        <span class="metric-name">Khả năng chịu lỗi (Resilience):</span>
        <div class="metric-bar-bg"><div class="metric-bar-fill" style="width: ${data.scores.resilience * 10}%; background: #d97706;"></div></div>
        <span class="metric-score" style="color: #d97706;">${data.scores.resilience}/10</span>
      </div>
      <div class="metric-row">
        <span class="metric-name">Tính đơn giản (Simplicity):</span>
        <div class="metric-bar-bg"><div class="metric-bar-fill" style="width: ${data.scores.simplicity * 10}%; background: #7c3aed;"></div></div>
        <span class="metric-score" style="color: #7c3aed;">${data.scores.simplicity}/10</span>
      </div>
    </div>

    <div class="card-grid" style="margin-top: 1rem;">
      <div class="concept-box" style="border-left-color: #10b981;">
        <div class="concept-title" style="color: #059669;">✅ Ưu Điểm Nổi Bật</div>
        <p style="font-size: 0.88rem;">${data.pros}</p>
      </div>
      <div class="concept-box" style="border-left-color: #ef4444;">
        <div class="concept-title" style="color: #dc2626;">⚠️ Hạn Chế Đánh Đổi</div>
        <p style="font-size: 0.88rem;">${data.cons}</p>
      </div>
    </div>
  `;
}

// Module 3: Calculators
function computeAvailability() {
  const mttf = parseFloat(document.getElementById('calcMTTF').value);
  const mttr = parseFloat(document.getElementById('calcMTTR').value);
  const resBox = document.getElementById('availResult');

  if (isNaN(mttf) || isNaN(mttr) || mttf <= 0 || mttr < 0) {
    resBox.style.display = 'block';
    resBox.innerHTML = '<span style="color: #ef4444;">Vui lòng nhập giá trị hợp lệ (> 0).</span>';
    return;
  }

  const avail = (mttf / (mttf + mttr)) * 100;
  const downtimeHoursPerYear = ((100 - avail) / 100) * 8760;
  const downtimeMinsPerYear = downtimeHoursPerYear * 60;

  resBox.style.display = 'block';
  resBox.innerHTML = `
    <strong>Kết quả tính toán:</strong><br>
    &bull; Tính sẵn sàng ($A$): <strong style="color: #0284c7; font-size: 1.15rem;">${avail.toFixed(4)}%</strong><br>
    &bull; Tổng thời gian gián đoạn (Downtime) ước tính: <strong>${downtimeHoursPerYear.toFixed(2)} giờ/năm</strong> (~${downtimeMinsPerYear.toFixed(1)} phút/năm).<br>
    <em>${avail >= 99.999 ? '🌟 Đạt tiêu chuẩn Vàng Five Nines (99.999%)!' : 'Cần tối ưu giảm MTTR hoặc tăng MTTF để nâng cao độ sẵn sàng.'}</em>
  `;
  renderMathSafe(resBox);
}

function computeRMA() {
  const n = parseInt(document.getElementById('calcRMA_N').value);
  const uActual = parseFloat(document.getElementById('calcRMA_U').value);
  const resBox = document.getElementById('rmaResult');

  if (isNaN(n) || isNaN(uActual) || n <= 0 || uActual <= 0) {
    resBox.style.display = 'block';
    resBox.innerHTML = '<span style="color: #ef4444;">Vui lòng nhập số hợp lệ.</span>';
    return;
  }

  const bound = n * (Math.pow(2, 1 / n) - 1) * 100;
  const isSchedulable = uActual <= bound;

  resBox.style.display = 'block';
  resBox.innerHTML = `
    <strong>Kết quả kiểm chứng RMA:</strong><br>
    &bull; Cận trên Liu & Layland với $n = ${n}$: <strong>${bound.toFixed(2)}%</strong><br>
    &bull; Tải CPU thực tế khai báo: <strong>${uActual.toFixed(2)}%</strong><br>
    &bull; Đánh giá: ${isSchedulable ? 
      '<span style="color: #059669; font-weight: 700;">✅ Chắc chắn 100% thỏa mãn mọi Deadline (Schedulable Guaranteed)!</span>' : 
      '<span style="color: #d97706; font-weight: 700;">⚠️ Tải vượt cận trên Liu & Layland ($U > U_{bound}$). Hệ thống có thể bị trễ hạn chót (Cần phân tích sâu qua Time Demand Analysis).</span>'}
  `;
  renderMathSafe(resBox);
}

// Module 4: Multi-Chapter Quiz Engine
function renderQuizQuestion() {
  const qData = quizQuestions[currentQuizIdx];
  document.getElementById('quizQIndex').textContent = currentQuizIdx + 1;
  document.getElementById('quizTotalQ').textContent = quizQuestions.length;
  document.getElementById('quizQuestionText').textContent = qData.q;
  document.getElementById('quizExplanation').style.display = 'none';
  document.getElementById('quizNextBtn').style.display = 'none';

  const optsContainer = document.getElementById('quizOptionsList');
  optsContainer.innerHTML = '';

  const labels = ['A', 'B', 'C', 'D'];
  qData.opts.forEach((optText, idx) => {
    const btn = document.createElement('button');
    btn.className = 'quiz-opt-btn';
    btn.innerHTML = `<span class="quiz-opt-key">${labels[idx]}</span><span>${optText}</span>`;
    btn.onclick = () => handleQuizAnswer(idx, qData.ans, qData.ex);
    optsContainer.appendChild(btn);
  });
}

function handleQuizAnswer(selectedIdx, correctIdx, explanation) {
  const buttons = document.querySelectorAll('.quiz-opt-btn');
  buttons.forEach(b => b.disabled = true);

  if (selectedIdx === correctIdx) {
    buttons[selectedIdx].classList.add('correct');
    userScore++;
  } else {
    buttons[selectedIdx].classList.add('wrong');
    buttons[correctIdx].classList.add('correct');
  }

  answeredCount++;
  document.getElementById('quizScoreText').textContent = `${userScore} / ${answeredCount}`;

  const expBox = document.getElementById('quizExplanation');
  expBox.style.display = 'block';
  expBox.innerHTML = `<strong>Giải thích chi tiết:</strong> ${explanation}`;

  const nextBtn = document.getElementById('quizNextBtn');
  nextBtn.style.display = 'inline-block';
  nextBtn.textContent = currentQuizIdx < quizQuestions.length - 1 ? 'Câu Tiếp Theo →' : 'Xem Kết Quả Tổng Kết 🎉';
}

function nextQuestion() {
  if (currentQuizIdx < quizQuestions.length - 1) {
    currentQuizIdx++;
    renderQuizQuestion();
  } else {
    showQuizSummary();
  }
}

function showQuizSummary() {
  const box = document.getElementById('quizQuestionText');
  const pct = Math.round((userScore / quizQuestions.length) * 100);
  box.innerHTML = `
    🎉 <strong>Chúc Mừng Bạn Đã Hoàn Thành Toàn Bộ 25 Câu Hỏi!</strong><br><br>
    Kết quả chung cuộc: <span style="color: #059669; font-size: 1.5rem; font-weight: 800;">${userScore} / ${quizQuestions.length} (${pct}%)</span><br>
    <em>${pct >= 80 ? 'Xuất sắc! Bạn đã làm chủ 100% kiến thức nền tảng và chuyên sâu của học phần SWD392!' : 'Bạn hãy ôn tập lại các chương có kết quả chưa tốt nhé!'}</em>
  `;
  document.getElementById('quizOptionsList').innerHTML = '';
  document.getElementById('quizExplanation').style.display = 'none';
  document.getElementById('quizNextBtn').style.display = 'none';
}

function restartQuiz() {
  currentQuizIdx = 0;
  userScore = 0;
  answeredCount = 0;
  document.getElementById('quizScoreText').textContent = '0 / 0';
  renderQuizQuestion();
}

// KaTeX Safe Multi-Trigger Auto-Render
function renderMathSafe(el) {
  const target = el || document.body;
  if (typeof renderMathInElement === 'function' && target) {
    try {
      renderMathInElement(target, {
        delimiters: [
          { left: '$$', right: '$$', display: true },
          { left: '\\[', right: '\\]', display: true },
          { left: '$', right: '$', display: false },
          { left: '\\(', right: '\\)', display: false }
        ],
        ignoredTags: ['script', 'noscript', 'style', 'textarea', 'pre', 'code'],
        throwOnError: false
      });
    } catch (err) {
      console.warn('KaTeX render error:', err);
    }
  }
}

// Multi-trigger timers ensuring KaTeX renders reliably across any connection speed
document.addEventListener('DOMContentLoaded', () => renderMathSafe());
window.addEventListener('load', () => renderMathSafe());
setTimeout(() => renderMathSafe(), 100);
setTimeout(() => renderMathSafe(), 300);
setTimeout(() => renderMathSafe(), 800);
setTimeout(() => renderMathSafe(), 1800);
"""
