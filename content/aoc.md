Title: Chinh phục Advent of Code 2021 bằng Rust
Date: 2022-01-04
Category: Trang chủ
Tags: aoc, adventofcode, rust,
Slug: aoc2021
Authors: hvnsweeting
Summary: chiến game coding hot nhất tháng 12 mỗi năm, bằng ngôn ngữ hot nhất trên các bảng xếp hạng: Rust.

Advent of code (viết tắt AoC) là một cuộc thi code hàng năm kéo dài suốt 25 ngày trong tháng 12.
Mỗi ngày, lúc 12h trưa giờ Việt Nam (UTC+7), một bài toán đố nhỏ gồm 2 phần dưới dạng
câu chuyện "giải cứu đêm noel" sẽ được mở. Người chơi giải được phần 1 mới được chơi phần 2, giải
xong mỗi phần sẽ nhận được 1 sao. 12 giờ trưa ngày 25/12 sẽ ra bài cuối cùng, chỉ có 1 phần,
người chơi đủ 49 sao sẽ được tặng 1 sao và kết thúc trò chơi.

[Advent](https://www.lexico.com/definition/advent) /ˈadvɛnt/ trong tiếng Anh nghĩa là

> The first season of the Church year, leading up to Christmas and including the four preceding Sundays.

> (tôn giáo) kỳ trông đợi, mùa vọng (bốn tuần lễ trước ngày giáng sinh của Chúa) - theo [tratu.soha.vn](http://tratu.soha.vn/dict/en_vn/Advent)

Trang web [adventofcode.com](https://adventofcode.com/) được tạo bởi [Eric Wastl](http://was.tl/)
xuất hiện lần đầu vào [năm 2015](https://adventofcode.com/2015), ngày càng phổ biến và được cộng đồng
lập trình viên toàn cầu mong chờ mỗi tháng 12.

[![Back to December](https://img.youtube.com/vi/QUwxKWT6m7U/0.jpg)](https://www.youtube.com/watch?v=QUwxKWT6m7U)

Để thêm phần gay cấn, AoC có [bảng xếp hạng toàn cầu leaderboard](https://adventofcode.com/2021/leaderboard), người giải đầu tiên mỗi phần sẽ được 100 điểm và giảm dần. Người chơi cũng có thể tự tạo bảng xếp hạng riêng,
giúp các cộng đồng có thể tự chơi với nhóm của mình. PyMi tổ chức AoC với giải
thưởng hấp dẫn từ 2020, bảng xếp hạng tại [đây](https://adventofcode.com/2021/leaderboard/private) nhập mã  `416592-f7938347`

Trò chơi thu hút cả những lập trình viên nổi tiếng thế giới như:

- [Peter Norvig](http://norvig.com/) - giáo sư đầu ngành AI, giám đốc nghiên
cứu của Google. Năm 2020, [2021](https://github.com/norvig/pytudes/blob/main/ipynb/Advent-2021.ipynb) giải gần như tất cả các bài bằng Python trong 1 file Jupyter Notebook.
- José Valim - tác giả ngôn ngữ lập trình [Elixir](https://elixir-lang.org/), [livestream trên twitch](https://www.twitch.tv/collections/k_DLnk2tvBa-fQ) năm nay giải AoC với Elixir LiveBook (tương đương Jupyter Notebook).
- [geohot](https://en.wikipedia.org/wiki/George_Hotz) - hacker, người đầu tiên jailbreak iOS, hack PS3, ... https://www.youtube.com/watch?v=OxDp11u-GUo

Mỗi người chơi đến với AdventOfCode có một lý do khác nhau: có người để đua top
giật giải, có người dùng để học ngôn ngữ lập trình mới, phương pháp lập trình
mới (như Test Drive Development - TDD), người dùng để giải trí, thoát khỏi công việc nhàm chán
hàng ngày, người lại dùng để "ôn tập hàng năm" các kiến thức cấu trúc dữ liệu giải thuật "căn bản"
từng học trên giấy mà 10 năm đi làm
chưa dùng bao giờ như thuật toán Dijkstra, Priority queue, binary tree...

AoC có [cộng đồng Reddit](https://www.reddit.com/r/adventofcode/) đông đảo với
hơn 30 nghìn thành viên, nơi chia sẻ code bài giải, những video
thực hiện hiển thị, game hóa bài toán/bài giải và nhiều điều hấp dẫn khác.

Là một người chơi AoC lâu năm [từ 2018](https://github.com/hvnsweeting/adventofcode),
với 3 năm liền dùng Elixir, năm nay tôi quyết định chơi bằng Rust.

## Rust - ngôn ngữ lập trình tham lam: Performance, Reliability, Productivity - chọn cả 3!
![Rust](https://www.rust-lang.org/logos/rust-logo-blk.svg)

Ngôn ngữ hiện đại (từ 2010), [6 năm liền](https://stackoverflow.blog/2020/01/20/what-is-rust-and-why-is-it-so-popular/ )
được bình chọn là ngôn ngữ được [yêu thích nhất theo khảo sát của StackOverflow](https://insights.stackoverflow.com/survey/2021#section-most-loved-dreaded-and-wanted-programming-scripting-and-markup-languages).

Rust có thể dùng để thay cho:

- C++: [https://hacks.mozilla.org/2016/07/shipping-rust-in-firefox/](https://hacks.mozilla.org/2016/07/shipping-rust-in-firefox/)
- Go: [https://blog.discord.com/why-discord-is-switching-from-go-to-rust-a190bbca2b1f](https://blog.discord.com/why-discord-is-switching-from-go-to-rust-a190bbca2b1f)
- Python: [https://dropbox.tech/infrastructure/rewriting-the-heart-of-our-sync-engine](https://dropbox.tech/infrastructure/rewriting-the-heart-of-our-sync-engine)
- Ruby: [https://deliveroo.engineering/2019/02/14/moving-from-ruby-to-rust.html](https://deliveroo.engineering/2019/02/14/moving-from-ruby-to-rust.html)
- NodeJS: [https://www.rust-lang.org/static/pdfs/Rust-npm-Whitepaper.pdf](https://www.rust-lang.org/static/pdfs/Rust-npm-Whitepaper.pdf)

Rust thường được dùng để thay C++, C, được chọn khi một phần của hệ
thống cần tốc độ tối đa. Rust luôn đứng top đầu về tốc độ trong các bảng xếp hạng
benchmark [[1](https://benchmarksgame-team.pages.debian.net/benchmarksgame/box-plot-summary-charts.html)] [[2](https://www.techempower.com/benchmarks/)].

### Các phần mềm phổ biến viết bằng Rust
- [Servo](https://github.com/servo/servo) browser engine trong trình duyệt FireFox
- [ripgrep (rg)](https://github.com/BurntSushi/ripgrep) - thay cho grep command line, nhanh hơn, xịn hơn
- một phần của NodeJS npm: [https://www.rust-lang.org/static/pdfs/Rust-npm-Whitepaper.pdf](https://www.rust-lang.org/static/pdfs/Rust-npm-Whitepaper.pdf)
- FireCracker VM (để chạy các container phía dưới AWS Lambda) [https://github.com/firecracker-microvm/firecracker](https://github.com/firecracker-microvm/firecracker)
- Linux kernel hỗ trợ Rust bên cạnh C [https://lore.kernel.org/lkml/20211206140313.5653-1-ojeda@kernel.org/](https://lore.kernel.org/lkml/20211206140313.5653-1-ojeda@kernel.org/)

Bài viết sẽ giới thiệu vừa đủ các khái niệm của Rust đã dùng để chinh phục
50 bài toán đố của AoC 2021.

### Cài đặt
Chạy lệnh ghi trên trang [rustup.rs](https://rustup.rs/) để cài:

```
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
```

Mặc dù các hệ điều hành đều có package manager để cài Rust như Ubuntu `apt`, Fedora `yum`, hay MacOS `homebrew`,
`rustup` là công cụ được khuyên dùng chính thức vì nó có khả năng cài thêm các phần liên quan
đến việc code Rust như: document, auto-complete engine,... mà thường không có khi
cài qua package manager.

Code Rust có thể dùng [IntelliJ](https://www.jetbrains.com/rust/), hay [VSCode](https://marketplace.visualstudio.com/items?itemName=rust-lang.rust) để có hỗ trợ auto-complete, các editor
khác sẽ cần tự cài đặt thêm thủ công hơn.

### Tài liệu
- “the book” The Rust Programming Language: [https://doc.rust-lang.org/book/](https://doc.rust-lang.org/book/)
- Nửa giờ học Rust [https://fasterthanli.me/articles/a-half-hour-to-learn-rust](https://fasterthanli.me/articles/a-half-hour-to-learn-rust)
- Và nhiều tài liệu khác tại [https://www.rust-lang.org/learn](https://www.rust-lang.org/learn)

### Cách học
Gõ `rustup doc`, đọc 4 chương đầu + chương 8 trong
[https://doc.rust-lang.org/book/](https://doc.rust-lang.org/book/)
là đủ để code.

### Build & run
Rust compile code thành file binary rồi chạy.
Rust compiler có câu lệnh `rustc`, gõ `rustc file.rs` để compile, rồi chạy `./file`.
Nhưng Rust có kèm "cargo", package manager của Rust, như pip của Python, như
npm của nodejs... cargo hỗ trợ mọi tác vụ cần để code 1 Rust project.

Để tạo 1 Rust project, gõ:

```
$ cargo new project-name
     Created binary (application) `project-name` package
$ cd project-name/
```
lệnh này sinh ra file config cho cargo `Cargo.toml` và code 1 chương trình hello world
nằm trong src/main.rs

```
./Cargo.toml
./src
./src/main.rs
```

rồi chạy:

```
$ cargo run
   Compiling project-name v0.1.0 (/tmp/project-name)
    Finished dev [unoptimized + debuginfo] target(s) in 0.60s
     Running `target/debug/project-name`
Hello, world!
```

Để chạy test, gõ

```
$ cargo test
```

Để format code, gõ

```
$ cargo fmt
```

### Hello, World!
Gõ lệnh `cargo new` đã tự tạo ra code hello world, trong file src/main.rs:

```rs
fn main() {
    println!("Hello, world!");
}
```

Code của chương trình Rust nằm trong file `main.rs` và chạy từ function `main`.
`fn main() {...}` định nghĩa 1 function tên `main`, sử dụng từ khóa `fn`, thân
function nằm trong cặp `{}`.

```rs
    println!("Hello, world!");
```

không khác Python là mấy:

```
print("Hello, world!")
```

`println!()` trông như 1 function, nhưng trong Rust, khi thấy dấu `!` thì đó là
biểu diễn của 1 macro.

- macro **sinh ra code** thực hiện việc "in ra màn hình"
- Python `print` function thực hiện việc "in ra màn hình"

Mọi câu lệnh trong Rust kết thúc bằng dấu chấm phẩy `;`

### [ProjectEuler.net problem 1](https://projecteuler.net/problem=1)

> Tính tổng các số tự nhiên nhỏ hơn 1000 chia hết cho 3 hoặc 5.

Để tạo 1 biến, gõ `let tên = giá trị;`

```rs
fn main() {
    let mut result = 0;
    for i in 0..1000 {
        if i % 3 == 0 || i % 5 == 0 {
            result += i;
        }
    }
    println!("Kết quả: {}", result);
}
```

Cũng không quá khác code Python:

```py
result = 0
for i in range(0, 1000):
    if i % 3 == 0 or i % 5 == 0:
        result += i
print("Kết quả {}".format(result))
```

Rust giống C/C++/Java, dùng `{}`làm khối lệnh nhóm các câu lệnh trong if/for/function,
khác với Python dùng indentation (thụt vào 4 dấu space).
Biến trong Rust mặc định không
thay đổi được sau khi tạo, phải thêm từ khóa `mut` (viết tắt của mutable): `let mut result = 0;` để thay đổi `result`.
`println!` nhận 1 string, với `{}` để format, rồi tới các giá trị theo sau.

Rust có kiểu vector `Vec`, tương tự như Python `list`:

```rs
fn main() {
    let mut vec = vec![];
    for i in 0..1000 {
        if i % 3 == 0 || i % 5 == 0 {
            vec.push(i);
        }
    }
    let result: i32 = vec.iter().sum();
    println!("{}", result);
}
```

nhưng...

mặc dù có không ít khái niệm tương tự Python, hay syntax rút gọn trông cũng gần
giống, thì Rust lại là một con quái vật hoàn toàn khác, khác Python nhiều hơn
là giống.

#### Giống Python
Rust có các kiểu dữ liệu built-in tương tự Python:

| Python        | Rust      | Chú thích cho Rust
|---------------|-----------|--------------------
| list          | Vec       | vector
| dict          | HashMap   |
| set           | HashSet   |
| tuple         | (a, b)    | dùng cú pháp, không có kiểu ở dạng tên
| int           | i64, i32..| có u64 u32... cho kiểu không âm, usize cho kích thước
| float         | f64, f32  |
| bool          | bool      |
| str           | &str, String    |
| KHÔNG CÓ      | char      |
| None          | None      | giá trị

##### Tuple

```rs
let (name, age) = ("PYMI", 6);
```

##### Vector
Vector tương tự như Python list. Lặp qua các phần tử của 1 vector:

```rs
let vec = vec![1, 2, 3, 5];
for n in vec {
    println!("{}", n);
}
```

##### HashSet

```rs
use std::collections::HashSet;
fn main() {
    let mut set: HashSet<i32> = HashSet::from([2, 3, 1, 1, 2, 3, 5]);
    set.extend([3, 4, 5]);
    dbg!(&set);
}

[src/main.rs:5] &set = {
    5,
    4,
    1,
    3,
    2,
}
```

- `dbg!` để **print debug** trong Rust.

##### HashMap

HashMap key không có thứ tự, tương tự với Python dict trước 3.6,
cú pháp import `use std::collections::HashMap;`
như Python `from collections import Counter`:
```rs
use std::collections::HashMap;
fn double(x: i32) -> i32 {
    return x * 2;
}
fn main() {
    let mut d: HashMap<&str, i32> = HashMap::from([("Hà Nội", 1_612), ("Cà Mau", 967)]);
    d.insert("TP HCM", 687);
    for (k, v) in d {
        println!("{}: {}", k, double(v));
    }
}
//Hà Nội: 1612
//TP HCM: 687
//Cà Mau: 967
```

Cú pháp type của function tương tự Python:

```py
def double(x: int) -> int:
    return x * 2

def main():
    d: dict[str, int] = dict([("Hà Nội", 1_612), ("Cà Mau", 967)])
    d["TP HCM"] = 687
    for (k, v) in d.items():
        print("{}: {}".format(k, double(v)))
main()
```

Khác với đoạn code giải Project Euler 1, code trên có khai báo type
cho các biến. Rust không bắt buộc phải khai báo type khi nó có thể tự
suy luận được,
vì vậy đa số code không cần ghi type, khi nào cần, Rust compiler sẽ thông báo.

### Giải [ngày 1](https://adventofcode.com/2021/day/1)
Nhìn chung các bài trong 7-8 ngày đầu tiên thường dễ, độ khó tăng dần về sau,
đặc biệt là tuần cuối cùng.

> How many measurements are larger than the previous measurement?

Cho một dãy số tự nhiên (độ sâu của tàu ngầm) tăng giảm tùy ý.
Có bao nhiêu lần độ sâu tăng so với lần trước. Ví dụ:

```
199 (N/A - no previous measurement)
200 (increased)
208 (increased)
210 (increased)
200 (decreased)
207 (increased)
240 (increased)
269 (increased)
260 (decreased)
263 (increased)
```

Phần chú thích trong `()` là hướng dẫn, đề chỉ cho 1 file chứa các số, mỗi số 1 dòng.
Ví dụ trên có 7 lần tăng.

Các bước làm:

- đọc file input vào thành các dòng chứa các string
- biến kiểu string thành integer (số nguyên)
- lặp qua các giá trị, đếm số lần giá trị sau lớn hơn giá trị trước.

Bài giải, theo kiểu dùng vòng lặp:

```rs
fn main() {
    let s = "199
200
208
210
200
207
240
269
260
263";
    let lines: Vec<&str> = s.lines().collect();
    let mut increases_count = 0;
    let mut prev: &str = lines[0];
    for line in &lines[1..] {
        let n: i32 = line.parse().unwrap();
        let p: i32 = prev.parse().unwrap();
        if n > p {
            increases_count += 1;
        }
        prev = line;
    }
    println!("{}", increases_count);
}
```

Người chơi có thể dùng `std::fs::read_to_string` để đọc từ file, nhưng ngày đầu
tiên dùng Rust, với một bài khởi động đơn giản thế này thì phần cản trở tốc độ giải cũng chính là
Rust. Bỏ qua việc đọc file trong lúc gấp gáp này hoàn toàn chấp nhận được.
Một vài điểm chú ý:

- `line.parse()` để parse string thành integer. Rust tự biết parse thành kiểu
gì do vế trái khai báo kiểu cho kết quả `let n: i32`. `parse` không trả ngay về
số mà trả về kiểu `Result`, Result chứa số kiểu i32, hoặc chứa Error
nếu không parse được. `.unwrap()` để lấy ra giá trị `i32` hoặc panic dừng chương
trình luôn nếu parse gặp lỗi.
- Python chỉ có kiểu `int` duy nhất cho integer, trong Rust có nhiều kiểu số: `i32`
cho kiểu integer với kích thước 32 bit, giá trị từ `-2**31` tới `2**31-1` (-2147483648..=2147483647), tương tự
với `i64`. Ngoài ra còn có kiểu `u32` (unsigned int), chỉ chứa số không âm, với
`u32` có giá trị từ `0` tới `2**32-1` (`0..=4294967295`), tương tự cho `u64`.
- `&str` là 1 trong 2 kiểu string hay dùng trong Rust, kiểu còn lại là `String`,
ngoài ra Rust có nhiều kiểu string khác dùng trong các trường hợp riêng biệt.
- `s.lines()` không trả ngay về một `Vec<&str>`, nó trả về kiểu `Lines`. Để biến
thành kiểu `Vec`, dùng `collect()`. Chú ý vế trái phải khai báo kiểu do Rust
không thể tự suy ở đây vì người dùng có thể gọi `collect()` mà nhận được nhiều
kiểu khác nhau như Vec, HashSet, ... tùy ý.
- `&lines[1..]`, Vector có slice như Python, thay cú pháp `[a:b]` bằng `[a..b]` và
không có index âm (như -1).

Cách trên không được coi là code theo kiểu Rust, mà giống viết code C/Python dịch sang
Rust hơn. Một phiên bản khác sử dụng `iterator` mang phong cách functional programming,
phải đến ngày thứ 10 trở đi, hay đọc xong [chương 13 trong "The Rust Book"](https://doc.rust-lang.org/stable/book/ch13-00-functional-features.html) mới quen được kiểu này:

```rs
fn main() {
    let s = std::fs::read_to_string("input01").unwrap();
    let lines: Vec<i32> = s.lines().map(|i| i.parse().unwrap()).collect();
    let increases_count = lines
        .iter()
        .zip(&lines[1..])
        .filter(|(prev, next)| next > prev)
        .count();
    println!("{}", increases_count);
}
```

Ý tưởng khác một chút, thay vì duyệt qua dãy số, ta duyệt qua 2 dãy cùng 1 lúc
với `zip`, dãy thứ 2 bắt đầu từ phần tử index 1, và filter (lọc)
ra các cặp mà có giá trị sau lớn hơn giá trị trước, rồi đếm.

`|(prev, next)| next > prev` là một closure, giống như Python lambda nhưng viết
bao nhiêu dòng cũng được. Code này tương tự Python `lambda t: t[1] > t[0]`.

Sau khi nhập kết quả giải xong phần 1, đề phần 2 hiện ra yêu cầu thay vì đếm số
sau lớn hơn số trước thì đếm tổng 3 số sau lớn hơn tổng 3 số trước.

```
1
2
3
4
```

thì có 2+3+4 > 1+2+3.

Tạo 1 list mới chứa tổng của 3 số liên tiếp, sau đó dùng list
đó làm đầu vào cho code của phần 1.

```rs
let lines: Vec<i32> = lines
    .iter()
    .zip(&lines[1..])
    .zip(&lines[2..])
    .map(|((x1, x2), x3)| x1 + x2 + x3)
    .collect();
```

ở đây một lần nữa dùng zip để duyệt qua 3 dãy số cùng lúc.

### Giải [ngày 3](https://adventofcode.com/2021/day/3)

Tính năng lượng tiêu thụ của tàu dựa trên báo cáo

```
00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010
```

Cách tính: `power = epsilon rate * gamma rate`.
Với gamma rate là các bit xuất hiện nhiều nhất ở mỗi cột trong tất cả các số.
Và epsilon rate là các bit xuất hiện ít nhất ở mỗi cột.
Ví dụ trên: cột 1 có nhiều số 1 nhất, cột 2 có nhiều số 0 nhất, ...
sau 5 cột ta có `10110`, đổi ra hệ cơ số 10 được giá trị 22.

Giải phần này, chỉ cần làm đúng như các bước mà đề bài mô tả, lấy các giá trị
theo từng cột, đếm giá trị nào nhiều nhất rồi cho vào 1 list, cuối cùng biến
thành số.

```rs
fn day02() -> i32 {
    let s = std::fs::read_to_string("input02").unwrap();
    let mut gamma_bits: Vec<_> = vec![];
    let mut epsilon_bits: Vec<_> = vec![];
    let lines: Vec<&str> = s.lines().collect();
    for idx in 0..lines[0].len() {
        let mut one = 0;
        let mut zero = 0;
        for line in lines.iter() {
            let chars: Vec<char> = line.chars().collect();
            if chars[idx] == '0' {
                zero += 1;
            } else {
                one += 1;
            }
        }
        if one > zero {
            gamma_bits.push(1);
            epsilon_bits.push(0);
        } else {
            gamma_bits.push(0);
            epsilon_bits.push(1);
        }
    }
    to_i32(gamma_bits) * to_i32(epsilon_bits)
}
fn to_i32(bits: Vec<i32>) -> i32 {
    let mut r = 0;
    for (idx, b) in bits.iter().enumerate() {
        r += b * 2i32.pow((bits.len() - idx - 1) as u32)
    }
    r
}
```

Các điểm chú ý:

- Rust dùng các kiểu khác nhau cho các loại số khác nhau. `bits.len()` hay `enumerate()`
là kiểu `usize`, chứa số nguyên không âm, dùng để đo kích thước. Nghe thì giống
u32 hay u64 nhưng Rust hay C++ coi đây là kiểu riêng biệt và lập trình viên phải
tự convert sang kiểu khác nếu muốn dùng khác đi. Số mũ của pow phải là kiểu u32.
Dùng `as u32` để ép kiểu từ `usize`. Cũng không thể viết `2.pow()` mà phải dùng
`2i32` để chỉ rõ kiểu của nó.
- Dùng `vec.push(i)` để thêm `i` vào cuối `vec`, như Python list.append.
- `for (idx, b) in bits.iter().enumerate()` như Python `for idx, b in enumerate(bits)`,
tuple trong Python không cần thiết có `()` còn trong Rust là bắt buộc.
- Có thể bỏ trống kiểu phần tử của Vec bằng dấu gạch dưới `_`: `Vec<_>` do đoạn
code sau có phần push(), Rust sẽ tự suy ra kiểu dựa vào kiểu của giá trị được push.
- Rust tự return dòng cuối cùng không có dấu `;`. Cũng có thể viết `return to_i32(gamma_bits) * to_i32(epsilon_bits);`

### Các bài hay, nổi bật
- Day 15: tìm đường đi ít nguy hiểm nhất, có thể sử dụng thuật toán trong
  sách giáo khoa "cấu trúc dữ liệu và giải thuật": Dijkstra (/ˈdaɪkstrəz/).
  Google code sẵn hoặc lên [wikipedia xem pseudocode](https://en.wikipedia.org/wiki/Dijkstra's_algorithm#Pseudocode) rồi viết lại.
  Điểm thú vị là để tăng tốc thuật toán này, cần dùng khái niệm có tên
  [Priority Queue](https://en.wikipedia.org/wiki/Dijkstra's_algorithm#Using_a_priority_queue), một loại queue đặc biệt, giúp tìm kiếm min hay max tức thì `O(1)`.
  Trong Python có thể dùng [`import heapq`](https://docs.python.org/3/library/heapq.html), trong Rust có sẵn kiểu [BinaryHeap](https://doc.rust-lang.org/std/collections/struct.BinaryHeap.html).
- Không ít bài toán người chơi sẽ phải viết các "hàm đệ quy" - (Recursive function)
  để giải, như **metaverse** của [day 21](https://adventofcode.com/2021/day/21).
- Năm nay vắng bóng ["game of life"](https://github.com/norvig/pytudes/blob/main/ipynb/Life.ipynb), nhưng vẫn có một phiên bản trá hình trong [day 20](https://adventofcode.com/2021/day/20).
- Day 16, người chơi phải viết 1 parser và chạy đoạn code **BITS** để tính toán,
  hệ thống này giống một ngôn ngữ [nhà LISP](https://pp.pymi.vn/article/scm1/) và có thể "cheat" ra [dùng
  LISP để giải cho nhanh](https://github.com/hvnsweeting/adventofcode/blob/master/2021/src/day16.rs)
- Day 18 có kiểu dữ liệu Binary Tree, nếu chưa đọc hết [chương 15 "The Rust Book"](https://doc.rust-lang.org/stable/book/ch15-01-box.html#enabling-recursive-types-with-boxes) thì sẽ
  khá khó để biểu diễn kiểu dữ liệu recursive này trên Rust. Nên tạm "cheat" ra
  [dùng Python để giải](https://github.com/hvnsweeting/adventofcode/blob/master/2021/src/day18.ipynb).
- Day 19 là bài phải code code trâu bò nhất. Tương tự day 20 của năm 2020, ám
  ảnh người chơi mãi về sau với lượng code vài trăm dòng cần viết. Lý do: bài này
  được ra vào ngày thứ 7/chủ nhật cuối cùng trong giải.
- Và cũng có những bài giải tay nhiều khi nhanh hơn viết code như [day 23](https://adventofcode.com/2021/day/23). Giải
  tay giống như đang chơi game.
  Thậm chí có người chơi trên reddit đã [viết game
  để giải bài này](https://www.reddit.com/r/adventofcode/comments/rmspb7/2021_day_23_it_was_nice_on_paper_but_its_even/).


## Ownership, move, borrow & clone
Khó có thể code Rust 25 ngày mà không động đến khái niệm borrow-checker, ownership.

Rust không có Garbage Collector (viết tắc GC).

Các ngôn ngữ như JavaScript, Python, Ruby, PHP, Go, Java, C# có GC nên lập
trình viên có thể tạo các giá trị tùy ý, GC sẽ theo dõi và tự xóa đi các giá trị
không dùng nữa.

Code C/C++ không có GC, lập trình viên cần tự viết code cấp phát (allocate) và giải phóng
 (free) bộ nhớ (memory) để tạo các kiểu dữ liệu (trên heap).

Rust theo cách riêng của mình, đưa ra khái niệm "ownership" để biết ai là chủ
của 1 giá trị, giúp quản lý bộ nhớ mà không cần tới GC.

#### Real "hello, Rust!"
Chương trình sau, dựa vào các kiến thức từ ví dụ đã đưa ra, kết hợp kinh nghiệm
lập trình các ngôn ngữ khác thì thấy hoàn toàn hợp lý, Rust
compile báo lỗi:

```rs
fn sum(v: Vec<i32>) -> i32 {
    let mut s = 1;
    for x in v {
        s = s + x;
    }
    return s;
}
fn product(v: Vec<i32>) -> i32 {
    return 1;
}
fn main() {
    let v: Vec<_> = vec![1, 2, 3, 5];
    let _s = sum(v);
    let _p = product(v);
}
```
Compile lỗi:
```
error[E0382]: use of moved value: `v`
  --> main.rs:14:22
   |
12 |     let v: Vec<_> = vec![1, 2, 3, 5];
   |         - move occurs because `v` has type `Vec<i32>`, which does not implement the `Copy` trait
13 |     let _s = sum(v);
   |                  - value moved here
14 |     let _p = product(v);
   |                      ^ value used here after move
```

Rust compiler hướng dẫn chi tiết về vấn đề xảy ra, thậm chí đôi khi
đưa ra cả hướng dẫn sửa code. Lỗi xảy ra `use of moved value: v` với chỉ dẫn:

- tại dòng 13, sum nhận đầu vào v: "value moved here".
- dòng 14, product nhận đầu vào v: "value used here after move".

trong các ngôn ngữ lập trình khác, việc các đoạn code dùng chung 1 giá trị là chuyện
hoàn toàn bình thường và không có gì phải suy nghĩ, Rust thì khác.

#### owner và move
Khi gán biến,

```fn
let x = vec![1,2,3];
let y = x;
let z = x; // not work, compile error:  value used here after move
```

Ban đầu, `x = vec![1,2,3]`, x là owner (chủ sở hữu) của giá trị `vec![1,2,3]`.
Khi viết `y = x`, quyền sở hữu được chuyển
sang cho y. Sau dòng này, x không còn dính dáng tới `vec![1,2,3]`, hay không còn giá trị,
không thể dùng được nữa, nên không thể gán cho z được.

Tương tự, khi gọi function sum, sum sẽ trở thành chủ sở hữu mới của giá trị mà v đang chứa,
sau dòng này, v không còn hợp lệ. Việc chuyển đổi quyền sở hữu này gọi là
"move" ownership.

Thay vì chuyển quyền sở hữu, có thể thực hiện "mượn": borrow. Function sẽ khai báo
mình muốn own (sở hữu), hay muốn borrow (mượn).

Function sum viết lại để borrow, thêm dấu `&` trước kiểu của xs:
`fn sum(xs: &Vec<i32>) -> i32 {`

và khi gọi function: `sum(&vec)`.

Ký hiệu `&` gọi là reference. `&v` tạo một reference **refer** (chỉ) đến giá trị của
vec nhưng không own nó.

```rs
fn sum(v: &Vec<i32>) -> i32 {
//...không đổi...
}
fn product(v: Vec<i32>) -> i32 {
    return 1;
}
fn main() {
    let v: Vec<_> = vec![1, 2, 3, 5];
    let _s = sum(&v);
    let _p = product(v);
}
```
Code mới sẽ chạy được, do sum chỉ borrow giá trị của v, chứ không own,
v vẫn là chủ của vector để sau đó, move cho product trở thành owner.

#### Stack và heap <id="heap">
Trong máy tính, có 2 loại bộ nhớ cấu trúc theo cách khác nhau:

Stack **thường** có kích thước nhỏ (VD: 2KB, 4KB, 8KB,... cũng có thể [lớn dần lên đến vô cùng](https://dave.cheney.net/2013/06/02/why-is-a-goroutines-stack-infinite)), hoạt động như kiểu dữ liệu "stack" (last in first out - LIFO),
dữ liệu nhét vào stack (push) phải có kích thước biết trước (khi compile),
lấy dữ liệu từ stack (pop) thường nhanh hơn heap.
Các kiểu dữ liệu có thể chứa trong stack có kích thước biết trước: như
số (i32 - 32 bits, i64, f64, ...), string cố định (&str), array (`[3;i32]`).

Heap là vùng bộ nhớ tự do, khi muốn dùng phải yêu cầu hệ điều hành cấp cho (allocate),
dùng xong nếu không giải phóng trả lại hệ điều hành thì chương trình sẽ dùng
ngày càng nhiều RAM, gọi là memleak (memory leak).

Khi tạo 1 Vector hay HashMap trong Rust, kích thước của chúng có thể thay đổi
khi chạy (VD: thêm phần tử vào vector), nên chúng nằm trên heap. Lý do không
thấy code để alloc/free ở các ví dụ trên bởi Rust thực hiên tự động free giá trị khi biến
"out of scope" (thường là ra khỏi block `{}`).

Với các kiểu dữ liệu trên stack, không cần borrow bởi chúng sẽ tự copy do
các giá trị này nhỏ. Với các kiểu dữ liệu trên heap, cần gọi `.clone()` để
copy giá trị. Người mới code Rust có thể dùng `clone()` để tránh các vấn đề
ban đầu về ownership cho tới khi nắm được ownership & borrow.

Xem thêm tại [đây](https://doc.rust-lang.org/stable/book/ch04-01-what-is-ownership.html).

## Kết quả
PyMi AoC 2021 kết thúc vào 12 giờ trưa ngày 26/12/2021, với giải thưởng:

![leaderboard]({static}/images/aoc21_leaderboard.png)

- giải nhất: [tung491](https://github.com/tung491/advent_to_code_2021) học viên PyMiHN1706
- giải nhì: [thevivotran](https://github.com/thevivotran) học viên PyMiHCM2008.
- giải ba: stuncb97 học viên PyMiHN2010 - cựu vô địch 2020.

Một tràng pháo tay cho các game thủ dù bận công việc vẫn nhịn ăn trưa cày
marathon code suốt 25 ngày 🎉😍

## Kết luận
Advent of Code là một chuyến phiêu lưu thú vị hàng năm, là cơ hội tuyệt vời
để "vui vẻ" với code, học được thêm không ít điều mới mẻ.

Rust dù hơi dài dòng
so với Python, không hợp để code nhanh trong các cuộc thi, nhưng không phải
quá khó, lại là một vũ khí hạng nặng ngang C/C++ cho vào balo mang đi chiến khi cần.
Hàng ngàn lập trình viên đã liên tục vote Rust là ngôn ngữ yêu
thích nhất, còn bạn?

Và nhớ đừng quên đọc [văn mẫu](https://github.com/norvig/pytudes/blob/main/ipynb/Advent-2021.ipynb) từ giám đốc nghiên cứu Google nhé!

Tạm biệt 2021, chúc mừng năm mới 2022!

## Finish
Toàn bộ code giải 25 bài
(trừ bài 23 giải bằng giấy và bút) có trong [repo](https://github.com/hvnsweeting/adventofcode/tree/master/2021/src)
PS: đây là code của 1 Rust newbie.

<img src="{static}/images/aoc21.png" width=800>

## Tham khảo
- Stack vs Heap [https://doc.rust-lang.org/stable/book/ch04-01-what-is-ownership.html](https://doc.rust-lang.org/stable/book/ch04-01-what-is-ownership.html)
- [https://matklad.github.io//2020/09/20/why-not-rust.html](https://matklad.github.io//2020/09/20/why-not-rust.html)

## Ủng hộ tác giả
- [Ủng hộ tác giả 🍺](https://www.familug.org/p/ung-ho.html)
