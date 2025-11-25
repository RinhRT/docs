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
- End devices
- Intermediate devices
- Network media

![Network infrastructure](../../images/Screenshot%202025-11-25%20151858.png)

### 4.1 End devices
