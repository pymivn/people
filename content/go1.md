Title: Vừa đủ để đi (go)
Date: 2020-09-06
Category: Trang chủ
Tags: golang, go
Slug: go
Authors: hvnsweeting
Summary: Học vừa đủ Golang để nguy hiểm - phần 1

Series bài viết giúp lập trình viên đã biết Python bắt đầu code Go mượt mà hơn - tài liệu bổ trợ cho [Go tour](https://tour.golang.org/) chứ không để thay thế - phần 1.

## Golang là gì

![gopher](https://golang.org/lib/godoc/images/home-gopher.png)

Go (hay còn gọi là Golang theo tên trang chủ [golang.org](https://golang.org)) là một ngôn ngữ lập
trình mới xuất hiện trong công chúng vào năm 2009 (vs: Python 1991, Java 1995),
tại Google.

Go được thiết kế ra với mục tiêu thay thế cho C++, nhưng khi tung ra cộng
đồng, nó lại trở thành ngôn ngữ hấp dẫn đối với các lập trình viên dùng
ngôn ngữ bậc cao hơn như Python, [Ruby](https://blog.iron.io/how-we-went-from-30-servers-to-2-go/), PHP, NodeJS... nhờ khả năng chạy code
nhanh, dùng ít tài nguyên hơn, deploy dễ hơn so với các ngôn ngữ này.

Go trở thành một trào lưu (trend) công nghệ trên internet, với các bài viết
"Write X in Go" luôn trở thành bài hot (và giờ thì tới Rust).
Go được sử dụng như một ngôn ngữ "backend", rất thịnh hành tại các startup
công nghệ để viết "service" trong các hệ thống "microservice", web API.
[Go còn được dùng phổ biến để viết các câu lệnh command line](https://blog.golang.org/survey2019-results).

Go đã ở giai đoạn "production ready", đủ ổn định và đã được chạy trên các [hệ thống
lớn trên toàn cầu](https://github.com/golang/go/wiki/GoUsers). Các sản phẩm opensource viết bằng Go được dùng rộng rãi như:
Kubernetes, Docker, Terraform, InfluxDB, Prometheus, Grafana, ...

Những lĩnh vực khác cũng đã có mặt Go nhưng chưa thực sự thành công: mobile,
frontend (JavaScript), làm website (như Django/RubyOnRails), Machine Learning.

## Những ưu điểm nổi bật của Go

- Ngôn ngữ đơn giản: Go có ít khái niệm hơn các ngôn ngữ lập trình khác
C++/Java/Python/Ruby... Go tại năm 2020 có [25
keywords](https://golang.org/ref/spec#Keywords), [Python 3.8 có 35
keywords](https://docs.python.org/3.8/reference/lexical_analysis.html#keywords).
Hầu hết các công ty tuyển lập trình viên Go đều không yêu cầu kinh nghiệm code
Go,
 chỉ cần tuyển 1 lập trình viên đã dùng ngôn ngữ khác, qua training 1-2 tuần
 là đã có thể viết code production, trông không khác gì lập trình viên lâu năm.
- Code Go viết bằng chính Go, ai cũng có thể đọc [kiểu dữ liệu map được viết thế nào](https://github.com/golang/go/blob/master/src/runtime/map.go) - so với Python (CPython) sẽ phải đọc code C.
- Hệ thống thư viện có sẵn (stardard library) đa dạng, đầy đủ - ngang ngửa Python, thậm chí còn hơn: gửi HTTP request chỉ cần dùng `net/http`, không phải [cài requests như Python (mặc dù Python có thể dùng urllib nhưng không mấy ai dùng)]({filename}/requests.md), đầy đủ `json`, `regexp`, cho tới HTTP server sẵn sàng chạy production.
- Compile nhanh: so với các ngôn ngữ C/C++/Java/C#... thì Go compile nhanh gấp
nhiều lần
- Sản phẩm compile tạo ra là 1 file binary. Sau đó
 chỉ cần mang file này đi chạy là xong - điểm này khác biệt lớn so với Python,
 NodeJS, Ruby - phải cài các "dependency" (pip/npm/gem) rồi mới chạy được code (Go cũng cần
 tải các dependency, nhưng chỉ cần thực hiện trước khi compile ra file binary).
- Code chạy nhanh: Go tuy không nhanh bằng C/C++/C#/Java trong hầu hết các
  trường hợp, chậm hơn cỡ 2-5 lần, nhưng nhanh hơn Python/Ruby cỡ [20-100 lần](https://benchmarksgame-team.pages.debian.net/benchmarksgame/which-programs-are-fastest.html),
- Tốn ít memory - bộ nhớ: ít hơn [Ruby cỡ 15 lần](https://blog.iron.io/how-we-went-from-30-servers-to-2-go/)
- Quản lý bộ nhớ tự động (tương tự Python/Ruby/Java...)
- Dễ viết code concurrency, dùng multi-core (thay vì dùng thread/async).

## Những khác biệt chủ yếu với Python
### Cách viết và chạy code
Go là compiled language, trước khi chạy được code phải qua 1 bước compile để
tạo ra file binary, rồi sau đó mới chạy được file này.
[Go không có sẵn REPL, không bật lên gõ code trực tiếp như Python được]({filename}/repl.md).
Mỗi lần sửa gì, thử gì, phải compile lại rồi mới chạy được.

```
go build
./filename
```

Vậy nên cách nhanh nhất để thử 1 đoạn code trong Go có lẽ là viết unittest.
[test rất phổ biến với một Go project](https://golang.org/doc/code.html#Testing),
là một phần có sẵn trong bộ công cụ dev.

Với 1 file code đơn giản, có thể dùng lệnh `go run main.go` để làm gộp 2 bước,
compile rồi chạy file kết quả luôn.

### Auto format - go fmt
Go là ngôn ngữ lập trình đầu tiên đưa 1 công cụ format code tự động vào tiêu chuẩn,
chấm dứt mọi tranh cãi về code-style/format code. Ý tưởng tuyệt vời này sau được
copy sang nhiều ngôn ngữ khác (như [Python black]({filename}/black.md))

```
go fmt
```

### Static typing
Python là ngôn ngữ dynamic typing, Go là static typing.
Nếu chưa từng code ngôn ngữ static typing hay chưa dùng type annotation của Python,
khác biệt này sẽ gây chút khó khăn lúc bắt đầu code Go.

Theo [python wiki](https://wiki.python.org/moin/Why%20is%20Python%20a%20dynamic%20language%20and%20also%20a%20strongly%20typed%20language)
> In a statically typed language, the type of variables must be known (and
usually declared) at the point at which it is used. Attempting to use
it will be an error. In a dynamically typed language, objects still have a
type, but it is determined at runtime. You are free to bind names (variables)
to different objects with a different type. So long as you only perform
operations valid for the type the interpreter doesn't care what type they
actually are.

Static/dynamic typing nói tới kiểu (type) của 1 biến (variable/name).
Trong dynamic typing, kiểu của 1 biến có thể thay đổi:

```python
x = 10
x = "PyMi"
```

Trong static typing, kiểu của 1 biến là cố định, và được khai báo ngay từ
trước khi dùng, code sau sẽ gặp lỗi khi compile, và không tạo ra binary nào để chạy.

```go
x := 10
x = "PyMi"
```

```
cannot use "PyMi" (type untyped string) as type int in assignment
```

Trong Python3.6+, [sử dụng type annotation, kết hợp với mypy]({filename}/mypy.md)
để check cũng sẽ
cho lỗi tương tự (nhưng vẫn chạy được).

```python
x: int = 10
x = "PyMi"
print(x)
```

```
$ mypy typetest.py
typetest.py:2: error: Incompatible types in assignment (expression has type "str", variable has type "int")
Found 1 error in 1 file (checked 1 source file)
```

Kiểu của các biến trong Go nói chung phải khai báo (declare), Go có thể tự suy
luận (type inference) được trong một vài trường hợp đơn giản.

```go
var x int
var s string
x = 10
s = "PyMi"
```

### Low level
Được thiết kế nhằm thay C/C++ pha lẫn sự đơn giản dễ đọc của Python,
code Go thường đơn giản hơn code C/C++ nhưng khá "thủ công"/"low level"
so với code Python. Lập trình viên Python code Go nên quen với việc bỏ bớt
đi nhiều tính năng tiện lợi, phải viết nhiều code hơn.

- Go không có list comprehension
- Go không có map/filter
- Go không có kiểu set
- Go không có `4 in [2,3,4]` để [kiểm tra phần tử có trong list không](https://stackoverflow.com/questions/38654383/how-to-search-for-an-element-in-a-golang-slice)
- Sort trong Go chắc chắn dài hơn `L.sort(reverse=True)`
- Reverse string sẽ không phải là`s[::-1]` mà [dài cả mét](https://stackoverflow.com/questions/1752414/how-to-reverse-a-string-in-go)
- Không đơn giản chỉ `json.loads` để biến `str` thành `dict` mà phải định
  nghĩa struct theo cấu trúc của JSON.

Code Go nhìn chung sẽ dài hơn code Python, vậy nên lập trình viên nên sắm cho
mình một IDE xịn (như GoLand/IntelliJ IDEA , VSCode hay `vim` + `vim-go`), với khả năng [dùng snippet để
sinh code](https://code.visualstudio.com/docs/editor/userdefinedsnippets).

Sự bất tiện này sẽ đỡ khó chịu đi nhiều khi đã quen dùng snippet.

## Học lập trình Go (khi đã biết Python)
### Bao nhiêu là đủ? Em vui là được có phải không!
Không ai đọc hết quyển từ điển tiếng Việt rồi mới ra nói câu đầu tiên,
không ai học lên tiến sỹ âm nhạc rồi mới chạm tay vào đánh đàn. Khi [học Python
tại PyMi.vn](https://pymi.vn), ta học từng chút, dùng từng chút, chứ không học hết lý thuyết
cả Python rồi mới thực hành. Cũng không phải học `async`, `threading`, [metaclass](https://stackoverflow.com/questions/100003/what-are-metaclasses-in-python)
rồi mới chịu đi làm.

Học Go cũng vậy, dùng gì học đấy, cần gì học đấy.
Cần gì thì phụ thuộc vào bạn định làm gì, một Python web developer sẽ học
Django, ORM, làm việc với database trong khi một SysAdmin/DevOps engineer lại
làm việc với file, process...

### Go tour

Tài liệu chính thống, đầy đủ và hiệu quả để học go là Go Tour: [https://tour.golang.org/](https://tour.golang.org/)

### Viết code Go
[Cài Go lên máy rồi viết code ra file](https://golang.org/doc/tutorial/getting-started), hoặc code online trên trang Play [https://play.golang.org/](https://play.golang.org/)

Go chạy code từ function `main` thuộc `package main`. code "Hello world!" như sau:

```go
package main

import "fmt"

func main() {
	fmt.Println("Hello, world.")
}
```

### Naming
Go dùng `camelCase`, với ý nghĩa đặc biệt khi chữ cái đầu viết hoa hay viết thường.
Nếu viết hoa, var/function/type đó sẽ trở thành "public", code bên ngoài package hiện tại truy cập được, còn không viết hoa sẽ là "private".

### Data types
#### Built-in
- nil: `nil` là một giá trị, không có kiểu, đại diện cho sự "không tồn tại".
- bool: kiểu boolean gồm 2 giá trị `true` `false`, các boolean operator `&&` (and), `||` (or) tuân theo [`short-circuit`](https://pymi.vn/tutorial/boolean/).
- int: các kiểu số trong Go đều có kích thước, int có kích thước 32 hoặc 64 bits [tùy theo bản (chủ yếu 64 bits)](https://golang.org/doc/faq#q_int_sizes).
  Các kiểu cụ thể `int8 int16 int32 int64`, có kích thước là 2 mũ n, int8 int16 thường chỉ dùng khi tối ưu về memory. int64 biểu diễn được giá trị trong khoảng (`-2**64/2, 2**64/2`), muốn tính giá trị lớn có thể [sử dụng package có sẵn `math/big`](https://golang.org/pkg/math/big/#Int.String).
- `float32` hoặc `float64`: chú ý không có kiểu `float`. [Tuân theo chuẩn IEE754](https://pymi.vn/blog/why-not-float/) nên `x, y, z := 0.1, 0.1, 0.1` thì `x + y + z == 0.3` sẽ trả về false. Chú ý ở trên tạo các biến để các giá trị 0.1 có kiểu float64, nếu viết trực tiếp `0.1 + 0.1 + 0.1 == 0.3` sẽ là so sánh constants và trả về true [https://play.golang.org/p/TWRRr_lM7jk](https://play.golang.org/p/TWRRr_lM7jk). Đọc thêm về constants tại [blog Go](https://blog.golang.org/constants).
- string: giống như string của Python, immutable, có thể truy cập dùng index: `s[3]`. String bên dưới là 1 chuỗi các byte, hay một byte array/byte slice `[]byte{'h', 'e', 'l', 'l', 'o'}`, có thể convert thành string: `string(bytes)`. Python cũng có kiểu `bytes`, cũng chuyển thành `str` bằng cách decode `b'abc'.decode('utf-8')`.
- array/slice: Go array giống như C, các phần tử phải cùng kiểu, và kích thước cố định không đổi. [Array ít được dùng trực tiếp](https://www.youtube.com/watch?v=5DVV36uqQ4E)
  nó được dùng bên dưới slice và slice linh hoạt như list trong Python. Ví dụ về slice
```go
	ns := []int{0, 1}
	fmt.Printf("%v\n", ns)
	ns = append(ns, 2)
	fmt.Printf("%v\n", ns)
	ns = append(ns, ns...)  // như extend trong python list
	fmt.Printf("%v\n", ns)
```
[https://play.golang.org/p/SCW8F0EqCmW](https://play.golang.org/p/SCW8F0EqCmW)

- map: giống dict của Python, key phải so sánh `==` được, map và slice không
làm key được, key không theo thứ tự (unordered). Map trong Go dùng khi cần nối
key-value, tìm kiếm nhanh, nhưng không dùng như 1 object như dict Python.
Do map phải có kiểu cố định cho key, value. [Xem code](https://play.golang.org/p/JRu3lp_mEGj)

```go
	users := make(map[int]string)

	users[20081269] = "Pymier69"
	users[20081234] = "Pymier1"
	users[20081239] = "Pymier2"
	for k, v := range users {
		fmt.Printf("%d: %s\n", k, v)
	}
	println(users[20081239])
```

Cú pháp [`composite literal`](https://golang.org/ref/spec#Composite_literals) giúp tạo giá trị cho struct/slice/array/map.

```go
  xs := []int{3,2,1}
  m := map[int]string{
         123: "foo",
         345: "bar",
     }
```

Các kiểu khác `struct`, `pointer`, `function`, `interface`, `channel`
sẽ được nhắc tới sau, xem đầy đủ tại [spec](https://golang.org/ref/spec#Types).

#### Struct & method
Python có class, cung cấp đủ các tính năng tiêu chuẩn của OOP (object-oriented
programming - lập trình hướng đối tượng).  Định nghĩa 1 class tạo ra 1
kiểu dữ liệu mới và cho phép đóng gói dữ liệu (data) với tính năng (method) lại
với nhau.

Go `struct`: A struct is a collection of fields.

struct không cung cấp các tính năng của OOP (như inheritance), nhưng cũng
tạo ra 1 kiểu dữ liệu mới và cho phép đóng gói dữ liệu (data) với tính năng
(method) lại với nhau. [https://play.golang.org/p/tQMPLn9OXcj](https://play.golang.org/p/tQMPLn9OXcj)

```go
type Rectangle struct {
	Width  float64
	Height float64
}

func (r Rectangle) Area() float64 {
	return r.Width * r.Height
}

func main() {
	r := Rectangle{Width: 2, Height: 3}
	fmt.Printf("%f %T", r, r.Area())
}
```

Code tương tự trong Python3, với type annotation

```python
class Rectangle():
    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height

    def area(self) -> float:
        return self.width * self.height

def main():
    print(Rectangle(width=2, height=3).area())
```

Trong Go, function gắn với các struct gọi là method, `(r Rectangle)` gọi là receiver, đứng trước tên `Area()` trông lạ so với các ngôn ngữ khác, nhưng nó đóng vai trò như `self` trong Python method.

>  Remember: a method is just a function with a receiver argument.

#### interface, type assertion, type switch

Một interface type định nghĩa 1 tập hợp các method.
> An interface type is defined as a set of method signatures.

Một value của type interface có thể chứa bất kỳ giá trị nào implement các method qui định trong interface đó.

Empty interface `interface{}` là trường hợp đặc biệt, nó có thể chứa mọi giá
trị do không cần có method nào.

Một value kiểu `interface{}` đánh sập mọi đảm bảo về type trong Golang, biến
Go thành dynamic typing như Python. Nó như lối thoát linh hoạt giữa mọi
sự cứng nhắc/static.

Sử dụng type assertion để truy cập giá trị ẩn dưới `interface{}`:

```go
    var anything interface{}
    anything = "PyMi.vn"
    fmt.Printf("%v %T\n", anything, anything)
    anything = 42
    fmt.Printf("%v %T\n", anything, anything)
    x := 10
    fmt.Printf("%v %T\n", x+anything.(int), anything.(int))
```

[https://play.golang.org/p/mNXTI-4C3pU](https://play.golang.org/p/mNXTI-4C3pU)

hoặc dùng `switch` để xử lý các kiểu khác nhau:

```go
	switch v := i.(type) {
	case int:
		fmt.Printf("Twice %v is %v\n", v, v*2)
	case string:
		fmt.Printf("%q is %v bytes long\n", v, len(v))
```

### Control flow (if/else/for)
Go không có while, dùng for để loop đủ kiểu. Để lặp vô hạn như while, dùng `for { }`.

if cho phép định nghĩa một biến chỉ dùng trong if, khá giống với warus operator của Python 3.8.

```go
	y := 3
	if x := y + 2; x > 2 {
		println("big number")
	} else {
		println("We don't talk any more")
	}
	ns := []string{"meo", "bo", "ga"}

	for key, value := range ns {
		if len(value) < 3 {
			fmt.Printf("%d %s\n", key, value)
		}
	}
```

[https://play.golang.org/p/rHJP4ghomzo](https://play.golang.org/p/rHJP4ghomzo)

### Function
Định nghĩa function không khác Python đáng kể, ngoại trừ việc thay vì return tuple, Go có thể return nhiều giá trị (và không có kiểu tuple).

```go
func TwiceAndThrice(x int) (int, int) {
    return x * 2, x * 3
}
```

[Go không hỗ trợ overloading - một function dùng với số lượng argument khác nhau](https://golang.org/doc/faq#overloading)
, nên cũng không hỗ trợ default argument `pyfunc(x, y=10)`.

Cách duy nhất để gọi function là đưa vào các argument theo thứ tự, không
có [keyword argument như Python](https://docs.python.org/3/tutorial/controlflow.html#keyword-arguments) (`python_function(x=5, y=7)`).

Có thể dùng function làm argument của function khác, việc này rất phổ biến trong Go, khái niệm này có tên `first class function`.
Function nhận function khác làm argument được gọi là `higher order function`.

### Error handling
Go không có exception, lỗi không được xử lý khiến chương trình kết thúc qua việc gọi function "panic" (runtime error).
Ví dụ khi dùng type assertion để truy cập kiểu string dưới 1 empty interface chứa giá trị int.

```go
panic: interface conversion: interface {} is int, not string
```

Các function thay vì tạo ra exception, thường trả về giá trị Error kèm kết quả.
Ví dụ function trong package `strconv` dùng để convert string thành int:

```go
func Atoi(s string) (int, error)
```

Nếu thành công, error sẽ là `nil` còn biến kiểu int chứa giá trị, nếu s không phải dạng string của 1 số int, error sẽ có giá trị khác `nil` và thường chứa chi tiết về lỗi xảy ra. `error` là kiểu dữ liệu interface.

```go
type error interface {
	Error() string
}
```

mọi kiểu dữ liệu có method `Error()` return `string` đều có thể là 1 `error`.

Do các function đều viết theo cách này, nên code gọi 1 function trong Go thường đi kèm với 1 đoạn kiểm tra `error` ngay sau đó rồi mới xử lý giá trị nhận được:


```go
    s := "42"
    value, err := strconv.Atoi(s)
    if err != nil {
        log.Fatal(err)
    }
    println(value / 2)
```

Cách làm này gây nhiều tranh cãi, nhưng vẫn là cách làm chính thống của Go.
Go dễ dãi hơn so với Java (khi 1 function xảy ra exception gì thì phải khai báo có thể xảy ra exception, và code gọi bắt buộc phải xử lý).
Bỏ qua giá trị của `err` là chuyện hoàn toàn làm được, như viết code Python không xử lý exception, khi có error xảy ra, chương trình thường sẽ... chết.

Cách return error này không ÉP được lập trình viên phải xử lý mọi lỗi, nhưng tạo ra 1 nền văn hóa trong cộng đồng code Golang: luôn xử lý (hay ít nhất là nghĩ tới) error mọi lúc, mọi nơi.

### Import

Cú pháp tương tự Python

```
import "packagename"
import "fmt"
```

rồi gọi function qua `package.Function`, vd: `fmt.Println`

### Package & Install 3rd packages
Đầu mỗi file code Go phải bắt đầu bằng
```go
package packagename
```
Tất cả các file go trong cùng 1 thư mục (không tính thư mục con) phải khai
báo cùng package, chúng sẽ được gộp lại làm một (trừ phần import, mỗi file
phải tự import thư viện mình dùng). Có thể coi việc các file khác nhau chỉ để
thuận tiện tổ chức code, chứ vẫn là trong 1 file. Các function trong cùng 1
package (khác file) có thể gọi nhau thoải mái, không cần import lẫn nhau.

Việc này khác với Python, mỗi file.py tự động là 1 module riêng biệt.

Go cài package bằng lệnh `go get`, sau đó import tên package - là một đường dẫn theo cấu trúc URL online.

```sh
$ go get github.com/stretchr/testify/assert
```

Package "testing" của Go không có "assert", cài package từ github rồi dùng
assert.Equal để kiểm tra 2 giá trị có bằng nhau không, và message hiển thị khi chúng không bằng nhau.

```go
// main_test.go
package main

import (
	"github.com/stretchr/testify/assert"
	"testing"
)

func TestSomething(t *testing.T) {
	// assert equality
	assert.Equal(t, 123, 123, "they should be equal")
}
```

```sh
 $ go test -v
=== RUN   TestSomething
--- PASS: TestSomething (0.00s)
PASS
ok  	_/home/hvn/MyData	0.002s
```
Danh sách các package xem tại [awesome-go](https://github.com/avelino/awesome-go) và [godoc](https://godoc.org/)

### IO: read/write file
Đọc file từng dòng và ghi file:

Ghi file:

- Tạo file với os.Create, thu được 1 File struct
- Gọi method File.WriteString để ghi string

Đọc file:

- Mở file bằng os.Open, thu được 1 File struct
- Tạo 1 "Scanner" để giúp xử lý logic đọc file theo từng dòng
- Lặp qua scanner.Scan() để lấy từng dòng qua scanner.Text()

[https://play.golang.org/p/Jv80_bRJc2H](https://play.golang.org/p/Jv80_bRJc2H)

## Hành động của chúng ta

Giải bài [Project Euler 1](https://projecteuler.net/problem=1) bằng Go:

```go
package main

import "fmt"

func main() {
	sum := 0
	for i := 0; i < 1000; i++ {
		if i%3 == 0 || i%5 == 0 {
			sum = sum + i
		}
	}
	fmt.Printf("%d\n", sum)
}
```

## People & Community
Go có cộng đồng trên toàn cầu, có forum/slack/IRC để thảo luận, xem tại [help](https://golang.org/help/#help) - có cả bằng Tiếng Việt.

Những nhân vật đáng chú ý/follow trong cộng đồng Go gồm các tác giả, core dev, ...

- [Go blog](https://blog.golang.org/index)
- [Rob Pike](https://en.wikipedia.org/wiki/Rob_Pike)
- [Dave Cheney](https://dave.cheney.net/category/golang)
- [Russ Cox](https://swtch.com/~rsc/)

## Kết luận

Go là một ngôn ngữ lập trình đơn giản và thú vị, với những kiến thức trong bài này, ta đã có thể bắt đầu dùng Go để viết các chương trình không hề đơn giản.
Phần tiếp sẽ trình bày chi tiết về các khái niệm chỉ có trong Go mà không có trong Python như Pointer, sự khác biệt về cách tổ chức package trong Go, declaration & initialization (khai báo và khởi tạo variable), cùng các standard library quan trọng nhất cho một SysAdmin/DevOps.

## References
- [https://hn.algolia.com/?q=go](https://hn.algolia.com/?q=go)
- [https://hn.algolia.com/?dateRange=all&page=0&prefix=true&query=golang&sort=byPopularity&type=story](https://hn.algolia.com/?dateRange=all&page=0&prefix=true&query=golang&sort=byPopularity&type=story)
- [https://github.com/golang/go/wiki/SuccessStories](https://github.com/golang/go/wiki/SuccessStories)
- [https://blog.iron.io/go-after-2-years-in-production/](https://blog.iron.io/go-after-2-years-in-production/)
- [Notes on the Go translation of Reposurgeon - from Python](http://www.catb.org/~esr/reposurgeon/GoNotes.html)

HVN at [http://pymi.vn](http://pymi.vn) and [https://www.familug.org](https://www.familug.org).
