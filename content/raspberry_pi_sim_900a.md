Title: Dùng Raspberry Pi để gửi và nhận SMS với Sim900A

Date: 2018-10-09

Category: Trang chủ

Tags: raspberry, pi, sim, 900a, sms

Slug: raspberry-pi-sim900a

Author: tudoanh

Summary: Hướng dẫn kết nối module Sim900A với Raspberry Pi 3 B+, dùng để gửi và nhận tin nhắn SMS

Dạo này vì lý do công việc nên cần phải tìm cách kết nối và sử dụng module Sim900A với con Raspberry Pi 3, dùng để nhận SMS.  

Tìm hiểu mấy hôm, rất là cực nên hôm nay mình viết lại bài này, cho những ai cần tới sau này đỡ tốn thời gian mày mò lại từ đầu.  

### Chuẩn bị

Để bắt đầu, bạn cần:  

- Một combo **Raspberry Pi 3 B+** đầy đủ nguồn, thẻ nhớ, đã cài đặt **Raspbian** 
- Một module **Sim900A**

![http://bizweb.dktcdn.net/100/048/138/products/sim900a.jpg?v=1485443752007](http://bizweb.dktcdn.net/100/048/138/products/sim900a.jpg?v=1485443752007)

- Đầy đủ dây nối

  ![https://i.imgur.com/C40X3gs.png](https://i.imgur.com/C40X3gs.png)

### Kết nối

Chỉ cần bạn kết nối đúng các cổng Tx, Rx, Gnd và nguồn 5v vào Pi là xong. Tham khảo ảnh dưới:

![https://i.ytimg.com/vi/louSyBRkvO4/maxresdefault.jpg](https://i.ytimg.com/vi/louSyBRkvO4/maxresdefault.jpg)



Ảnh thực tế:

![https://i.imgur.com/KRanp3y.jpg](https://i.imgur.com/KRanp3y.jpg)

![https://i.imgur.com/dQhoN8e.jpg](https://i.imgur.com/dQhoN8e.jpg)



### Cài đặt

Đầu tiên ta cần mở cổng **ttyS0** 

Bạn có thể dùng "raspi-config" để mở UART:

1. Trong "Interfacing Options", chọn "Serial"
2. Chọn "No" khi được hỏi "You want a login shell over serial?".
3. Chọn "Yes" khi được hỏi "You want the hardware enabled?"
4. Khởi động lại

Thực ra, bạn có thể sửa file */boot/config.txt* và sửa **enable_uart=1**, và **console=serial0,115200** (hoặc **console=ttyS0,115200**) ở trong */boot/cmdline.txt*



Và bạn có thể bật *terminal* lên và test xem kết nối thành công chưa bằng cách gửi command **AT\r\n** đến khi nào trả về **OK** là thành công.

Ví dụ:

![https://i.imgur.com/59K45tV.png](https://i.imgur.com/59K45tV.png)



Link asciinema:

https://asciinema.org/a/U3oPOg0vX4CZ5u3mWTTIr0FTS

Sau đó bạn có thể gửi và đọc tin nhắn bằng lib mình đã viết ở đây (Ví dụ cách sử dụng ở trong link):

https://github.com/tudoanh/sim900a

Chúc các bạn thành công.