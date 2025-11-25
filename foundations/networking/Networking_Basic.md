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

> Mối quan hệ giữa client và server dựa trên cơ chế request-response.
> 
> Bất kỳ thiết bị hoặc chương trình đều có thể là client và ngược lại nó đều có thể là server.

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

| Tiêu chí | Mô hình Client-Server (Máy Khách - Máy Chủ) | Mô hình P2P (Ngành Hàng) |
| -------- | ------------------------------------------- | ------------------------ |
| Kiến trúc | Tập trung (Centralized) | Phi tập trung (Decentralized) |
| Vai trò | Có sự phân biệt rõ ràng: Server cung cấp dịch vụ/tài nguyên; Client yêu cầu dịch vụ. | Tất cả các máy (Peer/Node) đều ngang hàng. Mỗi Peer vừa là Client (yêu cầu) vừa là Server (cung cấp). |
| Lưu trữ | Tập trung trên máy chủ. | Phân tán trên các máy ngang hàng. |
| Luồng dữ liệu | Client gửi yêu cầu tới Server. Server xử lý và trả lời về Client. (Client ↔ Server) | Dữ liệu truyền trực tiếp giữa các Peer. (Peer ↔ Peer) |
| Điểm lỗi | "Dễ bị lỗi đơn điểm (Single Point of Failure). Nếu Server lỗi, toàn bộ hệ thống tê liệt." | "Khả năng chịu lỗi cao. Nếu một Peer lỗi, mạng vẫn hoạt động nhờ tài nguyên phân tán." |
| Khả năng mở rộng (Scalability) | "Hạn chế. Khi số lượng Client tăng, Server dễ bị quá tải (Bottleneck)." | "Tốt hơn trong việc chia sẻ tài nguyên. Càng nhiều Peer tham gia, khả năng cung cấp càng mạnh." |
| Bảo mật | "Tốt hơn. Bảo mật, xác thực và quản lý tập trung tại Server." | Kém hơn. Khó kiểm soát và đảm bảo an ninh trên từng Peer. |
| Chi phí | "Cao. Cần đầu tư vào Server mạnh, phần mềm và quản trị viên chuyên nghiệp." | Thấp. Tận dụng tài nguyên máy tính có sẵn. |
| Ứng dụng điển hình | "Web, Email (Gmail/Outlook), Ngân hàng trực tuyến, Cơ sở dữ liệu công ty." | "Chia sẻ tệp (BitTorrent), Tiền điện tử (Blockchain), Một số ứng dụng VoIP." |

## 4. Network Components

Cơ sở hạ tần mạng (The network infrastructure) bao gồm ba thành phần chính:
1. End devices
2. Intermediate devices
3. Network media

![Network infrastructure](../../images/Screenshot%202025-11-25%20151858.png)

### 4.1 Network Infrastructure (Thiết bị hạ tầng mạng)

Đây là những thiết bị cốt lõi giúp kết nối, định tuyến, quản lý và bảo vệ lưu lượng trong mạng.

1. Hub (Bộ chia mạng – lớp 1 OSI)
    - Thiết bị cơ bản nhất.
    - Không thông minh, không hiểu địa chỉ MAC.
    - Khi nhận được dữ liệu → broadcast ra tất cả các cổng.
    - Nhược điểm: dễ gây xung đột (collision), tốc độ chậm.
    - Hub đã lỗi thời trong các mạng hiện đại.

2. Switch (Bộ chuyển mạch – lớp 2 OSI)
    - Thiết bị phổ biến nhất trong mạng LAN.
    - Hiểu và sử dụng địa chỉ MAC để gửi đúng gói tin đến đúng thiết bị.
    - Giảm xung đột, cải thiện tốc độ mạng.
    - Hỗ trợ VLAN, QoS, Spanning Tree…
    - Switch = Phiên bản thông minh hơn và hiện đại hơn nhiều so với Hub.

3. Router (Bộ định tuyến – lớp 3 OSI)
    - Giúp kết nối nhiều mạng khác nhau (LAN ↔ WAN, LAN ↔ Internet).
    - Hiểu địa chỉ IP, định tuyến dựa trên các bảng routing.
    - Có thể cấp IP qua DHCP, NAT/PAT, firewall cơ bản.
    - Router giúp đưa máy tính của bạn ra Internet.

4. Firewall (Tường lửa – lớp 3/4/7)
    - Bảo vệ mạng bằng cách cho phép hoặc chặn lưu lượng theo:
    - IP, port, URL, ứng dụng…
    - Firewall có hai dạng:
    - Hardware Firewall (thiết bị phần cứng)
    - Software Firewall (chạy trong hệ điều hành)

5. Access Point (AP – Điểm truy cập WiFi)
    - Tạo mạng không dây (WiFi) cho các thiết bị kết nối.
    - Có hai loại:
        - Standalone AP (hoạt động độc lập).
        - Controller-based AP (điều khiển tập trung).

6. Modem
    - Chuyển đổi tín hiệu số (digital) ↔ tín hiệu analog từ nhà mạng (ISP).
    - Ví dụ:
        - Modem cáp.
        - Modem quang (ONT – Optical Network Terminal).
        - Hầu hết modem của ISP tích hợp luôn Router & WiFi.

7. Load Balancer
    - Phân phối lưu lượng giữa nhiều server.
    - Giúp giảm tải, tăng khả năng chịu lỗi.

8. Network Server (Trong hạ tầng)
- Các máy chủ chuyên dụng như:
    - DHCP Server (cấp IP)
    - DNS Server (phân giải tên miền)
    - Authentication Server (xác thực người dùng)
    - File Server (lưu trữ)

### 4.2 End Devices (Thiết bị đầu cuối)

End devices là các thiết bị do người dùng trực tiếp sử dụng hoặc là thiết bị cuối cùng xử lý dữ liệu.

1. Máy tính cá nhân (PC/Laptop)
    - Thiết bị phổ biến nhất dùng để truy cập mạng.

2. Điện thoại thông minh (Smartphone)
    - Kết nối WiFi hoặc 4G/5G.

3. Máy chủ (Server)
Cung cấp dịch vụ:
    - Web
    - Database
    - Email
    - Cloud
    - Authentication
    - Máy chủ vừa có thể là thiết bị hạ tầng vừa là thiết bị đầu cuối tùy ngữ cảnh.

4. Máy in mạng (Network Printer)
    - Cho phép in qua LAN hoặc WiFi.

5. IoT Devices (Thiết bị IoT)
- Ví dụ:
    - Camera an ninh
    - Cảm biến
    - Smart TV
    - Smart home devices (đèn, ổ cắm, khóa cửa…)

6. VoIP Phones (Điện thoại IP)
    - Sử dụng mạng để gọi điện thay vì đường dây thoại truyền thống.

7. Access Terminal / Thin Client
    - Dùng trong hệ thống doanh nghiệp, siêu thị, ngân hàng…

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
