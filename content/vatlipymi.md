Title: Học Vật Lý với Python
Date: 2021-07-24
Category: Trang chủ
Tags: python, vật lý, điện, esp8266, IoT, voltage, GPIO
Slug: vatlipymi
Authors: hvnsweeting
Summary: Ôn tập môn điện dùng MicroPython trên ESP8266

Trong không khí toàn dân ở nhà ôn tập môn Vật Lý vào năm Covid-19 thứ 2,
một "thầy giáo Python" cũng không thể giấu nổi tình yêu với môn học của tự nhiên
này và quyết chuyển sang mở lớp ôn tập môn điện.

Sau 30 phút chăm chỉ và tập trung, các học viên sẽ có thể thắp sáng 1 cái
đèn (LED) sử dụng MicroPython trên vi xử lý ESP8266.

![hi]({static}/images/bulb.jpg)

Trong 3 môn học "tự nhiên" của trường phổ thông, Toán được cho là "công thức",
"trừu tượng", "khô khan",
thì Lý, Hóa lẽ ra phải gần hơn với thực hành.
Ở các trường học "dưới xuôi" có điều kiện, được thực hành trong phòng thí nghiệm,
chơi với mô hình,
thì với học sinh miền núi năm 200X chúng tôi, thứ thực hành duy nhất trong
môn Hóa là giấy quỳ tím thả vào axit chuyển sang đỏ,
còn môn Lý chắc là tự bật cái công tắc bóng đèn nhà mình.

Cảnh báo: tác giả không có bằng cấp sư phạm môn Vật Lý, cũng không phải kỹ sư
điện.

Vì là giờ học thực hành, nên học viên cố gắng kiếm thiết bị để làm theo nhé.

## Chuẩn bị dụng cụ
- Một thiết bị vi xử lý ESP 8266 (mức giá < 60.000 VND). Ví dụ [Wemos D1 Mini](https://shopee.vn/M%E1%BA%A1ch-Thu-Ph%C3%A1t-WiFi-ESP8266-Wemos-D1-mini-(NodeMCU-Mini-D1)-c%C3%B3-k%C3%A8m-b%E1%BB%99-Jump-c%E1%BA%AFm-i.106323333.1791339648?position=11)
- Máy tính có Python (tốt nhất là dùng hệ điều hành Ubuntu hay MacOS)
- 1 Điện trở 220 Ohm (1000 VND?)
- 2 dây nối (1000 VND?)
- 1 đèn LED (1000 VND?)
- (Khuyến khích - cho đơn giản) hay mua một bộ kit cơ bản gồm cả 3 thứ trên với
  [giá 95.000 VND](https://www.cytrontech.vn/p-raspberry-pi-pico-basic-kit-without-pico).

## Cài đặt MicroPython lên ESP8266
Làm theo hướng dẫn trong bài [Dùng MicroPython với wifi board ESP-8266]({filename}/micropy.md).

## Mạch điện

Hình vẽ sử dụng [circuit-diagram](https://www.circuit-diagram.org/editor/)

<img src="{static}/images/circuit.svg">

<img src="{static}/images/circuit_h.jpg" width=500>
<img src="{static}/images/circuit_topdown.jpg" width=300>

## Nối mạch
- Cắm 1 dây vào pin ghi chữ G của ESP8266, nối đầu dây còn lại vào 1 đầu của điện trở
- chân còn lại của điện trở nối vào chân ngắn của đèn LED
- chân dài của đèn LED nối vào GPIO Pin 14 của ESP8266. Trên Wemos D1 mini là D5.
- cắm điện cổng USB cho ESP8266.
- bật terminal, kết nối vào ESP8266 qua câu lệnh picocom:

```
sudo picocom /dev/ttyUSB0 --baud 115200
```

Gõ code Python

```py
>>> import machine
>>> machine.freq()
80000000

>>> from machine import Pin
>>> led = Pin(14, Pin.OUT)
>>> led.on()
>>> led.off()
```

Sẽ thấy đèn LED sáng sau khi `led.on()` rồi tắt sau `led.off()`.

<img src="{static}/images/circuit_on.webp" width=300>


## Pin là gì

<img src="https://www.wemos.cc/en/latest/_images/d1_mini_v3.1.0_1_16x16.jpg" width=300>

16 ô tròn nhỏ trong hình là 16 pin của mạch Wemos D1 Mini.

Pin là điểm tiếp xúc kim loại, là nơi để vi xử lý tương tác với bên ngoài (như đọc/ghi "dữ liệu",...)
bật tắt bóng đèn, đọc thông tin từ các sensor (cảm biến) như đo nhiệt độ, ...

Mỗi Pin có chức năng riêng, để biết mỗi mạch có pin nào làm gì, cần tìm tài liệu
của mạch đó (thường ở trang chủ) hoặc trong tài liệu kèm khi bán.
Theo [wemos.cc](https://www.wemos.cc/en/latest/d1/d1_mini.html)

```
+------+------------------------------+--------------+
| Pin  | Function                     | ESP-8266 Pin |
+======+==============================+==============+
| TX   | TXD                          | TXD          |
+------+------------------------------+--------------+
| RX   | RXD                          | RXD          |
+------+------------------------------+--------------+
| A0   | Analog input, max 3.2V       | A0           |
+------+------------------------------+--------------+
| D0   | IO                           | GPIO16       |
+------+------------------------------+--------------+
| D1   | IO, SCL                      | GPIO5        |
+------+------------------------------+--------------+
| D2   | IO, SDA                      | GPIO4        |
+------+------------------------------+--------------+
| D3   | IO, 10k Pull-up              | GPIO0        |
+------+------------------------------+--------------+
| D4   | IO, 10k Pull-up, BUILTIN_LED | GPIO2        |
+------+------------------------------+--------------+
| D5   | IO, SCK                      | GPIO14       |
+------+------------------------------+--------------+
| D6   | IO, MISO                     | GPIO12       |
+------+------------------------------+--------------+
| D7   | IO, MOSI                     | GPIO13       |
+------+------------------------------+--------------+
| D8   | IO, 10k Pull-down, SS        | GPIO15       |
+------+------------------------------+--------------+
| G    | Ground                       | GND          |
+------+------------------------------+--------------+
| 5V   | 5V                           | \-           |
+------+------------------------------+--------------+
| 3V3  | 3.3V                         | 3.3V         |
+------+------------------------------+--------------+
| RST  | Reset                        | RST          |
+------+------------------------------+--------------+
```

## GPIO là gì
General-Purpose Input/Output (GPIO) là khái niệm về mặt logic chứ không phải vật
lý như pin nói trên.

Trong 16 pin của Wemos D1 mini, chỉ có 11 pin được gọi là digital pin D0-D8, G,
RX, TX tương ứng với các GPIO pin.
Chú ý cách đánh số khác nhau giữa pin vật lý (D5) so với GPIO pin (GPIO14),
chúng không có quy luật, để biết chính xác cần tra tài liệu cho từng mạch.

Khi lập trình điều khiển các GPIO pin, có thể đổi chúng ở 2 trạng thái:

- high (on) - điện 3.3V
- low (off) - điện 0V

Pinout là tài liệu liệt kê nối pin trên mạch ứng với GPIO pin nào.

## Resistor - điện trở
Resistor /rɪˈzɪstə/ điện trở, là thứ cản trở dòng điện. Trong bài này dùng để giảm
cường độ dòng điện/hiệu điện thế trước khi gặp đèn LED - tránh cháy nổ. Trên
resistor thường có 4 vạch màu (color band) trở lên với 10 màu để ký hiệu nó có
điện trở bao nhiêu Ω (đơn vị Ohm. Việt sub: ôm).

### Cách đọc vạch màu trên điện trở
Hai vạch đầu đổi trực tiếp ra số, vạch tiếp theo là hệ số nhân, và vạch cuối cùng là
khả năng chịu đựng sai lệch tính theo phần trăm.

Trong bài, sử dụng "đỏ đỏ nâu vàng":

- đỏ(2) đỏ(2) nâu(x10) = 22 * 10 = 220Ω
- vàng = +-5%

Cách nhớ các màu theo tiếng Anh:

> Bad Beer Rots Out Your Guts But Vodka Goes Well – Get Some Now.

- Bad - Black: 0
- Beer - Brown: 1
- Rots - Red: 2
- Out - Orange: 3
- Your - Yellow: 4
- Guts - Green: 5
- But - Blue: 6
- Vodka - Violet: 7
- Goes - Grey: 8
- Well - White: 9

<img src="{static}/images/resistors.jpg" width=600>

## LED là gì
Light-Emitting Diode (LED) - là một Diode (Việt sub: "đi ốt") có khả năng phát
ra ánh sáng. Trong tiếng Việt thường hay gọi là lét, nhưng trong tiếng Anh,
người ta vẫn đọc từng chữ cái L-E-D (Việt sub: eo-l i đi).

LED phát ra ánh sáng nhờ việc electron
trong semiconductor (chất bán dẫn) kết hợp với các hố electron (nguyên tử mà bị
thiếu electron) sinh ra năng lượng ở dạng photon ánh sáng. Được phát minh từ
[1907 nhưng mãi tới 1962](https://en.wikipedia.org/wiki/Light-emitting_diode)
mới được đưa vào sản xuất. Ngày nay LED là công nghệ phát sáng rất quan
trọng được dùng phổ biến để làm bóng đèn,

[Năm 2014, giải Nobel Vật Lý được trao cho nhóm phát minh ra LED ánh sáng xanh lam (blue)](https://www.nobelprize.org/prizes/physics/2014/summary/).


### Các loại bóng đèn

- Bóng đèn dây tóc - loại bóng đèn đầu tiên trên thế giới, được phát minh đồng thời
[bởi Joseph Swan và Edison năm 1879](https://en.wikipedia.org/wiki/Edison_light_bulb),
dùng điện làm nóng dây tóc dẫn tới phát sáng.
- Đèn tuýp / đèn huỳnh quang (Fluorescent Lamp): đèn tuýp tên tiếng Anh là
Tubelight - nói đến hình dạng cái ống của nó. Nếu ngày nay
dịch như ngày xưa, ta sẽ lên `Diu Tuýp` để xem clip. Loại đèn này sử dụng bột
phốt pho để phát sáng khi có các ánh sáng cực tím va vào. Ánh sáng cực tím
được tạo ra bằng cách phóng điện vào khí trơ (như Argon/Neon) làm thủy ngân bay hơi.
Đèn huỳnh quang có chứa thủy ngân, rất độc hại khi thải ra môi trường.
- Bóng đèn compact: compact tiếng Anh nghĩa là thu gọn/chặt lại. Cái tên được
giữ 1 phần gốc tiếng Anh, tên đầy đủ là compact fluorescent lamp (CFL). Về
mặt nguyên lý vẫn là đèn huỳnh quang, nhưng nhỏ gọn, cho hiệu năng cao hơn,
hay tiết kiệm điện hơn.
- Bóng đèn LED: bóng đèn sử dụng các LED để tạo ánh sáng trắng thay các công
nghệ nói trên. Đây là công nghệ hiện đại nhất ngày này: tiết kiệm, hiệu quả,
ít hại môi trường. LED là công nghệ, nó có thể thay thế cho đèn huỳnh quang và
đóng vai 1 bóng đèn tuýp, hay thay đèn dây tóc như bóng đèn tròn.

LED thường có 2 chân, chân dài là anode (đầu dương +), và chân ngắn là cathode
(đầu âm -).

## Điện hoạt động thế nào ở đây
<img src="{static}/images/circuit.svg">

Khi code `led.on()` chạy xong, ESP8266 đặt hiệu điện thế 3.3V tại GPIO14 (Pin D5),
dòng điện chạy qua chân + của LED, qua chân - tới điện trở rồi theo dây nối
tới pin G (ground - nối đất, điện thế là ~0V). Chiều dòng điện ngược với chiều của electron.
Các electron chạy từ G qua điện trở R, giảm điện thế hai đầu LED, election qua
LED làm phát sáng LED, rồi tới GPIO14.

## Các câu hỏi vật lý

### Voltage - hiệu điện thế
Hiệu điện thế (hay điện áp) - ký hiệu ở Việt Nam là U, ký hiệu bên tây là V.
Đơn vị: **volt** - ký hiệu **V**.

Hiệu là kết quả của phép trừ, ở đây chỉ độ chênh lệch về điện thế,
hay "áp lực".

### Current - cường độ dòng điện
Cường độ dòng điện - ký hiệu là I.
Đơn vị: **ampere** - ký hiệu **A**.

Cường độ là độ mạnh của dòng điện.

### Ohm's law - định luật Ohm
Khi qua vật dẫn điện, hiệu điện thế và cường độ dòng điện tỷ lệ thuận với nhau.

```
I = V/R
```
hay

```
R = V/I
```
tỷ lệ này gọi là "resistance" (điện trở) của vật dẫn điện, ký hiệu chữ R
là từ đây ra.

```
1 Ohm = 1 Volt / 1 Ampere.
```

Thứ khái niệm kiểu tỷ lệ như này khá phổ biến trong Vật Lý, như

```
vận tốc = quãng đường / thời gian
1 m/s = 1m / 1s
```

Ba khái niệm này có thể hình dung như một thác nước chảy từ trên cao xuống (U),
và vào đá giữa dòng (R) mà giảm tốc độ (I).

Trong điện dùng hàng ngày, các thiết bị điện hầu hết có điện trở R cố định,
nên khi U lớn thì I cũng sẽ lớn theo (tỷ lệ thuận).

### Công thức
Trong mạch mắc nối tiếp, I không đổi tại mọi điểm.

```
V = I*R + I*R_led
V = V1 + I*R_led
```

Như vậy việc cho điện trở 220 Ohm vào nhằm giảm hiệu điện thế cho LED.
Cụ thể:

```
3.3V = I*220 + I*R_led
```

### Không dùng điện trở có sao không?
Thứ phá hỏng thiết bị điện khi cắm nhầm thiết bị 110V vào điện 220V là do hiệu
điện thế (như 1 loại áp lực) của dòng cao hơn của thiết bị có thể chịu được.
Cường độ dòng điện không phải là nguyên nhân.

### Điện trong nhà mắc nối tiếp hay song song
Khi mắc song song, V không đổi tại mọi điểm.
V là thứ quan trọng nhất khi nói về dòng điện, vậy nên các thiết bị trong nhà
nối song song để có V như nhau - như được cấp (220V).
Thiết bị này không bị tụt áp V khi dùng thiết bị khác.

### Đấu ngược chân LED có sao không?
LED không chịu được voltage ngược, nên cũng sẽ cháy.

## Kết luận

Việc học tập, ngoài mục tiêu thu nhận "kiến thức", thì phải vui, không vui học
làm sao vào?
Ngày nay, người học đi học như gánh nặng, người dạy đi dạy như cho xong, trả
bài. Chẳng còn thấy mấy ai nói "đi học cho vui", "vui được đi học" nữa.

Nếu ngày càng có nhiều giáo viên mang lại hứng thú với môn Vật Lý như trên
mạng những ngày qua, tôi tin rằng một ngày không xa, ở Việt Nam, người người
nói về Vật Lý, ăn Vật Lý, ngủ Vật Lý (như người Nga trong [The Queen's
Gambit](https://www.imdb.com/title/tt10048342/) mê
chơi cờ vua) thì chẳng bao lâu nữa, Việt Nam sẽ trở thành một cường quốc Vật Lý,
[giỏi cả lý
thuyết](https://vnexpress.net/viet-nam-gianh-ba-huy-chuong-vang-olympic-vat-ly-quoc-te-4329711.html)
lẫn thực hành như trên các khẩu hiệu. Phóng lên trời, bay qua
Sao Hỏa, bỏ lại xa đằng sau cả Mỹ lẫn Tàu...

## Đọc bài viết tôi không thấy vui
Vì là môn thực hành, nên bạn phải tận tay cắm mạch, thấy bóng đèn sáng, làm cháy
LED khói mù mịt nổ văng tung tóe mới cảm nhận được cảm giác thỏa mãn này.

Khó có thể có cảm giác gì khi đọc "lý thuyết đánh đàn" hay "các bước nấu bún
giả cầy".

## Học thêm
Nếu có đam mê về phần cơ học, con lắc, điện xoay chiều, vũ trụ, lượng tử, ...
hay tất tần tật Vật Lý phổ thông, hãy tham gia lớp học miễn phí của
cô [VatliMinhThu](https://www.facebook.com/VatliMinhThu/) nhé!

## Tham khảo
- https://electronics.stackexchange.com/a/20689
- https://www.raspberrypi.org/documentation/usage/gpio/
- https://www.arduino.cc/en/reference/board
- [Color band system](https://en.wikipedia.org/wiki/Electronic_color_code#Resistor_code)
- [Mạch nối tiếp và song song](https://vi.wikipedia.org/wiki/M%E1%BA%A1ch_n%E1%BB%91i_ti%E1%BA%BFp_v%C3%A0_song_song)

## Hết
HVN at [http://pymi.vn](http://pymi.vn) and [https://www.familug.org](https://www.familug.org).

- [Ủng hộ tác giả 🍺](https://www.familug.org/p/ung-ho.html)
