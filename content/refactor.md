Title: Refactor 10 dòng code thành 90 dòng
Date: 2023-05-09
Category: Trang chủ
Tags: python, refactor, software engineering, test, rust
Slug: refactor
Authors: hvnsweeting
Summary: refactor không phải để code ngắn đi

Refactor là một phần công việc không thể thiếu của lập trình viên, sau khi code xong chạy được mà "chưa đẹp", lập trình viên sẽ chỉnh sửa đoạn code cho "đẹp" hơn, cũng có thể nhanh hơn, cũng có thể ngắn hơn, cũng có thể dễ hiểu hơn...

Vấn đề với refactor: là một khái niệm chung chung, không có ví dụ cụ thể, khó học/luyện tập để trở thành 1 kỹ năng. Best-practice của ngôn ngữ này lại có thể là điều không ai làm ở ngôn ngữ khác. Sách vở viết về refactor cũng chỉ có 1 quyển được cộng đồng mạng nhắc tới ?!!! [Refactoring - Improving the Design of Existing Code by Martin Fowler, with Kent Beck, 2018](https://martinfowler.com/books/refactoring.html).  PyMi cũng từng có 1 bài viết giới thiệu việc [refactoring code kèm với IPython]({filename}/repl.md).

<center>
![Refactor](https://images.unsplash.com/photo-1545697729-0ab8f5b1954c?ixlib=rb-4.0.3&q=85&fm=jpg&crop=entropy&cs=srgb&dl=zoltan-tasi-CLJeQCr2F_A-unsplash.jpg&w=640)

Photo by <a href="https://unsplash.com/@zoltantasi?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Zoltan Tasi</a> on <a href="https://unsplash.com/photos/CLJeQCr2F_A?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash</a></center>

Bài viết này dựa trên chapter 12 trong cuốn [The Rust Programming Language](https://doc.rust-lang.org/book/ch12-03-improving-error-handling-and-modularity.html) (còn hay gọi là **The book**), kèm phóng tác, chuyển dịch sang Python, thêm "bình phẩm" và nhiều nhiều câu hỏi. Sử dụng ví dụ từ sách Rust khiến người đọc có thể tin cậy trình độ của tác giả... Steve Klabnik, Carol Nichols - những cái tên nổi tiếng bậc nhất trong thế giới Rust.

### Refactoring là gì
Trong tiếng Anh, refactoring có nghĩa:

[cambridge](https://dictionary.cambridge.org/dictionary/english/refactoring):

> refactoring isn’t in the Cambridge Dictionary yet. You can help!

[dictionary.com](https://www.dictionary.com/misspelling?term=refactoring):

> No results found for refactoring

theo từ điển tiếng Anh, từ **refactoring** không tồn tại.

Theo [Wikipedia](https://en.wikipedia.org/wiki/Code_refactoring):

> In computer programming and software design, code refactoring is the process of restructuring existing computer code—changing the factoring—without changing its external behavior

là việc chỉnh sửa lại code đã tồn tại mà không thay đổi tính năng của code.

Theo quảng cáo của cuốn sách về [Refactoring](https://martinfowler.com/books/refactoring.html) nối tiếng nhất:
> Refactoring is a controlled technique for improving the design of an existing code base. Its essence is applying a series of small behavior-preserving transformations, each of which "too small to be worth doing". However the cumulative effect of each of these transformations is quite significant. By doing them in small steps you reduce the risk of introducing errors. You also avoid having the system broken while you are carrying out the restructuring - which allows you to gradually refactor a system over an extended period of time.

Ở đây dùng **refactoring** như 1 danh từ, **refactor** như 1 động từ.

### Refactoring để làm gì
Refactor để cải thiện, nâng cao

- Tính dễ bảo trì, fix bug: Maintainability.
- Tính dễ mở rộng/thay đổi: Extensibility.
- Tốc độ chạy: Performance.

### Ví dụ refactor 10 dòng code
Viết 1 chương trình giống như câu lệnh grep trên UNIX, tức nhận 2 đầu vào trên dòng lệnh là "từ khóa tìm kiếm" và tên file, in ra màn hình các dòng chứa từ khóa ấy.
Ví dụ tìm từ `root` trong file `/etc/passwd` trên Ubuntu, MacOS,...

```sh
$ grep root /etc/passwd
root:x:0:0::/root:/bin/bash
```

Code Python 10 dòng, không tính ngoài function main, dịch trực tiếp từ [ví dụ Rust](https://doc.rust-lang.org/book/ch12-00-an-io-project.html):

```py
# $ python3 grep.py root /etc/passwd
# root:x:0:0::/root:/bin/bash
import sys


def main():
    query = sys.argv[1]
    file_path = sys.argv[2]
    try:
        with open(file_path) as f:
            contents = f.read()
    except IOError:
        exit("Should have been able to read the file")
    for line in contents.splitlines():
        if query in line:
            print(line)


if __name__ == "__main__":
    main()
```

Code này hoàn toàn ổn: sạch đẹp, đúng chuẩn PEP8, và quan trọng nhất: chạy ra đúng kết quả.  Vậy có cần refactor không?  Tùy.
Đó là chỗ khó khi nói về refactoring, không có gì rõ ràng, chính xác, mọi thứ đều "tùy".
Tùy vào:

- chương trình nhỏ hay to, 10 dòng hay 10000 dòng
- chương trình dùng 1 lần hay trong dự án 1 năm ++
- chạy 1 giây hay chạy 1 giờ mới xong
- team 1 người hay 10 người code cùng

Trong ví dụ cụ thể này, đoạn code trên hoàn toàn không cần refactor. Nhưng đây là bài viết về refactor, hãy xem tác giả sẽ biến đoạn code này thành 90 dòng ra sao.

#### 4+1 vấn đề của đoạn code

- Function `main` thực hiện 2 công việc khác nhau. Khi chương trình lớn lên, `main` sẽ thực hiện thêm nhiều công việc nữa khiến cho nó khó hiểu, khó test, khó thay đổi 1 công việc mà không ảnh hưởng đến các công việc khác. Không test được: cách duy nhất để biết từng đoạn code trong main chạy đúng hay sai là chạy thử nó, với nhiều đầu vào khác nhau và dùng mắt kiểm tra kết quả.  Nên tốt nhất là tách ra thành mỗi function thực hiện duy nhất 1 công việc + có thể viết unittest.
- Biến `query` và `file_path` là "configuration" của chương trình, biến `contents` dùng để thực hiện logic. Khi `main` dài hơn, sẽ cần nhiều biến hơn, khi có nhiều biến hơn, sẽ khó để nhớ/theo dõi mục đích của từng biến. Nên tốt nhất là gộp các biến configuration vào 1 struct (class) để khiến mục đích của chúng rõ ràng.
- Dù code đã in ra thông báo khi có exception lúc đọc file, nhưng có hơn 1 lý do có xảy ra exception khi đọc file: file không tồn tại, không có quyền để đọc file... In ra nội dung "không mở được file" không hề có ích cho người dùng biết vấn đề thực sự là gì.
- Khi người dùng không đưa vào đủ 2 đầu vào trên dòng lệnh, sẽ xảy ra IndexError, exception này không giải thích rõ ràng tới người dùng chuyện gì xảy ra. Tốt nhất là đặt **tất cả** code xử lý exception vào chung 1 chỗ để sau này chỉ cần xem 1 chỗ nếu logic xử lý exception cần thay đổi, đồng thời giúp hiển thị nội dung lỗi rõ ràng dễ hiểu hơn tới người dùng.
- Đoạn này không có trong bản Rust: việc đọc toàn bộ nội dung file vào RAM với `f.read()` là một "code smell", khiến đoạn code này không xử lý được file có kích thước lớn hơn RAM.

#### Thực hiện refactoring
Function `main` chỉ nên giới hạn tính năng:

- gọi function xử lý các đầu vào từ dòng lệnh
- setup các configuration (cấu hình) khác
- gọi `run` function trong file khác, ví dụ lib.py
- xử lý exception có thể xảy ra

##### Tách code xử lý đầu vào
Viết function `parse_config` nhận các argument, trả về:

- tuple các config: `(query, content)`, nhưng function `main` gọi `parse_config` sẽ lại unpacking tuple này thành các biến khác nhau. Đây là dấu hiệu của việc sử dụng chưa đúng "abstraction". Việc trả về tuple cũng không "gắn" được `query` và `file_path` vào với config. Vậy nên
- trả về 1 dictionary hoặc 1 Config object (Config class instance). Ở đây sẽ trả về 1 Config object cho giống ví dụ trong Rust.

```py
class Config:
    def __init__(self, query, file_path):
        self.query = query
        self.file_path = file_path

def parse_config(argv: list[str]) -> Config:
    query = argv[1]
    file_path = argv[2]
    return Config(query, file_path)

def main() -> None:
    config = parse_config(sys.argv)
    try:
        with open(config.file_path) as f:
            contents = f.read()
    except IOError:
        exit("Should have been able to read the file")
    for line in contents.splitlines():
        if config.query in line:
            print(line)
```

##### setup các configuration (cấu hình) khác
Giả sử chương trình sẽ nhận thêm biến environment (môi trường) `IGNORE_CASE`, nếu được set, chương trình sẽ không phân biệt chữ hoa chữ thường khi tìm kiếm. Đây là ví dụ về chương trình có thể nhận config từ nhiều nguồn khác nhau, ta chỉ cần thay đổi class `Config` và `parse_config`:

```py
class Config:
    def __init__(self, query, file_path, ignore_case):
        self.query = query
        self.file_path = file_path
        self.ignore_case = ignore_case

def parse_config(argv: list[str]) -> Config:
    query = argv[1]
    file_path = argv[2]
    ignore_case = os.environ.get("IGNORE_CASE")
    return Config(query, file_path, ignore_case)
```

##### gọi run function trong file khác, ví dụ lib.py
Tách toàn bộ logic của chương trình, ngoại trừ phần xử lý exception ra 1 file khác tên `lib.py` và đặt tên function là `run`:

```py
# lib.py
# Class Config...
def run(config: Config):
    with open(config.file_path) as f:
        contents = f.read()

    for line in contents.splitlines():
        if config.query in line:
            print(line)
```

```py
import lib
def main():
    config = lib.parse_config(sys.argv)
    try:
        lib.run(config)
    except IOError:
        exit("Should have been able to read the file")
```

Giờ đây `run` lại gặp vấn đề của `main`: làm nhiều việc, nhưng ít ra nó cũng chia bớt 2 việc cho `main` là parse config và xử lý exception. Khi một chương trình `run`, nó có thể thực hiện nhiều việc khác nhau, ở đây tiếp tục tách mỗi việc thành 1 function riêng. Việc đọc file không phức tạp hơn 1 dòng nên để nguyên, việc tìm kiếm string tách ra thành function `search`. Function `search` thay vì print, sẽ trả về 1 list chứa các string chứa từ khóa tìm kiếm, để việc print lại cho `run`. Như vậy có thể viết unittest kiểm tra logic của function quan trọng này thay vì kiểm tra bằng mắt.

```py
def search(query: str, contents: str) -> list[str]:
    result = []
    for line in contents.splitlines():
        if query in line:
            result.append(line)
    return result


def run(config: Config):
    with open(config.file_path) as f:
        contents = f.read()
    for line in search(config.query, contents):
        print(line)
```

Test:

```py
import unittest

import lib

class TestGrep(unittest.TestCase):
    def test_search_found(self):
        res = lib.search("us", "Among us\nSome write Rust\nSome write promt\nAll write Python")
        self.assertEqual(res, ["Among us", "Some write Rust"])
    def test_search_not_found(self):
        res = lib.search("HTML", "Among us\nSome write Rust\nSome write promt\nAll write Python")
        self.assertEqual(res, [])
```

Chạy test:

```
$ python3 -m unittest test_grep.py -vvv
test_search_found (test_grep.TestGrep) ... ok
test_search_not_found (test_grep.TestGrep) ... ok

----------------------------------------------------------------------
Ran 2 tests in 0.000s

OK
```

##### Thêm tính năng dễ dàng nhờ refactor
CHÚ Ý: thêm tính năng không nằm trong phạm vi refactor, ở đây minh họa tác dụng của việc refactor.

Khi mọi tính năng cơ bản đã ổn định, viết thêm code để xử lý khi người dùng set env `IGNORE_CASE`. Có 2 cách xử lý:

- thêm 1 boolean argument cho function search, `search(query, contents, ignore_case=False)`. Việc dùng boolean argument còn được gọi là [flag argument](https://martinfowler.com/bliki/FlagArgument.html) thường được xem như [code smell](http://www.informit.com/articles/article.aspx?p=1392524) vì nó ám chỉ function này làm nhiều hơn 1 việc. Trong trường hợp này, khi `ignore_case=True` sẽ chỉ gọi thêm 1 method (`lower()`) với mỗi dòng, chứ không "làm việc khác" nên argument này hoàn toàn OK. Một ví dụ tương tự, trong Python sort, có argument `reverse=True` hoặc `False` để thay đổi thứ tự sắp xếp.
- viết 1 function riêng `search_case_insensitive(query, contents)`, tác giả chọn phương án này mà không giải thích tại sao. Nhược điểm của phương án này là nếu phần code chung của 2 function là 30 bước, sẽ phải copy lại phần code chung. Nhưng cũng có thể cải thiện bằng việc tách riêng ra 1 function nữa như `search_internal` mà cả 2 `search`, `search_case_insensitive` cùng gọi.

Ở đây ta sẽ làm giống như ví dụ trong phiên bản Rust:

```py
def search(query: str, contents: str) -> list[str]:
    result = []
    for line in contents.splitlines():
        if query in line:
            result.append(line)
    return result

def search_case_insensitive(query: str, contents: str) -> list[str]:
    query = query.lower()
    result = []
    for line in contents.splitlines():
        if query in line.lower():
            result.append(line)
    return result
```

##### Xử lý exception
`main` cần xử lý exception từ 2 function `parse_config` và `run`, riêng biệt, để làm rõ hơn các exception đã xảy ra, ta tạo ra exception cho từng lỗi cụ thể.

```py
def parse_config(argv: list[str]) -> Config:
    query = argv[1]
    file_path = argv[2]
    ignore_case = os.environ.get("IGNORE_CASE")
    return Config(query, file_path, ignore_case)
```

function này có thể thiếu `query`, thiếu `file_path`, vậy viết:

```py
def parse_config(argv: list[str]) -> Config:
    try:
        query = argv[1]
    except IndexError:
        raise IndexError("Didn't get a query string")

    try:
        file_path = argv[2]
    except IndexError:
        raise IndexError("Didn't get a file path")
```
các exception này chứa nội dung mà người dùng có thể hiểu được.

Chạy thử với 3 trường hợp lỗi:
```
$ python3 grep.py
Problem parsing arguments: Didn't get a query string

$ python3 grep.py root
Problem parsing arguments: Didn't get a file path

$ python3 grep.py root /etc/passssss
Application error: [Errno 2] No such file or directory: '/etc/passssss'
```

Tới đây, chương 12 của **The book** kết thúc.

### Bonus: xử lý file kích thước lớn tùy ý

thay
```py
with open(config.file_path) as f:
    contents = f.read()
for line in search(config.query, contents):
    print(line)
```

Thành
```py
with open(config.file_path) as f:
    for line in search(config.query, f):
        print(line)
```
sử dụng `f` như 1 iterable, mỗi lần lấy 1 dòng ra, trong search, thay:
```py
for line in contents.splitlines():
```
Thành:
```py
for line in f:
    line = line.rstrip("\r\n")
```

Function `search` thay vì trả về 1 list sẽ yield từng dòng (generator).

```py
def search(query: str, contents: Iterable) -> Generator[str, None, None]:
    for line in contents:
        line = line.rstrip("\r\n")
        if query in line:
            yield line
```
#### So sánh code Rust và Python
Phiên bản code cuối cùng sẽ khác một chút so với nội dung viết trong bài, nhằm làm giống phiên bản Rust nhất: ví dụ phần unittest sẽ chỉ viết 2 unittest như bản Rust, unittest bên trên bị xóa đi để so sánh cho công bằng.

Code Python ngắn hơn Rust một chút:
```
$ wc -l grep.py test_grep.py lib.py
  18 grep.py
  25 test_grep.py
  52 lib.py
  95 total

$ wc -l src/main.rs src/lib.rs
  16 src/main.rs
 106 src/lib.rs   # rust viết test vào luôn file code
 122 total
```

Xem code:

- [grep.py]({static}/refactor/grep.py) - online <https://glot.io/snippets/gky3ldwlxs>
- [lib.py]({static}/refactor/lib.py) - online <https://glot.io/snippets/gky3ldwlxs>
- [main.rs]({static}/refactor/main.rs) - online <https://gist.github.com/rust-play/5689af5322e9e26eb95458a159289f43>
- [lib.rs]({stataic}/refactor/lib.rs) - online <https://play.rust-lang.org/?version=stable&mode=debug&edition=2021&gist=0f6695e6359b96aae6ca976cc23b5c07>

#### Bài học
- function `main` chỉ nên parse config và xử lý exception
- tách riêng logic chương trình ra thành (các) file riêng, chứa các function con cho dễ test
- viết unittest
- tạo abstraction khi cần thiết (class), giúp chia rõ vai trò của các biến khác nhau
- exception cần chứa thông tin có ích cho người dùng (thay vì chỉ developer mới hiểu được)
- mọi thứ đều là tương đối

### Kết luận
Refactoring để nâng cao chất lượng (Maintainability, Extensibility, Performance) của code, không phải để làm ngắn.

### Tham khảo

- <https://martinfowler.com/books/refactoring.html>
- <https://doc.rust-lang.org/book/ch12-03-improving-error-handling-and-modularity.html>
- <https://martinfowler.com/books/refactoring.html>
- <https://martinfowler.com/bliki/FlagArgument.html>
- <http://www.informit.com/articles/article.aspx?p=1392524>

Hết!

HVN at [http://pymi.vn](http://pymi.vn) and [https://www.familug.org](https://www.familug.org).

- [Ủng hộ tác giả 🍺](https://www.familug.org/p/ung-ho.html)
