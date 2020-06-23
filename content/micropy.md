Title: Dùng MicroPython với wifi board ESP-8266
Date: 2018-10-21
Category: Trang chủ
Tags: micropython, embedded, esp8266, iot
Slug: micropython
Authors: hvnsweeting
Summary: Chạy code Python trên thiết bị với chỉ 96KB RAM và 4MB bộ nhớ flash.

Khi trở thành một trong những ngôn ngữ lập trình phổ biến nhất thế giới,
Python không chỉ được dùng trong làm web, data science, hay sysadmin tool mà
nó còn đá sang cả một lĩnh vực vốn giới hạn về tài nguyên: nhúng.

Bình thường khi bật Python lên để in ra màn hình dòng "hello, world" ta đã
dùng tới 8MB bộ nhớ. Vậy nên việc dùng Python cho lập trình nhúng thường nghe
có vẻ không phù hợp.

[MicroPython](http://micropython.org) ra đời, là một bản thu gọn của Python, tối ưu chạy trên các vi xử
lý cũng như các môi trường giới hạn về tài nguyên.
Bài này khám phá việc chạy MicroPython trên một thiết bị tí hon
có tên WEMOS D1 mini.

## WEMOS D1 mini

Là 1 bảng mạch điện có khả năng thu phát sóng wifi (wifi board) có kích thước
nhỏ hơn ngón chân cái của người lớn, thiết bị này có giá 2 USD.

![WEMOS D1 Mini]({static}/images/wemos1.jpg)

Bảng mạch này sử dụng vi điều khiển (microcontroller) ESP-8266, với xung nhịp
80MHz/160MHz, 96KB RAM và 4 MB Flash.

### Microcontroller

> A microcontroller is a small computer on a single integrated circuit. In modern
terminology, it is similar to, but less sophisticated than, a system on a chip
or SoC; an SoC may include a microcontroller as one of its components. A
microcontroller contains one or more CPUs along with memory and programmable
input/output peripherals.

Một vi điều khiển là một máy tính nhỏ, trên một mạch điện tử (P/S: SoC là khái
        niệm tương tự, nhưng phức tạp hơn). Nó có một hoặc nhiều CPU, memory và
chỗ để thực hiện vào ra dữ liệu.

Hãy nhìn vào chiếc máy bàn hay laptop bạn đang dùng, nó có 1 cục CPU to bằng
lòng bàn tay, vài thanh RAM dài như bàn tay, các cổng vào ra đều to bằng ngón
tay. Mỗi cục CPU đều từ 2-3 GHz (so với 80MHz), ổ cứng vài trăm GB (so với 4MB),
1-16 GB RAM (so với 96KB RAM).
Ta sẽ thấy microcontroller nhỏ bé và "yếu ớt" đến chừng nào.

![WEMOS D1 Mini]({static}/images/esp8266.jpg)

### MicroPython

Phiên bản Python dành riêng cho các thiết bị tí hon này nhỏ tới mức chỉ cần
256kB không gian chứa code, và 16kB RAM.

## Cài đặt MicroPython lên WEMOS D1 Mini trên Ubuntu 16.04

(Windows hay OSX cần cài driver, hãy lên trang chủ của WEMOS để tải và xem
 hướng dẫn).

Cắm thiết bị vào máy tính sử dụng dây micro USB (dây sạc điện thoại android),
sẽ thấy nháy đèn trên thiết bị, gõ lệnh `dmesg` để xem Linux kernel báo nhận
thiết bị:

```
$ dmesg
...
[  992.253009] usb 2-1: new full-speed USB device number 5 using xhci_hcd
[  992.402181] usb 2-1: New USB device found, idVendor=1a86, idProduct=7523
[  992.402185] usb 2-1: New USB device strings: Mfr=0, Product=2, SerialNumber=0
[  992.402187] usb 2-1: Product: USB2.0-Serial
[  992.402757] ch341 2-1:1.0: ch341-uart converter detected
[  992.403119] usb 2-1: ch341-uart converter now attached to ttyUSB0
```

```
$ file /dev/ttyUSB0
/dev/ttyUSB0: character special (188/0)
```

Ta có thấy xuất hiện 1 file mới gọi là `/dev/ttyUSB0`, đây chính là thiết bị
vừa kết nối.

### Cài đặt MicroPython sử dụng esptool

Cài đặt esptool dùng pip:

```
$ pip install esptool
Collecting esptool
...
Successfully installed ecdsa-0.13 esptool-2.5.1 pyaes-1.6.1 pyserial-3.4
```

Xóa nội dung hiện tại trong flash memory

```
$ sudo /home/hvn/py36/bin/esptool.py --port /dev/ttyUSB0 erase_flash
esptool.py v2.5.1
Serial port /dev/ttyUSB0
Connecting....
Detecting chip type... ESP8266
Chip is ESP8266EX
Features: WiFi
MAC: b4:e6:2d:3b:22:1b
Uploading stub...
Running stub...
Stub running...
Erasing flash (this may take a while)...
Chip erase completed successfully in 1.6s
Hard resetting via RTS pin...
```

Tải MicroPython bản dành cho ESP8266: bản mới nhất tại thời điểm viết bài
http://micropython.org/resources/firmware/esp8266-20180511-v1.9.4.bin

Ghi micropython lên flash memory:

```
$ sudo /home/hvn/py36/bin/esptool.py --port /dev/ttyUSB0 --baud 460800 write_flash --flash_size=detect -fm dio 0 ~/esp8266-20180511-v1.9.4.bin
esptool.py v2.5.1
Serial port /dev/ttyUSB0
Connecting....
Detecting chip type... ESP8266
Chip is ESP8266EX
Features: WiFi
MAC: b4:e6:2d:3b:22:1b
Uploading stub...
Running stub...
Stub running...
Changing baud rate to 460800
Changed.
Configuring flash size...
Auto-detected Flash size: 4MB
Flash params set to 0x0240
Compressed 604872 bytes to 394893...
Wrote 604872 bytes (394893 compressed) at 0x00000000 in 9.0 seconds (effective 536.4 kbit/s)...
Hash of data verified.

Leaving...
Hard resetting via RTS pin...
```

Sau khi cài đặt xong, bấm nút "reset" trên thiết bị để khởi động lại, ngay sau
đó bật WIFI của laptop hay điện thoại lên ta sẽ thấy một mạng WIFI có tên
`MicroPython-xxxxxx`, có thể kết nối vào WIFI này với password `micropythoN`.
Ở đây ta không cần làm việc này. Tiếp tục cài đặt để kết nối với thiết bị qua
cổng COM:

Cài `picocom`:

```
$ sudo apt install -y picocom
$ sudo picocom /dev/ttyUSB0 --baud 115200
picocom v1.7

port is        : /dev/ttyUSB0
flowcontrol    : none
baudrate is    : 115200
parity is      : none
databits are   : 8
escape is      : C-a
local echo is  : no
noinit is      : no
noreset is     : no
nolock is      : no
send_cmd is    : sz -vv
receive_cmd is : rz -vv
imap is        :
omap is        :
emap is        : crcrlf,delbs,

Terminal ready

>>> 2**1000
10715086071862673209484250490600018105614048117055336074437503883703510511249361224931983788156958581275946729175531468251871452856923140435984577574698574803934567774824230985421074605062371141877954182153046474983581941267398767559165543946077062914571196477686542167660429831652624386837205668069376
```

Sau khi kết nối, ta lập tức sử dụng Python interpreter như bình thường.

Python interpreter đóng vai trò như 1 hệ điều hành ở đây, mỗi lần reset thiết bị,
nó sẽ lại bật lại Python interpreter.
Mọi tương tác với thiết bị (đọc/ghi file) đều thực hiện qua code python.

```
>>> import os
>>> os.getcwd()
    '/'
>>> os.listdir()
['boot.py', 'main.py']
```

Hai file này được chạy mỗi lần thiết bị khởi động.

Xem nội dung file `boot.py`:

```python
>>> f = open('boot.py')
>>> print(f.read())
# This file is executed on every boot (including wake-boot from deepsleep)
#import esp
#esp.osdebug(None)
    import gc
#import webrepl
#webrepl.start()
    gc.collect()
```

File `main.py` chứa code của người dùng muốn chạy mỗi lần bật thiết bị. Ví dụ ta muốn hiển thị dòng hello PyMi:

```python
>>> f = open('main.py', 'wt')
>>> f.write('print("Hello Pymi.vn")')
22
>>> f.close()
```

Bấm nút reset sẽ thấy:

```
...
ets_task(40100130, 3, 3fff83ec, 4)
Hello Pymi.vn

MicroPython v1.9.4-8-ga9a3caad0 on 2018-05-11; ESP module with ESP8266
Type "help()" for more information.
>>>

```

Thao tác với các chân Pin

```python
>>> from machine import Pin
>>> P0 = Pin(0, Pin.OUT)
>>> P0.
__class__       IN              IRQ_FALLING     IRQ_RISING
OPEN_DRAIN      OUT             PULL_UP         init
irq             off             on              value
>>> P0.on()
>>> P0.off()
>>>
```

### Baud
Baud /ˈbɔːd/ ở câu lệnh trên là một độ đo "symbol rate" (symbol per second), để
quyết định tốc độ giao tiếp qua một kênh thông tin.

## Kết luận
Với MicroPython trên thiết bị, ta đã có thể thực hiện điều khiển các chân Pin hay gửi HTTP request như code Python bình thường. Giờ thì giới hạn chỉ còn là trí tưởng tượng của bạn.

## Tham khảo

- http://docs.micropython.org/en/latest/esp8266/tutorial/intro.html#intro
- https://wiki.wemos.cc/products:d1:d1_mini
