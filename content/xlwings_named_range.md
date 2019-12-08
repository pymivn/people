Title: Sử dụng xlwings tương tác với MS Excel
Date: 2019-12-08
Modified: 2018-12-08
Author: htlcnn
Tags: python, xlwings, excel, vba
Category: Trang chủ
Summary: Giới thiệu thư viện xlwings dùng để tương tác với MS Excel
Slug: xlwings-named-range


[xlwings](https://github.com/xlwings/xlwings) là 1 thư viện Python dùng để tương tác giữa Python và MS Excel. Hoạt động được trên Windows và Mac. xlwings có các tính năng:
- **Scripting**: Tự động hóa/tương tác với Excel từ môi trường Python, sử dụng cú pháp gần với VBA mà vẫn "Pythonic".
- **Macros**: Viết các script python thay thế cho VBA macros, giúp code dễ đọc hơn. Sau khi viết script python xong, chỉ cần gọi 1 hàm trong VBA là script chạy.
- **UDFs**: Viết hàm người dùng tự định nghĩa bằng ngôn ngữ Python và sử dụng được hàm đó trong excel (Windows only).
- **REST API**: cung cấp REST API cho Excel workbook.

## Cài đặt:
```python
pip install xlwings
```
## Sử dụng:
1. Một số thao tác cơ bản:

```python
import xlwings as xw

# mở workbook mới
new_wb = xw.Book()
# hoặc
opening_wb = xw.Book('name_of_opening_workbook')
# hoặc
open_new_workbook = xw.Book('full/relaive_path_to_xls')

# Lấy các sheets có trong file excel 
xw.sheets

# Làm việc với dữ liệu trong 1 sheet
sht = xw.sheets[0]
print(sht.range('A1').value)
sht.range('A1').value = 'xxx'

# tự động tìm bảng
# https://docs.xlwings.org/en/stable/datastructures.html#range-expanding
sht.range('A1').expand()
# ...
```
**Ngoài ra, [xlwings còn tích hợp pandas](https://docs.xlwings.org/en/stable/datastructures.html#pandas-dataframes).**

2. Xử lý trường hợp cụ thể:
Trong video [này](https://www.youtube.com/watch?v=wm7RNejVh8E), xlwings được dùng để tự động tạo các named range cho hàng loạt file có cấu trúc tương tự. Mục đích là để làm bước tiếp theo: link giá trị từ nhiều file vào 1 file tổng hợp, dựa vào named range trong từng file chi tiết. Tham khảo mã nguồn: https://gist.github.com/htlcnn/0ddd4e0023e0b623bc0e6006a9f9520c

Trong script này còn sử dụng Excel VBA API: [WorkBook.Names.Add](https://docs.microsoft.com/en-us/office/vba/api/excel.names.add) (tra cứu toàn bộ ở [đây](https://docs.microsoft.com/en-us/office/vba/api/overview/excel/object-model), được cung cấp qua `xw_object.api`). Tức là những gì không được cung cấp sẵn cú pháp Pythonic, ta sẽ sử dụng VBA API.

Hạn chế: range expand chỉ ứng dụng được cho vùng dữ liệu liên tục. Với "bảng" có các dòng/cột trống (để "format" cho đẹp) thì sẽ bị ngắt tại chỗ có dòng/cột trống. Vì vậy, thường sẽ phải chọn 1 range khá lớn/1 magic number để lấy được toàn bộ vùng dữ liệu cần xử lý.

Mọi việc phải xử lý trong video demo sẽ đơn giản hơn nếu có 1 file excel mẫu ban đầu, được định nghĩa sẵn các named range, sau đó mới duplicate ra để điền dữ liệu vào. Tuy nhiên, thực tế không như thế, ta phải xử lý lỗi một cách nhanh nhất, cũng giống như khi tập chép phạt: `"Anh xin lỗi\n" * 100`