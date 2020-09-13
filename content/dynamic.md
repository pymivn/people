Title: In ra màn hình số 1 - ngôn ngữ nào nhẹ nhất?
Date: 2018-05-27
Category: Trang chủ
Tags: python, tip,
Slug: dynamic
Authors: hvnsweeting
Summary: dash, bash, awk, perl, ruby, nodejs, python, elixir, guile - tất cả lên thớt!


Nếu chỉ cần in ra mà hình số 1, ngôn ngữ lập trình nào sẽ chạy tốn ít RAM nhất?

Thí nghiệm sau sẽ cho ta thấy các chương trình cần bao nhiêu RAM để chạy và in
ra số 1, kết thúc dòng bằng một dấu xuống dòng (newline `\n`).

Ta dùng chương trình `/usr/bin/time` để có cả thông số về RAM (`RSS`) thay vì chỉ gõ time - lệnh builtin của bash.


## bash4.3

```
$ /usr/bin/time bash -c 'echo 1'

1

0.00user 0.00system 0:00.00elapsed 100%CPU (0avgtext+0avgdata 3064maxresident)k

0inputs+0outputs (0major+136minor)pagefaults 0swaps
```

## dash

```
$ /usr/bin/time /bin/dash -c 'echo 1'
1
0.00user 0.00system 0:00.00elapsed ?%CPU (0avgtext+0avgdata 1492maxresident)k
0inputs+0outputs (0major+67minor)pagefaults 0swaps
```

## mawk

```
$ /usr/bin/time mawk 'BEGIN {print 1}'

1

0.00user 0.00system 0:00.00elapsed 100%CPU (0avgtext+0avgdata 1932maxresident)k

0inputs+0outputs (0major+86minor)pagefaults 0swaps

```

## gawk 4.1.3

```
$ /usr/bin/time gawk 'BEGIN {print 1}'

1

0.00user 0.00system 0:00.00elapsed 42%CPU (0avgtext+0avgdata 3632maxresident)k

552inputs+0outputs (2major+173minor)pagefaults 0swaps

```

## Python3.5.2

```
$ /usr/bin/time python3 -c 'print(1)'

1

0.03user 0.01system 0:00.05elapsed 98%CPU (0avgtext+0avgdata 9292maxresident)k

0inputs+0outputs (0major+1100minor)pagefaults 0swaps
```

## Python2.7.12

```
$ /usr/bin/time python2 -c 'print(1)'

1

0.01user 0.00system 0:00.01elapsed 94%CPU (0avgtext+0avgdata 6640maxresident)k

0inputs+0outputs (0major+819minor)pagefaults 0swaps
```

## Ruby 2.3.1

```
$ /usr/bin/time ruby -e 'puts 1'
1
0.03user 0.01system 0:00.04elapsed 100%CPU (0avgtext+0avgdata 10336maxresident)k
0inputs+0outputs (0major+1595minor)pagefaults 0swaps
```

## Perl v5.22.1
```
$ /usr/bin/time perl -e 'print "1\n"'

1

0.00user 0.00system 0:00.00elapsed 100%CPU (0avgtext+0avgdata 4144maxresident)k

0inputs+0outputs (0major+176minor)pagefaults 0swaps
```

## NodeJS 6.11.2

```
$ /usr/bin/time node -p '1'

1

0.09user 0.00system 0:00.10elapsed 100%CPU (0avgtext+0avgdata 24080maxresident)k

0inputs+0outputs (0major+2920minor)pagefaults 0swaps

```

## Elixir 1.6.3

```
$ /usr/bin/time elixir -e 'IO.puts 1'

1

0.17user 0.04system 0:00.16elapsed 137%CPU (0avgtext+0avgdata 29268maxresident)k

16inputs+0outputs (1major+7837minor)pagefaults 0swaps

```

## Guile 2.0.11
```
$ /usr/bin/time guile -c '(display 1) (newline)'

1

0.02user 0.00system 0:00.01elapsed 115%CPU (0avgtext+0avgdata 7720maxresident)k

0inputs+0outputs (0major+976minor)pagefaults 0swaps

```

##  printf 8.25 - chương trình viết bằng C

```
$ /usr/bin/time printf '1'

10.00user 0.00system 0:00.00elapsed 100%CPU (0avgtext+0avgdata 1844maxresident)k

0inputs+0outputs (0major+72minor)pagefaults 0swaps

```


## Làm lại toàn bộ bằng Python
Tạo một dictionary, chứa các tên ngôn ngữ - kèm với câu lệnh sẽ dùng để thử nghiệm


```python
import shlex
import subprocess


programs = {
    'bash': 'bash -c "echo 1"',
    'dash': 'dash -c "echo 1"',
    'mawk': "mawk 'BEGIN {print 1}'",
    'gawk': "gawk 'BEGIN {print 1}'",
    'python2.7': 'python2 -c "print(1)"',
    'python3.5': 'python3 -c "print(1)"',
    'ruby2.3': 'ruby -e "puts 1"',
    'node6': 'node -p 1',
    'perl5': "perl -e \"print '1\n'\"",
    'elixir': 'elixir -e "IO.puts 1"',
    'guile': 'guile -c "(display 1) (newline)"',
    'printf': 'printf "1\n"'
}


import re

def get_rss_from_stderr(stderr):
    match = re.compile('(?P<rss>\d+)maxresident').search(err.decode('utf-8'))
    return int(match.group('rss'))


import pandas as pd

languages = []
rsses = []
for language, cmd in programs.items():
    cmd = ['/usr/bin/time'] + shlex.split(cmd)
    process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = process.communicate()
    assert out.decode('utf-8') == '1\n'
    rss = get_rss_from_stderr(err)
    print(language, rss)
    languages.append(language)
    rsses.append(rss)

df = pd.DataFrame(index=languages, data=rsses, columns=['RSS'])

df_sorted_rss = df.sort_values(by='RSS')

# run in Jupyter
from matplotlib import pyplot as plt
import matplotlib
matplotlib.style.use('fivethirtyeight')

%matplotlib inline
df_sorted_rss.plot.bar(title='RSS size in byte when print 1');
```

![Dynamic typing languages]({static}/images/dynamic.png)

## Kết luận

Khoan vội kết luận rằng cả thế giới nên chuyển hết về dùng dash cho đỡ tốn RAM hay xa lánh Elixir vì nó chạy tới 30 MB RAM để in số 1 ra màn hình.

Sử dụng đúng công cụ, cho đúng vấn đề thích hợp mới là điều quan trọng.

- dash được viết ra để dùng làm `shell (sh)` cho Ubuntu, nó cần nhẹ, dù trả giá bằng việc không nhiều tính năng, và chỉ là một shell scripting language
- [bash](http://www.familug.org/search/label/bash) là shell được dùng phổ biến nhất thế giới
- awk là ngôn ngữ lập trình đã gắn liền với lịch sử của thế giới UNIX, rất tiện để tính toán dữ liệu cột / hàng. Với AWK cùng các CLI tool truyền thống, người ta có thể [giải quyết bài toán "big data" nhanh gấp 200 lần dùng Hadoop (EMR)](https://adamdrake.com/command-line-tools-can-be-235x-faster-than-your-hadoop-cluster.html)
- mawk nhanh hơn gawk
- perl5 luôn có chỗ đứng của nó, nó vẫn ở trên máy Ubuntu dù chưa bao giờ mình chủ ý cài
- [guile](http://www.familug.org/search/label/guile) là extension language chính thức được lựa chọn bởi GNU, nó chính là ngôn ngữ scheme được mang vào ứng dụng thực tế
- [Python](http://pymi.vn/) - ngôn ngữ dễ đọc, phổ biến nhất thế giới, đã đẩy ngành tính toán khoa học từ bộ môn trong phòng thí nghiệm trở thành ngành hot nhất trái đất. PS: Python khi bật lên đã dùng ~ 8MB RAM.
- Ruby còn dùng nhiều RAM hơn nữa, dù về mặt tính năng thường được so ngang với Python, nhưng mặt ứng dụng vào khoa học thì là vực so với trời Python.
- NodeJS là một JavaScript engine chuyển biến cả ngành web, cũng chưa rõ sao nó ngốn gần 25MB để bật lên, có khi đó vốn là bản chất của JavaScript.
- [Elixir](http://elixir.pymi.vn/) không chỉ bật lên một interpreter như bash, mà đó là cả hệ thống phân tán - chạy máy ảo BEAM của Erlang, nên con số 30MB thậm chí còn là hơi ... ít.

Bài này không xét các ngôn ngữ mà phải viết thành file, compile mới chạy, vì tác giả quá lười.

PS: học hết đống trên ở [đây](http://www.familug.org/2016/12/free-ebook.html)

Hết.

HVN at [https://pymi.vn](https://pymi.vn) and https://www.familug.org
