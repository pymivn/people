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

  ![https://i.imgur.com/vvIy62p.jpg](https://i.imgur.com/vvIy62p.jpg)

- Dây chuyển đổi USB - UART PL2303 (Có thể không có)

  ![https://i.imgur.com/wWkr422.jpg](https://i.imgur.com/wWkr422.jpg)

- Đầy đủ dây nối

  ![https://i.imgur.com/C40X3gs.png](https://i.imgur.com/C40X3gs.png)

### Kết nối

Chỉ cần bạn kết nối đúng các cổng *Tx, Rx, Gnd và nguồn 5v* vào Pi là xong. Tham khảo ảnh dưới:

![https://i.ytimg.com/vi/louSyBRkvO4/maxresdefault.jpg](https://i.ytimg.com/vi/louSyBRkvO4/maxresdefault.jpg)



Ảnh thực tế (Nếu kết nối thẳng vào GPIO)

![https://i.imgur.com/KRanp3y.jpg](https://i.imgur.com/KRanp3y.jpg)

![https://i.imgur.com/dQhoN8e.jpg](https://i.imgur.com/dQhoN8e.jpg)



Còn nếu kết nối qua USB

![https://i.imgur.com/2DHsQCx.jpg](https://i.imgur.com/2DHsQCx.jpg)

### Cài đặt

Đầu tiên ta cần mở cổng **ttyS0**

Bạn có thể dùng "raspi-config" để mở UART:

![https://i.imgur.com/NVchkKl.png](https://i.imgur.com/NVchkKl.png)

1. Trong "Interfacing Options", chọn "Serial"
2. Chọn "No" khi được hỏi "You want a login shell over serial?".
3. Chọn "Yes" khi được hỏi "You want the hardware enabled?"
4. Khởi động lại

Thực ra, bạn có thể sửa file */boot/config.txt* và sửa **enable_uart=1**, và **console=serial0,115200** (hoặc **console=ttyS0,115200**) ở trong */boot/cmdline.txt*



Và bạn có thể bật *terminal* lên và test xem kết nối thành công chưa bằng cách gửi command **AT\r\n** đến khi nào trả về **OK** là thành công. (Nếu kết nối qua GPIO thì sẽ là **/dev/ttyS0**, còn qua USB thì sẽ là **/dev/ttyUSB0**)

Ví dụ:

![https://i.imgur.com/59K45tV.png](https://i.imgur.com/59K45tV.png)



Link asciinema:

[![asciicast](https://asciinema.org/a/U3oPOg0vX4CZ5u3mWTTIr0FTS.png)](https://asciinema.org/a/U3oPOg0vX4CZ5u3mWTTIr0FTS)

Sau đó bạn có thể gửi và đọc tin nhắn bằng lib mình đã viết ở đây (Ví dụ cách sử dụng ở trong link):

https://github.com/tudoanh/sim900a

Ví dụ về kết quả nhận được bằng lệnh **AT+CNMI=3,2,0,0,0**

![https://i.imgur.com/ecz65hk.png](https://i.imgur.com/ecz65hk.png)

Về chi tiết cách sử dụng các lệnh AT và các khái niệm GPIO, UART mình sẽ để sang một bài khác.

Chúc các bạn thành công.



Tham khảo:

1. https://pinout.xyz/
2. http://mlab.vn/9216-huong-dan-lap-trinh-module-sim900a-va-arduino.html
3. https://www.developershome.com/sms/checkCommandSupport3.asp
4. https://raspberrypi.stackexchange.com/questions/82696/how-do-i-connect-gsm-sim-900a-to-a-raspberry-pi-3
5. https://www.espruino.com/datasheets/SIM900_AT.pdf
6. https://hristoborisov.com/index.php/projects/turning-the-raspberry-pi-into-a-sms-center-using-python/#Connecting_the_3gModem

