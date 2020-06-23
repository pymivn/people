Title: C thật là đơn giản
Date: 2020-02-19
Category: Trang chủ
Tags: C, Python, strace, syscall, UNIX, sysadmin
Slug: cde
Authors: hvnsweeting
Summary: C đơn giản hơn Python?

Đơn giản, nhanh, chậm, xinh, cao, thấp, giỏi, xịn... đều là những khái niệm
mang tính chất tương đối. Có cái hơn khi so sánh ở góc độ này, nhưng lại kém
khi so sánh ở góc độ khác. Trong ngành lập trình, mọi thứ đều là sự đánh đổi
(trade off),
không có giải pháp nào thỏa mãn tất cả mọi nhu cầu (silver bullet) - hoặc có
nhưng chưa ai tìm ra.

Không cần bàn cãi, ai cũng đồng ý code Python dễ đọc, viết hơn C, hay... đơn
giản hơn. Nhưng cái đơn giản đó, là đơn giản với con người, với lập trình viên,
còn với máy tính thì hoàn toàn ngược lại.

Ta sẽ thử nghiệm chương trình đơn giản nhất trái đất: hello world viết bằng C
và Python rồi so sánh dùng `strace` - một công cụ debug "cao cấp" thường
dùng bởi các SysAdmin.

### strace

```sh
$ whatis strace
strace (1)           - trace system calls and signals
```
Bài viết thực hiện trên Ubuntu 18.04, `cc` - C compiler có lẽ là có sẵn.
Hoặc nếu không có, hãy cài bằng `sudo apt-get install -y  build-essential strace`

### C Programming language

4 dòng code C
```c
#include <stdio.h>

int main(void) {
    puts("Hello world!");
}
```

Compile rồi chạy - yeah, cực đơn giản, không cần gì khác cả, cũng không cần
làm việc đơn giản này trở thành rắc rôi.

```sh
$ cc hello.c -o hello  # compile, sinh ra file hello
$ ./hello  # chạy file hello
Hello world!
```

Giờ chạy với `strace` để xem chương trình siêu đơn giản này gọi những system call
nào, `-C` sẽ hiển thị bảng thống kê, `-S calls` sẽ sắp xếp thống kê này
theo cột `calls`, giảm dần.

```sh
$ strace -CScalls ./hello
execve("./hello", ["./hello"], 0x7fff1e9af718 /* 68 vars */) = 0
brk(NULL)                               = 0x56174aa4e000
access("/etc/ld.so.nohwcap", F_OK)      = -1 ENOENT (No such file or directory)
access("/etc/ld.so.preload", R_OK)      = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/etc/ld.so.cache", O_RDONLY|O_CLOEXEC) = 3
fstat(3, {st_mode=S_IFREG|0644, st_size=106420, ...}) = 0
mmap(NULL, 106420, PROT_READ, MAP_PRIVATE, 3, 0) = 0x7f867f8fc000
close(3)                                = 0
access("/etc/ld.so.nohwcap", F_OK)      = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/lib/x86_64-linux-gnu/libc.so.6", O_RDONLY|O_CLOEXEC) = 3
read(3, "\177ELF\2\1\1\3\0\0\0\0\0\0\0\0\3\0>\0\1\0\0\0\260\34\2\0\0\0\0\0"..., 832) = 832
fstat(3, {st_mode=S_IFREG|0755, st_size=2030544, ...}) = 0
mmap(NULL, 8192, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_ANONYMOUS, -1, 0) = 0x7f867f8fa000
mmap(NULL, 4131552, PROT_READ|PROT_EXEC, MAP_PRIVATE|MAP_DENYWRITE, 3, 0) = 0x7f867f2fe000
mprotect(0x7f867f4e5000, 2097152, PROT_NONE) = 0
mmap(0x7f867f6e5000, 24576, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_FIXED|MAP_DENYWRITE, 3, 0x1e7000) = 0x7f867f6e5000
mmap(0x7f867f6eb000, 15072, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_FIXED|MAP_ANONYMOUS, -1, 0) = 0x7f867f6eb000
close(3)                                = 0
arch_prctl(ARCH_SET_FS, 0x7f867f8fb4c0) = 0
mprotect(0x7f867f6e5000, 16384, PROT_READ) = 0
mprotect(0x56174a941000, 4096, PROT_READ) = 0
mprotect(0x7f867f916000, 4096, PROT_READ) = 0
munmap(0x7f867f8fc000, 106420)          = 0
fstat(1, {st_mode=S_IFCHR|0620, st_rdev=makedev(136, 5), ...}) = 0
brk(NULL)                               = 0x56174aa4e000
brk(0x56174aa6f000)                     = 0x56174aa6f000
write(1, "Hello world!\n", 13Hello world!
     )          = 13
exit_group(0)                           = ?
+++ exited with 0 +++
% time     seconds  usecs/call     calls    errors syscall
------ ----------- ----------- --------- --------- ----------------
  0.00    0.000000           0         5           mmap
  0.00    0.000000           0         4           mprotect
  0.00    0.000000           0         3           fstat
  0.00    0.000000           0         3           brk
  0.00    0.000000           0         3         3 access
  0.00    0.000000           0         2           close
  0.00    0.000000           0         2           openat
  0.00    0.000000           0         1           read
  0.00    0.000000           0         1           write
  0.00    0.000000           0         1           munmap
  0.00    0.000000           0         1           execve
  0.00    0.000000           0         1           arch_prctl
------ ----------- ----------- --------- --------- ----------------
100.00    0.000000                    27         3 total
```

Có tổng cộng 27 syscall được thực hiện, 3 fail.

### Python

Một chương trình Python 3.6 in ra màn hình dòng chữ `hello world` tương tự:

```sh
$ strace -cScalls python3 -c 'print("Hello world!")'
Hello world!
% time     seconds  usecs/call     calls    errors syscall
------ ----------- ----------- --------- --------- ----------------
  9.22    0.000277           2       166        32 stat
  7.96    0.000239           3        94           fstat
  7.19    0.000216           3        79           read
  7.19    0.000216           3        68           rt_sigaction
  8.09    0.000243           4        58           close
 10.25    0.000308           5        57         2 openat
  1.63    0.000049           1        43         6 lseek
 17.78    0.000534          16        34           mmap
  0.43    0.000013           1        18           getdents
 12.62    0.000379          24        16           mprotect
  2.43    0.000073           6        12           brk
  1.66    0.000050           4        12         2 ioctl
  5.03    0.000151          17         9         9 access
  0.37    0.000011           1         8           lstat
  2.46    0.000074          19         4           munmap
  0.30    0.000009           3         3           dup
  0.27    0.000008           3         3         1 readlink
  0.23    0.000007           2         3           sigaltstack
  0.63    0.000019          19         1           write
  0.53    0.000016          16         1           rt_sigprocmask
  0.00    0.000000           0         1           getpid
  0.00    0.000000           0         1           execve
  0.00    0.000000           0         1           fcntl
  0.00    0.000000           0         1           sysinfo
  0.00    0.000000           0         1           getuid
  0.00    0.000000           0         1           getgid
  0.00    0.000000           0         1           geteuid
  0.00    0.000000           0         1           getegid
  0.43    0.000013          13         1           arch_prctl
  0.80    0.000024          24         1           futex
  0.60    0.000018          18         1           set_tid_address
  0.63    0.000019          19         1           set_robust_list
  0.53    0.000016          16         1           prlimit64
  0.73    0.000022          22         1           getrandom
------ ----------- ----------- --------- --------- ----------------
100.00    0.003004                   703        52 total
```

Do output quá dài nên ở đây thay đổi câu lệnh, để có đầy đủ output hãy chạy
với option C hoa:

```sh
$ strace -CScalls python -c 'print("hello world")'
```

Chương trình Python đơn giản này thực hiện tới 703 syscall, 52 fail.

### Kết luận
27 với 703 thì cái nào "hơn"?

27 nhỏ hơn 703, còn 703 thì lớn hơn 27. Lập trình C cũng rất đơn giản, đúng
không!

Vậy nên khi lập trình, luôn nhớ rằng mọi thứ đều là tương đôi, đều phải đánh
đổi. Mấy em gái đã xinh mà code Python lại giỏi, chỉ có 2 khả năng xảy ra:

- 1 là thiếu cái gì đó
- 2 là học Python ở [PYMI](https://pymi.vn) rõ ràng <3.

### Đọc thêm
- System call: https://hvnsweeting.github.io/syscall.html
