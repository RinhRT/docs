# ***SQL INJECTION IN DIFFERENT PARTS OF THE QUERY***

## I. Tiêm mã vào trong các truy vấn

Hầu hết các lỗ hổng SQL Injection đều xuất hiện bên trong mệnh đề **WHERE** của truy vấn **SELECT**. Các chuyên gia kiểm thử (tester) giàu kinh nghiệm thường đã quá quen thuộc với dạng lỗi này.

Tuy nhiên, lỗ hổng SQL Injection có thể **xảy ra ở bất kỳ vị trí nào bên trong truy vấn**, cũng như trong các loại truy vấn khác nhau. Một số vị trí phổ biến khác thường phát sinh lỗi SQLi bao gồm:

- Trong câu lệnh **UPDATE**, nằm ở các ***giá trị được cập nhật hoặc trong mệnh đề WHERE***.
- Trong câu lệnh **INSERT**, nằm trong ***các giá trị được chèn vào***.
- Trong câu lệnh **SELECT**, nằm ở tên ***bảng (table) hoặc tên cột (column)***.
- Trong câu lệnh **SELECT**, nằm ở mệnh đề ***ORDER BY***.

## II. Ví dụ về các lỗi trong truy vấn

### 1. Trong câu lệnh ***UPDATE*** (cập nhật giá trị)

- Lỗi này thường xảy ra ở chức năng "cập nhật thông tin cá nhân" (profile).
- Ví dụ:

    ``` sql
    UPDATE users SET email = '$email_nguoi_dung_nhap' WHERE id = 123
    ```

- Cách khai thác (payloads): tạo payloads là ``` attacker@gmail.com', role='admin ```
- Kết quả câu lệnh trở thành:
    ``` sql
    UPDATE users SET email = 'attacker@gmail.com', role='admin' WHERE id = 123

    // Kẻ tấn công vừa cập nhật được tài khoản của mình vừa được thăng quyền lên quản trị viên (leo thang đặc quyền - Privilege Escalation). 
    ```

### 2. Trong câu lệnh ***INSERT*** (chèn giá trị)

- Thường gặp ở chức năng "Đăng ký tài khoản mới" hoặc "Viết bình luận", "Thêm vào giỏ hàng",...

    Ví dụ với mã nguồn bên dưới đây:
    ``` sql
    INSERT INTO comments (post_id, username, content) VALUES (1, 'Khach', '$noi_dung')
    ```

    - Cách khai thác(Payload): Nhập nội dung bình luận là `Hack!'), (1, 'Khach', 'Spam!`
    - Câu lệnh bị biến đổi: 
    ```sql
    INSERT INTO comments (post_id, username, content) VALUES (1, 'Khach', 'Hack!'), (1, 'Khach', 'Spam!')
    ```
    - Hậu quả: Phá vỡ cấu trúc ngoặc (), cho phép kẻ tấn công chèn nhiều hàng (record) vào cơ sở dữ liệu cùng lúc thay vì chỉ một hàng như ứng dụng dự kiến.

### 3. Trong câu lệnh ***SELECT*** (Tên bảng hoặc Tên cột)
- Xảy ra khi ứng dụng cho phép người dùng chọn trường dữ liệu để hiển thị hoặc xuất file (Ví dụ: "Bạn muốn xuất báo cáo theo cột nào?").
    
    Ví dụ như: 
    ``` sql
    SELECT $ten_cot FROM products
    ```

    - Cách khai thác (Payload): Chọn tên cột là `password FROM users --` 

    - Câu lệnh bị biến đổi: 
    ``` sql
    SELECT password FROM users -- FROM products
    ```
    - Hậu quả: Đoạn phía sau bị vô hiệu hóa bởi dấu `--` . Thay vì lấy dữ liệu sản phẩm, ứng dụng sẽ in ra toàn bộ mật khẩu của bảng users.

### 4. Trong câu lệnh ***SELECT*** (Mệnh đề ORDER BY)
- Trường hợp này rất nguy hiểm và phổ biến ở các bảng dữ liệu cho phép nhấp vào tiêu đề cột để sắp xếp (Sort A-Z). Tại vị trí `ORDER BY`, bạn không thể dùng các lệnh cơ bản như `UNION SELECT`.

    Ví dụ như:
    ``` sql
    SELECT * FROM users ORDER BY $cot_sap_xep
    ```

    - Cách khai thác (Payload): Bạn phải sử dụng kỹ thuật `Boolean-based` bằng lệnh `CASE WHEN`. Truyền vào: `(CASE WHEN (1=1) THEN username ELSE password END)`
    - Câu lệnh bị biến đổi:
    ```sql
    SELECT * FROM users ORDER BY (CASE WHEN (1=1) THEN username ELSE password END)
    ```

    - **Hậu quả**: Nếu `biểu thức đúng (1=1)`, bảng sẽ sắp xếp `theo cột username`. Nếu `biểu thức sai (1=2)`, bảng sắp xếp `theo password`. Bằng cách thay thế 1=1 bằng các câu truy vấn dò đoán (ví dụ: Ký tự đầu tiên của mật khẩu admin có phải là chữ A không?), kẻ tấn công quan sát sự thay đổi thứ tự sắp xếp của trang web để "mò" ra toàn bộ dữ liệu.