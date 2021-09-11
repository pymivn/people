Title: Python lên sao kê chậm - làm web được không?
Date: 2021-09-11
Category: Trang chủ
Tags: python, performance
Slug: slow
Authors: hvnsweeting
Summary: Python chậm hơn các ngôn ngữ lập trình khác nhưng có đủ nhanh cho bạn?

[Pymi.vn](https://pymi.vn) là một đơn vị đào tạo Python thực chiến ở Việt Nam,
học xong đi làm luôn. Chúng tôi đưa thẳng vấn đề với học viên
một sự thật về Python mà không hề giấu diếm: Python **chạy** chậm hơn (hầu hết) các
ngôn ngữ lập trình khác. Điều này được đưa vào bài học và học viên được
tự tay đo xem máy của mình tính được bao nhiêu phép +1 trong một giây. Xem kết quả tại: [cpu.pymi.vn](https://cpu.pymi.vn/)

Kết quả trung bình ở khoảng 15-30 triệu phép cộng / giây với các máy tính Intel i3 i5 i7.
Để làm mốc so sánh, code C tương tự có thể tính khoảng 1 tỷ phép cộng / giây (30-70x).

Đa số người mới đi học Python đều không hề biết chuyện này, họ đi học vì sự hot,
sự đơn giản,
ứng dụng khắp nơi của Python từ AI ML, DeepLearning, Blockchain, ...etc. Điều ấy
cho thấy một phần quan trọng về tính chất của người dùng: chọn ngôn ngữ lập trình
không phải vì nó CHẠY nhanh, họ không tìm học C/C++ hay Fortran.

Trong đó mâu thuẫn hơn cả, là ML/DeepLearning, lĩnh vực cần tính toán cực nhiều,
lại dùng Python phổ biến nhất.
Mâu thuẫn này thường để dành hỏi phỏng vấn các "data scientist" xem có hiểu tại
sao không? Còn với bạn đọc, chúng tôi để dành câu trả lời ở cuối bài.

![fast](https://images.unsplash.com/photo-1555980483-93e7b3529e1a?ixlib=rb-1.2.1&q=80&fm=jpg&crop=entropy&cs=tinysrgb&dl=kiril-dobrev-UB0QiVPsXgc-unsplash.jpg&w=800)

<center>Photo by <a href="https://unsplash.com/@kirildobrev?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Kiril Dobrev</a> on <a href="https://unsplash.com/s/photos/vietnam-hanoi?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash</a></center>


Để so sánh tốc độ, người dùng thực hiện các "benchmark", giải một bài toán cụ thể
và mang các phương án (ngôn ngữ/framework) ra so.

Trang web
[https://benchmarksgame-team.pages.debian.net/benchmarksgame/](https://benchmarksgame-team.pages.debian.net/benchmarksgame/)
thực hiện giải các bài toán/thuật toán cần tính toán nhiều và đưa ra kết quả.
Python trong bảng so sánh này, chỉ nhanh hơn hai ngôn ngữ phổ biến: Perl và Ruby.

<img src="https://benchmarksgame-team.pages.debian.net/benchmarksgame/download/fastest-more.svg" width="800">

[Top 4 đầu bảng: C++, C, Rust, Fortran](https://benchmarksgame-team.pages.debian.net/benchmarksgame/box-plot-summary-charts.html),
chú ý dòng kết luận quan trọng trên trang viết:

> It's important to be realistic: most people don't care about program performance most of the time.

## Python trong làm web
### Trên thế giới
Trang web viết bằng Python có lượng người truy cập lớn nhất thế giới hiện nay
có lẽ là Instagram.com - mạng xã hội hình ảnh ban đầu là 1 startup, sau đó
đã được Facebook mua lại.

Tại thời điểm viết bài, Instagram.com đứng thứ 21 toàn cầu về lượt truy cập
trên bảng xếp hạng của [Alexa](https://alexa.com), sau Netflix.com, trước Microsoft.com.
Instagram engineer blog về Python tại [https://instagram-engineering.com/tagged/python](https://instagram-engineering.com/tagged/python).

Một số ví dụ khác như [Uber core dùng Python](https://eng.uber.com/building-tincup-microservice-implementation/),
[DropBox dùng Python](https://dropbox.tech/tag-results.python),
hay [Youtube trước khi Google mua lại dùng Python](https://opensource.googleblog.com/2017/01/grumpy-go-running-python.html)
phục vụ hàng triệu request mỗi giây.

> The front-end server that drives youtube.com and YouTube’s APIs is primarily
> written in Python, and it serves millions of requests per second!

### Ở Việt Nam
Tại thời điểm viết bài 2021-09-11, Vnexpress.net là trang web của Việt Nam
đứng thứ #4 VietNam và #396 toàn cầu trên [Alexa.com](https://www.alexa.com/topsites/countries/VN)
3 trang top VN là Google, Youtube, Facebook. Nếu xem tiếp top 50 Việt Nam,
các tên hầu hết là các trang báo mạng, hay thương mại điện tử lớn như Shopee,
Lazada, Tiki.
Các trang này viết bằng công nghệ nào không rõ, nhưng rõ ràng là lượt truy cập
đều ít hơn Instagram đáng kể.

### Các đơn vị đo tốc độ trang web
#### Request per seconds (RPS) - throughput
RPS - có nơi viết là reqs/s, thường là đơn vị chính dùng để đo xem 1 trang web
có thể phục vụ được bao nhiêu yêu cầu mỗi giây. RPS còn có tên khác là ["throughput"](https://www.techempower.com/blog/2016/02/10/think-about-performance-before-building-a-web-application/).
Để bạn đọc hình dung được độ lớn của RPS tại các website thế nào, sau đây là vài ví dụ:

- Năm 2020, chương trình Rap Việt đạt kỷ lục có lượng người xem cùng lúc [cao
nhất tại Việt Nam với con số
1.051.000](https://tienphong.vn/thuc-hu-cau-chuyen-rap-viet-lap-ki-luc-nguoi-xem-cao-nhat-the-gioi-post1290225.tpo)...
cho thấy Youtube chạy ngon lành thế nào.
Đó là đỉnh cao tại Việt Nam, đất nước ~ 100 triệu dân, thì max là 1% xem cùng
một lúc (không ít người ở nước ngoài). Đừng tưởng tượng nước có 100 triệu dân
thì có cái gì 50 triệu người cùng làm một lúc.
- 9/2021, [chủ tịch thành phố HCM lên livestream giải đáp thắc mắc của người
dân](https://tuoitre.vn/chu-tich-ubnd-tp-hcm-tra-loi-truc-tuyen-vung-xanh-duoc-di-cho-1-tuan-lan-mo-dan-mot-so-dich-vu-20210906184222848.htm)
, có thể đoán hầu hết chỉ có người dân TPHCM mới xem, lượng view chụp trong ảnh là 74k,
trên tổng [dân số >=18 tuổi TPHCM cỡ khoảng 7.2 triệu người](https://tuoitre.vn/toc-do-tiem-vac-xin-o-tp-hcm-dan-tang-cao-da-co-hon-1-trieu-nguoi-tiem-mui-2-20210911085618942.htm) - tại thời điểm hầu hết
người dân đều ở nhà giãn cách xã hội theo chỉ thị 16, cho thấy Facebook livestream ngon lành thế nào.
- [mangadex.org với trung bình ~2000 rps](https://mangadex.dev/mangadex-v5-infrastructure-overview/) - #5,895 trên Alexa.com.
soha.vn - 1 trang báo mạng khá lớn của VCCorp, #50 VN, xếp #5,789 thế giới - gần với mangadex.
Nhaccuatui.vn - trang nghe nhạc lớn nhì, ba tại Việt
Nam, chỉ xếp #14,770. Vậy trừ khi bạn làm tại các công ty có website chạy top
50 VN, bạn mới có 2000 RPS.
- 2000 RPS => 2000 * 86400 = 172.800.000 requests/day. **172 triệu lượt truy cập**
mỗi ngày. Trang web của bạn/ công ty/ startup của bạn liệu có được 86400 reqs/day? (1 RPS).
- [Một lập trình viên đâu đó ngồi đo](https://mark.mcnally.je/blog/post/My%20%C2%A34%20a%20month%20server%20can%20handle%204.2%20million%20requests%20a%20day) thử với 1 cái máy ảo cloud 1CPU 2GB RAM £4 (5.5 USD == 126.000VND).
có thể chạy web Django với 54.3 RPS (54 * 86400 == 4.665.600 reqs/day),
thêm cache sẽ được 63.50RPS, và nếu chỉ có HTML/JS là 180.54 RPS.
Mức giá này khá rẻ, tại [DigitalOcean](https://bit.ly/dohvn),
cấu hình tương đương có giá 10USD/tháng. (Note: link refer, đăng ký bằng link
này được $100 miễn phí cho bạn, $20 cho Pymi.vn).
hay [BIZFLY CLOUD](https://bizflycloud.vn/cloud-server/bang-gia) của Việt Nam cũng giá ~200.000.

Chú ý: việc tính RPS thường tính trung bình, nhưng trên thực tế, mỗi website có
một "pattern" truy cập khác nhau. Ví dụ tại một vài thời điểm trong ngày, sẽ
có nhiều người truy cập đọc báo hơn là lúc 4h sáng. Các website thương mại điện
tử sẽ luôn "peak" khi chạy các khuyến mãi 6-6, 9-9, 11-11, black friday...

#### Concurrent User (CCU) - đơn vị mà chủ doanh nghiệp quan tâm
RPS mang tính chất con số về mặt kỹ thuật, nhưng khi truy cập 1 website, người
dùng thường thực hiện nhiều hơn 1 request. Ví dụ khi truy cập
[https://pymi.vn](https://pymi.vn), trình duyệt
sẽ thực hiện 8 requests (các file HTML/CSS/Javascript/ảnh), còn khi truy cập
vnexpress.net, trình duyệt thực hiện tới 73 requests.

Chủ doanh nghiệp, website, chỉ quan tâm con số mang tính chất kinh tế,
là có bao nhiêu người dang dùng mà không quan tâm có bao nhiêu request, vậy
nên con số Concurrent User (CCU - số người truy cập cùng lúc) ra đời.
Trong ví dụ Rap Việt trên, có 1 triệu người xem cùng lúc - 1 triệu CCU.
1 triệu CCU tương ứng với tối thiểu 1 triệu RPS, nhưng thường RPS cao hơn nhiều lần.

Một điều đáng nói khác, rằng không phải 73 requests đều gọi vào vnexpress.net mà
gọi đến các trang khác chứa ảnh, video...

Khi nói về CCU, chủ doanh nghiệp cũng không quan tâm hệ thống sử dụng bao
nhiêu máy tính ở đây. Nói 1 triệu RPS, không có nghĩa là phải dùng 1 máy,
1 triệu RPS/máy là rất cao, trên thế giới [Whatsapp đã làm được 1m TCP conn từ
2011](https://blog.whatsapp.com/1-million-is-so-2011/?lang=en),
[Elixir Phoenix fullstack web-framework chạy 2 triệu websocket
connections](https://www.phoenixframework.org/blog/the-road-to-2-million-websocket-connections)
năm 2015. Nhưng không ai cấm bạn chạy 200 máy sau load-balancer cả.
1.000.000 / 200 = 5.000 RPS.

[C10k](https://en.wikipedia.org/wiki/C10k_problem) là 1 vấn đề rất năm 2000, để
xử lý 10.000 connection, cùng với sự ra đời của NGINX.

#### Response time - latency, p95, p99
Một đơn vị quan trọng khác khi nói về tốc độ website là **response time** tên
khác là latency - thời
gian tính tức lúc người dùng gửi request đi cho tới khi nhận được nội dung trang web.
Con số này nói đơn giản chính là sự nhanh/chậm của website.
Response time là 10 giây thì người dùng sau khi vào thanh địa chỉ gõ enter, 10
giây sau mới nhìn thấy nội dung trang web.
(để thấy TOÀN BỘ nội dung trang web, người ta dùng thêm đơn vị đo "load time")

Nhưng nếu kết quả response lúc nhanh lúc chậm thì biết lấy số nào? đó là lúc
cần lôi bộ môn [thống
kê](https://medium.com/pymi/d%C3%B9ng-python-%C4%91%E1%BB%83-h%E1%BB%8Dc-th%E1%BB%91ng-k%C3%AA-8e41dfdaaf97)
ra để trình bày. Cách đơn giản nhất là lấy trung bình cộng,
nghe thì dễ, nhưng kết quả này thường vô dụng, bởi 198 lần load 1s mà 2 lần 901s
thì trung bình là: (99 * 2 + 901 * 2)/200 == 10.0s.

Cách làm phổ biến là dùng quantile 99 (hay 95) để đo: tức giá trị mà
99% các giá trị khác đều nhỏ hơn hoặc bằng, còn có tên gọi p99 (99th percentile).
Trong ví dụ trên, p99 là 1: `int(99/100 * 200 số) = 198`, sắp xếp các số tăng
dần thì số thứ 198 có giá trị là 1,
p100 ít khi được nhắc tới, đó là số lớn nhất trong tập.
Xem thêm về quantile và percentile ở phần link tham khảo.

Tại sao lại bỏ đi 1% như vậy? vì kết quả đo đạc có thể có các sai số do nhiều
lý do khác nhau và không có ý nghĩa với vấn đề (chậm do mạng bị cá mập cắn
trong 1 request, chẳng hạn).

### Tốc độ lý thuyết
Tương tự website benchmark
tốc độ tính toán của các ngôn ngữ, có website benchmark các webframework:
[techempower](https://www.techempower.com/benchmarks/#section=data-r20)

tại đây, mỗi framework thực hiện 7 loại test và được chấm điểm, đầu bảng hầu hết
là C++ hay Rust, luôn dành chiến thắng về tốc độ, nhưng không mấy ai làm web
site bằng C++ cả.

> Nhớ rằng: Instagram dùng Django.

Các web framework phổ biến của Python hầu như đều ở phía dưới bảng xếp hạng,
ngang ngửa với Ruby/PHP

- Django (359/436)
- Flask (370/436)
- Ruby On Rails (377/436)
- PHP Lavarel (388/436)

Riêng FastAPI cùng khu với Elixir, NodeJS, Java

- Golang Gin (162/436)
- NodeJS Express MySQL (287/436)
- FastAPI (247/436)
- Elixir Phoenix (251/436)
- Java Spring (317/436)

vậy kết luận dùng Go chạy nhanh hơn và đập hết Django, Java, Ruby app đi viết
lại ?

**Đừng!**

Kết quả của việc benchmark rất khó để đưa ra kết luận, và tốc độ thực sự phụ
thuộc vào bài toán cụ thể chứ không phải dựa và kết luận "hello world" của
framework.

Dù điểm trung bình của Golang + Gin framework (nhanh) hơn của FastAPI, nhưng
khi xem từng test cụ thể, như test data update (có sự ảnh hưởng lớn của database)
thì FastAPI bỏ xa xa xa Go + Gin. Website của bạn có update DB không? tùy trường
hợp. Khi chỉ đơn thuần tính toán và không động vào DB, Go rõ ràng dành chiến thắng.

Xem thêm phần [thắc mắc về tốc độ của FastAPI tại đây](https://github.com/tiangolo/fastapi/issues/1664#issuecomment-653580642).

Các kết quả benchmark dễ dàng bị đảo ngược chỉ với vài thay đổi phụ thuộc bài toán, như
trường hợp benchmark Flask sau:

- [bài này benchmark kết luận async Python không nhanh hơn sync](https://calpaterson.com/async-python-is-not-faster.html)
- [bài này chỉnh sửa lại 1 chút, và cho kết quả khác hoàn toàn](https://blog.miguelgrinberg.com/post/ignore-all-web-performance-benchmarks-including-this-one)

Tác giả [Flask mega tutorial Miguel Grinberg](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world) chỉ đưa ra kết luận cuối cùng với tên bài viết:

> Ignore All Web Performance Benchmarks, Including This One

Một bài viết khác thực hiện cải thiện website dùng [Flask + SQLAlchemy ORM từ 12RPS thành 75RPS](https://suade.org/dev/12-requests-per-second-with-python/).

Trong các trang web, tốc độ của website phần lớn phụ thuộc vào database,
kiến trúc, cache, hơn là phụ thuộc vào tốc độ của web framework.

### Load test Python
Cách để rút ra được kết quả chuẩn nhất, có ý nghĩa nhất là tự đo code của mình.
Công cụ để benchmark web site:

- ab (Apache benchmark tool) `sudo apt-get install apache2-utils`
- [Go hey](https://github.com/rakyll/hey)
- [C wrk](https://github.com/wg/wrk)
- [Locust.io python + webUI + distributed + graph report](https://locust.io/)

Thử benchmark code Flask+Gunicorn hello world, 1000 CCU:

```py
from flask import Flask
import time


app = Flask(__name__)

@app.route("/fast")
def fast():
    return "yes"
```

```
$ gunicorn app:app -w 9 -k gthread
```

Rồi chạy `wrk`:

```sh
$ ./wrk -c 1000 -d 10s http://localhost:8000/fast
Running 10s test @ http://localhost:8000/fast
  2 threads and 1000 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency   233.14ms   61.78ms 371.49ms   68.27%
    Req/Sec     2.13k   222.09     2.75k    67.50%
  42372 requests in 10.08s, 6.47MB read
Requests/sec:   4202.64
Transfer/sec:    656.75KB
```

4200rps với latency avg 200ms, max cũng chỉ là 371ms.

hay `ab`:

```sh
$  ab -n 10000 -c 1000 http://localhost:8000/fast

Concurrency Level:      1000
Requests per second:    3706.73 [#/sec] (mean)

Percentage of the requests served within a certain time (ms)
  50%    264
  66%    293
  75%    312
  80%    327
  90%    360
  95%    397
  98%    426
  99%    448
 100%    476 (longest request)
```

Test trên

```sh
AMD Ryzen 3 4300U - 4 cores - 8GB RAM

$ lsb_release -d; python3 --version
Description:    Ubuntu 20.04.3 LTS
Python 3.8.10


Flask               2.0.1
gunicorn            20.1.0

$ ./wrk --version
wrk a211dd5 [epoll] Copyright (C) 2012 Will Glozer
```

## Python trong hệ thống
Hai trường hợp minh họa code Python chạy đủ nhanh:

- [Khi sử dụng Kafka trong bài tăng tốc độ
10x](https://pp.pymi.vn/article/10x/), dùng thư viện
https://github.com/confluentinc/confluent-kafka-python, bên dưới thực chất gọi code C librdkafka,
thay Python bằng code Go [không làm nhanh
hơn](https://github.com/confluentinc/confluent-kafka-go/issues/490#issuecomment-655339047)
[thậm chí còn chậm
hơn](https://github.com/confluentinc/confluent-kafka-go/issues/567), giải pháp
có thể là
tìm một thư viện Kafka viết bằng Go rồi benchmark lại.
- Code C++ thường được coi là **hiển nhiên** nhanh hơn Python, [nhưng phải biết
bật tắt đúng thứ không sẽ chậm hơn](https://stackoverflow.com/questions/9371238/why-is-reading-lines-from-stdin-much-slower-in-c-than-python?rq=1)
- [c++11 regex slower than python - và nhớ rằng tuy nói là Python, nhưng rất nhiều chỗ của Python thực chất gọi code C bên dưới](
https://stackoverflow.com/questions/14205096/c11-regex-slower-than-python)

## Python trong xử lý data

Các thư viện tính toán khoa học trong Python đều sử dụng các ngôn ngữ tính toán
nhanh bên dưới, như Numpy/Pandas dùng C, PyTorch/Tensorflow dùng C++. Kết hợp
với cú pháp Python ở trên, tạo nên sự hoàn hảo của cả 2 thế giới: code đẹp, đơn
giản của Python, và tính nhanh (gần) như C/C++/Fortran.

## Kết luận

Đọc kết quả benchmark trên mạng rồi đưa ra kết luận là một việc làm rất nguy hiểm,
nên tự học cách benchmark cho trường hợp cụ thể của mình.

Tốc độ của ngôn ngữ lập trình & framework trên thực tế thường không quan trọng
bằng: tốc độ phát triển tính năng/ dự án, chi phí bỏ ra để viết lại bằng
một ngôn ngữ X chạy nhanh hơn.

## References
- [Ủng hộ tác giả 🍺](https://www.familug.org/p/ung-ho.html)
- [techempower - Think about Performance Before Building a Web Application](https://www.techempower.com/blog/2016/02/10/think-about-performance-before-building-a-web-application/)
- [page load time vs response time](https://www.pingdom.com/blog/page-load-time-vs-response-time-what-is-the-difference/)
- [Quantile](https://en.wikipedia.org/wiki/Quantile)
- [Percentile](https://en.wikipedia.org/wiki/Percentile)
- [FastAPI is fast](https://github.com/tiangolo/fastapi/issues/1664#issuecomment-653580642)
- [c11-regex-slower-than-python](https://stackoverflow.com/questions/14205096/c11-regex-slower-than-python)
- [why-is-reading-lines-from-stdin-much-slower-in-c-than-python](https://stackoverflow.com/questions/9371238/why-is-reading-lines-from-stdin-much-slower-in-c-than-python?rq=1)

HVN at [http://pymi.vn](http://pymi.vn) and [https://www.familug.org](https://www.familug.org)
