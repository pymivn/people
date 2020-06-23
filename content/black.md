Title: black - quên đi nỗi lo PEP8
Date: 2020-03-15
Category: Trang chủ
Tags: python, black, formatter
Slug: black
Authors: hvnsweeting
Summary: Viết code Python thì phải chuẩn PEP8, nếu nó tự chuẩn thì sao? yeah!!!

## Code Python phải chuẩn PEP8
Ngay khi bạn mới làm quen với Python được vài tuần, mới biết tí for loop hay
function, PEP8 từ đâu đó sẽ hiện ra.
PEP8 là hướng dẫn viết code chuẩn Python, chứ không phải chuẩn C, Java, hay
không có chuẩn nào cả.
Nếu tự hoc code một mình, có khi giờ này bạn đã làm ra vài chục script, chạy
ầm ầm mà vẫn chưa 1 lần nghe PEP8. Tiêu chuẩn code là thứ chỉ hiện ra rõ ràng,
khi ta làm việc với người khác, chỉ sau vài function, sự mâu thuẫn về style
sẽ hiện ra ngay, và khi ông Chí Phèo không đồng ý với style của Bá Kiến, thì
cả 2 phải lên phường và thống nhất dùng chuẩn chung mà làng Vũ Đại đặt ra - hay
ở đây ta gọi là PEP8.

PEP8 có thể xem chi tiết tại [PEP0008](https://www.python.org/dev/peps/pep-0008/)
hay [https://pep8.org/](https://pep8.org/),
tiêu chuẩn PEP8 được chấp nhận trên toàn trái đất, thậm chí [CIA](https://medium.com/pymi/cia-d%C3%B9ng-python-r%E1%BA%A5t-nhi%E1%BB%81u-32144ecddd50),
Google cũng
chỉ sửa đi chút xíu, bởi nó là chuẩn hay, chuẩn tốt.

## Chuyện đau đầu về xì tai (style)
Style vốn là một thứ dễ gây ra tranh cãi. Tôi thích kiểu Việt Nam dịu dàng,
anh thích kiểu Pháp say đắm, ông kia thích kiểu Mỹ mạnh mẽ và hùng hục. Vậy
ai là người sai?
Cuộc tranh cãi về style viết code đã kéo dài suốt từ ngày lập trình xuất hiện,
tới giờ vẫn chưa kết thúc. Bởi đã là style, thì khó nói chuyện đúng sai.

Thế rồi mọi cuộc chơi vui, cũng phải đến hồi kết. Một ngôn ngữ lập trình đơn
giản xuất hiện với tên hai chữ `Go` (sau để tránh nhầm lẫn thì gọi là Golang),
và để tăng thêm sự đơn giản, nó đi kèm
sẵn một chương trình với tên `gofmt` (đọc là gâu phằm) - chương trình này sẽ
format tất cả code trong thư mục về một chuẩn mà nó đã quy định. Ban đầu,
người ta vẫn còn tranh cãi về việc bị ép style, nhưng rồi sau một hồi, lợi ích
của mỗi cái tôi đã sụp đổ trước lợi ích tập thể mà `gofmt` mang lại: mọi đoạn
code đều trông giống nhau, khiến style không còn gì để tranh cãi, lập trình viên
nhìn code của thằng kia cũng giống như của mình, dễ đọc - dễ hiểu hơn, expert
hay newbie đều chung 1 style cả.

`gofmt` không phải là chương trình đầu tiên làm vậy, trước đây, trong cộng
đồng Python đã xuất hiện 1 chương trình tên `autopep8` hay Google cũng có
[YAPF](https://github.com/google/yapf). Nhưng `Go` là ngôn ngữ đầu tiên mang
code formatter vào chính thống, chính thức chấm dứt cuộc chiến vô bổ về style
kéo dài vài thập kỷ. Để rồi từ đó, các ngôn ngữ lập trình khác đua nhau học theo
như [Rust](https://github.com/rust-lang/rustfmt),
[Elixir](https://elixir-lang.org/blog/2018/01/17/elixir-v1-6-0-released/)
và Python thì có [black](https://github.com/psf/black).

Không có giải pháp nào để giải quyết 1 vấn đề tốt hơn là làm cho nó biến mất.

## black là gì
Black là một câu lệnh cài bằng pip: `pip install black`, yêu cầu Python3.6 trở
lên mới chạy. `black` xuất hiện như một project của một lập trình viên nào đó
trên in tơ nét, sau vài năm trở nên cực kỳ phổ biến, và giờ đã chính thức
được nằm dưới mái nhà PSF (Python Software Foundation) cùng với `requests`.

[https://github.com/psf/black/blob/master/black.py](https://github.com/psf/black/blob/master/black.py)

Code của black chỉ vọn vẹn 4000 dòng, sử dụng các tính năng mới nhất của Python
như f-string, type annotation, asyncio...
(vì thế nên yêu cầu Python3.6+ để chạy, mặc dù vẫn có thể format code 2.7)

## Dùng black để format code Python

Ví dụ có 1 file foo.py

```
def sum_two(a,b):
    c= a  + b


    return c

```
Nếu thành thạo PEP8, thấy ngay có 4 chỗ phải sửa ở đây:
`a,b` thiếu dấu space sau `,`, `c` thiếu dấu space theo sau, sau `a` thừa 1
space, thừa 1 dòng
trống trước return. Vậy chỉ 3 dòng code, người review phải gõ ra 4 "vấn đề"
về style, và người code ra 3 dòng này, khi đọc review cũng chẳng vui vẻ gì,
kể cả người ta nói đúng.

Chạy:

```sh
$ black foo.py
reformatted foo.py
All done! ✨ 🍰 ✨
1 file reformatted.

$ cat foo.py
def sum_two(a, b):
    c = a + b

    return c

```

Đẹp, chuẩn, ngon! Không còn gì mong đợi thêm.
black có nhiều option để chỉnh style cho phù hợp với tiêu chuẩn của bạn,
hay dùng nhất là để set độ dài của 1 dòng, vốn là 79 ký tự theo chuẩn PEP8,
thì black mặc định là 88:
```sh
  -l, --line-length INTEGER       How many characters per line to allow.
                                  [default: 88]
```

Bạn có thể gọi `black -l79 .` để theo PEP8.

## Hành động của chúng ta
Đã đến lúc để quên đi việc format code bằng tay, nhớ vài chục tiêu chuẩn
của PEP8, format code hãy để cho đen (black) không vâu lo - việc này để
đen không vâu lo.
Thêm dòng này vào `Makefile` của bạn:

```
fmt:
	black -l79 .
```

hay cài đặt text editor/IDE tự động chạy `black` sau mỗi lần save code.

Thêm dòng sau vào CI để bắt quả tang thằng nào không dùng black:


```
black --check .
```

Black sẽ thông báo các file chưa chuẩn format:

```
$ black --check .
would reformat /home/hvn/me/people/content/mypy_simple.py
would reformat /home/hvn/me/people/publishconf.py
would reformat /home/hvn/me/people/pelicanconf.py
would reformat /home/hvn/me/people/fabfile.py
Oh no! 💥 💔 💥
4 files would be reformatted, 1 file would be left unchanged.
```

## Kết luận
Hãy dùng `black`! Và đừng quên share bài viết này, để cộng đồng code Python
không còn mất thời gian ít bổ.
