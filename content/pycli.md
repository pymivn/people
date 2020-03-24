Title: Dùng Python như các CLI tool
Date: 2020-03-24
Category: Trang chủ
Tags: python, CLI
Slug: pycli
Authors: hvnsweeting
Summary: Python vốn được dùng để viết script, code trong file nhưng vẫn tỏa sáng khi gõ trong command line

Những "hacker" trên dòng lệnh luôn gõ nhoay nhoáy các ["command
line"](https://www.familug.org/search/label/CLI) để xử lý text: [grep, cut,
uniq, sort,...](https://www.familug.org/search/label/CCGU) hay đôi khi chơi hẳn
sed hoặc [AWK](https://pp.pymi.vn/article/awk/), thậm chí Perl5.

Thời xưa, Perl5 vốn là công cụ số một của các
[SysAdmin](https://www.familug.org/2015/01/e-tro-thanh-linux-sysadmin.html),
khi mà Python vẫn chưa phổ biến do quá sạch đẹp nhưng cũng hơi "dài dòng" (so
với Perl). Muốn làm gì với Python cũng phải viết ra 1 file, rồi chmod
a+x rồi mới chạy được. Perl thì có cả ngàn phép biến hóa chỉ bằng 1 dòng, gọi
là [one-liner](https://duckduckgo.com/?q=perl+one-liners&t=ffab&ia=web) hay
trên [Wikipedia](https://en.wikipedia.org/wiki/One-liner_program#Perl):

```perl
perl -lne 'print if $_ eq reverse' /usr/share/dict/american-english
```

1 dòng trên để tìm ra các từ "palindrome' (ngược xuôi như nhau).

## Python
### Python 1-liner
Python 1-liner vốn không ngắn như mong đợi, do code Python
nhấn mạnh vào sự rõ ràng dễ đọc, nên không có các ký tự bí hiểm `$_` như Perl. Viết
Python 1 dòng dùng option `-c` như sau:

```python
$ python3 -c 'import math; print(math.sqrt(2**1000))'
3.273390607896142e+150
```

Các dòng không cần phải xuống dòng mà dùng dấu `;` để ngăn cách. Nhưng viết
`for` hay `if` thì ... hơi khó.

### Python nhiều dòng
Cách này đơn giản hơn, viêt code thành nhiều dòng, ý hệt như code trong file. Dùng dấu single quote `'` rồi enter để gõ code, sau đó kết thúc bằng dầu single quote `'`.

```python
$ python3 -c '
> sum = 0
> for i in range(10):
>     sum += i
> print(sum)
> '
45
```

Ví dụ sau lấy ra Shell của user `root` ghi trong file /etc/passwd, viết HOA:

```python
$ cat /etc/passwd | python -c '
> import sys
> print(sys.stdin.readline().split(":")[-1].upper())
> '
/BIN/BASH
```

hay đếm số ký tự kết quả trên bằng lệnh `wc`:

```python
 $ cat /etc/passwd | python3 -c '
import sys
print(sys.stdin.readline().split(":")[-1].upper())
' | wc -c
11
```

Không phải 1 dòng, nhưng đẹp hơn 1 dòng, và hoàn toàn hợp lý.

Ví dụ khác để in JSON đẹp:

```python
$ echo '{"name": "PyMIers", "year": 2020}' | python3 -c '
import json, sys
print(json.dumps(json.load(sys.stdin), indent=4))'
{
    "name": "PyMIers",
    "year": 2020
}
```

Hay dùng module có sẵn:

```python
$ echo '{"name": "PyMIers", "year": 2020}' | python3 -m json.tool
{
    "name": "PyMIers",
    "year": 2020
}
```

Hoặc tìm các Palindromes trong file:

```python
$ python3 -c '
import sys
for line in sys.stdin:
    line = line.strip().lower()
    if len(line) > 1 and line == line[::-1]:
        print(line)
' < /usr/share/dict/american-english | head -5
ada
ana
anna
ara
ava
```

Cách khác:

```python
$ python3 -c '
import fileinput
for line in fileinput.input():
    line = line.strip().lower()
    if len(line) > 1 and line == line[::-1]:
        print(line)
' /usr/share/dict/american-english | head -3
ada
ana
anna
```

### Thử thách

Viết lại ví dụ sau chỉ dùng các command line, không dùng Python:
```python
$ cat /etc/passwd | python -c '
> import sys
> print(sys.stdin.readline().split(":")[-1].upper())
> '
/BIN/BASH
```

### Pro tips

- trong code không dùng dấu `'`
- **không được gõ sai** vì sửa lại hơi mệt, nếu không có khả năng này,
  hãy viết code vào file.

## Kết luận
Python dài và chất, đừng ngại dùng khi gõ CLI.
