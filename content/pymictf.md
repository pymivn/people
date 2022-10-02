Title: Ký sự một năm cướp giật (capture the flag)
Date: 2022-10-02
Category: Trang chủ
Tags: ctf, hacking, python, security, pwn, rev, crypto, web, misc, forensics
Slug: pymictf
Authors: hvnsweeting
Summary: 1 năm sau SYNK CTF 2021, team PyMi đã đứng top 10 Việt Nam trên ctftime.org, học được rất rất nhiều.

Tháng 10 năm 2021, tình cờ tham gia SNYK CTF sau 1 tin quảng cáo dạo trên email, lập team sau vài ngày rồi cháy 24 giờ, đứng thứ 42 bảng xếp hạng SNYK.io
Kể từ ngày ấy, đều đặn mỗi 2 ngày cuối tuần, [team CTF PyMi](https://ctftime.org/team/175619) đi chiến tất cả các giải lớn nhỏ. 
Từ newbie với ước mơ nhỏ bé "chỉ cần giải được 1 bài", giờ đã trở thành "thi thoảng mới giải được 1 bài, còn toàn giải được 2 bài trở lên".

Chơi CTF xong có một cảm giác thôi: sợ. 
Sợ đến mức phải rút dây điện ra để không còn bị hack nữa.
Mọi sự an toàn đều chỉ là "ảo tưởng", đến cả [chính phủ các cường quốc G7 còn bị
hack](https://www.imdb.com/title/tt3774114/), thì mấy cái trang web lương lập trình viên 10 triệu lấy đâu ra mà còn.

Bài viết chỉ nói tới phần kỹ thuật liên quan đến hacking, còn một phần khác đáng
sợ không kém là "social hacking" là nguyên nhân của hàng rổ vụ hack có thể tham khảo [trên in-tơ-nét](https://www.theverge.com/2022/9/16/23356959/uber-hack-social-engineering-threats).

![Ghost In The Wires](https://www.mitnicksecurity.com/hs-fs/hubfs/buy-ghost.png?width=448&name=buy-ghost.png)
<center>[Ghost In The Wires - cuốn sách về 1 hacker social-engineer số 1 thế giới](https://www.mitnicksecurity.com/ghost-in-the-wires)</center>

Có một câu nói khá khó nghe nhưng nổi tiếng:

> "There are two types of companies in the world: those that know they've been hacked and those that don't." - Misha Glenny

(từ điển dịch: có 2 loại công ty trên thế giới: loại biết họ đã bị hack, và loại không biết).

Dưới đây là những bài học cho lập trình viên làm web (NGHỀ NGUY HIỂM),
và những thành tựu, kinh nghiệm thu được từ chơi CTF trong suốt các ngày cuối tuần của 1 năm.

PS: bài viết dưới góc độ một newbie trong ngành security.

## Các bài PHẢI học cho web developer
### ĐÂY LÀ NGHỀ QUÁ NGUY HIỂM

Bước chân vào nghề lập trình web tưởng chỉ cần biết thiết kế DB theo 3 normalization form,
dùng cái DB SQL & NoSQL, dùng framework xịn nhất, hiểu kiến trúc MVC, biết pull docker về build rồi bật là đủ (ăn).
Nhưng nếu trong đầu không được trang bị đầy đủ kiến thức về security thì ngành làm web như một bãi mìn đầy kinh sợ.
Cụ thể hơn, nếu bạn đang làm lập trình web mà công ty không có training, và bạn 
cũng không hiểu đầy đủ (HIỂU không phải CHỈ là biết nghĩa) những từ đáng sợ sau, thì khả năng 96.69 %, công ty bạn
thuộc loại 2. Mà thậm chí hiểu đủ, cũng không làm cho bạn miễn dịch với hack.

Trường lớp học có thể dạy làm ra trang web, chạy được, đúng đủ tính năng,
những trang cá nhân này nếu có bị hack, cũng không có hậu quả lớn. Nhưng công ty,
muốn không bị hack, phải thực hiện nhiệm vụ training của mình, không làm tự chịu.

Các nghề khác cũng đều có nguy cơ bị hack dù là DevOps hay sysadmin, nhưng web là phổ biến nhất.

### Học có đủ vẫn bị hack như thường
Điển hình như năm 2021 lê thê tận sang 2022 vẫn còn, [log4shell](https://en.wikipedia.org/wiki/Log4Shell) là từ khóa đáng sợ nhất cho các doanh nghiệp lớn, nhỏ (đều code bằng Java), khi thư viện log phổ biến nhất của Java "log4j" dính lỗi bảo mật cho phép hacker có thể "làm đủ trò".
Lỗi này của ai để đi đổ lỗi? dù có hiểu đủ các lỗi bảo mật phổ biến
nhất, thì một cái bug "nhỏ" trong thư viện quá phổ biến này cũng đủ san bằng một 
công ty. (PS: các hacker thường không muốn "san bằng công ty" trừ khi quá ghét, mà muốn bí mật nằm vùng trong đó rồi hưởng lợi thì hơn).

### Path traversal, SQLi, XSS, SSTI, CSRF, JWT
Điều đáng sợ đầu tiên là hầu hết các lỗi bảo mật này đều được viết tắt, với
những chữ S, những chữ X, khiến cho chưa học thuộc từ khóa thì nhìn tên cũng đã sợ.

#### SQLi - SQL injection
Lỗi bảo mật phổ biến nhất thế giới từ 2005-2018 (số liệu chém gió mà chắc sẽ đúng), nguyên nhân 
là do nối/format string mà không dùng ? hay %s đã ghi chú trong các thư viện xử lý SQL.

Never do this -- insecure! (format SQL string)

```py
t = 'RHAT'
cur.execute(f"SELECT * FROM stocks WHERE symbol = '{t}'")
```

Do this instead

```py
t = ('RHAT',)
cur.execute('SELECT * FROM stocks WHERE symbol=?', t)
print(cur.fetchone())
```

(trích tài liệu [python sqlite3](https://docs.python.org/3.10/library/sqlite3.html#sqlite3-placeholders) - [postgres](https://www.psycopg.org/docs/usage.html#the-problem-with-the-query-parameters) cũng có tài liệu tương tự, 2022 DB nào cũng có hết).

Lỗ hổng này phổ biến tới mức công ty bảo mật hàng đầu cũng dính, tây cũng dính, tàu cũng dính,
để thấy dù đã sau hơn 15 năm lộng hành, ngành giáo dục thế giới vẫn chưa hoàn
thành nhiệm vụ. Lỗi này không từ ai, kể cả đại học, siêu học bằng cấp đầy mình mà ra,
đừng đổ tại học, vì học có dạy đâu mà biết. 

#### SSTI - Server side template injection 
Vẫn là "injection", tức nhét thêm 1 chút chút vào cái phần chính hợp lệ.

Ở SQLi thì inject thêm 1 phần câu SQL, ở "command injection" thì thêm 1 vài
dấu `;rm -rf /` đi kèm sau đầu vào được yêu cầu thì ở SSTI là thêm 1 chút (code)
vào chỗ mà phải nhập giá trị bình thường.

SSTI là việc hacker nhập vào một đoạn code, mà khi server thực hiện
render template (như django template, hay Jinja2)
sẽ chạy đoạn code này trên server. Về cơ bản khi dùng các template engine đều
đã xử lý SSTI bằng cách escape các ký tự "bất thường", nhưng vẫn không ít khi
các giá trị lọt vào không qua đường template render mà xử lý ngay như string trên python.

Ví dụ với fstring đầy uy lực theo [semgrep](https://semgrep.dev/docs/cheat-sheets/flask-xss/):

Bug:

```py
render_template_string(f"<div>{request.args.get("name")}</div>")
```

Fix:

```py
render_template_string("<div>{{ name }}</div>", name=request.args.get("name"))
```

#### XSS - Cross Site Scripting
XSS thực sự khó hơn 2 cái lỗi trên đối với lập trình viên Python, bởi nó dùng JavaScript.
Nhưng ở mức khó bình thường, nên vẫn học được. Cơ chế cơ bản như sau:
- Trang web cho người dùng nhập vào (ví dụ user), và sau đó sẽ hiển thị giá trị đó ở 1 trang khác
- Hacker nhập vào đoạn code javascript, phổ biến nhất là `<script>alert(1);</script>`
- Khi người dùng khác, hay nguy hiểm hơn là admin đọc nội dung này, nó sẽ chạy đoạn code JavaScript hacker đưa vào
trên máy họ. Đoạn code JavaScript thì có thể làm đủ trò, đơn giản nhất là gửi cookie của người dùng tới một trang khác để đánh cắp cookie này. Hacker sau đó lấy cookie này đăng nhập vào tài khoản người dùng, chiếm quyền.
Nguy hiểm nhất khi người bị hack là admin -> xong, hết bài.

Dùng framework cũng không miễn nhiễm với XSS. Ví dụ trang chủ của Flask:

Bug:

```py
@app.route("/index/<msg>")
def index(msg):
  return "Hello! " + msg
```

yes, sorry!!! nhưng nếu trang web lưu giá trị này lại và hiển thị ở 1 chỗ khác,
và người khác xem, thì nó đã đủ cơ chế để hacker thực hiện XSS bằng cách nhập
code JavaScript vào msg.

Fix:

chỉ return render_template() hay jsonify(), không return string trực tiếp.

[Django doc](https://docs.djangoproject.com/en/4.1/topics/security/#cross-site-scripting-xss-protection) có ví dụ khi trong template ghi

Bug:

```html
<style class={{ var }}>...</style>
```

Nếu hacker đưa được var với giá trị là `class1 onmouseover=javascript:func()`
thì code javascript này vẫn được chạy.

Fix: phải quote double quote -> `"{{ var }}"`.

Hay với link - tham khảo thêm tại [doc Flask](https://flask.palletsprojects.com/en/2.2.x/security/#cross-site-scripting-xss):

Bug:

```html
<a href="{{ value }}">click here</a>
```

Hacker nhập vào render thành: 

```html
<a href="javascript:alert('unsafe');">click here</a>
```

Fix: phải set [CSP](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Content-Security-Policy).

#### CSRF - Cross Site Request Forgery
bài tập về nhà cho bạn đọc, tự học. PS tham khảo tại doc [Django](https://docs.djangoproject.com/en/4.1/ref/csrf/).

#### JWT - JSON web tokens
[JWT](https://pyjwt.readthedocs.io/en/latest/) không phải lỗi bảo mật, nhưng hiểu đầy đủ về nó là quan trọng do việc sử
dụng phổ biến của công nghệ này trong authen.

#### Còn NHIỀU nữa
Xem nhiều các lỗi bảo mật phổ biến tại [OWASP](https://owasp.org/www-project-top-ten/)

#### Sysadmin, devops - command injection
Các tool bash/python của sysadmin thường dính lỗi "command injection" khi cho phép người dùng nhập 1 phần câu 
lệnh vào để chạy

Bug trên shell script:

```sh
echo "Hello $1"
```

Hacker nhập vào "hi; echo hello > hacked" là xong.

Hay dùng Python [subprocess](https://docs.python.org/3.10/library/subprocess.html#security-considerations):

Bug:

```py
subprocess.run(f"echo hello {username}", shell=True)
```

Fix:

```py
subprocess.run(f"echo hello {username}".split(), shell=False)
```

Dùng os.system tương đương trường hợp bug trên.

## "Bóc phốt" những hiểu nhầm về CTF

### Phải rất "giỏi máy tính" mới chơi được, phải biết code
Giải CTF có giải khó giải dễ, có bài khó bài dễ, nhiều bài kéo đề vào tool là ra 
kết quả, chưa kịp dùng não.

Nghề hack đã có từ ngày có máy tính, nên việc hack cũng có sẵn cả rổ tool để dùng,
vậy nên nhiều bài không cần phải code.

Có mục mới "OSINT", kỹ năng "tìm kiếm thông tin" cũng không cần dùng tới code, 
giống như giải đố, tìm vị trí, tìm ai đó trên các trang mạng xã hội.

Tất nhiên để làm được nhiều bài khó hơn thì cần biết code if/for.

### Chơi pwn (binary exploitation) hay rev (reverse engineer) phải biết đọc assembly như tiếng Việt
Tool rất quan trọng, và có nhiều tool rất xịn. 
Các cầu thủ đá bóng đi toàn giày đinh loại cực xịn, các runner đi Nike airflow màu hồng phá kỷ lục thế giới,
các game thủ dùng bàn phím độ trễ siêu thấp, chuột có dăm ba nút phụ để combat cho nhanh, chả nghề nào chân trần phi vào quái thú để thất bại rồi ra nghĩa địa cả (trở về là còn tốt).

Các pon thủ, rev thủ toàn dùng [IDA Pro](https://hex-rays.com/ida-pro/) bản trả tiền, [Ninja](https://binary.ninja/) hàng xịn, chứ hàng free như Ghidra hay radare2 nhiều khi không xịn bằng. 
### Chơi crypto phải giỏi toán
Giỏi toán (mà phải đúng loại toán) đúng là có lợi, có thể giải nhiều bài khó,
nhưng crypto cũng có nhiều tool sẵn như [RSACTFtool](https://github.com/RsaCtfTool/RsaCtfTool), nhét đề vào viết thêm tí code là giải được cả mớ. Nhớ luyện hết theo [CryptoHack](https://cryptohack.org/challenges/rsa/), đọc cả blog vì có mấy lần đề KHÓ ra trúng [bài blog trên cryptohack](https://blog.cryptohack.org/twitter-secrets).

### Toàn là code C, C++, Assembly
Mục pwn hay rev đa số là C/C++/asm, nhưng thi thoảng cũng có Python, Erlang, JavaScript.
Các mục khác (web/misc) sẽ chứa đủ loại ngôn ngữ chứ ít có C/C++/Asm.
### top 10 ctftime.org là giỏi nhất
Đầu tiên là chuyện rất thú vị, 6 tháng đầu năm, top 10 là một bộ mặt khác hoàn toàn với 
thời điểm đầu tháng 10 này. Cục diện thay đổi hoàn toàn, những top 10 vài tháng trước giờ 
đã tụt xuống 20 30.

Thứ hai, ctftime.org chỉ là phần nổi của tảng băng (rất chìm), đâu phải hacker nào cũng rảnh mà đi thi, còn đang bận hack cả thế giới. Riêng có giải [HTB Business](https://ctftime.org/event/1685) mới thấy các team security của các công ty ló mặt.

### Pickle vô dụng 
Một loại bài gần như giải nào cũng có, là lỗi bảo mật liên quan đến pickle. Nếu chơi cho vui thì nghe cũng được,
nhưng thứ không bảo mật thế giờ còn ai dùng? tìm mỏi mắt còn không thấy, đầu tư thời gian vào pickle chỉ để chơi CTF,
không có tác dụng trong thực tế... cho đến khi thấy nó: Bottle - một web framework rất phổ biến của Python, vẫn
dùng pickle khi get cookie, [issue mở từ 2016, vẫn chưa fix](https://github.com/bottlepy/bottle/issues/900).

## Những khó khăn
### Lịch chơi dày đặc
Bận rộn đi làm cả tuần, cuối tuần 2 ngày nghỉ lại chiến, tuần nào cũng thế, chưa
kịp ngấm giải này, học các kỹ thuật mới, thì đã tới giải khác. Chơi CTF có lẽ
là lý do blog này cả năm nay không có bài nào :p.

### writeup delay
Các bài viết hướng dẫn (gọi là writeup) sau giải bị delay 1 tới vài tuần, do ban tổ chức thường
yêu cầu các top team viết rồi nộp để chứng minh mình không cheat. Và sau vài ba
tuần, thì đang bận chiến giải khác quên mất cả đề rồi.

### pwn
Khó. 

Pwn thường hay chỉ "binary exploitation", với người code Python hay thậm chí $language
bất kỳ (trừ C/Assambly), thì đây là cả một thế giới hoàn toàn mới, mới tới mức 
đọc hướng dẫn cho newbie vẫn không hiểu gì. Từ cấu trúc file binary cho tới cách
làm stack overflow. 
Có giải của SamSung chỉ ngồi làm tut pwn trong đề cho hướng dẫn, rất hay và chi tiết.
Thò tay vào làm mà vẫn khó lên khó xuống với [python2 và 3](https://n.pymi.vn/py3utf8.html).

Trong CTF kiểu Jeopady, web và pwn là hai mục có tính "hack" nhất.

### Khó 
- 0CTF
- 3DCTF
- PPP

hai giải đầu của Trung Quốc, các hacker Trung Quốc thì khét tiếng khỏi nói rồi.
PPP top 1 ctftime.org nhiều năm. 

Các giải này chỉ vào đọc đề rồi hì hục cả 2 ngày vẫn không ra gì. Sợ.
## Mục tiêu kế tiếp
Sau năm đầu, cá nhân mình chơi tất cả các thể loại, từ misc, forensics qua crypto, tới
rev, sang web, thi thoảng đề dễ làm cả pwn hay chạy autopwn để tự giải.
Sang năm phấn đấu theo web và pwn cho nó thực chiến.

## Bài học rút ra và hành động của chúng ta 
- Biển học vô biên, bị điên thì học. Cứ ngỡ mình Python ngon ăn lắm, mà nhiều bài Pyjail (phá ra khỏi chương trình Python đã bị giới hạn các tính năng để chạy lệnh thoải mái - RCE) vẫn không giải được. Bước sang web hay binary thì 
ôi thôi cả một chân trời mới. Lại newbie lại từ đầu.
- Kiểu [byte](https://n.pymi.vn/byt351.html) ngày ngày đi code, 10 năm không bao giờ dùng thì đi chơi CTF giải nào cũng dùng. 
- Khi đi code, sử dụng các công cụ phát hiện lỗi bảo mật trong code như semgrep, bandit, snyk, ...
- Các công ty hãy cho nghỉ làm 1 ngày để các dev tự tập hack website của chính mình, training hand-on hack các lỗ hổng
bảo mật hay gặp nhất, lập team CTF chơi mục web hàng tuần.
## Bắt đầu từ đâu?
Tài liệu vô biên, search là ra cả đống tham khảo:
- [python cho hack với byte](https://n.pymi.vn/byt351.html)
- [PyMi SNYK 2021 writeup]({filename}/ctf.md)
- [repo của team CTF PyMi](https://n.pymi.vn/byt351.html)

### Kết luận
Cám ơn các anh em team CTF PyMi đã cùng chiến đấu suốt 1 năm trời, nhiều anh em
vẫn còn chưa biết mặt. Hy vọng năm thứ 2 sẽ gặp nhau được ít nhất 1 lần, không thì cũng
2 lần trở lên.

To another CTFking year.

Hết.

HVN at [http://pymi.vn](http://pymi.vn) and [https://www.familug.org](https://www.familug.org).

- [Ủng hộ tác giả 🍺](https://www.familug.org/p/ung-ho.html)
