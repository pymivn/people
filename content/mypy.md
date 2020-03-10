Title: Mypy - là trai hay là gái?
Date: 2020-03-10
Category: Trang chủ
Tags: python, mypy,
Slug: mypy
Authors: hvnsweeting
Summary: Là bạn hay là bè? là str hay int? Thêm type cho Python code mà không ho, không sốt, không toang.

Vài ba năm gần đây, làng Vũ Trụ rộn lên trào lưu thêm "type" vào các ngôn ngữ lập trình dynamic typing.

- [PHP](https://www.php.net/manual/en/functions.arguments.php#functions.arguments.type-declaration)
- [JavaScript|TypeScript](https://www.typescriptlang.org/)

Python đã già nhưng vẫn đú, cũng không bỏ lỡ cuộc đu trend này.
Kết quả là ngày hôm nay, bạn đã có thể thêm type vào code Python -
nếu muốn - như [DropBox](https://blogs.dropbox.com/tech/2019/09/our-journey-to-type-checking-4-million-lines-of-python/), [Instagram](https://instagram-engineering.com/let-your-code-type-hint-itself-introducing-open-source-monkeytype-a855c7284881)... . Python chính thức thêm [type hint/type annotation](https://www.python.org/dev/peps/pep-0484/)
vào từ bản 3.5,
chú ý rằng type này không ảnh hưởng/giúp đỡ gì bạn, nếu không sử dụng mypy hay
các IDE.

Mypy là static type checker - tool giúp phân tích code (static analysis) dựa trên type annotation, dự
án có sự tham gia của tác giả Python - Guido van Rossum, ... và cả [HVN](https://github.com/python/mypy/pull/4594)

## Thêm type để làm gì?
Các ngôn ngữ lập trình dynamic typing: Python, JavaScript, PHP, Ruby được
ưa chuộng và luôn chiếm vị trí top các bảng xếp hạng ngôn ngữ lập trình trong
những năm gần đây, hay Clojure, LISP, Erlang, Elixir... dù không lên đỉnh nhưng
vẫn luôn hot.
Dynamic typing giúp code trở nên ngắn gọn và linh hoạt.
Vậy thêm type (kiểu) làm gì? không lẽ để dài hơn và bớt linh hoạt hơn?

Code dài dòng thêm thì rõ là không ai muốn, bởi nếu muốn đã quay về viết Java
hết rồi, nhưng bớt linh hoạt hơn là một mục đích đáng xem xét.

Khi mọi thứ linh hoạt, nếu không tuân theo các quy tắc, không có kỷ luật cá nhân
tốt, sẽ dẫn tới rối loạn. Hoặc khi hệ thống trở nên phức tạp hơn,
nhiều tính năng phụ thuộc vào nhau, cũng dẫn tới việc không kiểm soát được.

Điều này sẽ dễ thấy hơn khi tham gia một dự án có nhiều lập trình viên.
Một team 5 Python dev làm việc đã quen với nhau, code
cùng chuẩn PEP8, cùng không thích OOP, ... hay nói cách khác là một team thực
thụ, sẽ code nhanh như tên lửa, vài giờ một tính năng, bay vèo vèo như
[YouTube dev](https://books.google.com.vn/books?id=eulODwAAQBAJ&lpg=PA136&dq=google+video+vs+youtube+python+story&pg=PA136&redir_esc=y#v=onepage&q=google%20video%20vs%20youtube%20python%20story&f=false) .

Một nhóm người khác với 5 lập trình viên, học
lập trình từ các nguồn khác nhau, trình độ khác nhau, thậm chí ngôn ngữ thành
thạo cũng khác nhau, nếu làm cùng một dự án sẽ rất rối loạn.
Có chỗ viết 3 class để gọi 1 function cho đúng chuẩn kế thừa, OOP của Java,
có function viết theo kiểu recursive, có chỗ đặt tên biến một chữ cái,
không viết function, một hàm main dài hàng trăm dòng,
function mỗi nhánh trả về một kiểu khác, viết decorator chỉ để dùng 1 lần và
thể hiện, sửa một function rồi các function khác hỏng theo... và hàng trăm thứ
khác có thể sai hơn nữa. Một team như vậy phát
triển sẽ rất chậm, nhiều bug, khó thêm tính năng,
thậm chí gây mệt mỏi, stress khi phải làm việc với nhau. Giải pháp thì lại
không thể là giải tán, cãi nhau, vậy làm gì?

Type là một phần giải pháp, type giúp đặt ràng buộc rõ ràng đầu vào đầu ra,
đảm bảo một function luôn trả về cùng 1 kiểu dù ở nhánh nào. Function
là kiến trúc cơ bản của 1 chương trình, một hệ thống. Khi function định nghĩa
rõ ràng, các bên tương tác (gọi function) với nhau cũng sẽ rõ ràng.
Nhân viên mới tuyển, sinh viên mới ra trường,
vào sửa function trả về nhầm kiểu sẽ bị type bắt lại ngay.

- Type là một thứ CÔNG CỤ giúp giảm sự linh hoạt của code, tăng thêm kỷ luật,
đảm bảo code ít bị rối loạn hơn. Nếu code 1 mình, hay bạn chắc chăn mình và
**các đồng nghiệp** đủ kỷ luật để không viết function trả về các kiểu khác nhau
thì type cũng không cần thiết.
- Type không nên là thứ can thiệp/cản trở nhiều vào mục đích của lập trình viên.
Ta muốn có công cụ trợ giúp, chứ không muốn nó chống lại mình. Type dài dòng
như của Java là một ví dụ điển hình khiến việc viết code cũng trở nên ngại.

## Sử dụng mypy

### Cài đặt

```
pip install mypy
```

#### Ví dụ 1 - đơn giản để bắt đầu

Ví dụ 1: đoạn code không có type:

File `mypy_simple.py`

```python
def sum_of_three(a, b, c):
    result = a + b + c
    return result

def main():
    result = sum_of_three(6, 9, 6) * 2
    message = "The answer of life: " + result
    print(message)

main()
```

Chạy mypy:

```sh
$ mypy mypy_simple.py
Success: no issues found in 1 source file
```

Không có gì xảy ra, do không function/name nào có type annotation cả.
Mặc định này giúp việc thêm type là tùy ý. Team có thể có người viết type,
có người không ở các function khác nhau, đều OK. Nếu cực nghiêm khắc,
có thể bật chế độ strict lên:

```sh
$ mypy --strict mypy_simple.py
mypy_simple.py:1: error: Function is missing a type annotation
mypy_simple.py:5: error: Function is missing a return type annotation
mypy_simple.py:5: note: Use "-> None" if function does not return a value
mypy_simple.py:6: error: Call to untyped function "sum_of_three" in typed context
mypy_simple.py:10: error: Call to untyped function "main" in typed context
Found 4 errors in 1 file (checked 1 source file)
```

Ở chế độ này, mọi thứ thiếu type annotation đều bị thông báo, đây chỉ là ví dụ
cực đoan, phải tốn khá nhiều công sức và làm quen mới có thể bật chế độ này lên,
vậy nên khó quá tạm thời bỏ qua.

Thêm type cho đoạn code trong ví dụ 1:
với Python type annotation, ta thường chỉ thêm cho định nghĩa của các function,
ít khi phải khai báo cho các variable. Ví dụ trên có 2 function, sau khi thêm
type vào `sum_of_three` sẽ trông như sau:

```python
def sum_of_three(a: int, b: int, c: int) -> int:
    result = a + b + c
    return result

def main() -> None:
    result = sum_of_three(6, 9, 6) * 2
    message = "The answer of life: {}".format(result)
    print(message)
```

3 argument đều có kiểu là `: int`, `-> int` nói rằng function này
trả về kiểu `int`.
Chạy lại lệnh mypy

```
$ mypy mypy_simple.py
Success: no issues found in 1 source file
```

Vẫn trông như không có gì xảy ra, nhưng thật ra là có, do code của ta không
có vấn đề gì nên mypy cũng không báo gì. Thử đổi trong function `main`,
cộng kết quả của `sum_of_three` (kiểu int) với một `str`:

```py
def main() -> None:
    result = sum_of_three(6, 9, 6) * 2
    message = "The answer of life: " + result
    print(message)
```

Nếu là lập trình viên JavaScript, bạn sẽ mong đợi một kết quả str bình thường,
`"The answer of life: 42"`, bởi JavaScript thuộc loại weak typing,
còn Python là strong typing: int là int, str là str, không cộng trừ lẫn lộn.

Nếu là một PyMier chân chính, bạn sẽ nhận ra ngay đoạn code này gặp exception
khi CHẠY THẬT, do cộng một str với một số int.

```sh
$ python mypy_simple.py
Traceback (most recent call last):
  File "mypy_simple.py", line 12, in <module>
    main()
  File "mypy_simple.py", line 8, in main
    message = "The answer of life: " + result
TypeError: must be str, not int
Command exited with non-zero status 1
```

Vậy ta chỉ biết, khi chạy thật, mà lúc ấy mới biết thì "toang" rồi.
Có cách nào **biết trước** khi chạy không? Mypy sẽ giúp làm chuyện ấy:

```
$ mypy mypy_simple.py
mypy_simple.py:8: error: Unsupported operand types for + ("str" and "int")
Found 1 error in 1 file (checked 1 source file)
```

Chú ý: việc phân tích function main chỉ xảy ra khi nó có type annotation:

```python
def main() -> None:
```

Function main không nhận argument, trả về kiểu None. Nếu bỏ `-> None` đi,
mypy sẽ không kiểm tra function main.

#### Ví dụ 2 - các containers: list, tuple, dict, set

```python
from typing import List, Tuple

def with_index(names: List[str]) -> List[Tuple[int, str]]:
    return [(idx, name) for idx, name in enumerate(names)]

def main() -> None:
    result = 21 * 2

    result = with_index(["Corona", "Tiger Nau", "TrucBach"])
    print(result)

main()
```
Chỉ có str, int, float, bool, None là các kiểu dùng ngay.
Với list, tuple, set, dict, cần phải import type tương ứng
từ standard lib `typing`, các type viết Hoa chữ cái đầu.
Có thể khai báo qua loa
`def with_index(names: List) -> List:`
hoặc chi tiết như trong ví dụ 2.

```sh
$ mypy mypy_simple.py
mypy_simple.py:11: error: Incompatible types in assignment (expression has type "List[Tuple[int, str]]", variable has type "int")
```

Lỗi này thường gặp, do chuyện dùng chung tên `result`,
mypy lần đầu gặp sẽ nghĩ `result` là kiểu `int`, qua dòng tiếp
theo lại suy luận nó được gán giá trị kiểu `List[Tuple[int, str]]`. Việc dùng
một biến để chỉ tới nhiều kiểu khác nhau không hiếm trong dynamic typing, nhưng
là chuyện không thể trong các ngôn ngữ static typing. Cách giải quyết chuẩn
nhất là đổi tên biến.

#### Ví dụ 3 - các object phức tạp, thư viện bên ngoài
Với các lập trình viên Python, type là một thứ lạ, vậy nên không phải dẽ gì ngồi đọc ngay ra kiểu của `resp` sau đây là gì mà gõ vào:

```python
from typing import Any
import requests

def process_response(resp: Any, msg: str = 'From: ') -> str:
    return msg + resp.json()['origin']

r = requests.get('https://httpbin.org/ip')
output = process_response(r)# + 10
print(output)
```

`Any` giúp điền vào chỗ trống khi không biết kiểu gì, đồng nghĩa
với việc mất đi một chút bảo vệ của mypy do mypy sẽ cho phép gọi
function `process_response` với argument đầu tiên thuộc bất kỳ kiểu nào.

`msg: str = 'From: '` là argument `msg`, kiểu `str`, với giá trị
default `From: `.

```
$ python mypy_simple.py
From: 111.212.107.29
```

Có một cách khác để nhờ mypy tìm giúp kiểu của `resp`, đó là khai báo sai kiểu,
thay `Any` thành `int`, chạy mypy sẽ thấy:

```
$ mypy mypy_simple.py
mypy_simple.py:5: error: "int" has no attribute "json"
mypy_simple.py:8: error: Argument 1 to "process_response" has incompatible type "Response"; expected "int"
Found 2 errors in 1 file (checked 1 source file)
```

Vậy kiểu của `resp` cần khai báo là Response, đầy đủ là `requests.models.Response`
có thể tìm ra bằng cách `print(type(r))`

#### Ví dụ 4 - function nhận vào nhiều kiểu

Cũng có lúc, ta muốn chủ ý nhận vào nhiều loại input khác kiểu,
nhưng chỉ giới hạn trong 1 nhóm, ví dụ như int, str, float, chứ không phải dict
hay list, nếu dùng `Any` thì dễ dãi quá:

```python
def any_number(n: int) -> str:
    return "This is {}".format(n)

any_number(6)
any_number("9")

### mypy check
error: Argument 1 to "any_number" has incompatible type "str"; expected "int"

```

Giải pháp là dùng Union.

```python
from typing import Union

def any_number(n: Union[int,float,str]) -> str:
```

Các kiểu type khác: [https://mypy.readthedocs.io/en/stable/kinds_of_types.html]( https://mypy.readthedocs.io/en/stable/kinds_of_types.html) đáng chú ý như Optional khi có thể trả về None, hay Callable là kiểu cho
function.

### Stub

```python
import boto3
```

```
mypy mypy_simple.py
mypy_simple.py:1: error: No library stub file for module 'boto3'
mypy_simple.py:1: note: (Stub files are from https://github.com/python/typeshed)
```

Sau khi Python chính thức thêm type notation, không có nghĩa là các core developer sẽ đi sửa hàng loạt các file thư viện đã chạy ổn định vài chục năm để
thêm type. Thay vào đó, họ tạo ra các stub file.
stub file là file chứa type annotation của các function trong library. Nó tương tự header file trong C/C++.

Ví dụ [itertools](https://github.com/python/typeshed/blob/master/stdlib/3/itertools.pyi)

Các stub file của Python standard lib được gom lại tại [python/typeshed](https://github.com/python/typeshed).

Các thư viện bên ngoài thường ít khi có sẵn stub file,
Ví dụ như `boto3` - thư viện cực kỳ phổ biến - và chính thức để làm việc với
API của AWS, tới nay vẫn chưa có stub file chính thức từ AWS.
Nên để đơn giản, thay vì phải chiến đấu với type, ta có thể bỏ qua:

```
$ mypy --ignore-missing-import .
```

hay tự tạo stub như [htlcnn](https://github.com/htlcnn/autocad_objectarx_python_stubs).
Xem hướng dẫn tự tạo stub file tại [mypy wiki](https://github.com/python/mypy/wiki/Creating-Stubs-For-Python-Modules)

### Những vấn đề type giúp giải quyết
- Kiểm tra kiểu, đảm bảo function trả về thống nhất một kiểu, nhận được đúng
  kiểu đầu vào.
- Giúp nhìn vào dòng def (thuật ngữ chính xác: function signature) là biết luôn
  cần gọi với argument nào, trả về kiểu gì.

### Những vấn đề type KHÔNG giúp giải quyết
- Thay cho unittest: unittest dùng để kiểm tra logic chứ không phải để kiểm tra kiểu. Do không có ràng buộc về kiểu, nên trong unittest thường kiểm tra cả kiều của đầu ra function, việc này hoàn toàn bị loại bỏ khi dùng mypy.
- Làm việc nhóm không hiệu quả: type chỉ là một phần giải pháp giúp xóa bớt sự
chênh lệch trình độ giữa các lập trình viên. Bạn nên tìm cách đào tạo, chia sẻ
kinh nghiệm, luyện tập cùng các đồng nghiệp thì hơn.

### Hành động của chúng ta
Thêm ngay dòng sau vào Makefile, hay hệ thống CI của bạn, ngay sau pep8, flake8 hay pylint:

```
mypy --ignore-missing-import .
```

## Kết luận
Type là một công cụ tốt cho các Pythonista như pylint pep8, giúp phát triển các dự án lớn hơn,
nhiều người tham gia một cách dễ dàng hơn, trong khi việc đầu tư thì không có
gì to tát cả - chỉ việc share bài viết này.
