Title: Học Haskell không phải trầm trồ - theo cách Pymi.vn
Date: 2021-06-10
Category: Trang chủ
Tags: haskell
Slug: haskell1
Authors: hvnsweeting
Summary: ngôn ngữ lập trình luôn được xếp vào nhóm "khó học nhất" - giống Python bất ngờ.

- Cảnh báo: rất giống Python
- Chú ý: không cần biết Python

Haskell (/ˈhæskəl/) - visub: ha-s-kồ - 1990.

Trang chủ: [https://www.haskell.org/](https://www.haskell.org/)

Haskell là ngôn ngữ functional (lập trình hàm), thuộc nhóm "pure" blah blah blah
có thể bỏ qua và gõ cho đến cuối bài, work first, talk cheap, later.

## Cài đặt
Hướng dẫn [trang chủ](https://www.haskell.org/downloads/#linux-mac-freebsd), hỗ trợ cả Windows
```sh
curl --proto '=https' --tlsv1.2 -sSf https://get-ghcup.haskell.org | sh
```
enter enter enter ... rồi mở terminal mới, gõ `ghci`.

```
ghci --version
The Glorious Glasgow Haskell Compilation System, version 8.10.5
```

## REPL

```hs
$ ghci
GHCi, version 8.10.5: https://www.haskell.org/ghc/  :? for help
Prelude> 1 + 1
2
Prelude> 2 * 1024
2048

Prelude> :quit
Leaving GHCi.
```

## Haskell Hello world
```sh
Prelude> print "Hello Pymier!"
"Hello Pymier!"
```

## Integer
cộng `+` trừ `-` nhân `*` mũ/lũy thừa `^`

```sh
Prelude> 54 + 5 * (2 + 1)
69
Prelude> 2 ^ 1000
10715086071862673209484250490600018105614048117055336074437503883703510511249361224931983788156958581275946729175531468251871452856923140435984577574698574803934567774824230985421074605062371141877954182153046474983581941267398767559165543946077062914571196477686542167660429831652624386837205668069376
```

## Float

```hs
Prelude> 4 / 2
2.0
Prelude> 5 / 2
2.5
Prelude> 5 / 2.5
2.0
Prelude> 0.1 + 0.1 + 0.1
0.30000000000000004

Prelude> 0.1 + 0.1 + 0.1 == 0.3
False
Prelude> 0.1 + 0.1 + 0.1 /= 0.3
True
```

[0.1 + 0.1 + 0.1 /= 0.3](https://pymi.vn/blog/why-not-float/)

## Boolean

```sh
Prelude> 2 < 5
True
Prelude> 2 > 5
False
Prelude> 1 + 1 == 2
True
Prelude> 2 - 1 /= 0
True
Prelude> 2 <= 2
True
Prelude> 1/0
Infinity
```


```sh
Prelude> True && True
True
Prelude> True && False
False
Prelude> False && True
False
Prelude> False && False
False
```

Haskell boolean có tính [short-circuit](https://pymi.vn/tutorial/boolean/) - dừng lại ngay khi có thể.
Đây là điều hiển nhiên nhờ một tính năng nổi bật của Haskell: **Lazy**.

## type
Các câu lệnh trong `ghci`

- `:help`
- `:info`
```hs
Prelude> :info mod
type Integral :: * -> Constraint
class (Real a, Enum a) => Integral a where
  ...
  mod :: a -> a -> a
  ...
  	-- Defined in ‘GHC.Real’
infixl 7 `mod`

Prelude> :info (+)
type Num :: * -> Constraint
class Num a where
  (+) :: a -> a -> a
  ...
  	-- Defined in ‘GHC.Num’
infixl 6 +
```

Hiển thị type:
```hs
Prelude> :set +t

Prelude> 1
1
it :: Num p => p

Prelude> 0.1
0.1
it :: Fractional p => p

Prelude> True
True
it :: Bool

Prelude> "ahihi PyMi.vn"
"ahihi PyMi.vn"
it :: [Char]

Prelude> [1..10]
[1,2,3,4,5,6,7,8,9,10]
it :: (Num a, Enum a) => [a]
```

`it` là biểu thức/kết quả cuối cùng bạn đã gõ. Tương tự `_` trong Python interpreter.
```hs
Prelude> 1
1
it :: Num p => p
Prelude> it + 2
3
it :: Num a => a
```

## ProjectEuler problem 1
https://projecteuler.net/problem=1

> If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
> Find the sum of all the multiples of 3 or 5 below 1000.

Tạo list các số từ 1 đến 5
```hs
Prelude> [1..5]
[1,2,3,4,5]
```

Haskell không dùng `%` cho phép chia lấy phần dư (modulo/remainder), code Python `10 % 3` tương đương với viết Haskell `mod 10 3`

Haskell dùng `|| &&` thay Python `or and`

[Python 2.0 **MƯỢN** list comprehension từ Haskell](https://docs.python.org/3/whatsnew/2.0.html#list-comprehensions)

```py
>>> sum([i for i in range(1000) if i % 3 == 0 or i % 5 == 0])
233168
```

Haskell dùng `|` thay chữ `for`, dùng `<-` thay chữ `in`, dùng `,` thay chữ `if` so với Python

```hs
Prelude> sum [i | i <- [1..999], mod i 3 == 0 || mod i 5 == 0]
233168
```

## Các đặc tính nổi biệt của Haskell
https://wiki.haskell.org/Introduction

> Haskell is a computer programming language. In particular, it is a polymorphically statically typed, lazy, purely functional language, quite different from most other programming languages. The language is named for Haskell Brooks Curry, whose work in mathematical logic serves as a foundation for functional languages. Haskell is based on the lambda calculus, hence the lambda we use as a logo.

- polymorphically statically typed
- lazy
- purely functional

hoặc xem phần features trên https://www.haskell.org/

### lập trình hàm là gì
Haskell là ngôn ngữ thuộc nhóm functional (lập trình hàm).

Trên lý thuyết,
có nghĩa nó dựa trên một nhóm lý thuyết có tên ["lambda calculus"](https://wiki.haskell.org/Lambda_calculus), một mô hình/hệ thống
tính toán dựa trên các function (hàm toán học), khác với mô hình các ngôn ngữ lập trình
C, Java, Python, Go... dựa trên gọi là Turing Machine.
Hai mô hình này được chứng minh về mặt toán học là có khả năng như nhau.

Về mặt thực hành, code với 1 ngôn ngữ functional thường có nghĩa là:
- không dùng vòng lặp for/while mà dùng các function có sẵn để làm việc tương tự
(vd: map, filter, fold, reduce,...) hoặc viết các [recursive function](https://pymi.vn/blog/print-recursively/) để thu được
kết quả tương ứng.
- Các kiểu dữ liệu thường là immutable, tức thay vì thay đổi 1 list, Haskell sẽ
tạo ra 1 list mới với những thay đổi đã thực hiện (và bỏ list cũ đi).

### Haskell purely functional là gì
pure function là một function không có "side effect". Side effect là việc
function thực hiện 1 thay đổi nào đó (thay đổi phần tử 1 list, đọc ghi 1 file,
in ra màn hình, kết nối internet, ...) nghe hơi vô lý nhưng Haskell sẽ dựa trên
1 khái niệm/cơ chế hoàn toàn khác để thực hiện các việc nói trên.

### Haskell lazy là gì
lazy là việc function chỉ thực hiện tính toán khi thực sự cần tới giá trị.
Ví dụ có thể viết code tạo ra 1 list từ 1 tới vô cùng, nhưng vì Haskell lazy,
nó chỉ lấy ra phần tử nó cần, chứ không tạo list từ 1 tới vô hạn từ đầu.

```hs
Prelude> take 10 [1..]
[1,2,3,4,5,6,7,8,9,10]
Prelude> take 20 [1..]
[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
```
## Kết luận
Ngày đầu của Haskell không hề khó hơn ngày đầu học Python. Đừng vì "cộng đồng
mạng" nói khó mà chưa thử đã tin!

## Tham khảo
- https://pymi.vn/tutorial/python-integer/
- https://pymi.vn/tutorial/python-calculation-2/
- [Rrealworldhaskel](http://book.realworldhaskell.org/read/getting-started.html)
