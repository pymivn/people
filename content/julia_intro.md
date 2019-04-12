Title: Biết Python - quen ngay Julia
Date: 2019-04-11
Category: Trang chủ
Tags: julia, python
Slug: julia_intro
Authors: hvnsweeting
Summary: Giống Python, mà nhanh gấp 2++, cũng rất gì và này nọ.

Julia là ngôn ngữ lập trình mới, trông rất giống code Python, chạy nhanh hơn Python3 [ít nhất 2 lần](https://benchmarksgame-team.pages.debian.net/benchmarksgame/faster/julia-python3.html)
và có nhiều tính năng hấp dẫn. Bạn không cần phải từ bỏ Python hay ngôn ngữ XYZ để học Julia, Julia chỉ đơn giản là một bông hoa đẹp mà ai thích... thì múc.

![Julia](https://docs.julialang.org/en/v1/assets/logo.png)

Julia là ngôn ngữ lập trình "làm gì cũng được", nhưng được tập trung vào lĩnh vực tính toán khoa học và muốn
thế chỗ Python (nhưng đường còn dài, và còn nhiều hơn trông gai).

### Cài đặt
Xem https://docs.julialang.org/en/v1/

Tại thời điểm viết bài (2019 tháng 4), Julia ở bản 1.1.0 - đã ổn định hơn trước rất nhiều, ít bug hơn, chạy nhanh hơn.

### Từ Python ngó sang

Julia trông rất giống Python, cách dùng các học, cách code cũng tương tự, nên nếu biết Python thì 
việc viết được code để làm công việc thường ngày (của 1 DevOps) chỉ trong vòng vài tiếng.

#### REPL
Gõ lệnh trực tiếp bằng lệnh `julia` trên Linux/MacOS

```julia
$ julia
               _
   _       _ _(_)_     |  Documentation: https://docs.julialang.org
  (_)     | (_) (_)    |
   _ _   _| |_  __ _   |  Type "?" for help, "]?" for Pkg help.
  | | | | | | |/ _` |  |
  | | |_| | | | (_| |  |  Version 1.1.0 (2019-01-21)
 _/ |\__'_|_|_|\__'_|  |  Official https://julialang.org/ release
|__/                   |

julia> 1 + 1
2
```

Đây gọi là chế độ "REPL" (Read-Eval-Print-Loop) == (gõ vào - chạy - in ra kết quả - cứ thế mà làm).

#### IPython
Không cần cài thêm gì, Julia REPL tự có đủ các tính năng thiết yếu của IPython.

Đọc document của 1 function? Gõ ?  rồi gõ bất cứ cái gì cần hỏi:


```julia
julia> 1 + 1
2
###### gõ ? xong , biến từ julia> thành help?>
help?> sum
search: sum sum! summary cumsum cumsum! isnumeric VersionNumber issubnormal get_zero_subnormals

...
 sum(itr)

  Returns the sum of all elements in a collection.

```

Màu mè (syntax highlight) cũng tự có sẵn rồi.

#### Chạy file code

File code Julia có đuôi `.jl`, ví dụ `hello.jl`.
Chạy file code bằng cách gõ lệnh: `julia hello.jl`

#### Cài đặt package

Để cài các package trên mạng, sử dụng package manager CÓ SẴN của Julia.
Chuyện về `virtualenv` tạm chưa bàn tới ở đây vì khá rõ ràng là không cần thiết (cài package 
[không cần gõ sudo gì cả](http://pymi.vn/blog/virtualenv/)).

Việc cài đặt package trong Julia thực hiện hơi khác so với Python Pip hay NodeJS NPM một chút.
Sẽ không có câu lệnh nào để gõ cả, không có chương trình thêm nào hết.
Julia thực hiện cài đặt package khi một đoạn code Julia được chạy (gọi function thực hiện cài đặt).

Ví dụ một file tên (tuỳ ý) như sau:

```julia
# gicungduoc.jl
using Pkg
Pkg.add("HTTP")
Pkg.add("JSON")
Pkg.add("DocOpt")

```

Chạy code này: `julia gicungduoc.jl` sẽ cài đặt các package, sau đó cứ thế mà dùng các thư viện này.

### The good, the OK, the ugly
#### The good - phần tốt
##### Pipe operator
Tốt hay xấu là tuỳ do từng người tự phán xét.
Hãy xem đoạn code sau:

Python: `''.join("  Py thon    ".strip().split())`

Julia: `"  Py thon    " |> strip |> split |> xs -> join(xs, "")`

Python

```python
def double(x):
    return x * 2
def incr(x):
    return x + 1

print(incr(double(incr(2))))
```

```julia
double(x) = x * 2
incr(x) = x + 1
println(2 |> incr |> double |> incr)
# 7
```

`|>` gọi là `Piping operator`, lấy đầu ra của function này làm đầu vào cho function khác.
Giúp việc goi funciton liên tục (và đọc nó) dễ dàng hơn.
Giống UNIX command.

##### Nhanh
Julia thường nhanh hơn Python [ít nhất 2 lần](https://benchmarksgame-team.pages.debian.net/benchmarksgame/faster/julia-python3.html)

##### Không quan trọng indentation
Dù bạn thụt ra thụt vào 2 3 4 5 ký tự, hay dùng tab đều không quan trọng.
Chuyện này vốn gây đau đầu cho không ít người dùng Python.

Python
```python
s = 0
for i in range(1000):
    if i % 3 == 0 or i % 5 == 0:
        s = s + i
print(s)
```

Julia

```julia
for i in 1:999
 if i % 3 == 0 || i % 5 == 0
   global s = s + i
 end
end
println(s)
# 233168
```

Julia dùng từ `end` để kết thúc `if` hay `for`, nên không cần thiết sử dụng dấu cách hay tab để thụt dòng.
Thậm chí có thể dùng `;` để phân cách các phần, và viết trên 1 dòng (bạn KHÔNG THỂ làm điều này với Python khi có for):

```julia
julia> s = 0; for i in 1:999; if i % 3 == 0 || i % 5 == 0; global s = s + i ; end ; end; println(s)
233168
```
##### Range bao gồm cả số kết thúc
Một điều gây khó chịu với người mới code Python là phần kết thúc của range không được tính.
Tức nếu viết `range(1,1000)` thì chỉ có từ 1 đến 999. Trong đầu luôn phải nhớ bớt đi 1.
Julia `1:999` nghĩa là 1 đến 999, không thêm bớt gì.

##### Không bị "leak" biến i trong vòng lặp ra ngoài
Đây là [1 bug của Python](https://stackoverflow.com/questions/3611760/scoping-in-python-for-loops), do sau này quá muộn để sửa, [người ta coi nó như 1 tính năng](https://www.wired.com/story/its-not-a-bug-its-a-feature/).

```python
for i in [1,2,3]:
    print(i)
print(i)  # i vốn ở trong vòng lặp for, nay thoát ra ngoài với giá trị = 3
```

##### Hỗ trợ functional
Viết map trong Julia rất dễ chịu - dễ đọc:
```
map([1,2,3]) do x
  x + 1
end
```

Cách viết dùng lambda: 
```julia
map(x -> x+1, [1,2,3])
```

sẽ tạo array chứa `[2,3,4]`

Python
```python
list(map(lambda x: x+1, [1,2,3]))
```

#### The OK - ổn
##### Index from 1
Chuyện này gây sốc với lập trình viên lâu năm C, Java, PHP, Python ...
Nhưng không phải là hiếm có. Lua, MatLab, R đều dùng index từ 1.

```julia
ns=[1,2,3,4]; print(ns[4])
```

Trong Julia code này sẽ in ra số 4 nhưng Python sẽ xảy ra exception do Python index đếm từ 0

Dùng nhiều sẽ quen và cũng không ghê gớm lắm, do Julia sử dụng cả phần cuối của range.

Ví dụ slice: Python lấy 3 số đầu tiên của list:

```python
ns[0:3]
```

Julia: 

```julia
ns[1:3]
```

Đều kết thúc là 3 - đều là số phần tử cần lấy.

Nhưng tệ hơn khi cần lấy 2 phần tử cuối:

```julia
ns[end-1:end]
```
`end` là một index magic (tự xuất hiện), đại diện cho index của phần tử cuối cùng.

Trong ví dụ này gõ số 4 thay end cũng được.

#### The ugly - thảm hại
Unicode string - sẽ rất đau đầu khi chuyển từ Python sang.

Index của string (mặc định Unicode) trong Julia là byte index, không phải index theo thứ tự của ký tự.

Python
```python
In [16]: w = "Điêu"

In [20]: w[0],w[1]
Out[20]: ('Đ', 'i')
```

Julia 
```julia
ulia> w = "Điêu"
"Điêu"

julia> w[1]
'Đ': Unicode U+0110 (category Lu: Letter, uppercase)

julia> w[2]
ERROR: StringIndexError("Điêu", 2)
Stacktrace:
 [1] string_index_err(::String, ::Int64) at /nix/store/2fmf5sqi0jx5zdlqx0gpw2m6nrsbcch2-julia-1.0.1/lib/julia/sys.dylib:?
 [2] getindex_continued(::String, ::Int64, ::UInt32) at /nix/store/2fmf5sqi0jx5zdlqx0gpw2m6nrsbcch2-julia-1.0.1/lib/julia/sys.dylib:?
 [3] getindex(::String, ::Int64) at /nix/store/2fmf5sqi0jx5zdlqx0gpw2m6nrsbcch2-julia-1.0.1/lib/julia/sys.dylib:?
 [4] top-level scope at none:0

julia> w[3]
'i': ASCII/Unicode U+0069 (category Ll: Letter, lowercase)
```

Do chữ `Đ` trong Unicode UTF-8 được biểu diễn bằng 2 byte, ta chỉ có thể truy cập 
được index 1, không truy cập được index 2. Và chữ `i` ngay sau `Đ` sẽ là index 3.

#### Exception
TBD


#### Chú ý
- Julia khởi động mất 0.2-0.4 giây, Python khởi động nhanh gấp 10.
- String trong Julia phải dùng double quote `""`, single quote `''` dành cho ký tự (Char).
- Nối string dùng `*` chứ không phải `+`.
- Sẽ không có method gắn liền vào các object như string hay list trong Python,
  thay vào đó là các function có sẵn (thường không cần import, gọi là trong [Base](https://docs.julialang.org/en/v1/base/base/))

### Ví dụ 1 chương trình CLI nhận argument, gọi HTTP với JSON

```julia
import HTTP
import JSON
using DocOpt  # import docopt function

function main()
    doc = """Fist Julia program which makes HTTP requests to httpbin endpoint

    Usage:
      main.jl request <endpoint>

    Options:
      -h --help     Show this screen.
      --version     Show version.
    """

    args = docopt(doc, version=v"0.0.1")
    endpoint = args["<endpoint>"]
    url = "https://httpbin.org/$endpoint"
    println("Accessing $url")
    resp = HTTP.get(url)
    d = JSON.Parser.parse(String(resp.body))
    println("My IP is " * d["origin"])

    println("Now also send post")
    r = HTTP.request("POST", "https://httpbin.org/post",
            ["Content-Type" => "application/json"],
            JSON.json(Dict('a'=>2, 'b'=>3))
            )
    data = JSON.Parser.parse(String(r.body))

    open("/tmp/data.json", "w") do f
        write(f, JSON.json(data["json"]))
    end
    open("/tmp/data.json", "r") do f
        d = JSON.Parser.parse(String(read(f)))
        println(d)
    end

    open(`ls -l`) do io
        for line in eachline(io)
            if !isa(match(r".*\.jl", line), Nothing)
                println(line)
            end
        end
    end
end

main()
```

Chạy

```
$ julia  main.jl  -h
Fist Julia program which makes HTTP requests to httpbin endpoint

Usage:
  main.jl request <endpoint>

Options:
  -h --help     Show this screen.
  --version     Show version.

$ julia main.jl request ip
Accessing https://httpbin.org/ip
My IP is 3.117.2.254, 3.117.2.254
Now also send post
Dict{String,Any}("b"=>3,"a"=>2)
-rw-r--r-- 1 viethung.nguyen viethung.nguyen 1189 Apr 12 08:38 main.jl
```

Code hoàn toàn tương đương với code Python.

### Kết luận
Còn chờ gì nữa?
Làm tí Julia thôi.

Phần tiếp theo (nếu có) sẽ đi vào các tính năng của Julia sử dụng trong tính toán khoa học.

### Tham khảo
- [https://docs.julialang.org/en/v1/](https://docs.julialang.org/en/v1/)
- [https://en.wikibooks.org/wiki/Introducing_Julia](https://en.wikibooks.org/wiki/Introducing_Julia)
- [https://lectures.quantecon.org/jl/](https://lectures.quantecon.org/jl/)