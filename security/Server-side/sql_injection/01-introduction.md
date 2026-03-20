# ***SQL INJECTION VULNERABILITY***

## Mục lục

- [1. Tổng Quan về SQL Injection](#1-tổng-quan-về-sql-injection)

- [2. Tác động của tiêm mã thành công là gì?](#2-tác-động-của-tiêm-mã-thành-công-là-gì)

---

## 1. Tổng Quan về SQL Injection

***SQL Injection*** là một kỹ thuật lợi dụng những **lỗ hổng về câu truy vấn** của các ứng dụng. Được thực hiện bằng cách chèn thêm một đoạn SQL để **làm sai lệnh đi câu truy vấn ban đầu**, từ đó có thể khai thác dữ liệu từ database. SQL injection có thể cho phép những kẻ tấn công thực hiện ***các thao tác như một người quản trị web, trên cơ sở dữ liệu của ứng dụng***.

> Tất cả các dữ liệu (trong form đăng nhập, người dùng nhập dữ liệu, trong trường tìm kiếm - người dùng nhập văn bản tìm kiếm hay biểu mẫu,...) đều đi vào cơ sở dữ liệu thì có thể bị SQL Injection.

## 2. Tác động của tiêm mã thành công là gì?

Một cuộc tấn công SQL Injection thành công thường mang lại những tác động không mong muốn như:

- Ăn cắp hoặc sao chép dữ liệu hệ thống.
- Đăng nhập với tài khoản người dùng khác.
- Xóa dữ liệu nhạy cảm, quan trọng của hệ thống.
- Người dùng có thể đăng nhập với tư cách người khác, kể cả quản trị viên.
- Người dùng có thể sửa đổi, thay đổi cấu trúc cơ sở dữ liệu, thậm chí xóa các bảng trong cơ sở dữ liệu ứng dụng.

> Những tác động trên gây ra hệ lụy to lớn đối với cả ứng dụng và người dùng.