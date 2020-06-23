## Perl 5 cho người lười

Perl là một ngôn ngữ lập trình phổ biến, từng là công cụ No.1 của các Sysadmin.
Xuất hiện vào năm 1987, Perl chứng kiến sự bùng nổ của internet, sự lớn mạnh của các hệ điều hành nhân Linux, sự ra đời của các ngôn ngữ lập trình như Python, PHP, Ruby ...

Perl vốn mang tiếng xấu là
- cú pháp khó đọc
- là ngôn ngữ chỉ để viết chứ không để đọc
- là lạc hậu, cũ (dù sao Perl cũng chỉ hơn Python có 4 tuổi, Python sinh năm 1991) ???!!!

# TODO IMAGE PERL LOGO HERE

Ngày nay, Perl càng ít được ưa chuộng, ngay cả lĩnh vực Perl từng mạnh nhất là viết script, giờ cũng bị cạnh tranh khốc liệt bởi Python, Ruby.
Thế nhưng ngôn ngữ xấu tiếng này vẫn có những điểm rực sáng và ảnh hưởng rất lớn:
- PCRE (Perl-compatible regular expressions)- cú pháp regex (regular expression) là phiên bản regex được sử dụng phổ biến, ngay cả trong các ngôn ngữ lập trình khác.
Việc dùng Regex như con dao 2 lưỡi, rất tiện dụng, nhưng khá khó đọc, và khó viết đúng.
- Khi xử lý các file text, perl được ví như `portable sed`. `sed`/`awk` là 2 công cụ không thể thiếu để chỉnh sửa file text hàng loạt trên `*NIX`.

Bài viết này giới thiệu ngắn gọn cú pháp của Perl5, đủ để đọc được code Perl trong các project viết sạch đẹp (hãy thử sau khi đọc đến cuối bài này), và có thẻ bắt đầu viết Perl thay sed.

### Perl 5
Perl có 2 phiên bản là Perl 5 và Perl 6, chú ý không phải 6 là bản thay thế Perl 5, mà Perl 6 có thể xem như một ngôn ngữ hoàn toàn khác.
Việc phát triển Perl 5 và Perl 6 được thực hiện song song.
Bài này chỉ bàn tới Perl từ xưa cho đến Perl 5.

```sh
$ perl --version

This is perl 5, version 22, subversion 1 (v5.22.1) built for x86_64-linux-gnu-thread-multi
(with 73 registered patches, see perl -V for more detail)

    Copyright 1987-2015, Larry Wall
...
```

**Larry Wall** là người tạo ra Perl.

Perl 5 thường có sẵn trên các máy tính `*NIX`: OSX, Ubuntu, RedHat ... hoặc nếu khong có, cài đặt cũng rất dễ dàng.
Xem thêm tại trang chủ [http://www.perl.org]()

```sh
 $ whatis -s1 perl
 perl (1)             - The Perl 5 language interpreter
 $ whatis -s1 cpan
 cpan (1)             - easily interact with CPAN from the command line
```

CPAN là tên kho package (thư viện) của Perl, tương tự như Pypi của Python. Nó có câu lệnh `cpan` tương đương với `pip` của Python hay `npm` của JavaScript.

#### perldoc
perldoc là câu lệnh để đọc doc của perl. Trên Ubuntu cài đặt bằng lệnh:

```
sudo apt-get install -y perl-doc
```

Bài viết này dựa theo doc có trong `perldoc perlintro`

Code perl thường ghi trong file `filename.pl`, chạy file này bằng lệnh `perl filename.pl`

```perl
# hello.pl
print("Hello PyMi.vn\n");
print "Merry Xmas\n";
```

Perl sử dụng ~ 4 MB để chạy đoạn code trên.

```sh
$ perl hello.pl
Hello PyMi.vn
Merry Xmas
$ /usr/bin/time perl hello.pl
Hello PyMi.vn
Merry Xmas
0.00user 0.00system 0:00.00elapsed 100%CPU (0avgtext+0avgdata 4124maxresident)k
0inputs+0outputs (0major+181minor)pagefaults 0swaps
```

Nếu không muốn viết vào file, có thể dùng option `-e` và gõ code trực tiếp:

```sh
$ perl -e 'print("Hello world\n");
print "Merry Xmas\n";
'
Hello world # output
Merry Xmas # output
```

IMAGE HERE #TODO perlecli.png

perl mặc định không có interactive mode như Python, không gõ từng dòng lệnh được.

### Cú pháp Perl 5

Một điều cần hiểu trước khi định phát biểu ý kiến gì về cú pháp của Perl: perl có khẩu hiệu soi đường (Perl motto) là
> "There's more than one way to do it."

Có hơn 1 cách làm việc gì đó. Nên cú pháp của Perl cũng sẽ có nhiều cách để làm cùng một việc.
Điều này khá trái ngược với motto của Python

> There should be one-- and preferably only one --obvious way to do it.

Từ đây trở đi, code sẽ viết bình thường và kết quả chạy code sẽ bắt đầu với dấu `->`

Vài quy tắc chung về cú pháp:
- dấu space không có ý nghĩa gì (trừ khi nằm trong string)
- dòng thường kết thúc bằng `;` (thay vì phải nhớ khi nào có khi nào không thì tốt nhất là cứ thêm vào)
- khi gọi sub routine (function), không bắt buộc phải có dấu `()`, `print "abc"` và `print("abc")` là như nhau.

#### Các kiểu dữ liệu đơn (giản)

KHÔNG CÓ kiểu Boolean (True/False), perl dùng số `1` với nghĩa có/đúng và empty string với nghĩa sai.

```perl
$ perl -e 'print(5<4 == "")'
1
```

##### String/integer/float


```perl
my $x =    10;
my $y =20.3;
print $x + $y - 2 * 10 / 3;
-> 23.6333333333333
```

Tạo biến NÊN dùng từ khóa `my` trước `$` tên biến.

```perl
my $name = "PyMi";
print "Hello $name\n"; # substitue name with value PyMi
print 'Hello $name\n'; # keep no change

-> Hello PyMi
-> Hello $name\n
```

String giống như `bash`, chỉ biến trong double quote `" $name "` mới được thay thế, single quote giữ nguyên nội dung.

## TODO
print 5 != 4 && 2 < 5 || !(3 > 5)
print "meo" ne "cho"

different number and comparision because variable has no type

print hello world: 4 MB RAM


$_


## Array - similar to Python list
my @names = ("chim", "meo", "ga", 42); # diff types
print($names[0]);

$#names  -> index of last elemen (like python[-1])

@names return number when do number operators:

@names + 5

Multiple index access
@names[1, 3]

Slice
@names[1..3]

sort @names
reverse @names

@ARGV @_
## Hash (key-value pairs) - smilar to Python dicto

```perl
my %phonebook = (
    HVN => "khong co so",
    PyMi => 0909090909,
);
print($phonebook{"HVN"})
print($phonebook{"khong ton tai"})
```

or
```
my $pymiers = {
    HVN => {
        address => "VietNam",
        homepage => "www.familug.org",
    }
}

print "Homepage is $pymier->{'HVN'}->{'homepage'}
```


## Control flow

if ( condition ) {
    ...
} elsif ( other condition1 ) {
    ...
} elsif ( other condition2 ) {
    ...
} else {
    ..
}

unless ( ... ) = if not something


while ( condition ) {
    ...
}
until ( condition ) {
    ...
}

while ( 1 ) {
    print "HELLO PyMI.vn"
}

for EXACTLY like C
for ($i = 0; $i <= 10; $i++) {
}


lovely foreach

```
foreach (@name) {
    print "Hello $_ \n"
}
```

OR

```
foreach my $key (keys %phonebook) {
    print "Value of $key is $phonebook{$key} \n"
}
```

## IO
open(my $in, "<", "input.txt")
open(my $out, ">", "input.txt")
open(my $appendout, ">>", "input.txt")

while $(<$in>) {
    print "Just read in this line $_";
}

close($in)
close($out)
close($appendout)


## Regex
    THE MOST FAMOUS, POPULAR, probably BEST THING IN PERL

my $phone = "0990009990";
if ($phone =~ /[0-9]{10,11}/) {
    print "Good phone number";
} else {
    print "Seem bad phone number";
}

print("Perl is good" =~ s/g/for f/)

```
perl -e 'my $words = "Perl is good";
print $word;
$words =~ s/g/for f/g;
print "$words \n"'
# Perl is for food
```

## Subroutine
Similar function in other lang


sub double {
my $x = shift;
return $x * 2;
}

print double(21);

sub sumtwo {
my ($first, $second) = @_;
return $first + $second
}
print sumtwo(2,3);


## Using module

use something

 use strict;
 use warnings;


## Sample program

```
#!/usr/bin/perl
use strict;
use warnings;
use IO::Handle;

my ( $remaining, $total );

$remaining = $total = shift(@ARGV);

STDOUT->autoflush(1);

while ( $remaining ) {
    printf ( "Remaining %s/%s \r", $remaining--, $total );
    sleep 1;
}

print "\n";
```

Thay sed
```
$ perl -i.bak -lp -e 's/Bob/Robert/g' *.txt
```

https://en.wikipedia.org/wiki/Perl

https://www.perl.org/

25000 package on CPAN
vs Python 162,637 projects as of 2018 Dec 24.

https://github.com/kaxap/arl/blob/master/README-Perl.md

https://github.com/brendangregg/FlameGraph/blob/90533539b75400297092f973163b8a7b067c66d3/dev/hcstackcollapse.pl
https://github.com/so-fancy/diff-so-fancy/blob/5c96bddd5b53df4171cb3ebc1a2e1e16f0611806/diff-so-fancy
https://github.com/mojolicious/mojo/blob/master/lib/Mojo/IOLoop/Server.pm
