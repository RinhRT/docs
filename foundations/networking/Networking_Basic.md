# NETWORKING BASIC

## 1. Các nội dung chính:

| CHỦ ĐỀ | MỤC TIÊU |
| -------- | -------- | 
| Clients và Server  | Giải thích khái niệm, vai trò giữa máy chủ và máy khách trong mạng máy tính. |
| Peer To Peer (P2P)  | Giải thích khái niệm, vai trò mô hình P2P trong mạng máy tính. |
| Network Components  | Giải thích vai trò về thiết bị cơ sở hạ tầng mạng máy tính.  | 
| ISP Connectivity Options | Mô tả các tùy chọn kết nối ISP. |

## 2. Clients and Server

> Như thế nào là client? Như thế nào là Server?

Client–Server là mô hình giao tiếp trong đó:
- ***Client*** là bất kỳ thiết bị hoặc chương trình nào gửi request đến một dịch vụ để yêu cầu tài nguyên hoặc xử lý dữ liệu.
- Ngược lại, ***Server*** là hệ thống hoặc tiến trình luôn chạy để lắng nghe request, xử lý chúng và gửi response (như dữ liệu, tài nguyên, thông báo trạng thái) trở lại client.  

> Một thiết bị có thể vừa làm client trong ngữ cảnh này và làm server trong ngữ cảnh khác.

---

## 3. Peer To Peer 

Mô hình Peer To Peer (P2P)?
- Peer To Peer (P2P) hay còn gọi là mạng đồng đẳng, là một mạng máy tính trong đó hoạt động của mạng chủ yếu dựa vào khả năng tính toán và băng thông của các máy tham gia chứ không tập trung vào một số nhỏ các máy chủ trung tâm như các mạng thông thường.

Trong mạng P2P:
- Mỗi thiết bị đều đống vai trò là ***máy khách(Client)*** và ***máy chủ(Server)***
- Các thiết bị có thể chia sẻ **trực tiếp** tài nguyên (như tệp tin, băng thông, sức mạnh xử lý) với nhau mà ***không cần một máy chủ trung tâm để quản lý*** hoặc điều phối.

➡️ Điều này tạo ra một hệ thống phi tập trung (decentralized), khác biệt hoàn toàn với mô hình client-server truyền thống, nơi một máy chủ chuyên dụng cung cấp tài nguyên cho nhiều máy khách.

---

> Mô hình P2P có gì khác so với Client-Server?

| Tiêu chí         | Client–Server             | P2P                               |
| ---------------- | ------------------------- | --------------------------------- |
| Kiến trúc        | Tập trung                 | Phi tập trung                     |
| Vai trò          | Tách biệt Client ↔ Server | Peer vừa là Client, vừa là Server |
| Lưu trữ          | Tập trung                 | Phân tán                          |
| Luồng dữ liệu    | Client ↔ Server           | Peer ↔ Peer                       |
| Điểm lỗi         | Dễ bị lỗi đơn điểm        | Khả năng chịu lỗi tốt             |
| Khả năng mở rộng | Thấp (server dễ quá tải)  | Tốt (thêm peer thì mạnh hơn)      |
| Bảo mật          | Dễ kiểm soát              | Khó kiểm soát                     |
| Chi phí          | Cao (cần server)          | Thấp (tận dụng máy người dùng)    |
| Ví dụ            | Web, Email, Ngân hàng     | BitTorrent, Blockchain            |

## 4. Network Components

Cơ sở hạ tần mạng (The network infrastructure) bao gồm ba thành phần chính:
1. End Devices – thiết bị đầu cuối dùng bởi người dùng.
2. Intermediate Devices – thiết bị trung gian quản lý, định tuyến, bảo vệ mạng.
3. Network Media – môi trường truyền dẫn (dây đồng, cáp quang, sóng vô tuyến).

![Network infrastructure](../../images/Screenshot%202025-11-25%20151858.png)

### 4.1 Network Infrastructure (Thiết bị hạ tầng mạng)

***Thiết bị hạ tầng mạng*** bao gồm các thành **phần vật lý** và **logic** tạo nên một mạng máy tính, như router, switch, modem, điểm truy cập (Access Point), cùng với các thành phần như máy chủ, tường lửa (firewall), cáp mạng và các phần mềm quản lý. Những thiết bị này kết nối với nhau để truyền tải, chia sẻ dữ liệu và cho phép các thiết bị giao tiếp, truy cập internet một cách ổn định và bảo mật. 

>
> Đây là những thiết bị cốt lõi giúp kết nối, định tuyến, quản lý và bảo vệ lưu lượng trong mạng.
>
> Những thiết bị này kết nối với nhau để truyền tải, chia sẻ dữ liệu và cho phép các thiết bị giao tiếp, truy cập internet một cách ổn định và bảo mật.
>

---

| Thiết bị      | Vai trò chính           | Lớp OSI |
| ------------- | ----------------------- | ------- |
| Hub           | Broadcast tín hiệu      | 1       |
| Switch        | Chuyển mạch theo MAC    | 2       |
| Router        | Định tuyến theo IP      | 3       |
| Firewall      | Lọc/bảo vệ lưu lượng    | 3–7     |
| Access Point  | Tạo WiFi                | 2       |
| Modem         | Chuyển đổi tín hiệu ISP | 1       |
| Load Balancer | Phân phối tải           | 4–7     |

### 4.2 End Devices (Thiết bị đầu cuối)

End devices là các thiết bị do người dùng trực tiếp sử dụng hoặc là thiết bị cuối cùng xử lý dữ liệu.

---

| Nhóm               | Ví dụ              | Chức năng                    |
| ------------------ | ------------------ | ---------------------------- |
| Người dùng         | Laptop, điện thoại | Truy cập mạng, chạy ứng dụng |
| IoT                | ESP32, camera      | Gửi/nhận dữ liệu cảm biến    |
| Thiết bị văn phòng | Máy in, máy scan   | Nhận job từ mạng             |

### 4.3 Network Media (Phương tiện truyền dẫn)

Đây là “đường đi” của dữ liệu.

1. Cáp đồng xoắn đôi (Twisted Pair – Ethernet Cable)
    - Cat5e, Cat6, Cat6A
    - Tốc độ: 100 Mbps → 1 Gbps → 10 Gbps
    - Khoảng cách tối đa: ~100m

2. Cáp quang (Fiber Optic)
    - Tốc độ cao hơn (10Gbps → 100Gbps → 400Gbps)
    - Khoảng cách xa hàng chục km
    - Chống nhiễu tuyệt đối
    - Hiện đại nhất và được dùng trong backbone mạng.

3. Sóng vô tuyến (Wireless Media)
    - WiFi
    - Bluetooth
    - 4G/5G
    - Zigbee
    - LoRaWAN

4. Coaxial Cable (Cáp đồng trục)
    - Dùng trong truyền hình cáp và Internet cáp (DOCSIS).

## 5. ISP Connectivity Options

### 5.1 ISP Services (ISPs)

ISP (Internet Service Provider) là ***nhà cung cấp dịch vụ Internet***, chịu trách nhiệm:
- Cung cấp kết nối Internet cho người dùng và doanh nghiệp.
- Cấp phát thiết bị mạng cơ bản (Modem/ONT).
- Quản lý băng thông, hỗ trợ kỹ thuật, bảo trì đường truyền.
- Kết nối hệ thống mạng khu vực của họ với Internet toàn cầu.
➡️ Hiểu đơn giản: ISP là cánh cổng đưa thiết bị của bạn (PC, điện thoại, router…) ra thế giới Internet.

### 5.2 ISP Connections

Các kết nối của ISP, bao gồm:

| Loại Kết Nối           | Công Nghệ      | Tốc Độ                | Độ Ổn Định                     | Phù Hợp Nhất                              |
| ---------------------- | -------------- | --------------------- | ------------------------------ | ----------------------------------------- |
| **Fiber Optic (FTTH)** | Cáp quang      | Rất nhanh (≈1 Gbps+)  | Rất ổn định, trễ thấp          | Gia đình, doanh nghiệp, gaming, streaming |
| **Cable Internet**     | Cáp đồng trục  | Nhanh (50–500 Mbps)   | Ổn định vừa, chậm giờ cao điểm | Nhà có sẵn truyền hình cáp                |
| **DSL / ADSL / VDSL**  | Dây điện thoại | Thấp–TB (24–100 Mbps) | Ổn định thấp khi xa tổng đài   | Nông thôn, nhu cầu cơ bản                 |
| **Cellular (4G/5G)**   | Sóng di động   | 4G: TB / 5G: nhanh    | Dao động theo tín hiệu         | Di động, dự phòng, nơi không có cáp       |
| **Satellite Internet** | Vệ tinh        | TB (25–100 Mbps)      | Trễ rất cao                    | Vùng hẻo lánh, hải đảo                    |

### 5.3 Cable and DSL Connections

1. Cable Internet:
    - Sử dụng cáp coaxial giống hệ thống truyền hình cáp.
    - Tốc độ: trung bình đến cao (100 Mbps – lên đến 1 Gbps).
    - Dễ bị ảnh hưởng bởi số lượng người dùng trong khu vực (shared bandwidth).

2. DSL (Digital Subscriber Line):
    - Chạy trên dây điện thoại xoắn đôi (twisted pair).
    - Không ảnh hưởng đến việc nghe/gọi điện thoại.
    - Tốc độ phụ thuộc vào khoảng cách tới trạm ISP.
    - Các chuẩn:
        - ADSL: tải xuống nhanh hơn tải lên.
        - VDSL: nhanh hơn ADSL, phổ biến tại các khu dân cư.

> So sánh kết nối Cable và DSL

| Tiêu chí      | Cable                        | DSL                           |
| ------------- | ---------------------------- | ----------------------------- |
| Loại cáp      | Coaxial                      | Dây điện thoại                |
| Tốc độ        | Cao (tới 1 Gbps)             | Thấp – Trung bình             |
| Ổn định       | Phụ thuộc người dùng khu vực | Phụ thuộc khoảng cách tới ISP |
| Giá           | Trung bình                   | Rẻ                            |
| Tính phổ biến | Rất phổ biến                 | Giảm dần                      |

### 5.4 Additional Connectivity Options

1. Cellular Internet (3G/4G/5G)
    - Sử dụng mạng di động để truy cập Internet.
    - Ưu điểm:
        - Có thể dùng mọi nơi có sóng di động.
        - Linh hoạt, tiện dụng cho người hay di chuyển.
    - Nhược điểm:
        1. Tốc độ phụ thuộc vào chất lượng sóng.
        2. Bị giới hạn data → vượt gói cước sẽ bị tính phí.

➡️ Rất hữu ích cho người không có cáp/wifi hoặc cần Internet di động.

2. Satellite Internet
    - Kết nối thông qua vệ tinh → phù hợp cho vùng sâu, vùng xa.
    - Yêu cầu: cần tầm nhìn trực tiếp lên bầu trời (không bị che bởi cây, nhà…).
    - Tốc độ: khá tốt, phụ thuộc gói cước.
    - Nhược điểm:
        1. Độ trễ (latency) cao.
        2. Chi phí thiết bị và lắp đặt ban đầu cao.
      
➡️ Giải pháp hữu ích nếu không có DSL, Cable hay Fiber.

3. Dial-up Internet (lỗi thời nhưng vẫn có nơi dùng)
    - Dùng modem và đường dây điện thoại analog.
    - Tốc độ rất thấp (56 Kbps).
    - Ưu điểm: rẻ, chỉ cần đường dây điện thoại cơ bản.
    - Nhược điểm: quá chậm, không dùng được cho ứng dụng hiện đại.

➡️ Chỉ nên sử dụng khi không còn lựa chọn nào khác.
