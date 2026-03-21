# ***SQL INJECTION VULNERABILITY***

## Mục lục

- [1. Tổng Quan về SQL Injection](#1-tổng-quan-về-sql-injection)

- [2. Tác động của tiêm mã thành công là gì?](#2-tác-động-của-tiêm-mã-thành-công-là-gì)

---

## 1. Tổng Quan về SQL Injection

***SQL Injection (SQLi)*** là một kỹ thuật tấn công ứng dụng web thông qua việc lợi dụng các lỗ hổng trong khâu **xử lý dữ liệu đầu vào**. Kẻ tấn công sẽ chèn (inject) các đoạn mã SQL độc hại vào các trường nhập liệu của người dùng, nhằm **thay đổi cấu trúc và logic của câu truy vấn ban đầu**.

Khi khai thác thành công, kẻ tấn công có thể tương tác trực tiếp với cơ sở dữ liệu (Database) ở backend, cho phép họ vượt qua các cơ chế xác thực và thực hiện các thao tác với quyền hạn của một quản trị viên cơ sở dữ liệu.

> ***Lưu ý***: Bất kỳ điểm tiếp nhận dữ liệu nào từ phía người dùng (form đăng nhập, thanh tìm kiếm, URL parameters, HTTP headers...) nếu được ghép trực tiếp vào câu lệnh SQL mà không qua quá trình làm sạch (sanitization) hoặc tham số hóa (parameterization) đều có nguy cơ dính lỗ hổng SQL Injection.

## 2. Tác động của tiêm mã thành công là gì?

Một cuộc tấn công SQL Injection thành công không chỉ dừng lại ở phạm vi cơ sở dữ liệu, mà còn mang lại những hậu quả tàn khốc cho toàn bộ hệ thống:

- **Đánh cắp dữ liệu (Confidentiality):** Trích xuất các thông tin nhạy cảm như mật khẩu người dùng, thông tin thẻ tín dụng, tài liệu nội bộ.
- **Sửa đổi dữ liệu (Integrity):** Thay đổi số dư tài khoản, giả mạo thông tin, hoặc chèn mã độc vào nội dung trang web.
- **Phá hoại dữ liệu (Availability):** Xóa bỏ các bản ghi quan trọng, thậm chí xóa toàn bộ các bảng (Drop tables) gây ngưng trệ ứng dụng.
- **Vượt qua xác thực (Bypass Authentication):** Đăng nhập trái phép dưới tư cách của người dùng khác hoặc quyền Quản trị viên cao nhất (Admin).
- **Thực thi mã từ xa (RCE):** Trong nhiều trường hợp, SQLi cho phép kẻ tấn công đọc/ghi file trên máy chủ, hoặc thực thi các lệnh hệ điều hành (OS Commands), dẫn đến việc chiếm quyền điều khiển toàn bộ máy chủ (Server Takeover).

---

<p align="right" style="padding-top: 60px">
    <a href="./02-detect_SQL_injection_vulnerabilities.md">Bài tiếp theo: Phát hiện lỗ hổng SQL Injection</a>
</p>