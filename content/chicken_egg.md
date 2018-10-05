Title: Quản lý, sử dụng package trong CHICKEN Scheme
Date: 2018-10-05
Category: Trang chủ
Tags: scheme, lisp, chicken, htdp
Slug: scm_egg
Authors: hvnsweeting
Summary: Con đường nhanh nhất để sử dụng 1 ngôn ngữ là dùng nó!

Học và hành thường ở rất xa nhau.
Ta có thể học đủ loại khái niệm, đủ loại cú pháp, viết các thuật toán để luyện
ngôn ngữ, nhưng rồi lại mãi luẩn quẩn ở đó, không thoát ra được, không bay
lên nổi. Viết 1 vòng for, 2 câu if bằng Python, JavaScript, Golang hay
[Elixir](https://elixir.pymi.vn/)
cũng không hơn nhau gì cả, chỉ thay đổi chút cú pháp thôi.

Thế nên cách "tốt nhất" để học 1 ngôn ngữ lập trình, không phải là học đủ các
khái niệm, best practice, viết code chuẩn đẹp tuyệt đối, mà là việc hoàn thành
một sản phẩm từ đầu đến tận X Y Z. Đưa ra sản phẩm cuối cùng, có thể là trang
web chạy với domain hẳn hoi, có thể là chương trình đóng thành package,
thành file cài đặt, hay game có giao diện đầy đủ.

Package manager giúp cài đặt các thư viện có sẵn là công cụ giúp ta đến đích
nhanh nhất. Python có pip, JavaScript có NPM, Elixir có mix, Rust có cargo ...
thì CHICKEN Scheme có `chicken-install`, câu lệnh có sẵn khi cài CHICKEN
Scheme.

## Cài đặt extension

CHICKEN Scheme gọi các gói thư viện là extension hay "egg".

`chicken-install tên-extension`

Ví dụ cài `regex`:

```bash
$ sudo chicken-install regex
[sudo] password for hvn:  GO PASSWORD
retrieving ...
connecting to host "chicken.kitten-technologies.co.uk", port 80 ...
requesting "/henrietta.cgi?name=regex&mode=default" ...
reading response ...
HTTP/1.1 200 OK
Date: Fri, 05 Oct 2018 14:28:32 GMT
Server: Apache/2.2.31 (Unix) DAV/2 PHP/5.5.36 mod_fastcgi/2.4.6
...
checking platform for `regex' ...
checking dependencies for `regex' ...
install order:
("regex")
installing regex:1.0 ...
changing current directory to /tmp/tempab50.21917/regex
  '/usr/bin/csi' -bnq -setup-mode -e "(require-library setup-api)" -e "(import setup-api)" -e "(setup-error-handling)" -e "(extension-name-and-version '(\"regex\" \"1.0\"))" 'regex.setup'
  '/usr/bin/csc' -feature compiling-extension -setup-mode    -s -O3 -d1 regex.scm -JS
  '/usr/bin/csc' -feature compiling-extension -setup-mode    -s -O3 -d0 regex.import.scm
  cp -r 'regex.so' '/var/lib/chicken/7/regex.so'
  chmod a+r '/var/lib/chicken/7/regex.so'
  cp -r 'regex.import.so' '/var/lib/chicken/7/regex.import.so'
  chmod a+r '/var/lib/chicken/7/regex.import.so'
  chmod a+r '/var/lib/chicken/7/regex.setup-info'
```

Bật `csi` lên để gõ code gọi function `grep`:

```scheme
$ csi
/usr/bin/rlwrap

CHICKEN
(c) 2008-2014, The Chicken Team
(c) 2000-2007, Felix L. Winkelmann
Version 4.9.0.1 (stability/4.9.0) (rev 8b3189b)
linux-unix-gnu-x86-64 [ 64bit manyargs dload ptables ]
bootstrapped 2014-06-07

#;1> (grep "[0-9]" (list "pymi" "2018" "pymi2018"))

Error: unbound variable: grep

	Call history:

	<syntax>	  (grep "[0-9]" (list "pymi" "2018" "pymi2018"))
	<syntax>	  (list "pymi" "2018" "pymi2018")
	<eval>	  (grep "[0-9]" (list "pymi" "2018" "pymi2018"))	<--
```

Nội dung error rõ ràng: `Error: unbound variable: grep` - không hiểu `grep`
là cái gì - nó không phải một variable/function đã tồn tại.

## Sử dụng / import extension

Dùng macro `use ten-extension` (tại bài này cứ hiểu là function cũng tạm ổn)

```scheme
#;1> (use regex)
; loading /var/lib//chicken/7/regex.import.so ...
; loading /var/lib//chicken/7/chicken.import.so ...
; loading /var/lib//chicken/7/irregex.import.so ...
; loading /var/lib//chicken/7/regex.so ...
#;2> (grep "[0-9]" (list "pymi" "2018" "pymi2018"))
("2018" "pymi2018")
```

Ta thu được list các phần tử có chứa số, string "[0-9]" là regular expression
biểu diễn một số hệ 10.

## Đọc tài liệu của module/function

`grep` ở trên làm gì? CHICKEN Scheme có chương trình `chicken-doc` để tra
tài liêu, tương tự python có `pydoc`. Để có `chicken-doc`, cần cài extension
với lệnh: `sudo chicken-install chicken-doc`.

```bash
$ chicken-doc grep
path: (regex grep)

-- procedure: (grep REGEX LIST [ACCESSOR])

Returns all items of `LIST` that match the regular expression `REGEX`. This procedure could be defined as follows:

  (define (grep regex lst)
    (filter (lambda (x) (string-search regex x)) lst) )

`ACCESSOR` is an optional accessor-procedure applied to each element before doing the match. It should take a single argument
and return a string that will then be used in the regular expression matching. `ACCESSOR` defaults to the identity function.
```

Pydoc đi kèm với Python có khả năng tương tự:

```bash
$ pydoc len

Help on built-in function len in module builtins:

len(obj, /)
    Return the number of items in a container.
```

## Liệt kê các extension có trên "mạng"

```
$ chicken-install -list
2d-primitives
3viewer
9ML-toolkit
9p
AD
F-operator
R
abnf
accents-substitute
...
```

Tại thời điểm viết bài, có 781 egg trong kho - hơi ít.

## Xem các extension library đã cài

Dùng lệnh `chicken-status`

```
$ chicken-status
apropos ......................................... version: 2.1.0
check-errors .................................... version: 2.2.0
chicken-doc ..................................... version: 0.4.7
chicken-doc-cmd ................................. version: 0.4.7
fmt ............................................. version: 0.808
fmt-c ........................................... version: 0.808
fmt-color ....................................... version: 0.808
fmt-js .......................................... version: 0.808
fmt-unicode ..................................... version: 0.808
iset .............................................. version: 2.0
```

## Gỡ extension

Sử dụng câu lệnh `chicken-uninstall TEN-extension`.

## Danh sách với thông tin các extension

Xem online tai [http://eggs.call-cc.org/4/]() cho bản CHICKEN stable hiện tại:
version 4.

Bài viết thực hiện trên:

```
$ lsb_release -r; csi -version
Release:	16.04

CHICKEN
(c) 2008-2014, The Chicken Team
(c) 2000-2007, Felix L. Winkelmann
Version 4.9.0.1 (stability/4.9.0) (rev 8b3189b)
linux-unix-gnu-x86-64 [ 64bit manyargs dload ptables ]
bootstrapped 2014-06-07
```

Hết phần 2.
