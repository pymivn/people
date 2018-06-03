Title: Awk siêu tốc
Date: 2018-05-27
Category: Trang chủ
Tags: awk, sysadmin, linux, csv, bigdata,
Slug: awk
Authors: hvnsweeting
Summary: học và dùng luôn trong 20 phút - yêu cầu dùng Ubuntu/OSX hay các hệ điều hành UNIX-like.


Nếu bạn đã biết 1 scripting language như Python hay Perl việc học AWK sẽ có vẻ hơi
thừa/ hơi ngần ngại. Nhưng AWK - ngôn ngữ lập trình sinh ra từ những năm 1970 luôn
có chỗ dùng, và sức mạnh đáng gờm.

Bài này giới thiệu các khái niệm cơ bản của ngôn ngữ lập trình AWK, một số cách dùng thông dụng, học xong có thể dùng ngay và vô cùng hữu ích với những người xử lý dữ liệu dạng cột/ bảng mà không biết Python.


Các lệnh trong bài này dùng `mawk` vì nó được biết là nhanh hơn các bản awk khác, nhưng về tính năng cơ bản là giống nhau, người đọc dùng bản nào cũng được, VD gawk

```
$ whatis awk
awk (1)              - pattern scanning and processing language
```

### Dùng trong các câu lệnh hàng ngày

AWK rất thích hợp để nhét vào 1 pipe các câu lệnh UNIX, việc mà Python vốn không sinh ra để làm

Ví dụ: đếm số dòng trong file /etc/passwd

```
$ wc /etc/passwd
  57   95 3193 /etc/passwd
```

Lệnh `wc` vốn sinh ra để đếm: dòng, số từ, số ký tự. Bạn có thể viết 1 script Python 5-7 dòng
làm chuyện này, nhưng 1 dòng? Hãy thử và nếu thành công, hãy comment!

Với AWK, làm việc này không khó khăn gì. Hãy bỏ qua nếu không hiểu gì, phần giải thích sẽ theo sau
```
$ cat /etc/passwd | mawk '{ words += NF; chars += length($0) + 1;} END { print NR, words, chars}'
57 95 3193
```
Một pipe (`cmd1 | cmd2 | cmd3`) thường bắt đầu bằng `cat file`, mặc dù nó không phải cách làm tốt (tốn thêm 1 câu lệnh cat - khi mà hầu hết các câu lệnh đều hỗ trợ đầu vào là 1 file), nhưng tiện, nên ta cứ bắt đầu với cat, khi nào cần tối ưu ta sẽ bỏ nó đi. Ở đây, `mawk` có thể nhận file để xử lý, ta viết lại:
```
$ mawk '{ words += NF; chars += length($0) + 1;} END { print NR, words, chars}' /etc/passwd
57 95 3193
```

Một ví dụ khác

```
$ head /etc/passwd
root:x:0:0:root:/root:/bin/bash
daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
bin:x:2:2:bin:/bin:/usr/sbin/nologin
sys:x:3:3:sys:/dev:/usr/sbin/nologin
sync:x:4:65534:sync:/bin:/bin/sync
games:x:5:60:games:/usr/games:/usr/sbin/nologin
man:x:6:12:man:/var/cache/man:/usr/sbin/nologin
lp:x:7:7:lp:/var/spool/lpd:/usr/sbin/nologin
mail:x:8:8:mail:/var/mail:/usr/sbin/nologin
news:x:9:9:news:/var/spool/news:/usr/sbin/nologin
```

Một yêu cầu quái dị có thể xuất hiện như: hãy tính tổng các số ở cột số 3, với các câu lệnh CLI truyền thống, ta làm như sau

```
$ echo $(cat /etc/passwd | cut -d: -f3 | xargs printf '%s +') 0 | bc
75624
```

`cut` giúp lấy cột thứ 3, phân cách bằng dấu `:`, dùng `printf` để nối các số lại bằng dấu `+`, vì thừa 1 dấu `+` ở đuôi nên ta `echo` thêm số 0 để cho hợp lệ rồi đưa vào lệnh `bc` để tính.

```
$ mawk -F: '{sum += $3} END { print sum }' /etc/passwd
75624
```

Tương tự `cut`, ta dùng `-F:` để chỉ ra sẽ dùng `:` để phân cách cột, lấy cột số 3 `$3`, cộng
lần lượt các giá trị vào biến `sum` - khi ta không khai báo, AWK mặc định đó là số 0 nếu thực hiện phép toán với số. Làm như vậy với mỗi dòng (gọi là *record* trong AWK):

```
{ sum += $3 }
```

Và khi hết các dòng (đánh dấu bằng END), ta print ra kết quả
```
END { print sum }
```

Khó có thể đánh bại sự ngắn gọn, sạch sẽ này.
## Record và field
AWK đọc text vào, mặc định sẽ cắt tại các dấu xuống dòng, tạo thành các record,
sau đó mặc định cắt tại dấu space (khoảng trắng), tạo thành các field.
Ta hoàn toàn có thể chỉ định AWK cắt ở ký tự khác.

## Cấu tạo một chương trình AWK

Một chương trình AWK cấu tạo bởi các câu lệnh (statements) với cú pháp:

```
              pattern   { action statements }
```

Chỉ có vậy.
Khi viết vào file thì viết mỗi câu lệnh 1 dòng, nhưng hoàn toàn có thể viết trên 1 dòng.

### partern

Có nhiều partern, nhưng 3 partern phổ biến và hữu ích nhất là:

- BEGIN: theo sau là hành động / câu lệnh khi chương trình bắt đầu
- END: theo sau là câu lệnh được chạy khi chương trình kết thúc
- KHÔNG GHI PATTERN: thực hiện câu lệnh này cho mỗi record

Ví dụ

```
'{sum += $3} END { print sum }'
```

Không có BEGIN, với mỗi record ta sẽ cộng dồn, và khi đọc hết các record rồi, ta print ra tổng. Chú ý: dấu `\` ở cuối dòng là cú pháp trong shell cho phép viết 1 dòng thành nhiều dòng, khi chạy chúng sẽ chỉ xem là 1 dòng.

```awk
$ echo 'pymi\npython\nfamilug' | mawk '\
 BEGIN { print "the begin" } \
 { printf "got line: %s has length %d\n", $0, length($0) }\
 { print "done process line ", NR }\
 END {print "DONE"}'

the begin
got line: pymi has length 4
done process line  1
got line: python has length 6
done process line  2
got line: familug has length 7
done process line  3
DONE
```

## parttern tìm kiếm

parttern này giúp tìm kiếm các record có chứa một regular expression (hoặc string cố định) và xử lý record đó.

Đếm số dòng chứa từ `print`:

```
$ echo -e "printf print \nprintf"
printf print
printf
$ echo -e "printf print \nprintf" | grep -c print
2
$ echo -e "printf print \nprintf" | mawk '/print/ { count += 1 } END { print count }'
2
```
## print
`print`  và `printf` là 2 output statements (câu lệnh xử lý đầu ra), không phải function nên
không sử dụng cú pháp gọi function `print(thing)`

```
$ mawk 'BEGIN { print "hello" }'
hello
```


## variable và field variable

Mỗi record chứa nhiều field, hãy tưởng tượng như 1 dòng spreadsheet/excel có nhiều ô ứng với các cột.
Các variable có sẵn:

- `$0` - toàn bộ 1 record (dòng) - chú ý `$X` là tên biến hợp lệ trong AWK, dấu $ dùng để truy cập giá trị của field
- `$1` - field 1 (hay có thể nghĩ là cột số 1)
- `$2` - field 2
- ...
- `$NF` - field cuối cùng
- NF - số field
- NR - thứ tự của record, tăng dần sau khi xử lý xong mỗi record

Khi truy cập biến, không sử dụng thêm bất cứ ký tự nào (khác với bash, bash phải thêm $varname).

```
$ echo '1, Le Van Xe, 27, Ha Noi, 0990090090' | mawk -F, '{ print $NF}'
 0990090090
$ echo '1, Le Van Xe, 27, Ha Noi, 0990090090' | mawk -F, '{ print $0}'
1, Le Van Xe, 27, Ha Noi, 0990090090
$ echo '1, Le Van Xe, 27, Ha Noi, 0990090090' | mawk -F, '{ print NF }'
5
```

Chỉ cần nắm rõ tên các variable có sẵn này, ta đã có một tool cực mạnh để xử lý dữ liệu dạng bảng như Excel/CSV/SQL.

## Các kiểu dữ liệu
AWK có string, số (chia làm float và integer), và array.
Ta không bàn tới array ở đây, vì nếu cần lập trình gì phức tạp hơn một câu lệnh AWK đơn giản, ta  có thể sử dụng Python cho sạch sẽ, gọn gàng, tiện lợi.

## Control flow
Là ngôn ngữ lập trình đầy đủ, AWK có if/else/for/while như các ngôn ngữ lập trình "giống C" khác. Ví dụ đếm số chẵn và số lẻ

```
$ echo -e '1\n2\n3\n4\n20\n30' | mawk '\
{ if ($1 % 2 == 0) \
     { chan += 1 } \
  else { le += 1 } \
} \
END { print chan, le }'

5 1
```

## Function
AWK có sẵn các funtion xử lý string, số thì đủ các phép toán, các function sin cos ..., người dùng cũng có thể định nghĩa function của họ. Xem thêm ở [đây](https://www.gnu.org/software/gawk/manual/gawk.html#Functions).

### Bonus - giải bài projecteuler 1
[Tính tổng các số nhỏ hơn 1000 chia hết cho 3 hoặc 5](https://projecteuler.net/problem=1)


```
$ seq 1 999 | mawk '{ if ($1 % 3 == 0 || $i % 5 == 0) sum += $1 } END { print sum }'
233168
```
## Tham khảo
- [mawk homepage manpage](http://invisible-island.net/mawk/manpage/mawk.txt)
- [ubuntu 16.04 man 1 mawk](http://manpages.ubuntu.com/manpages/xenial/en/man1/mawk.1.html)
- [GNU awk](https://www.gnu.org/software/gawk/manual/gawk.html#Top)
- [AWK on big data](https://adamdrake.com/command-line-tools-can-be-235x-faster-than-your-hadoop-cluster.html)

Hết

HVN at [http://pymi.vn](http://pymi.vn) and [https://www.familug.org](https://www.familug.org).
