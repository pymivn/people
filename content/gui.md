Title: Làm app giao diện đồ hoạ với Python
Date: 2018-08-18
Category: Trang chủ
Tags: python, gui, tk,
Slug: gui
Authors: hvnsweeting
Summary: Không gì là không thể - đã dễ, lại còn đẹp

Giao diện đồ hoạ (GUI - Graphic User Interface) vốn từng là một phần không thể thiếu khi nói về lập trình. Dù học ngôn ngữ lập trình nào, người ta cũng nghĩ tới chuyện "làm sao để có giao diện đồ hoạ".

Thế giới thay đổi, thứ từng quan trọng của ngày hôm qua thì hôm nay chưa chắc đã cần tới. Thời đại tất cả mọi thứ đều chuyển lên web, thì web/app mobile trở thành giao diện để tương tác với người dùng, chứ không phải các phần mềm có giao diện chạy trên máy tính như trước kia.
Giờ đây người ta: nghe nhạc trên web, xem film trên web, chơi game trên web, soạn thảo văn bản trên web... khó còn ứng dụng nào không đưa lên web nữa. Vậy nên về mặt "sự nghiệp", có vẻ như bạn nên đầu tư vào kỹ năng làm web thay vì học để tạo một app trên desktop như cách đây chục năm.

Dĩ nhiên, GUI không ngay lập tức biến mất, vẫn có nhu cầu sử dụng, vẫn có người dùng, vẫn có hàng tá thư viện đồ hoạ tồn tại từ lâu (và vẫn tiếp tục phát triển), vẫn có những game mà chỉ chơi được trên máy tính do yêu cầu về hiệu năng mà web không đáp ứng nổi (như Half-Life/ đế chế / đua xe ...).

Python hỗ trợ không ít các thư viện làm GUI app, có thể kể tới: Qt, WxWidgets, Tkinter, [Kivy (làm cả app mobile)](https://kivy.org/)... xem đầy đủ tại:

- [https://docs.python.org/3/faq/gui.html]()
- [https://www.python.org/about/apps/#desktop-guis]()
- [https://docs.python-guide.org/scenarios/gui/]()

<a href="https://en.wikipedia.org/wiki/Qt_(software)">Qt</a> là nền tảng phát triển ứng dụng dùng trong công nghiệp, hỗ trợ mọi hệ điều hành phổ biến, và rất "xịn". Nếu có nhu cầu làm ứng dụng desktop với Python, hãy đầu tư vào Qt để có một sản phẩm đẳng cấp, không kém bất kỳ nền tảng nào khác.

Tk là hệ thống thư viện đồ hoạ đơn giản, dễ dùng, chạy trên cả 3 hệ điều hành phổ biến: Windows, Ubuntu, OSX/MacOS và điều quan trọng nhất: thư viện `tkinter` đi kèm mọi bộ cài Python, nên muốn dùng không cần phải cài đặt gì thêm.

Bài viết hướng dẫn tạo một chương trình đồ hoạ sử dụng `tkinter` với Python 3.6, thực hiện trên MacOS Sierra (10.12.6).

## Khái niệm cơ bản về một chương trình giao diện đồ hoạ.
Một chương trình có giao diện đồ hoạ là một chương trình luôn chạy cho tới khi người dùng thoát chương trình. Dễ suy ra ở đây có chạy 1 vòng lặp vô hạn để luôn hiển thị giao diện (gọi là main loop). Chương trình này hoạt động dựa trên những tương tác của người dùng và phản ứng với các tương tác đó (bấm nút này thì chạy cái kia). Loại chương trình như vậy thuộc loại mô hình "Event-driven programming".

Các thao tác của người dùng được gọi là các **event**,
các hành động tương ứng của chương trình (các function) được gọi là các **callback**, gắn vào các bộ phận giao diện. Gắn callback vào nút bấm thì khi ta bấm nút, callback sẽ được gọi.

Các bộ phận giao diện như nút bấm, chữ, ô nhập ký tự ... được gọi là các **widget**.

## Lập trình GUI với Tkinter

Code gõ trực tiếp trên IPython:

```python
# on Ubuntu, requires install: `sudo apt-get install -y python3-tk`
In [1]: import tkinter as tk

In [2]: tk.Frame(tk.Tk()).mainloop()
```

Nếu Tk hoat động trên máy bạn, ngay lập tức một cửa sổ trắng tinh sẽ hiện ra.

![emptygui]({static}/images/gui.png)


`Tk()` tạo một cửa sổ chính  (main window), `Frame` là một widget có khả năng chứa các widget khác. Gọi function `mainloop()` để chạy giao diện mãi mãi cho tới khi người dùng đóng lại.

### Các widget
Tkinter có sẵn 17 widget:

`Button` `Canvas` `Checkbutton` `Entry` `Frame` `Label` `Listbox` `Menu` `Menubutton` `Message` `Radiobutton` `Scale` `Scrollbar` `Text` `Spinbox` `LabelFrame` `PanedWindow`

Sau đây ta viết một GUI app có hiển thị tiêu đề (Label), có một ô nhập địa chỉ trang web (Entry), có một nút bấm để kiểm tra status của trang web (Button).

Bài viết sử dụng thư viện `requests` (cài bằng `pip install requests`), nếu chưa biết dùng [pip](http://pymi.vn/blog/virtualenv/) hay không cài được, hãy xem ví dụ tương tự mà không kết nối internet tại [đây](https://docs.python.org/3/library/tkinter.html#a-simple-hello-world-program).

```python
# on Ubuntu, requires install: `sudo apt-get install -y python3-tk`
import tkinter as tk
import urllib.request


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(text="PyMi.vn checker")
        self.label.pack()

        self.entrythingy = tk.Entry()
        self.entrythingy.pack()

        self.contents = tk.StringVar()
        self.entrythingy["textvariable"] = self.contents
        self.entrythingy.bind("<Key-Return>", self.check_site)

        self.hi_there = tk.Button(self)
        self.hi_there["text"] = (
            "Check web site up/down." " Enter URL with http(s):"
        )
        self.hi_there["command"] = self.check_site
        self.hi_there.pack()

        self.quit = tk.Button(self, text="QUIT", command=root.destroy)
        self.quit.pack()

    def check_site(self, event=None):
        url = self.contents.get().strip() or "https://pymi.vn"
        if not url.startswith("http"):
            url = "http://{}".format(url)

        # fake useragent as cloudflare block python agent
        r = urllib.request.Request(
            url,
            method="HEAD",
            headers={"User-Agent": "python-requests/2.23.0"},
        )
        resp = urllib.request.urlopen(r, timeout=2)
        print("response: {} {}".format(resp.status, resp.url))


root = tk.Tk()
app = Application(master=root)
app.master.title("My checker app")
app.master.minsize(300, 200)
app.mainloop()
```

Code trên:

- phần init chỉ là thủ tục
- tạo một label với text cần hiển thị
- tạo entry để người dùng nhập nội dung, gán giá trị người dùng nhập vào `self.contents`, bind widget entry với phím Enter (trên MacOS gọi là return), và chạy method `check_site` khi người dùng gõ enter.
- tạo nút bấm với dòng chữ "Check site", gọi method `check_site` khi người dùng bấm nút
- tạo nút bấm "Quit" để thoát chương trình
- set thanh tiêu đề `title` và kích thước cho chương trình qua `app.master`.

Kết quả:

![checker]({static}/images/checker.png)

Danh sách đầy đủ các widget xem tại [https://github.com/python/cpython/blob/3.6/Lib/tkinter/__init__.py](https://github.com/python/cpython/blob/3.6/Lib/tkinter/__init__.py)  - search `(Widget` (các subclass của class Widget).


Thử các ví dụ có sẵn đi kèm với Python:

```
python3 -m turtledemo.minimal_hanoi
python3 -m turtledemo.sorting_animate
```

hay xem code 1 IDE viết bằng tk: [thonny](https://github.com/thonny/thonny/tree/v3.3.4)

## Kết luận

Tk nhẹ gọn, có sẵn, dễ dùng, đủ dùng khi bạn thấy đủ. Bao giờ thấy ngột ngạt, có lẽ lại chuyển sang Qt, các khái niệm lập trình giao diện dù dùng library/framework nào cũng đều tương tự nhau.

## Tham khảo
- Tkinter: https://docs.python.org/3/library/tkinter.html

Hết.
HVN @ [https://pymi.vn]() and [https://www.familug.org/]()
