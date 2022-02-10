Title: Ký sự chiếm cờ tại SNYK CTF 2021
Date: 2021-10-06
Category: Trang chủ
Tags: ctf, hacking, python, docker, regex, golang, stego, javascript
Slug: ctf
Authors: hvnsweeting, khanhduy8, các Pymiers và khách mời
Summary: SNYK CTF 2021 write-up

## CTF là gì?

Capture the Flag (CTF) là một trò chơi được ưa chuộng của những người trong
ngành bảo mật thông tin, thường tổ chức theo dạng cuộc thi với nhiều đội
tham gia và có đội dành chiến thắng.

CTF có 3 dạng phổ biến:

- Jeopardy-style CTFs: Đề thi thường gồm nhiều dạng bài thuộc
các lĩnh vực khác nhau trong ngành: cryptography, stego, binary analysis,
reverse engineering, mobile security, web hacking, OS, Linux...
- attack-defence: mỗi đội được giao cho 1 hệ thống có các lỗi bảo mật, và 2 đội
sẽ vá hệ thống của mình đồng thời tấn công hệ thống của đội khác.
- mixed: đủ dạng

CTF với người làm bảo mật giống như
[LOL](https://www.leagueoflegends.com/en-us/) với các thanh niên chơi esport
vậy, cũng có các giải đấu lớn thế giới.
Danh sách các giải đấu lớn có thể xem trên [ctftime](https://ctftime.org/ctfs),
nổi tiếng nhất có thể kể tới DEF CON CTF, phổ biến nhất có thể gọi tên Google CTF.

## SNYK CTF 2021

[SNYK.io](https://snyk.io/) là một công ty làm về bảo mật, cung cấp các dịch vụ
phát hiện lỗi bảo mật tích hợp vào hệ thống khi phát triển phần mềm ở các doanh
nghiệp và cộng đồng opensource. Năm nay snyk tổ chức CTF và team pymi nhận được
[lời quảng cáo trên "PythonWeekly" email](https://mailchi.mp/pythonweekly/python-weekly-issue-519), chiến thôi.
Đây là lần thứ 2 HVN tham gia một giải CTF, lần đầu là tại [Framgia
Code War
2017](https://viblo.asia/p/code-war-2017-online-round-write-ups-part-1-aWj531Y1Z6m),
bẵng cái 4 năm, không có kinh nghiệm gì mới do công
việc chẳng liên quan tới hắc hiếc gì.

**https://ctf.snyk.io/ Fetch the Flag at SnykCon 2021!**

**October 5, 9:00 am - 7:00 pm ET**

đăng ký rồi rủ rê team 5 người.

Cách tính điểm: 500 cho mỗi bài, giảm dần theo số lượt giải. Tức giải xong sớm
thì sẽ được điểm cao, sau khi giảm dần, điểm có thể tới min là 50.

Các bài thi sẽ cần đi tìm 1 đoạn flag dạng `SNYK{...}` rồi điền vào website
của snyk.

## Cảnh báo
Code trong các cuộc thi CTF thường được viết ra nhanh nhất, nên thường không
theo các chuẩn sạch gọn đẹp hay tối ưu, nó đơn giản là thứ bạn viết ra khi có
sức ép về mặt thời gian và mục tiêu là kết quả.
Chỉ nên dùng để tham khảo, tránh dùng làm văn mẫu.

### Cảnh báo 2
Bạn đọc chưa quen phần nào có thể bỏ qua phần đó, các bài chia theo các lĩnh
vực khác nhau.

Bài viết bởi HVN, các phần do các tác giả khác viết có ghi rõ trong từng bài.

## Các bài đã giải trong thời gian thi đấu

![done]({static}/images/ctf_solved.jpg)

## Coding
### CALC-UL8R

Đề cho 1 địa chỉ để nc vào

```sh
$ nc 35.211.207.36 8000
  ____    _    _     ____      _   _ _     ___  ____
 / ___|  / \  | |   / ___|    | | | | |   ( _ )|  _ \
| |     / _ \ | |  | |   _____| | | | |   / _ \| |_) |
| |___ / ___ \| || ||_____| |_| | |__| (_) |  _ <
 \____/_/   \_\_____\____|     \___/|_____\___/|_| \_\


31521 * 2455 - 29590 - o - 40881 + 34681 = 77331423
o =
```

cần tính giá trị của biến, trong ví dụ này là `o`, rồi nhập vào.
Cứ nhập xong, enter, phía server sẽ trả về 1 phép tính khác.

Vậy có 2 việc cần làm:

- kết nối đến server để nhận đề và gửi kết quả: việc này có thể dùng Python telnetlib
- đọc biểu thức và tính ra kết quả

Do lần đầu dùng [`telnetlib`](https://docs.python.org/3/library/telnetlib.html#telnet-example), nên cũng khá vất vả một lúc mới tìm
ra cách đọc dùng [regex](https://pp.pymi.vn/article/10x/)
thay vì dùng string.

- `read_until("string")` sẽ đọc đến khi thấy "string" thì trả nội dung về
- `expect(list, timeout=None)`  đọc đến khi 1 trong các regex  pattern match.

Sau khi đã gửi nhận được, cần viết code giải phương trình, ban đầu mình có tự viết code để giải phương trình bằng cách thay biến trong phương trình (1 ký tự, dùng regex) bằng số 0, rồi chuyển vế các phép tính còn lại. Cách làm đơn giản này đúng cho đến khi nó sai: biểu thức có phép nhân. Nghĩ tới giải phương trình trên Python là nghĩ tới sympy, search `sympy solve equation` thấy ngay

- [https://stackoverflow.com/a/30776918/807703](https://stackoverflow.com/a/30776918/807703)

sửa lại để nhận mọi biến, PS: ở đây mình ko chăm chỉ viết tay từ a đến z mà gõ 1 dòng Python là xong

```py
>>> import string; ', '.join(string.ascii_lowercase)
'a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z'
```

Code giải phương trình
```py
from sympy import solve
from sympy.abc import a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z
from sympy.parsing.sympy_parser import parse_expr

def solve_meThis(string_):
    try:
        lhs =  parse_expr(string_.split("=")[0])
        rhs =  parse_expr(string_.split("=")[1])
        solution = solve(lhs-rhs)
        return solution
    except:
        print("invalid equation")


equation = text.decode("utf-8").splitlines()[-1]
valid_text = equation

[result] = solve_meThis(valid_text)
```

Thực hiện gửi nhận liên tục các phép tính cho đến khi server trả về kết quả:

```py
(-1, None, b'\nSNYK{37d779963c037715c02624b6963008f55e92d12e8714a15b7a905c1c997d1afc}\n')
```

File Jupyter Notebook dùng giải bài này
[https://gist.github.com/hvnsweeting/7e00e139912b9d65a1ec7c1913fdb513](https://gist.github.com/hvnsweeting/7e00e139912b9d65a1ec7c1913fdb513)

### Random flag generator - python
Một bài được tag thẻ `python`, cho 1 file code python và 1 file log:

```py
import random
import time
import hashlib

seed = round(time.time())

random.seed(seed, version=2)

while True:
    rnd = random.random()

    hash = hashlib.sha256(str(rnd).encode()).hexdigest()
    flag = f"SNYK{{{hash}}}"

    if "5bc" in hash:
        with open("./flag", "w") as f:
            f.write(flag)
        break
    else:
        print(f"Bad random value: {rnd}")

print("Flag created 🎉")
```

```
Bad random value: 0.3719072557403058
Bad random value: 0.3702330745519661
Bad random value: 0.0634360689087381
Bad random value: 0.2952684217196877
Bad random value: 0.49843979869018884
Bad random value: 0.7895773927381043
Bad random value: 0.2917373566923527
Bad random value: 0.9030776618431813
Bad random value: 0.7181809628413409
Bad random value: 0.28050872595896736
Bad random value: 0.17458286936713008
Bad random value: 0.2767390568969583
Bad random value: 0.5492478684168797
Bad random value: 0.2641653670084557
Bad random value: 0.5156703392963877
Bad random value: 0.32839693347899057
Bad random value: 0.6998299885658202
Bad random value: 0.5811672985185747
Bad random value: 0.4644468325648108
Bad random value: 0.49982517906634727
Bad random value: 0.9333988943747559
Bad random value: 0.7513893164652713
Bad random value: 0.18638831058360805
Flag created 🎉
```

Đọc code thấy để tìm được flag, cần tìm ra
giá trị `seed` mà người ra đề đã dùng.
Các học viên [học Python tại Pymi.vn](https://pymi.vn) đều được học: các function trong `random` chỉ là "gỉa ngẫu nhiên" và thực chất là chạy thuật toán sinh số ngẫu nhiên dựa trên giá trị `seed`. `seed` trong bài này gợi ý là UNIX timestamp, chạy từ 0 tới khoảng 1 tỷ 6 (1633537375).
Cách tìm đơn giản là sửa lại code, chạy lần lượt với từng seed, so sánh đầu ra (thay vì print thì cho vào 1 string) với file log. Nếu giống nhau tức đó là gía trị seed cần tìm.

Vấn đề ở cách làm này, khi Python thực hiện khoảng 16 triệu phép +1 mỗi giây (xem [cpu.pymi.vn](https://cpu.pymi.vn/)), thì để tính 1 tỷ 6 phải mất ít nhất 100 giây.
Mỗi giá trị seed lại sinh nhiều random value, thời gian sẽ gấp thêm 20 - 30 lần. Và khi mang chạy thật, mỗi giây nó tính khoảng được 5000-10000 seed. Tức quá chậm và cần tăng tốc.
Ném thêm các giải pháp như dùng thread/multiprocess cũng không khá hơn là bao.
Sau 30 phút, 1 tiếng không ra kêt quả, và giải xong 1 bài khác trong thời gian chờ này, mình quay lại tối ưu code.

Thay vì tính hết output của mỗi seed, cho nó dừng lại ngay nếu dòng log đầu tiên khác với dòng đầu tiên trong log.txt.
Sau 1-2 phút đã có kết quả.

Code: [https://gist.github.com/hvnsweeting/619ecf04aa9b57bd6b44f3fcc57fe8c2](https://gist.github.com/hvnsweeting/619ecf04aa9b57bd6b44f3fcc57fe8c2)

### Russian doll
Đề bài cho ở dạng đã mã hóa:

> Esp qwlr td DOKnGoIgKSsVvizaEAJmEgxiEShQKjjgyfeLhdutuIhObpZr IIEPL pyncjaepo. Alddhzco stye: iiii.

và sau khi @pham [dùng tool](https://planetcalc.com/1434/) để giải mã [ROT15](https://www.familug.org/2014/12/programming-phe-rot13.html) thì thu được nội dung:

> The flag is SDZcVdXvZHhKkxopTPYbTvmxTHwFZyyvnutAwsjijXwDqeOg XXTEA encrypted. Password hint: xxxx.

CTF thường là vậy, sau lớp này sẽ qua lớp khác.
Giờ để ý lại tên bài, cũng với hàm ý tương tự, Russian doll Matryoshka, trong con này là con khác.

![doll](https://images.unsplash.com/photo-1613981948475-6e2407d8b589?ixlib=rb-1.2.1&q=80&fm=jpg&crop=entropy&cs=tinysrgb&dl=didssph-PB80D_B4g7c-unsplash.jpg&w=640)

<center>
Photo by <a href="https://unsplash.com/@didsss?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Didssph</a> on <a href="https://unsplash.com/s/photos/russian-doll?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash</a>
</center>

với lượng điểm thu được cho bài này là 490/500 lúc  October 6th, 2:44:17 AM, sau ~7 tiếng, thì đây rõ là 1 bài khó.
Hoặc nó tiết lộ 1 phần về công cụ của người chơi đều là Python, vì sao hãy đọc tiếp...
Cho một thuật toán mã hóa cho trước, với key là 4 ký tự, hẳn không khó khăn gì các team có thể tải ngay lib Python trên mạng về và bruteforce vài phút là có ngay kết quả. Đen thay, 2 thư viện tìm thấy đầu tiên, đều có vẻ không dùng được

- [https://pypi.org/project/xxtea/](https://pypi.org/project/xxtea/)

có 1 dòng yêu cầu ` # Key must be a 16-byte string.`
Trong khi bài này key là 4 ký tự.

- [https://pypi.org/project/xxtea-py/](https://pypi.org/project/xxtea-py/)

một cái lib khá oái oăm khi cài thì ok mà dùng thì lại đòi cffi, và hầu hết mọi người dừng lại ở đó.

Vậy phải làm sao? kết quả khi search cũng trả về nhiều thư viện cho ngôn ngữ khác như C, C++, Golang... mà ngồi viết C sau 10 năm không viết thì rất căng.
Nhưng cuối cùng, Golang lại là giải pháp, nhờ vài năm code Go ăn tiền, sau 5 phút, ten ten có luôn kết quả:

```go
package main

import (
	"encoding/base64"
	"fmt"
	"log"
	"strings"

	"github.com/xxtea/xxtea-go/xxtea"
)

func main() {
	encodedString := "SDZcVdXvZHhKkxopTPYbTvmxTHwFZyyvnutAwsjijXwDqeOg"
	originalStringBytes, err := base64.StdEncoding.DecodeString(encodedString)
	if err != nil {
		log.Fatalf("Some error occured during base64 decode. Error %s", err.Error())
	}

	key := "1234567890"
	for _, a := range key {
		for _, b := range key {
			for _, c := range key {
				for _, d := range key {
					keyNow := string(a) + string(b) + string(c) + string(d)
					decrypt_data := string(xxtea.Decrypt(originalStringBytes, []byte(keyNow)))
					if strings.Contains(decrypt_data, "SNYK") {
						fmt.Printf("%s\n", decrypt_data)
					}
				}
			}
		}
	}
}
```

[Code](https://gist.github.com/hvnsweeting/b8d518fdd67b85e9bf9f6a16af6221af)

kết luận ở đây là thành thạo thêm một ngôn ngữ backup phổ biến như
C/C++/Java/C#/Golang sẽ rất hữu ích khi không dùng được Python. Nói thì dễ, chứ
thành thạo 1 ngôn ngữ đến mức dùng được lúc áp lực thời gian không phải chuyện
ai cũng có thời gian/tiền của đầu tư, giải pháp khác có vẻ dễ hơn là kiếm team
member với tool set khác nhau.

PS: lib `xxtea-py` sau khi cài `sudo apt install -y build-essential python3-dev`
và `pip install cffi xxtea-py` trên Ubuntu 20.04, chạy được ra kết quả

```py
import base64
import xxtea

s = 'SDZcVdXvZHhKkxopTPYbTvmxTHwFZyyvnutAwsjijXwDqeOg'
secret = base64.decodestring(s.encode("utf-8"))
for a in range(10):
    for b in range(10):
        for c in range(10):
            for d in range(10):
                r = xxtea.decrypt(secret, "{}{}{}{}".format(a,b,c,d))
                if b"SNYK" in r: exit(r)
```

## Linux/system
### All your flags are belong to root - Linux CLI

Bài cho 1 user `u`, password và 1 địa chỉ để SSH vào.
Sau khi login, thấy như sau:

```sh
all-your-flags-are-belong-to-root-p4j0:~$
```

gõ `ls` không thấy file gì. `cd` lung tung, tới `/`, `ls` thấy file `/flag` nhưng file này chỉ `root` mới đọc được.

Gõ thử `sudo` không có, gõ `su -l` để
trở thành root nhận được 1 message:

```sh
all-your-flags-are-belong-to-root-p4j0:/$ su -l
su: must be suid to work properly

$ ls -la `which su`
lrwxrwxrwx    1 root     root            12 Jun 15 14:34 /bin/su -> /bin/busybox
```

File su này khá khác thường so với máy bình thường:

```
~$ ls -la `which su`
-rwsr-xr-x 1 root root 67816 Jul 21  2020 /usr/bin/su
```

Để từ user thường chiếm được quyền root đọc file /flag, cần "làm cách nào đó", và lời gợi ý là **suid**.

`SUID` là khái niệm ít phổ biến với người dùng CLI thông thường, họ học hết chmod 755 777 400 là khá đủ rồi.
`SUID` là một giá trị đặc biệt để cấp quyền cho user, khi user chạy chương trình sẽ dùng UID của người sở hữu file thay vì UID của user, hay
nói cách khác, trở thành người sở hữu / "chiếm quyền" trong lúc chạy chương trình này.
Khi chmod, set SUID sử dụng số `4` trước số chmod thông thường. Ví dụ `4755`.
Lệnh `su` ở trên là 1 ví dụ có SUID.
Lý do mình biết tới SUID, do công việc trước đây có viết một chương trình thực hiện gửi ICMP (ping), mà lại yêu cầu quyền root. Trong khi bình thường gõ lệnh ping thì không phải sudo/su bao giờ. Hóa ra [lệnh ping (ngày xưa) set SUID](https://security.stackexchange.com/a/222800/11544) (giờ ko set nữa).

Dùng `find` tìm trên máy các file có set SUID:

```
$ find / -perm -4000
```

Tìm thấy file lệnh `curl`. `curl` là chương trình thường dùng để gửi HTTP request, nó cũng đọc được file khi thay `http://` bằng `file://`

```
all-your-flags-are-belong-to-root-p4j0:/$ curl file:///flag
SNYK{06b0e0ae4995af71335eda2882fecbc5008b01d95990982b439f3f8365fc07f7}
```

PS: Nhìn lại, nếu hiểu ý của đề thì đó là lời gợi ý file flag nằm ở `/` (root).

Ref

- [https://security.stackexchange.com/a/222800/11544](https://security.stackexchange.com/a/222800/11544)
- [https://www.redhat.com/sysadmin/suid-sgid-sticky-bit](https://www.redhat.com/sysadmin/suid-sgid-sticky-bit)
- [https://www.linuxjournal.com/content/gettin-sticky-it](https://www.linuxjournal.com/content/gettin-sticky-it)
- [https://www.linuxnix.com/suid-set-suid-linuxunix/](https://www.linuxnix.com/suid-set-suid-linuxunix/)

### Robert Louis Stevenson - docker

Đề cho 1 file Docker image chứa "kho báu". Tải file này về,
không nhớ chính xác là tên gì, tạm gọi là `file.tar`.
Bản chất các file "chương trình"/"data" trên máy tính thường là một dạng file archive/nén như zip/tar.
Docker image cũng vậy:

```
# tar xf ../file.tar
# grep -Rin SNYK .
Binary file ./b3b0b5528b213a9d35315784c9907fdeb5d8bf89a0bb012ee63546b3a1c2e10b/layer.tar matches
# tar xf .././b3b0b5528b213a9d35315784c9907fdeb5d8bf89a0bb012ee63546b3a1c2e10b/layer.tar
# grep -Rin SNYK
ak/pp/tv/bc/22/flag:1:SNYK{23acc4111e1905ba1832cab7f1660284e3d1b91d3c2ead7bcec41ee8a4bd5ce9}
```

Ref:

- [https://www.familug.org/2012/09/nen-giai-nen-bang-command-line-trong.html](https://www.familug.org/2012/09/nen-giai-nen-bang-command-line-trong.html)
- [https://github.com/moby/moby/blob/master/image/spec/v1.2.md#combined-image-json--filesystem-changeset-format](https://github.com/moby/moby/blob/master/image/spec/v1.2.md#combined-image-json--filesystem-changeset-format)
- [https://github.com/hvnsweeting/pocker](https://github.com/hvnsweeting/pocker)
- [grep: https://www.familug.org/2012/10/vai-combo-lenh-de-nho-d-se-uoc-update.html](grep: https://www.familug.org/2012/10/vai-combo-lenh-de-nho-d-se-uoc-update.html)

PS: Robert Louis Stevenson là tác giả của truyện "đảo giấu vàng" (Treasure Island)


## Steganography (stego - giấu tin trong ảnh)

### qrrr
via [khanhduy8](https://github.com/khanhduy8)

![qr]({static}/images/ctf_qrrr.png)

Bài cho một file ảnh QR đủ màu sắc.
Lấy zalo ra quét thử không được, như vậy file này thực ra không phải QR đúng chuẩn.
Nhìn vào màu sắc của hình thì có vẻ như QR này gồm 3 mã QR tương ứng với 3 đoạn mà khi ghép lại với nhau ta có được flag.
OK. Giờ dùng một công cụ đơn giản để xử lý file ảnh này. Link Tool: [stegonline.georgeom.net](https://stegonline.georgeom.net/upload)
Một file ảnh màu RGB này có 3 bit planes là (Red, Green, Blue).
Thử với plane Red với giá trị là 6/8 [ta có](https://i.ibb.co/zX5y40c/red.png),
trông có vẻ ổn nhưng với ảnh QR để quét thì ta cần reverse lại màu. Sau khi reverse ta được

![reversed]({static}/images/ctf_qrrr2.png)

Quét mã này ra: `12d99aa3a92f1abbb7d40786`
Do không có {} nên đây chắc là đoạn giữa
Tương tự thử với Green 6 được: SNYK{6947bd4818ffc1768f2
Với Green 7: 5ff8d4e4958d8007a3897}
Ghép 3 đoạn lại ra flag: `SNYK{6947bd4818ffc1768f212d99aa3a92f1abbb7d407865ff8d4e4958d8007a3897}`

PS: ngày hôm sau, khanhduy8 nhận ra qrrr là lời gợi ý về 3 mã qr.

PPS: hvn dùng Firefox trên Android mở ra ngay phần đuôi trong 3 mã, kết luận: không dùng zalo.

## Exploit (khai thác lỗ hổng bảo mật)

### Invisible Ink - javascript
via [khanhduy8](https://github.com/khanhduy8)

Bài này cho 1 link web và một [file source code]({static}/ctf/index.js), 1 file [package.json]({static}/ctf/package.json).
Có thể đọc source, thấy nghi nghi rồi google thư viện `lodash`, nhưng pro @hvn
setup [công cụ của Snyk](https://docs.snyk.io/)
để quét rồi nên ta có kết quả vulnerbility

![snyk scan]({static}/images/ctf_snyk_scan.jpeg)

Chú ý đến vul thứ 2. Đây là PoC của exploit vul này [Prototype Pollution in lodash | Snyk](https://snyk.io/vuln/SNYK-JS-LODASH-450202)
Trong file source code có đoạn check:
`if(output.flag)`
nếu `true` sẽ response giá trị của flag
biến output hiện tại đang là:
`output = {}` nên sẽ không trả về kết quả chúng ta cần
Trong source code có sử dụng Unsafe Object recursive merge

```
merge (target, source)
	foreach property of source
	if property exists and is an object on both the target and the source
		merge(target[property], source[property])
	else target[property] = source[property]
```

trong đó target là output còn source là request nên chỉ cần thay request bình thường từ:
`{"message": "ping"}`
sang
`{"constructor": {"prototype": {"flag": true}}}`
khi này thì Object đã bị thêm vào thuộc tính `flag:true`
Do đó `output.flag` sẽ trả về true. Ta có response chứa flag:
`SNYK{6a6a6fff87f3cfdca056a077804838d4e87f25f6a11e09627062c06f142b10dd}`

![snyk scan]({static}/images/ctf_lodash.jpeg)

## Kết quả
Team PyMi xếp thứ 44 / 537 đội có ghi điểm, có lúc xếp thứ 24. 3h buồn ngủ quá
ae lăn quay hết nên tụt hạng mạnh :))

![44]({static}/images/ctf_rank.png)

Theo đánh giá của 1 dân chơi thì giải CTF này thuộc loại trung bình, chưa khó,
nhưng không phải game chuyên nghiệp do chỉ kéo dài 10 tiếng và lợi thế về
múi giờ cho bên đông Mỹ (8PM giờ Việt Nam -> 6AM), các giải chuyên nghiệp sẽ
kéo dài 24h để đảm bảo công bằng.

Đi thi với tinh thần cọ sát, các bài thi rất thú vị, học được nhiều điều mới
nên rất vui.

## Kết luận
CTF là một **trò chơi** thú vị. Như mọi trò chơi khác, nó dễ gây nghiện, và
nghiện quá là không tốt. CTF có loại khó, có loại không khó tẹo nào, để bắt đầu
chơi, hãy học dùng lệnh trên Linux, lập trình 1 ngôn ngữ bất kỳ
và tham gia thử các game dễ như trên [overthewire.org](https://overthewire.org/wargames/)
hay khó hơn là [Google CTF beginners quest](https://capturetheflag.withgoogle.com/beginners-quest)
chơi nhiều là khác quen, và làm quen với chuyện "không phải bài nào mình cũng giải được".

## Updated 2022-02-10 - phần 2 by @pham
#### Lời nói đầu

Đây là một giải CTF của snyk.io - một tổ chức phát triển platform dạng "Audit source code", như nhận định ban đầu thì các task thiên về dạng programming, misc, và một số bài là lỗ hổng web mức độ medium.

Trong giải thì mình khá là phế khi không giải được mấy task quan trọng, mặc dù đã nhìn ra cách giải, nhưng payload không hiểu sao không work, thật là buồn, thôi năm sau phục thù cùng anh em

Sau cuộc thi thì mình không viết writeup ngay, đến giờ viết lại thì nội dung không được trọn vẹn, ae thông cảm :)

#### Task Magician
Đây là một task old-school về `PHP Type Juggling Vulnerabilities`
dạng như:

```
var_dump(md5('240610708') == md5('QNKCDZO'));
```

Do không sử dụng toán tử `===` (giống nhau về cả value và type) mà sử dụng `==`  (chỉ cần giống nhau về value), ta hoàn toàn có thể tìm được strings có md5 thỏa mãn điều kiện bài toán.

Tham chiếu thêm tại:
[https://www.netsparker.com/blog/web-security/php-type-juggling-vulnerabilities/](https://www.netsparker.com/blog/web-security/php-type-juggling-vulnerabilities/ )

#### Task not_hot_dog
Task cung cấp cho mình bộ ba `n,e,c` ta có thể biết ngay đây là một bài attack RSA, với c là bản mã, sau khi giải mã ra sẽ thu được FLAG.

Do khi implement RSA họ sử dụng e lớn, nên sẽ bị ảnh hưởng bởi  Wiener attack (đây cũng là dạng old-school RSA trong các giải CTF)
Sử dụng công cụ tại: https://github.com/orisano/owiener để thu được flag.

```py
>>> import owiener
>>> e = 387825392787200906676631198961098070912332865442137539919413714790310139653713077586557654409565459752133439009280843965856789151962860193830258244424149230046832475959852771134503754778007132465468717789936602755336332984790622132641288576440161244396963980583318569320681953570111708877198371377792396775817
>>> n = 609983533322177402468580314139090006939877955334245068261469677806169434040069069770928535701086364941983428090933795745853896746458472620457491993499511798536747668197186857850887990812746855062415626715645223089415186093589721763366994454776521466115355580659841153428179997121984448771910872629371808169183
>>> d = owiener.attack(e, n)

>>> print (d)
40127490441880177477224469176371044914847896019034308382923938039797354608313
```

#### Task Browser preview
![done]({static}/images/browser_preview.png)

Với tên và cách setup task này thì có thể thấy đây là một task về bug SSRF (Server-side request forgery)
SSRF như tên gọi thì attacker sẽ khiến cho server thực hiện những request tùy ý (tùy vào từng trường hợp mà các protocol sẽ là http/dns/ftp/smpt/gopher...) như vậy khi có bug SSRF chúng ta sẽ bypass được các bộ filter về source IP  - do request đến từ chính server (localhost)

Chức năng của web là nhập vào một URL, ta sẽ preview được nội dung trang web đó.
URL phải validate dạng như sau:

```java
    static boolean isUrlValid(String url) {
        Pattern domainPattern = Pattern.compile("^https?://[a-z-0-9]+[.][a-z]+.*$", Pattern.CASE_INSENSITIVE);
        Matcher matcher = domainPattern.matcher(url);

        return matcher.find();
    }

```

Đọc source thì thấy tiếp  server có handler ở port 7654, có thể read flag thông qua phương thức này.
```java
class DebugServer {
    public void run() throws IOException {
        HttpServer server = HttpServer.create(new InetSocketAddress(7654), 0);
        server.createContext("/flag", new FlagHandler());
        server.setExecutor(null);
        server.start();
    }
}
```
Như vậy ý đồ là quá rõ  ràng, mình sẽ nhập vào một URL dạng localhost:7654/flag để get flag, URL làm sao thỏa mãn được bộ filter trên là OK.
Mình sử dụng URL dạng: http://domain.localhost:7654/flag
Có thể kham khảo các cách `bypass localhost` của hacktrick
https://book.hacktricks.xyz/pentesting-web/ssrf-server-side-request-forgery

#### Electronbuzz
grep nội dung là ra được FLAG.

#### Instant flag checker

Task này mình cũng không còn nhớ rõ đề và script hôm đó viết, chắc hôm đó giải lẹ qua nên viết console luôn, không lưu lại file.

Về ý tưởng của bài này là dạng bruteforce để thu được flag, vậy tại sao để bruteforce được thành công ?

Đó là sử dụng time-based, các giá trị đúng sẽ có response time khác với với các giá trị sai.
Trong những vấn đề mà server không phản hồi cho mình nội dung response (tức là bị blind) thì việc áp dụng kỹ thuật time-based (bắt server thực hiện các heavy task) hoặc sử dụng kỹ thuật outbound (đẩy http request hay dns request ra public server khác) thực sự hữu ý.


#### Tổng kết
Chân thành cảm ơn các anh em @bác Hưng, @đăng hoàng, @Duy Hồ, @ Khang lê hôm đó đã thức đêm làm cùng.
Hy vọng năm sau ae sẽ phục thì dành được rank cao hơn (target top 20)


HVN at [http://pymi.vn](http://pymi.vn) and [https://www.familug.org](https://www.familug.org).

- [Ủng hộ tác giả 🍺](https://www.familug.org/p/ung-ho.html)
