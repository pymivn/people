Title: Bắt đầu lập trình CHICKEN Scheme
Date: 2018-09-03
Category: Trang chủ
Tags: scheme, lisp, chicken, htdp
Slug: scm1
Authors: hvnsweeting
Summary: Cu Hít ở xứ sở LISP - 1 trong 2 ngôn lập trình lâu đời nhất trái đất.

Ba năm trước, khi chúng tôi bắt đầu mở khóa học đầu tiên dạy lập trình Python tại
[PyMi](https://pymi.vn), có 8 học viên đi học, hầu hết đều là sysadmin của một
công ty nào đó từng động tới OpenStack/SaltStack/Ansible.
Mới chỉ 3 năm trước, khi những người nghe tới Python tại Việt Nam
là những "hàng hiếm", thì tại thời điểm này, 2018, Python nhan nhản mọi nơi,
các trường (đại) học bắt đầu đưa Python vào chương trình giảng dạy, các
công ty tuyển Python như điên dại, làm Machine Learning, làm Odoo...
các chị em kế toán, ngân hàng bắt đầu kéo nhau đi học code Python!

Hầu hết số đông đến với Python không phải vì ham mê lập trình, yêu thích những
dòng code sạch sẽ, mà đơn giản bởi (1) công việc yêu cầu (2) kiếm tiền.
Khi đạt được múc đích rồi thì sao? đơn giản là thì thôi. Việc này không có gì
sai cả.

Vậy còn những người ham mê lập trình, yêu thích code thì làm gì? Họ tiếp tục
đào sâu thêm, học thêm vô vàn kiến thức trong thế giới lập trình, mở rộng
ra những ngôn ngữ mới, cách viết code mới, cách suy nghĩ mới.

Python thành công bởi ngôn ngữ sạch sẽ, (dẫn tới) cộng đồng đông đảo, (dẫn
tới) các thư viện có sẵn rất nhiều, chất lượng chuẩn, cập nhật hàng ngày.
Hầu hết các ngôn ngữ bạn từng nghe tên sẽ nằm trong nhóm này, những ngôn ngữ
còn lại (có tới hàng ngàn ngôn ngữ lập trình) thường bị xem là "đã chết".
Một ngôn ngữ mã nguồn mở chỉ thực sự chết khi cộng đồng không còn một ai,
những ngôn ngữ bạn chưa nghe tên bao giờ có khi đơn giản vì bạn không quen
ai dùng ngôn ngữ đó.

Python sinh năm 1991, C sinh năm 197x, thì LISP sinh ra vào năm 1958 (60 năm
trước - chỉ sau Fortran 1 năm - [xem bảng tuổi các ngôn
ngữ](https://www.familug.org/2016/02/python-python-tuoi-gi.html) ).
Hẵn rất dễ cho rằng LISP đã chết, vì chẳng gặp ai ở Việt Nam dùng nó. Cho tới
khi bạn gặp một anh kỹ sư xây dựng dùng AutoCAD vẽ bản vẽ 2D thiết kế nhà,
và cộng đồng này vẫn truyền tay nhau những đoạn code LISP.

Cộng đồng quốc tế rất đánh giá cao LISP, và có những thời điểm lịch sử, LISP
được gọi là ngôn ngữ của AI (một hướng phát triển AI rất khác so với
Machine Learning/Deep Learning sau này).

LISP (**LIS**t **P**rocessor) là tên của một gia đình các ngôn ngữ lập trình,
có 2 nhánh (dialect) chính là Common Lisp và Scheme. Cả 2 dialect này đều có
đặc điểm chung sử dụng rất nhiều dấu `()` nhưng khi thò tay vào code thì lại có
rất nhiều điểm khác. Một ví dụ viết function tính số gấp đôi của số đầu vào
bằng CHICKEN Scheme (một bản Scheme *còn sống*):

```scheme
(define (double x)
   (* x 2)
)
```

Gọi function:

```scheme
(define n 21)
(double n)
```

So với Python:

```python
def double(x):
    return x * 2

n = 21
double(n)
```

Nếu xét kỹ, cú pháp của Scheme (`define`) ít khái niệm/ký tự/nhất quán hơn
Python (`:`, `def`, `=`, `return`).

Một khái niệm khác rất quan trọng/phổ biến/nổi bật của LISP là sử dụng
macro (cùng khái niệm Macro trong C - nhưng mạnh mẽ hơn, ở một đẳng cấp hoàn
toàn khác).

## Các dialect của LISP

### Common Lisp

Common Lisp để tồn tại sau nhiều năm lịch sử với sự cạnh tranh của hàng ngàn ngôn
ngữ lập trình khác, đã tự biến đổi mình như một sinh vật tiến hóa. Nó gom vào
mình cả lịch sử lẫn những mảnh ghép của cộng đồng, khiến cho Common Lisp khá
đồ sộ, thực dụng. Những từ khóa cơ bản trong Common Lisp như `cdr`, `car`
là viết tắt của những khái niệm phổ biến những năm 195x nhưng ngày nay không
còn được nhắc tới, cho nên Common Lisp hơi khó đọc đối với dân ngoại đạo.
Bộ tiêu chuẩn Common Lisp dài [hơn 1000 trang
giấy](https://www.techstreet.com/standards/incits-226-1994-r1999?product_id=56214)

Bản chạy opensource phổ biến nhất của CL là : [SBCL](http://www.sbcl.org/)
một số bản thương mại rất đắt tiền.

### Scheme

Scheme ra đời vào những năm 197X, với mong muốn có một bản LISP trong sạch,
dễ đọc, nhỏ gọn, không còn chứa những di tích lịch sử, không còn những từ khóa
khó hiểu như `cdr`, `car`. Scheme được dùng làm ngôn ngữ chính
để dạy học lập trình tại đại học danh giá MIT - nổi tiếng theo đó là SICP
- cuốn sách luôn nằm trong top 10 các cuốn sách về lập trình (xem cuối bài).

NOTE: sau này vì lý do thực dụng, MIT dạy SICP bằng Python, không dùng Scheme
nữa.

Scheme được thống nhất thành tiêu chuẩn viết tắt là R5RS, R6RS, R7RS
hay đầy đủ là **Revised^5 Report on the Algorithmic Language Scheme** -
**R**evised Revised Revised Revised Revised **R**eport ... **S**cheme.
Mỗi lần "revised" như vậy (tăng lên 1 số),
tiêu chuẩn lại thêm bớt gì đó, và chuyện này không phải ai cũng đồng ý, nên
nhiều bản chạy (implementation) quyết định chỉ
hỗ trợ R5RS mà ko chịu lên R6.

Các bản Scheme nổi bật:

- CHICKEN scheme
- Guile (cài sẵn trên các máy Ubuntu)
- Chez scheme
- Gambit
- MIT Scheme

### Clojure
Clojure nổi bật là 1 LISP-dialect HIỆN ĐẠI. Nó chạy trên JVM (như Java)
và được dùng phổ biến trong các doanh nghiệp công nghệ - tại thời điểm
năm 2018. Xem thêm tại [trang chủ của Clojure](https://clojure.org/about/lisp).

### Racket
Racket từng là PLT Scheme, từng tuân theo tiêu chuẩn Scheme (S_RS) cho tới khi
nó tiến hóa thành một thứ khác rất nhiều. Racket cũng là một ngôn
ngữ hiện đại trong gia đình LISP.

### Emacs Lisp
LISP dialect dùng để phát triển các tính năng cho editor Emacs - một chương
trình chỉnh sửa code lâu đời, được ưa thích trong giới lập trình viên.

## Học để làm gì?
- Vui
- Mở mang suy nghĩ, thay đổi cách nghĩ - khi trên tay bạn chỉ có một cái búa
thì mọi thứ bạn thấy đều là cái đinh.
- Để thực hành khi đọc những cuốn sách hay nổi tiếng: SICP, HTDP

### Có để làm được không?

- Cái này tùy vào chuyện bạn làm gì. Nếu lập trình nhúng có thể bạn sẽ dùng 1
LISP dialect X, nhưng viết micro service tại các doanh nghiệp dùng Java,
Clojure lại là lựa chọn hấp dẫn hơn. Có thể tham khảo hướng dẫn học
Common Lisp năm 2018 [A road to Common
Lisp](http://stevelosh.com/blog/2018/08/a-road-to-common-lisp/)

- Những người học dùng LISP thường đã có công việc ổn định, không còn lo học
ngôn ngữ đầu tiên để xin việc - vậy nên chuyện có mang đi làm được hay không
không quá quan trọng ở đây. Học LISP xong, theo một cách nào đó, sẽ khiến
bạn trở thành lập trình viên Python giỏi hơn.

Loạt bài này sử dụng [CHICKEN scheme](http//call-cc.org).

## Cài đặt
Trên trang chủ của các bản LISP đều có hướng dẫn cài đặt chi tiết.
Trên ubuntu 16.04, `guile` có sẵn, cài CHICKEN scheme chỉ bằng một câu lệnh:

```
sudo apt install -y chicken-bin
```

Lệnh này cài bản `Version: 4.9.X`, cài xong bật lên để gõ code như python
interpreter:

```
$ csi
CHICKEN
(c) 2008-2014, The Chicken Team
(c) 2000-2007, Felix L. Winkelmann
Version 4.9.0.1 (stability/4.9.0) (rev 8b3189b)
    linux-unix-gnu-x86-64 [ 64bit manyargs dload ptables ]
    bootstrapped 2014-06-07

#;1> (+ 1 2 3 4 5)
    15
```

Để hỗ trợ chỉnh sửa tiện hơn, trên Ubuntu nên cài thêm `rl-wrap` và chạy
`rl-wrap csi`.

## Tài liệu
Sách free online thì có 2 cuốn đã lừng danh

  - [SICP -  Structure and Interpretation of Computer Programs](https://mitpress.mit.edu/sites/default/files/sicp/index.html)
  - [HTDP - How to Design Programs]( https://htdp.org/2018-01-06/Book/)

Các bài viết

- ["Nhật ký" từ Python qua Guile Scheme](http://www.draketo.de/proj/py2guile/)
- Lập trình viên Python có thể xem phần hướng dẫn cơ bản dành riêng cho Python
developer trên [wiki của CHICKEN](http://wiki.call-cc.org/chicken-for-python-programmers)
- [Hành trình của Python dev vào thế giới Scheme](https://www.artima.com/weblogs/viewpost.jsp?thread=251474)

Trên đây là tài liệu về Scheme, tài liệu Common Lisp cũng không thiếu,
và đều online/free - xem tại [A road to Common
Lisp](http://stevelosh.com/blog/2018/08/a-road-to-common-lisp/)

## Emacs
Khi lập trình LISP, người dùng được khuyên sử dụng Emacs đặc biệt là
common lisp với SLIME. Đây không phải điều bắt buộc, nhưng nếu chưa từng dùng
Emacs, đây là một cơ hội tuyệt vời để trải nghiệm (vì emacs dùng Emacs Lisp).

Hết phần 1.
