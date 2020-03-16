Title: Django dễ hơn Flask
Date: 2020-03-16
Category: Trang chủ
Tags: python, django, flask
Slug: djangovsflask
Authors: hvnsweeting
Summary: Flask là một micro-framework, thường được xem như đơn giản hơn Django, nhưng nói vậy mà không phải vậy.

Django và Flask là hai web-framework phổ biến nhất - thành công nhất của Python.
Ngày này, khi nhìn các bảng tuyển dụng, sẽ thường thấy yêu cầu Django để làm web
nhưng Flask dần trở thành công cụ quen thuộc của giới làm data.
Nếu ai có hỏi "nên học cái nào" thì câu trả lời chuẩn nhất chỉ có một: nên học
cả hai.

## Web framework là gì
Một framework là một bộ thư viện, thường gồm nhiều tính năng phục vụ đưa ra
sản phẩm cuối cùng chạm tới người dùng. Ví dụ `requests` là một library,
chỉ cung cấp tính năng HTTP client, hay `bs4` chỉ cung cấp tính năng bóc tách/
truy cập dữ liệu HTML, hay `sqlalchemy` là library giúp truy cập và tương tác
với database, thì Flask/Django cung cấp một bộ khung kèm các "thư viện" để
làm ra một sản phẩm tới tay người dùng (trang web).
Frame trong tiếng Anh có nghĩa là "khung", framework cung cấp cái khung, lập
trình viên điền những thứ mình muốn vào đó, framework sẽ tự lo chạy. Vì vậy
khi dùng framework, sẽ có cảm giác như ta không biết nó hoạt động thế nào,
chỉ biết là điền đúng những thứ yêu cầu thì nó sẽ hoạt động.

Django là framework đầy đủ (full-fledge), có đủ mọi thứ, nên sẽ càng có thêm
cảm giác ta chỉ điền chút xíu là nó tự chạy, mọi thứ đều có khuôn mẫu sẫn rồi.
Flask là micro-framework, chỉ có phần khung cơ bản, các phần còn lại cho phép
người dùng tùy chọn mà đắp vào, vậy nên có phần dễ hiểu hơn, ít phép màu hơn.

Cũng vì sự khác biệt này, dẫn tới tài liệu trang chủ của 2 framework viết
rất khác nhau. Flask vào đời bằng một website dùng 7 dòng code, khiến người dùng
rất dễ học, dễ bắt đầu với sự đơn giản này. Còn Django lại dùng ví dụ phức tạp,
mặc định người dùng sẽ cần làm thứ "phức tạp" như vậy nên học thế cho quen.

Thế nhưng nếu không dựa vào 2 cái tutorial đấy để đánh giá, liệu Django có
phức tạp hơn Flask, hay thậm chí còn đơn giản hơn? Bài nầy sẽ dựa trên 2 yếu
tố để so sánh: 1. số khái niệm bạn cần biết 2. số dòng code bạn cần viết.

Bắt đầu.

### Cài đặt

#### Cài đặt Flask
```
pip install flask
```

#### Cài đặt Django

```
pip install django
```

Kết quả: hòa, dễ như nhau: `Flask 1 - Django 1`

### Viết một website hello world và hello mình

#### Flask
Tạo 1 file tên bất kỳ nhưng tốt nhất đặt là `hello.py` (tuyệt đối không đặt
là `flask.py` do trùng tên flask)

```python
1 from flask import Flask
2 app = Flask("my website")
3
4 @app.route("/")
5 def hello_world():
6    return "Hello world"
7
8 @app.route("/hello/<string:name>")
9 def hello(name):
10    return "Hello {}".format(name)
```

Chạy, [theo hướng dẫn trên trang chủ](https://flask.palletsprojects.com/en/1.1.x/quickstart/#a-minimal-application)
(nếu dùng Windows vào xem lệnh tương ứng):
```sh
$ export FLASK_APP=hello.py
$ flask run
 * Running on http://127.0.0.1:5000/
```

Điểm ấn tượng nhất ở đây là chỉ có 10 dòng, trong đúng 1 file, mà chạy thành
trang web.

Tổng số thao tác phải làm: 3 - tạo 1 file, điền nội dung, gõ lệnh để chạy.

#### Django
Django không làm web trong 1 file, nó dùng các câu lệnh có sẵn để sinh ra các
file, tức ta chỉ phải gõ lệnh, chứ không phải gõ nhiều code.
Gõ 3 lệnh sau là chạy luôn trang web:
```
$ django-admin startproject project1
$ cd project1/
$ ./manage.py startapp hello
$ ./manage.py runserver
Starting development server at http://127.0.0.1:8000/
```
Ngay lập tức đã có trang web mẫu của Django - thậm chí chưa gõ tí code nào.
Để có kết quả giống Flask ở trên, cần sửa 2 file:

File `hello/views.py`, viết các function tương tự flask:

```python
from django.http import HttpResponse

def hello_world(request):
    return HttpResponse("Hello world")

def hello(request, name):
    return HttpResponse("Hello {}".format(name))
```

File `project1/urls.py` thêm 3 dòng:

```
from hello import views

urlpatterns = [  # có sẵn
    path('admin/', admin.site.urls),  # có sẵn
    path('', views.hello_world, name='hello_world'),
    path('hello/<str:name>', views.hello, name='hello'),
] # có sẵn
```

Giờ chạy `./manage runserver` sẽ có kết quả y hệt Flask.

#### So sánh thao tác
Tổng số dòng code phải thêm vào Django là 8 - cũng chính bằng số dòng Flask
phải viết - không tính dòng trống. Django phải chạy nhiều hơn 2 lệnh - nhưng
chỉ cần phải làm khi bắt đầu dự án. Flask viết code trong 1 file, còn Django
phải sửa 2 file. ở đây có thể xem như hòa nhau không bên nào hơn/kém quá cả.

#### So sánh khái niệm
Phần khác nhau chủ đạo giữa Django và Flask là cách ghi URL.
Người dùng Flask tạo một Flask object, đặt tên là app, sau đó sử dụng
`decorator`
```
@app.route("/hello/<string:name>")
```

để gắn đường dẫn `/hello/name` cho function ngay dưới nó (function hello).
Decorator không phải một khái niệm đơn giản ở đây, mặc dù người dùng có thể
cứ nhắm mắt rồi gõ `@` theo và hiểu nôm na là gắn đường dẫn cũng được.

Django chọn giải pháp ghép đường dẫn với function thông qua file `urls.py`,
import module `views` từ thư mục `hello/` (tạo lúc chạy "startapp hello"),
sau đó gán đường dẫn bằng cách gọi function `path`:
```python
    path('hello/<str:name>', views.hello, name='hello'),
```

Dài dòng hơn Flask một chút là phải ghi `name="hello"`, không có `/` ở đầu URL,
và kiểu `str` thì ghi là `str` chứ không ghi `string` như Flask.

Khi mới bắt đầu, khó có thể thấy lý do Django viết riêng file `urls.py` để làm
gì, khi mà flask @ lên đầu rất gọn ghẽ. Thì tới lúc có 20 URL bạn sẽ hiểu tại
sao. Làm thế nào để liệt kê tất cả URL trong app của mình? Các URL của Flask
rải rác khắc nơi, mỗi cái nằm trên đầu 1 function, nếu như mỗi function dài 50
dòng, thì việc tìm sẽ khá vất vả - hoặc phải dùng chức năng tìm kiếm, hoặc phải
có IDE để hỗ trợ. Còn với Django tất cả đều nằm gọn trong `urls.py`.

Không hiểu tại sao Flask lại chọn `string` để ám chỉ kiểu string trong Python,
vốn viết là `str`, Django lại ghi thêm điểm ở đây.

Có thể bạn đã biết, rằng không nhất thiết phải dùng `@` trong Flask,
bởi decorator này chỉ làm đơn giản có 1 việc: giống Django. Thay vì viết hai
dòng `@app.route` trên đầu function, viết hai dòng này SAU khi định nghĩa
các function:

```
app.add_url_rule("/", "hello_world", hello_world)
app.add_url_rule("/hello/<string:name>", "hello", hello)
```

Đây chính làm điều mà `@app.route` làm, như mô tả trong tài liệu của nó:

> A decorator that is used to register a view function for a
given URL rule.  This does the same thing as :meth:`add_url_rule`
but is intended for decorator usage::

Chốt: Django gõ nhiều hơn 2 lệnh, sửa thêm 1 file, nhưng sử dụng ít khái niệm
cao cấp hơn Flask. Nếu dễ tính, thì cho là hòa, còn không Django dành chiến
thắng ở đây.

Tỉ số: `2 - 2`

### Thêm trang dùng template
#### Flask
Tạo 1 thư mục tên `templates` ngay cạnh file `hello.py`, rồi tạo file
`index.html` chứa code HTML và Jinja2 template.
```jinja2
{% for fw in frameworks %}
  {% if fw|length > 5 %}
    <b>{{ fw }}</b>
  {% else %}
    {{ fw }}
  {% endif %}
{% endfor %}
```

Code sửa thành
```python
from flask import Flask, render_template
@app.route("/web")
def frameworks():
    return render_template("index.html", frameworks=["Flask", "Django"])
```

#### Django
Tạo thư mục tên `templates/hello` trong thư mục
`hello`, sau đó tạo `index.html` và nội dung copy y hệt phần template của Flask.

Thêm function sau vào `hello/views.py`
```
# chú ý render đã được import sẵn ở file view.py ngay khi tạo app
def frameworks(request):
    return render(request, "hello/index.html", {"frameworks": ["Flask", "Django"]})
```
Và thêm 1 dòng vào `project1/urls.py`:
```
  path('web', views.frameworks, name='frameworks'),
```

Ngoài ra phải thêm `'hello'` vào file `project1/settings.py`
Trong list `INSTALLED_APPS`
```python
 INSTALLED_APPS = [
     ...,
     'hello',
 ]
```

Phần này lại hòa, template mặc định của Flask là `jinja2` tương đương với
Django template, kể cả cú pháp cũng rất giống nhau. Django phải thêm 1
dòng vào file `settings.py` nhưng việc này cũng chỉ phải làm một lần duy nhất
(lẽ ra nên làm luôn sau khi createapp từ đầu).

### Django app
Khi chạy lệnh `startproject` ban đầu, nó sinh ra các file cần thiết cho một
dự án Django (`urls.py`, `settings.py`, `manager.py` ..., và nó chỉ phải chạy
duy nhất 1 lần trong 1 dự án. Với Flask, bạn tạo thư mục bằng tay.

Django đưa ra khái niệm có nhiều *app* trong một dự án. Flask cũng có khái
niệm tương tự, gọi là [Blueprint](https://flask.palletsprojects.com/en/1.1.x/blueprints/).
Nó không cần thiết cho ví dụ 6-10 dòng, nhưng khi làm một website nhiều tính năng
thì blueprint là cách tổ chức chính thức của Flask, ngay cả trong bài tutorial
của Flask cũng dùng luôn khái niệm này. Như vậy chỉ khác nhau việc học trước
hay học sau, chứ không phải Flask thì không dùng tới.

Flask không ép (không hướng dẫn) người dùng cách tổ chức code, khi dự án lớn
dần lên, có 3-5000 dòng code, ắt phải sinh ra file mới, phải sắp xếp, tổ chức
sao cho hợp lý - mà thế nào là hợp lý thì không phải ai cũng tìm ngay ra cách.
Dự án Flask khi rơi vào tay lập trình viên chưa có nhiều kinh nghiệm làm web
sẽ dẫn tới code mỗi thứ một nơi, đi tìm cũng thấy mệt. Flask không hướng dẫn
người dùng ngay từ đầu, nếu gặp phải người chưa có kinh nghiệm tổ chức, sẽ
trở thành vô tổ chức.

Django bắt đầu bằng việc đặt mỗi thứ vào một nơi quy định sẵn, ban đầu có vẻ
hơi phiền phức, nhưng sự gọn gàng ngăn nắp sẽ trả lợi ích rõ ràng về sau.
Bạn có thể xem 10 dự án Django, cấu trúc đều như nhau, như mẫu của Django,
thì 10 dự án Flask mỗi cái một kiểu.

Tỉ số: Flask 2 - Django 3

### Thêm Database, thêm tính năng đăng nhập, thêm trang admin
Đến đây, việc của người dùng Django là mở tài liệu ra, đọc phần model, đọc phần
admin page rồi làm theo hướng dẫn, đầy đủ hàng trăm tính năng có sẵn, thì
người dùng Flask lại phải lo đi tìm:
- dùng database nào? nếu dùng MySQL thì dùng driver nào?
- có dùng ORM không? nếu có thì phải học SQLAlchemy, tương đương với học Django ORM
- dùng SQLAlchemy rồi có phải dùng flask-sqlalchemy không (có).
- khi đổi schema table (thêm/bớt/sửa cột trong 1 SQL table) thì phải làm thế nào?
  MigrateDB thì dùng cái gì? (Flask-Migrate / alembic)
- Viết trang admin (ví dụ website quản lý sinh viên thì đây là trang để thêm/bớt/sửa/xóa sinh viên)
  thì viết ra sao (có thể dùng flask-admin)
- Đăng nhập thì làm thế nào? (flask-httpauth)
- Nhập/validate form thì dùng cái chi? (WTForm)
- ... tiếp tục ...

Còn với Django? tất cả những thứ trên đều có sẵn trong Django, không phải tìm,
cài gì cả, cứ thế đọc tài liệu rồi lôi ra dùng thôi.

Tỉ số: Flask 2 - Django 4

### Kết quả
Hòa.

## Hành động của chúng ta
`pip install django` dùng ngay và luôn thôi.

## Kết luận
Bài này không nói Django hoàn hảo, dùng cho mọi trường hợp. Ví dụ nếu
website của bạn không dùng database, không cần trang admin (như web của data
science) thì Flask nhanh, nhẹ hơn Django nhiều phần. Hay khi bạn biết mình đang
làm gì, biết đủ những thư viện để dùng ghép lại xịn hơn cả những gì Django
có sẵn, thì Flask là lựa chọn tuyệt hảo. Flask không phải đồ chơi, [phần
core của Uber đã từng được viết bằng
Flask](https://eng.uber.com/building-tincup-microservice-implementation/),
[Airflow](https://airflow.apache.org/) - công cụ không thể thiếu trong các hệ
thống data cũng chính là một sản phẩm dùng Flask. Vậy nên, hãy học cả 2, nhé.
Và nhớ là, Django không hề khó như bạn tưởng.
