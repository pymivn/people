Title: Lib requests có gì hay mà dùng thay urllib
Date: 2020-03-18
Category: Trang chủ
Tags: python, requests, urllib, HTTP,
Slug: requests
Authors: hvnsweeting
Summary: Giải mã thành công của thư viện được dùng nhiều nhất trong Python

Python là một ngôn ngữ già, có thể bạn chưa biết, [Python tuổi
dê](https://www.familug.org/2016/02/python-python-tuoi-gi.html)
Python ra đời [từ thời mới có
HTTP](https://en.wikipedia.org/wiki/History_of_the_World_Wide_Web#1980%E2%80%931991:_Invention_and_implementation),
và nổi tiếng là [hỗ trợ tận răng](https://xkcd.com/353/), nên không
có gì lạ nếu Python có kèm sẵn thư viện standard để thực hiện HTTP request
với tên `urllib`.

Vậy nhưng khi lên mạng tìm kiếm hay hỏi quanh đây: **dùng gì để gọi HTTP
trong Python?**, câu trả lời phần lớn đều là cài: `pip install requests`.

Requests không phải có từ ngày Python xuất hiện, nhưng vào thời Python 2.6 2.7
(cỡ 2012-2013), requests đã rất phổ biến, ví dụ như câu trả lời [trên
StackOverFlow năm 2013](https://stackoverflow.com/a/15869929/807703).

Requests (có chữ s) xuất hiện với một API cực kỳ thân thiệt, với motto (khẩu
hiệu):
**Python HTTP for Humans** do `urllib` có sẵn trong Python2 quá rắc rối.
API của requests nổi tiếng đến mức [gần như ngôn ngữ lập trình nào cũng
có một thư viện "nhái" requests của
Python](https://github.com/levigross/grequests), nó quá đơn giản, tới mức
... trước đây không thư viện nào từng làm vậy.

(API của thư viện là các function mà thư viện đó public cho người dùng sử dụng,
ví dụ requests có: requests.get, requests.post.)

![requests logo](https://raw.githubusercontent.com/psf/requests/master/ext/requests-logo.png)

Sau gần chục năm phát triển, `requests` giờ đã nằm dưới mái nhà [Python Software
Foundation](https://github.com/psf/requests/).

Với các tính năng được quảng cáo ở bản [v1.0.0, cuối năm 2012](https://github.com/psf/requests/tree/v1.0.0)

```
    International Domains and URLs
    Keep-Alive & Connection Pooling
    Sessions with Cookie Persistence
    Browser-style SSL Verification
    Basic/Digest Authentication
    Elegant Key/Value Cookies
    Automatic Decompression
    Unicode Response Bodies
    Multipart File Uploads
    Connection Timeouts
    Thread-safety
```

Có thể dễ đoán rằng những tính năng được quảng cáo trên chính là những gì
`urllib` Python thời đó chưa hỗ trợ (trong Python còn có cả thư viện tên
`urllib2`... để thêm phần phức tạp). Nhưng với Python 3.5 trở đi, rất nhiều
trong số trên đã được hỗ trợ trong `urllib`.

Còn đây là các tính năng được quảng cáo ở [phiên bản mới nhất](https://github.com/psf/requests/blob/v2.23.0/README.md#supported-features--bestpractices):

```
    Keep-Alive & Connection Pooling
    International Domains and URLs
    Sessions with Cookie Persistence
    Browser-style SSL Verification
    Automatic Content Decoding
    Basic/Digest Authentication
    Elegant Key/Value Cookies
    Automatic Decompression
    Unicode Response Bodies
    HTTP(S) Proxy Support
    Multipart File Uploads
    Streaming Downloads
    Connection Timeouts
    Chunked Requests
    .netrc Support
```

Nếu bạn đọc các tính năng này mà không hiểu gì, thì nó chỉ chứng minh một điều
là HTTP là một giao thức rất lằng nhằng và phức tạp.
Đáng kể nhất có:

- Browser-style SSL Verification: liên quan tới SSL - tức là bảo mật. `urllib`
mãi tới [Python 3.4.3 mới thực hiện kiểm tra SSL một cách mặc
định](https://docs.python.org/3/library/http.client.html#http.client.HTTPSConnection):

> Changed in version 3.4.3: This class now performs all the necessary
> certificate and hostname checks by default. To revert to the previous,
> unverified, behavior ssl._create_unverified_context() can be passed to
> the context parameter.

- Connection Pooling: bình thường khi viết code truy cập vào 1 website, ta
có thể nghĩ đơn giản là requests.get rồi lấy kết quả là xong chuyện, hết phiên.
Nếu muốn truy cập trang khác cùng website đó, ta lại requests.get để truy cập
mới. Phía dưới `requests.get` thực hiện tạo 1 `TCP connection`, sau đó mới gửi
`HTTP request` qua `connection` này. Việc tạo
connection là công việc khá tốn kém (CPU, thời gian), đặc biệt với HTTPS,
tạo SSL connection còn tốn hơn nhiều lần. Do vậy, để
tăng hiệu năng, requests sẽ tự giữ lại `connection` và dùng lại để truy cập
website nếu như các yêu cầu sau đó cùng website, khác page. Xem code tại
[adapters.py](https://github.com/psf/requests/blob/v2.23.0/requests/adapters.py#L129).

Việc này ảnh hưởng tới hiệu năng, nhưng không ảnh hưởng gì nếu bạn chỉ gọi
1 request tới mỗi website.

## Đọc code requests
Lib `requests` thuộc loại nhỏ, tổng cộng 5000 dòng gồm rất nhiều comment.
Nó tận dụng các thư viện ngoài khác thay vì tự làm
tất cả: `urllib3` để thực hiện connection pooling, thực hiện HTTP requests,
dùng `certifi` để cung cấp các SSL certificate mới nhất như các trình duyệt.

```
$ wc -l *| sort -nr
wc: __pycache__: Is a directory
   5049 total
    982 utils.py
    954 models.py
    767 sessions.py
    549 cookies.py
    533 adapters.py
    305 auth.py
    161 api.py
    131 __init__.py
    126 exceptions.py
    123 status_codes.py
    119 help.py
    105 structures.py
     72 compat.py
     42 _internal_utils.py
     34 hooks.py
     18 certs.py
     14 __version__.py
     14 packages.py
```

Phần API đơn giản lừng danh nằm trong file `api.py`, trích bỏ comment:

```python
from . import sessions

def request(method, url, **kwargs):
    # By using the 'with' statement we are sure the session is closed, thus we
    # avoid leaving sockets open which can trigger a ResourceWarning in some
    # cases, and look like a memory leak in others.
    with sessions.Session() as session:
        return session.request(method=method, url=url, **kwargs)

def get(url, params=None, **kwargs):
    kwargs.setdefault('allow_redirects', True)
    return request('get', url, params=params, **kwargs)

def options(url, **kwargs):
    kwargs.setdefault('allow_redirects', True)
    return request('options', url, **kwargs)

def head(url, **kwargs):
    kwargs.setdefault('allow_redirects', False)
    return request('head', url, **kwargs)

def post(url, data=None, json=None, **kwargs):
    return request('post', url, data=data, json=json, **kwargs)

def put(url, data=None, **kwargs):
    return request('put', url, data=data, **kwargs)

def patch(url, data=None, **kwargs):
    return request('patch', url, data=data, **kwargs)

def delete(url, **kwargs):
    return request('delete', url, **kwargs)
```

### urllib3
[`urllib3`](https://urllib3.readthedocs.io/en/latest/) là dependency quan trọng
của `requests`, nó đảm nhận những công việc nặng nề:

> urllib3 brings many critical features that are missing from the Python
> standard libraries:

    Thread safety.
    Connection pooling.
    Client-side SSL/TLS verification.
    File uploads with multipart encoding.
    Helpers for retrying requests and dealing with HTTP redirects.
    Support for gzip and deflate encoding.
    Proxy support for HTTP and SOCKS.

Code mẫu:

```python
>>> import urllib3
>>> http = urllib3.PoolManager()
>>> r = http.request('GET', 'http://httpbin.org/robots.txt')
>>> r.status
200
>>> r.data
'User-agent: *\nDisallow: /deny\n'
```

## urllib
urllib và urllib2 thời Python2.7 là những em gái dính lời nguyền mà ai cũng
muốn tha thứ. Nhưng ở Python 3.6+, việc dùng urllib không còn quá phức tạp,
hãy coi nó như 1 file, nhớ đóng file, hoặc dùng `with`.

### urllib đã kiểm tra SSL certificate

```python
Python 3.6.9 (default, Nov  7 2019, 10:44:02)
[GCC 8.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import urllib.request
>>> from urllib.request import urlopen
>>> with urlopen("https://dantri.com") as f:
...     content = f.read()
...     print(content[:100])
...
Traceback (most recent call last):
  File "/usr/lib/python3.6/urllib/request.py", line 1318, in do_open
    ...
    self._sslobj.do_handshake()
ssl.SSLError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed (_ssl.c:852)
...
    raise URLError(err)
urllib.error.URLError: <urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed (_ssl.c:852)>

```

Kết quả tương tự khi dùng `requests` do URL `https://dantri.com` SSL certificate
đẫ hết hạn `Expire: January 19, 2020`

```python
>>> import requests
>>> requests.get("https://dantri.com")
Traceback (most recent call last):
  File "/home/hvn/py3/lib/python3.6/site-packages/urllib3/connectionpool.py", line 672, in urlopen
    ...
  File "/usr/lib/python3.6/ssl.py", line 689, in do_handshake
    self._sslobj.do_handshake()
ssl.SSLError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed (_ssl.c:852)
```

### urllib redirect ngon lành

```python
>>> r = requests.get("https://gmail.com")
>>> r.url
'https://accounts.google.com/ServiceLogin?service=mail&passive=true&rm=false&continue=https://mail.google.com/mail/&ss=1&scc=1&ltmpl=default&ltmplcache=2&emr=1&osid=1'

>>> from urllib.request import urlopen
>>> r = urlopen("https://gmail.com")
>>> r.url
'https://accounts.google.com/ServiceLogin?service=mail&passive=true&rm=false&continue=https://mail.google.com/mail/&ss=1&scc=1&ltmpl=default&ltmplcache=2&emr=1&osid=1'
```

### urllib với JSON API

```python
>>> import json
>>> from urllib.request import urlopen
>>> with urlopen("https://httpbin.org/ip") as f:
...     content = json.load(f)
...     print(content)
...
{'origin': '171.247.169.69'}

>>> import json
>>> from urllib.request import Request, urlopen
>>> with urlopen(
...   Request("https://httpbin.org/post", method="POST",
...           data=json.dumps({"name": "Pymi", "since": 2015}).encode('utf-8'),
...           headers={'Content-Type': "application/json"})
...           ) as resp:
...     print(json.load(resp)['json'])
...
{'name': 'Pymi', 'since': 2015}
```

### Tra cứu thông tin COVID-19

```python
>>> with urlopen("https://corona-stats.online/IT") as f:
...     print(f.read().decode("utf-8"))
...
╔═══════╤═══════╤═══════════╤═══════════╤════════╤════════╤═════════════╤═════════════╤═════════╤══════════╗
║       │ State │ Confirmed │ Recovered │ Deaths │ Active │ Mortality % │ Recovered % │ 1 Day ▲ │ 1 Week ▲ ║
╟───────┼───────┼───────────┼───────────┼────────┼────────┼─────────────┼─────────────┼─────────┼──────────╢
║ Italy │ Total │    31,506 │     2,941 │  2,503 │ 26,062 │        7.94 │        9.33 │ 3,526 ▲ │ 21,357 ▲ ║
╚═══════╧═══════╧═══════════╧═══════════╧════════╧════════╧═════════════╧═════════════╧═════════╧══════════╝

Stay safe. Stay inside.

Code: https://github.com/sagarkarira/coronavirus-tracker-cli
Twitter: https://twitter.com/ekrysis

Last Updated on: 18-Mar-2020 16:03 UTC
```

## Hành động của chúng ta
Có thể dùng `urllib` khi script/chương trình chỉ truy cập mỗi website
một lần, dùng trong các script ngắn, hay khi không tiện cài `requests`.
Nhớ sử dụng [`requests` Session](https://requests.readthedocs.io/en/v2.9.1/user/advanced/#session-objects)
khi truy cập 1 website nhiều lần để tăng hiệu năng.


## Kết luận
Requests thành công vì sự đơn giản không thể hơn của nó, chứ không phải vì
kỹ thuật cao siêu phức tạp.

> A designer knows he has achieved perfection not when there is nothing left to add, but when there is nothing left to take away.
> The New Hacker's Dictionary - Eric S. Raymond,

Nhớ mặc định là dùng `requests`, nhưng không bị sốc khi thấy người ta dùng
`urllib`.
