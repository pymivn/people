Title: (Quá nhiều để) refactor 10 dòng code thành 30 dòng
Date: 2023-05-09
Category: Trang chủ
Tags: python, refactor, software engineering, test
Slug: refactor
Authors: hvnsweeting
Summary: refactor không phải để code ngắn đi

Refactor là một phần công việc không thể thiếu của lập trình viên, sau khi code xong chạy được mà "chưa đẹp", lập trình viên sẽ chỉnh sửa chút xíu đoạn code cho "đẹp" hơn, cũng có thể nhanh hơn, cũng có thể ngắn hơn, cũng có thể dễ hiểu hơn...

Vấn đề với refactor: là một khái niệm chung chung, không có ví dụ cụ thể, khó học/luyện tập để trở thành 1 kỹ năng. Sách vở viết về refactor cũng chỉ có 1 quyển được cộng đồng mạng nhắc tới ?!!! [Refactoring - Improving the Design of Existing Code by Martin Fowler, with Kent Beck, 2018](https://martinfowler.com/books/refactoring.html).  PyMi cũng từng có 1 bài viết giới thiệu việc [refactoring code kèm với IPython]({filename}/repl.md).

Bài viết này dựa trên chapter 12 trong cuốn [The Rust Programming Language](https://doc.rust-lang.org/book/ch12-03-improving-error-handling-and-modularity.html), kèm chuyển dịch sang Python, thêm "bình phẩm" và nhiều nhiều câu hỏi. Sử dụng ví dụ từ sách Rust khiến người đọc có thể tin cậy trình độ của tác giả... Steve Klabnik - nổi tiếng bậc nhất trong thế giới Rust.

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
Để cải thiện, nâng cao

- Tính dễ bảo trì, fix bug: Maintainability.
- Tính dễ mở rộng/thay đổi: Extensibility.
- Tốc độ chạy.

Chú ý một số lĩnh vực đặc thù như out sourcing - chạy đua deadline, giao sản phẩm, thu tiền rồi thôi, thì cả 3 thứ trên có sự ưu tiên không hề cao, vậy nên cũng có thể không có refactor gì hết.

### Ví dụ refactor 10 dòng code
Viết 1 chương trình giống như câu lệnh grep trên UNIX, tức nhận 2 đầu vào trên dòng lệnh là "từ khóa tìm kiếm" và tên file, in ra màn hình các dòng chứa từ khóa ấy.

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
- chạy 1s hay chạy 1 giờ mới xong
- team 1 người hay 10 người code cùng

Trong ví dụ cụ thể này, đoạn code trên hoàn toàn không cần refactor. Nhưng đây là bài viết về refactor, hãy xem tác giả sẽ biến đoạn code này thành 50 ra sao.

#### 4 vấn đề của đoạn code

- Function `main` thực hiện 2 công việc khác nhau. Khi chương trình lớn lên, main sẽ thực hiện thêm nhiều công việc nữa khiến cho nó khó hiểu, khó test, khó thay đổi 1 công việc mà không ảnh hưởng đến các công việc khác. Không test được: cách duy nhất để biết từng đoạn code trong main chạy đúng hay sai là chạy thử nó, với nhiều đầu vào khác nhau và dùng mắt kiểm tra kết quả.  Nên tốt nhất là tách ra thành mỗi function thực hiện duy nhất 1 công việc + có thể viết unittest.
- Biến `query` và `file_path` là "configuration" của chương trình, biến `contents` dùng để thực hiện logic. Khi main dài hơn, sẽ cần nhiều biến hơn, khi có nhiều biến hơn, khiến khó để nhớ/theo dõi mục đích của từng biến. Nên tốt nhất là gộp các biến configuration vào 1 struct (class) để khiến mục đích của chúng rõ ràng.
- Dù code đã in ra thông báo khi có exception lúc đọc file, nhưng có tới N lý do có xảy ra expect khi đọc file: file không tồn tại, không có quyền để đọc file... In ra nội dung "không mở được file" không hề có ích lợi cho người dùng biết vấn đề thực sự là gì.
- Khi người dùng không đưa vào đủ 2 đầu vào trên dòng lệnh, sẽ xảy ra IndexError, exception này không giải thích rõ ràng tới người dùng chuyện gì xảy ra. Tốt nhất là đặt **tất cả** code xử lý exception vào chung 1 chỗ để sau này chỉ cần xem 1 chỗ nếu logic xử lý exception cần thay đổi, đồng thời giúp hiển thị nội dung lỗi rõ ràng dễ hiểu hơn tới người dùng.

#### Thực hiện refactoring
Function main chỉ nên giới hạn tính năng:

- gọi function xử lý các đầu vào từ dòng lệnh
- setup các configuration (cấu hình) khác
- gọi run function trong file khác, ví dụ lib.py
- xử lý exception nếu xảy ra exception

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

def main():
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
##### gọi run function trong file khác, ví dụ lib.py
##### xử lý exception nếu xảy ra exception

### Kết luận
HVN at [http://pymi.vn](http://pymi.vn) and [https://www.familug.org](https://www.familug.org).

- [Ủng hộ tác giả 🍺](https://www.familug.org/p/ung-ho.html)
