Title: Free variable
Date: 2021-06-07
Category: Trang chủ
Tags: python,
Slug: free
Authors: hvnsweeting
Summary: tự do như biến

Python có 2 loại variable (biến): local, global, và free (đếm từ 0, tất nhiên).

![free](https://images.unsplash.com/photo-1546672117-f83291ce87a9?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=MnwyMzI1MzN8MHwxfHJhbmRvbXx8fHx8fHx8fDE2MjMwNzQxNTI&ixlib=rb-1.2.1&q=80&w=600)

## 3 loại variable trong Python

### binding
`x = 42` trong Python đọc là bind name x tới object 42.
Tham khảo thêm tại bài [Python call by gì?](https://pymi.vn/blog/call-by/)

### global variable
Đoạn code sau

```py
print(x)
x = 42
```

`x` viết sát lề, gọi là global variable. Chạy đoạn code trên sẽ hiện ra
exception:

```py
NameError: name 'x' is not defined
```

do code dùng x trước khi x được bind tới object 42.

### local variable
Đoạn code tiếp theo, chạy sẽ thấy gì? Gợi ý: không phải NameError:

```py
def foo():
    print(x)
    x = 42

foo()
```

`x = 42` nằm trong 1 block (trong thân function hay class), gọi là local variable.
Trong 1 block, dùng 1 variable/name trước khi bind nó (tức là có bind, nhưng
bind sau khi dùng), exception sẽ xảy ra là

```py
UnboundLocalError: local variable 'x' referenced before assignment
```

### free variable
```py
def foo():
    print(x)

foo()
```
Xóa `x = 42` trong ví dụ phần local, ta chạy đoạn code này, lại thấy NameError.
```py
NameError: name 'x' is not defined
```

Lần này không xảy ra UnboundLocalError, do đoạn code không bind x = 42
trong thân function (block). `x` ở đây là một free variable.

Free variable hoạt động theo cách ... rất tự do:

```py
x = 42
def foo():
    print(x)

x = 96
foo()
```
Màn hình sẽ hiện ra `42` hay `96`?

Việc tính toán tên `x` có giá trị gì, được thực hiện khi function **CHẠY**.
Khi gọi `foo()` ở trên, x đã có giá trị là 96.


## Static analysis
Việc dùng các công cụ (phần mềm/chương trình) để phân tích/tìm lỗi code bằng
cách đọc code (text) - mà không cần chạy code, gọi là static analysis.
Trong Python phổ biến các công cụ như `pep8`, `flake8`, `pylint`, [`mypy` cũng
có thể tính luôn](https://pp.pymi.vn/article/mypy/), hay các tính năng
tích hợp sẵn của IDE như Pycharm.

`flake8` cơ bản giống `pep8` (tên mới là `pycodestyle`), thêm tính năng phát
hiện thư viện không dùng tới/ hay biến không tồn tại.

```py
import math
def foo():
    print(x)
    x = 42
foo()
```

khi chạy `flake8` với file code, `flake8` sẽ phát hiện ra thư viện
`math` được import nhưng không dùng, tên `x` chưa được định nghĩa.

```py
$ flake8 scope.py
scope.py:1:1: F401 'math' imported but unused
scope.py:5:11: F821 undefined name 'x'
scope.py:6:5: F841 local variable 'x' is assigned to but never used
```

`flake8` rất hữu ích khi dễ dàng phát hiện các lỗi đơn giản như gõ nhầm tên
biến hay dùng biến không tồn tại như trên.
Nhưng khi `x` là free variable, không công cụ nào của Python có thể phát hiện
ra lỗi này cho tới khi chạy mới thấy exception:

```py
def n_pymi_vn() -> int:
    s = x + 1
    return s

r = n_pymi_vn()
x = 10
print(r)
```

Do `x` là free variable, các công cụ phải quét hết cả file code để tìm `x`,
và nó tìm thấy, nên tin rằng `x` có tồn tại, nhưng đã quá muộn rồi.
Một ví dụ vô lý hơn nữa, để thấy sự bất lực của các công cụ static analysis:

```py
def n_pymi_vn() -> int:
    s = x + 1
    return s

if 1 > 10:
    x = 10
r = n_pymi_vn()
print(r)
```

## Hành động của chúng ta
Hạn chế hết mức việc sử dụng global variable, free variable, cần biến gì thì
đưa argument vào function biến đó, code "sát tường" cho hết vào 1 function
main và gọi main() nếu cần chạy.

## Kết luận
Tính dynamic của Python khiến các công cụ khó có thể xử lý mọi trường hợp,
công cụ sẽ chỉ giúp một phần, phần còn lại là sự cẩn thận của lập trình viên.

Tự do phải chăng cần trong khuôn khổ?

## Tham khảo
- [https://docs.python.org/3/reference/executionmodel.html#interaction-with-dynamic-features](https://docs.python.org/3/reference/executionmodel.html#interaction-with-dynamic-features)
