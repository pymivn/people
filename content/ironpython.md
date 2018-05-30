Title: IronPython
Date: 2018-05-30
Author: htlcnn
Tags: python, ironpython, windows, implementation
Category: Trang chủ

## IronPython là gì?

Theo giới thiệu ở [trang chủ IronPython](http://ironpython.net/):
> IronPython is an open-source implementation of the Python programming language which is tightly integrated with the .NET Framework. IronPython can use the .NET Framework and Python libraries, and other .NET languages can use Python code just as easily.
>
> Ironpython là 1 "implementation" mã nguồn mở của ngôn ngữ lập trình Python, tích hợp chặt chẽ với .NET Framework. IronPython có thể sử dụng .NET Framework và các thư viện Python, các ngôn ngữ .NET khác cũng có thể đọc và chạy code Python dễ dàng.


## Cài đặt IronPython
Vào trang chủ download bộ cài đặt về (link download ở trang chủ là link github). Thời điểm viết bài, IronPython đang ở phiên bản 2.7.8: https://github.com/IronLanguages/ironpython2/releases/tag/ipy-2.7.8. IronPython 3 đang trong quá trình phát triển, chưa có bản chính thức.


## Sử dụng
- Bật IronPython interpreter bằng cách chạy (bấm đúp - double click) vào file ở đường dẫn: `C:\Program Files (x86)\IronPython 2.7\ipy.exe` hoặc `C:\Program Files (x86)\IronPython 2.7\ipy64.exe`. Hoặc gõ đường dẫn file `ipy.exe, ipy64.exe` vào `Command Prompt/PowerShell`

```python
Microsoft Windows [Version 6.1.7601]
Copyright (c) 2009 Microsoft Corporation.  All rights reserved.

C:\Users\HTL>"c:\Program Files (x86)\IronPython 2.7\ipy.exe"
IronPython 2.7.3 (2.7.0.40) on .NET 4.0.30319.42000 (32-bit)
Type "help", "copyright", "credits" or "license" for more information.
>>> print("Hello from IronPython")
Hello from IronPython
```
- Chạy 1 python script đã viết sẵn bằng cách gõ vào Command Prompt: `C:\Program Files (x86)\IronPython 2.7\ipy.exe đường_dẫn\đến\script.py`. Ví dụ nội dung file `D:\HTL\Desktop\script.py`:
```python
print("Hello from inside a Python script")
```

```
C:\Users\HTL>"c:\Program Files (x86)\IronPython 2.7\ipy.exe" D:\HTL\Desktop\script.py
Hello from inside a Python script
```

## Sử dụng .NET Framework và Python libraries
IronPython có sẵn thư viện `clr` hỗ trợ load các .NET Assemblies (VD như các file .dll) và sử dụng các công cụ trong đó. IronPython cũng có các libraries kèm theo tương tự như CPython:
```python
C:\Users\HTL>"c:\Program Files (x86)\IronPython 2.7\ipy.exe"
IronPython 2.7.3 (2.7.0.40) on .NET 4.0.30319.42000 (32-bit)
Type "help", "copyright", "credits" or "license" for more information.
>>> import clr
>>> clr.AddReference('System')
>>> from System import Environment
>>> print(Environment.SystemDirectory)
C:\Windows\system32
>>> import math
>>> print(math.pi)
3.14159265359
```

## Kết luận
- Học ngôn ngữ Python là có thể sử dụng trên nhiều môi trường, với nhiều implementation khác nhau (CPython, IronPython, Jython...).
- IronPython là sự lựa chọn hợp lý khi làm việc với môi trường Windows và các phần mềm chạy trên Windows.
- Alternative: Trả lời cho câu hỏi "Mình vẫn muốn dùng CPython và vẫn muốn sử dụng .NET Framework thì làm như thế nào?" -> Tìm hiểu [pythonnet](http://pythonnet.github.io/) nhé. Tuy nhiên mình khuyến khích dùng IronPython để làm việc trên Windows và các phần mềm chạy trên Windows.