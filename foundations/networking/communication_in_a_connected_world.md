# Communication in a Connected World

## Network types

> "Network types" có thể hiểu là các loại mạng máy tính dựa trên phạm vi, phương tiện truyền dẫn hoặc cấu trúc.

### Local Network

***Local Network*** (Mạng cục bộ) là một hệ thống mạng máy tính được sử dụng để kết nối các thiết bị (như máy tính, máy in, điện thoại thông minh, máy chủ,...) trong một phạm vi địa lý nhỏ và giới hạn. Phạm vi này thường là:
- Trong một ngôi nhà hoặc căn hộ.
- Trong một văn phòng hoặc tòa nhà.
- Trong một khuôn viên trường học hoặc trung tâm dữ liệu.

> Mục đích chính của Mạng LAN là cho phép các thiết bị này giao tiếp với nhau để chia sẻ dữ liệu và tài nguyên.

## Data transmission

### Type of Personal Data

***Personal data*** có thể hiểu là **thông tin cá nhân** hoặc là **thông tin dạng cá nhân**(personally identifiable information), là bất kỳ thông tin liên quan đến một người mà có thể nhận dạng được.

Phân loại dữ liệu:
1. Dữ liệu ***"thông thường"*** (Non-sensitive):
  - Bao gồm những thông tin có khả năng nhận diện cá nhân nhưng ***không nằm trong*** nhóm cực kỳ ***nhạy cảm***. 
  - Ví dụ: tên, địa chỉ email, số điện thoại, địa chỉ nhà, IP address.

2. Dữ liệu ***"nhạy cảm"*** (Sensitive / Special categories):
  - Một số luật bảo hộ dữ liệu đặt ra nhóm dữ liệu cần bảo vệ cao hơn do **khả năng gây tổn hại lớn nếu bị lộ**. Ví dụ theo ICO và GDPR:
    - Chủng tộc hoặc nguồn gốc sắc tộc 
    - Quan điểm chính trị, tôn giáo hoặc triết lý 
    - Thành viên công đoàn 
    - Dữ liệu di truyền (genetic data) 
    - Dữ liệu sinh trắc học dùng để xác định danh tính (biometric) 
    - Dữ liệu sức khỏe, đời sống tình dục/thuộc tính tình dục
    - ...

### Common Methods of Data Transmission

#### Tín hiệu và Phương tiện Truyền thông Mạng

Sau khi dữ liệu được **chuyển đổi thành** một chuỗi các ***bit***, nó phải được biến đổi thành các tín hiệu có thể được gửi qua **phương tiện truyền thông mạng** (**network media**) đến đích của nó. Phương tiện truyền thông (**Media**) đề cập đến môi trường vật lý mà trên đó các tín hiệu được truyền đi.

Các ví dụ về phương tiện truyền thông là:
* Dây đồng (**copper wire**),
* Cáp quang (**fiber-optic cable**),
* Sóng điện từ (**electromagnetic waves**) truyền qua không khí.

---

#### Cấu tạo và Hành trình của Tín hiệu

Một tín hiệu (**A signal**) bao gồm các mô hình điện (**electrical patterns**) hoặc quang học (**optical patterns**) được truyền từ thiết bị được kết nối này sang thiết bị khác. Các mô hình này đại diện cho các bit kỹ thuật số (**digital bits**) (tức là dữ liệu) và di chuyển qua phương tiện truyền thông (**media**) từ nguồn đến đích dưới dạng:

* Một chuỗi các xung điện (**pulses of electricity**),
* Các xung ánh sáng (**pulses of light**),
* Hoặc sóng vô tuyến (**radio waves**).

Tín hiệu có thể được chuyển đổi nhiều lần trước khi cuối cùng đến đích, do phương tiện truyền thông (**media**) tương ứng thay đổi giữa nguồn và đích.

---

#### 3 Phương pháp Truyền tín hiệu Phổ biến

Có ba phương pháp truyền tín hiệu (**signal transmission**) phổ biến được sử dụng trong mạng:

* ***Tín hiệu Điện*** (**Electrical signals**) - Việc truyền tải đạt được bằng cách biểu diễn dữ liệu dưới dạng các xung điện (**electrical pulses**) trên dây đồng.
* ***Tín hiệu Quang*** (**Optical signals**) - Việc truyền tải đạt được bằng cách chuyển đổi các tín hiệu điện thành các xung ánh sáng (**light pulses**).
* ***Tín hiệu Vô tuyến*** (**Wireless signals**) - Việc truyền tải đạt được bằng cách sử dụng sóng hồng ngoại (**infrared**), vi sóng (**microwave**), hoặc sóng vô tuyến (**radio waves**) truyền qua không khí.