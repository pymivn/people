Title: Requests + bs4 <= Requests-HTML
Date: 2018-05-09
Author: tung491
Tags: requests-html, bs4, requests, python, crawl
Category: Trang chủ

## Giới thiệu
[Requests-HTML](http://html.python-requests.org/) được viết bởi Kenneth Reitz - tác giả của `requests` nổi tiếng, với mục đích cao cả là thay thế combo huyền thoại (với pymier) requests + bs4.  Trên trang chủ, requests-html tự mô tả như sau:

> This library intends to make parsing HTML (e.g. scraping the web) as simple and intuitive as possible

và đặc biệt chỉ hỗ trợ python3.

## Các tính năng nổi bật của requests-html
- Hỗ trợ đầy đủ JavaScript
- Hỗ trợ chọn thành phần của trang bằng CSS, Xpath
- Tự động theo chuyển trang

## Demo vài tính năng nổi bật
Cách cài đặt và sử dụng cơ bản của requests-html đã được tác giả nói rất rõ ở trang chủ do đó mính sẽ không nói lại nữa.

### Render
 Nhặt một đoạn văn bản mà đã được render bởi JavaScript:

```python
In [4]: r = session.get('http://www.familug.org/')
In [5]: r.html.render()
[W:pyppeteer.chromium_downloader] start chromium download.
Download may take a few minutes.
[W:pyppeteer.chromium_downloader] chromium download done.
[W:pyppeteer.chromium_downloader] chromium extracted to: /home/dosontung007/.pyppeteer/local-chromium/543305
In [6]: r.html.search('UEFI vs BIOS - tạo USB boot cài Windows {something} từ Ubuntu')['something']
Out[6]: '10'
```

Khi bạn chạy render() lần đầu, method sẽ tải về `Chromium headless` về thư mục `$HOME`.


### XPath Selector
 Requests-html hỗ trợ Xpath query như Scrapy

```
In [25]: r.html.xpath('//h3//a')
Out[25]:
[<Element 'a' href='http://www.familug.org/2018/04/uefi-vs-bios-tao-usb-boot-cai-windows.html'>,
 <Element 'a' href='http://www.familug.org/2018/04/alsa-pulseaudio-jack-ubuntu.html'>,
 <Element 'a' href='http://www.familug.org/2018/02/hello-2018.html'>,
 <Element 'a' href='http://www.familug.org/2017/12/dung-git-diff-voi-patch.html'>,
 <Element 'a' href='http://www.familug.org/2017/11/pgrep-e-grep-process.html'>,
 <Element 'a' href='http://www.familug.org/2017/11/vuot-qua-gioi-han-1-deploy-key-cua.html'>]
In [26]: r.html.xpath('//h3//a/@href')
Out[26]:
['http://www.familug.org/2018/04/uefi-vs-bios-tao-usb-boot-cai-windows.html',
'http://www.familug.org/2018/04/alsa-pulseaudio-jack-ubuntu.html',
'http://www.familug.org/2018/02/hello-2018.html',
'http://www.familug.org/2017/12/dung-git-diff-voi-patch.html',
'http://www.familug.org/2017/11/pgrep-e-grep-process.html',
'http://www.familug.org/2017/11/vuot-qua-gioi-han-1-deploy-key-cua.html']
```

### CSS Selector
```
In [26]: sel = '#Blog1 > div.blog-posts.hfeed > div:nth-child(1) > div > div > div > h3'

In [27]: r.html.find(sel, first=True)
Out[27]: <Element 'h3' class=('post-title', 'entry-title') itemprop='name'>

In [28]: r.html.find(sel, first=True).text
Out[28]: 'UEFI vs BIOS - tạo USB boot cài Windows 10 từ Ubuntu'
```
CSS selector này có thể copy từ developer tool của trình duyệt web.


## Tổng kết
Requests-html là 1 thư viện tiện lợi thay thế cho combo requests + bs4, dễ dàng chuyển lên scrapy nếu cần thực hiện dự án crawling lớn, chuyên nghiệp.

Chi tiết hơn xem tại: http://html.python-requests.org/.

HẾT.

TUNG491 at https://pymi.vn
