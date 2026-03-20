# DETECT SQL INJECTION VULNERABILITIES

## Mục lục

- [1. Làm như thế nào để phát hiện lỗ hổng SQL Injection?](#1-làm-như-thế-nào-để-phát-hiện-lỗ-hổng-sql-injection)

## 1. Làm như thế nào để phát hiện lỗ hổng SQL Injection?

Việc kiểm tra lỗ hổng này đôi khi rất dễ dàng. Đôi khi ta chỉ cần nhập **'** hoặc **"** vào ô nhập dữ liệu. Sau đấy chờ phản hồi từ phía ứng dụng. Nếu không trả về bất kỳ phản hồi hay thông báo, ta ngầm hiểu lỗi SQL Injection tồn tại ở điểm đấy. 

Khái quát quá trình kiểm thử thủ công sẽ bao gồm:

- Nhập ký tự ***nháy đơn*** **'** hoặc ***nháy kép*** **"** : Đây là cách kiểm tra đơn giản nhất. Nếu ứng dụng không sử lý kỹ, nó sẽ làm phá vỡ câu lệnh SQL.
  > Ví dụ như "http://urldemo321.xyz/?id=123"
  
  ``` php
  //Mã nguồn máy chủ:

  $id = $_GET['id'];
  // Lấy trực tiếp $id từ URL ghép vào chuỗi SQL
  $sql = "SELECT username, email FROM users WHERE id = '$id'"; 
  $result = $conn->query($sql);

  if (!$result) {
    // Hiển thị trực tiếp lỗi của Database ra màn hình
    die("Lỗi truy vấn: " . $conn->error); 
  }
  ```
  > Cách thực hiện: chèn thêm dấu nháy đơn vào url. 
  >
  > Ta được url như thế này: http://urldemo321.xyz/?id=123%27

---

- Thử cú pháp SQL thay đổi giá trị.
- Thử điều kiện boolean (**or 1=1** hoặc **or 1=2**), và quan sát sự khác biệt trong phản hồi của ứng dụng.
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

  ``` powershell
  curl -X POST http://urldemo321.xyz/login --data-urlencode "username=administrator ' OR 1=1 --" -d "password=123456789" -v
  ```
  > **-X POST**: Đây là hành động gửi dữ liệu. (-d cũng ngầm hiểu là POST).
  >
  > **--data-urlencode**: Đảm bảo payload SQLi của bạn được gói gém cẩn thận, không bị vỡ định dạng khi đi qua môi trường mạng.
  >
  > **-v (Verbose)**: Hiện thị đầy đủ thông tin, dành cho debug.

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
  curl -X POST http://urldemo321.xyz/subscribers --data-urlencode "email=test@gmail.com' OR SLEEP(5) --" -v
  ```

  - Cách 2: dùng sqlmap
  ``` bash
  sqlmap -u "http://urldemo321.xyz/subscribe" --data="email=test@gmail.com" --technique=T --dbs
  ```
  > (Cờ --technique=T chỉ định cho SQLMap biết: "Hãy chỉ dùng phương pháp Time-based (độ trễ thời gian) để tấn công trang web này").

---

- Thử OAST ***(Out-of-band Application Security Testing)***: Kỹ thuật này dùng cho các ***trường hợp đặc biệt "mù"*** (không báo lỗi, không đổi nội dung, không phản hồi chậm). Bạn chèn một đoạn mã ép cơ sở dữ liệu tự động tạo một kết nối mạng ra bên ngoài (ví dụ: truy vấn DNS đến một máy chủ do bạn kiểm soát). Nếu máy chủ của bạn nhận được tín hiệu kết nối, nghĩa là SQLi đã được thực thi thành công.