Title: Tuple comprehension
Date: 2018-09-10
Category: Trang chủ
Tags: python, tuple, list, comprehension, memory, generator
Slug: tuple_comps
Authors: hvnsweeting
Summary: List comprehension, set/dict comprehension, còn tuple? Generator là gì?

Python có sẵn (builtin) 4 kiểu dữ liệu "compound"/"container" quan trọng,
chúng dùng để chứa các giá trị. `list`, `tuple`, `set`, `dict`.

Một lập trình viên Python phải nắm thành thạo cả 4 kiểu dữ liệu trên và vận
dụng linh hoạt, biết điểm mạnh yếu của từng kiểu. Bàn về chuyện *ấy* lại cần
vài bài dài dòng khác nên sẽ giữ lại "để sau"/"lúc nào rảnh".

## Comprehension

**Comprehension** là một đặc sản của Python, một khi biết đến là hay bị nghiện,
thứ cú pháp ngắn gọn sạch sẽ ngọt như mía lùi cũng chính là vũ khí
giết những con ong ham ăn.

Cú pháp này Python ["vay mượn" mà không bao giờ trả từ
Haskell](https://docs.python.org/3/whatsnew/2.0.html)
 - một ngôn ngữ
vốn có tiếng khó học và vi diệu. Hãy thử xem 2 ví dụ sau:

```python
In [1]: names = ['vuong', 'tron', 'tam giac']

In [2]: more_than_four_chars = []

In [3]: for name in names:
   ...:     if len(name) > 4:
   ...:         more_than_four_chars.append(name.title())
   ...:

In [4]: print(more_than_four_chars)
['Vuong', 'Tam Giac']
```

4 dòng code (dòng print không tính)
trên để ta filter (lọc) từ một tập hợp đã cho, thu về các phần tử
thỏa mãn điều kiện (hơn 4 ký tự) rồi map (biến đổi) các ký tự đứng đầu thành
chữ hoa.

Dù đẹp sạch dễ hiểu lắm rồi, nhưng so với list comprehension:

```python
In [5]: names = ['vuong', 'tron', 'tam giac']

In [6]: print([name.title() for name in names if len(name) > 4])
['Vuong', 'Tam Giac']
```

thì sự ngắn gọn, đơn giản này đánh bại hoàn toàn cú pháp thông thường.

Và ta còn làm tương tự được với `set`, `dict`:

```python
In [9]: {i for i in [1,2,3,4,1,2] if i % 2 == 0}
Out[9]: {2, 4}

In [10]: {i: i**2 for i in range(5,10) if i % 2 == 1}
Out[10]: {5: 25, 7: 49, 9: 81}
```

## Tuple comprehension
Dễ tưởng tượng ra là ta sẽ có luôn **tuple comprehension** - vì nghe có vẻ hợp
lý mà:

```python
In [13]: type((i for i in range(5,10) if i % 2 == 0))
Out[13]: <class 'generator'>
```

SAI! khái niệm **tuple comprehension** không tồn tại. Cùng cú pháp nhưng kết
quả thu được là 1 **generator**.

## Vì sao thế?
Tuple được tạo ra, ban đầu trông như 1 phiên bản thiếu tính năng của `list`,
nhưng mục đích tạo ra tuple là hoàn toàn khác. `tuple` được dùng như khái
niệm `struct` trong các ngôn ngữ khác, nó là tập hợp của các thông tin khác
nhau:

```python
In [14]: student = ('Meo', 18, '0699609096', 'PyMi.vn')
```

và khi dùng thì unpack các giá trị ra:

```python
In [15]: name, age, phone, school = student

In [16]: print(school)
PyMi.vn
```

Còn list dùng để lặp qua/ duyệt qua:

```python
In [17]: names = ['vuong', 'tron', 'tam giac']

In [18]: for name in names:
    ...:     print('Hello các bạn mình là {}'.format(name.title()))
    ...:
Hello các bạn mình là Vuong
Hello các bạn mình là Tron
Hello các bạn mình là Tam Giac
```

Xem thêm tại [FAQ của
Python](https://docs.python.org/3/faq/design.html#why-are-there-separate-tuple-and-list-data-types).

Ok, vậy chẳng có nghĩa lý gì để "comprehension" ra tuple cả.

## Lập trình viên phê list comprehension túy lúy!
Đã dùng là nghiện, mà nghiện là rất khó tỉnh. List comprehension hấp dẫn vậy
nên thường bị dùng SAI, lạm dụng. Một điều duy nhất quan trọng cần nhớ:

> List comprehension là để tạo ra list.

Thế nhưng không ít lần, nó bị lạm dụng, khi người ta không cần đến list:

- khi chỉ cần đếm "số lượng phần tử"
- để tính tổng
- để in ra màn hình
- để viết những vòng lặp điều kiện phức tạp.

List comprehension tạo ra 1 list, vậy nên nếu không cần tới list kết quả đó
thì không nên dùng tới list comprehension mà hãy dùng vòng lặp for thông thường:

Đừng viết:

```python
In [19]: [print(name.upper()) for name in names]
VUONG
TRON
TAM GIAC
Out[19]: [None, None, None]
```

Hãy viết:

```python
In [20]: for name in names:
    ...:     print(name.upper())
    ...:
VUONG
TRON
TAM GIAC
```

Ta không tạo ra 1 cái list vô nghĩa chứa 3 phần tử `None` - tức là tiết kiệm bộ
nhớ (memory).

Đừng viết:

```python
In [21]: len([i for i in range(100,1000) if i % 2 == 0])
Out[21]: 450
```

Hãy viết:

```python
In [22]: c = 0

In [23]: for i in range(100, 1000):
    ...:     if i % 2 == 0:
    ...:         c = c + 1
    ...:

In [24]: print(c)
450
```

vì ta sẽ không tạo ra 1 list (tạm) chứa 450 phần tử.

Và đừng viết:

```python
In [25]: sum([i for i in range(5000000)])
Out[25]: 12499997500000
```

Mà hãy viết:

```python
In [26]: sum_zero_to_5mil = 0

In [27]: for i in range(5000000):
    ...:     sum_zero_to_5mil = sum_zero_to_5mil + i
    ...:

In [28]: sum_zero_to_5mil
Out[28]: 12499997500000
```

bởi ta sẽ không *vô tình* tạo ra một list chiếm tới ~180MB bộ nhớ chỉ để tính
tổng.

Cách tính
```python
In [32]: import sys

In [33]: list_size =  sys.getsizeof([i for i in range(5000000)])

In [34]: all_numbers_size = sys.getsizeof(5000000) * 5000000

In [35]: print(list_size, all_numbers_size, list_size + all_numbers_size)
40215168 140000000 180215168
```

Và nếu như số vòng `for` hay lệnh `if` trong list comprehension nhiều hơn 2,3
nó không còn sạch sẽ và dễ đọc nữa, hãy quay trở về dùng vòng lặp `for` thông
thường. [Ở CIA họ dạy thế](https://wikileaks.org/ciav7p1/cms/page_26607631.html
).

List/set/dict comprehension rất tiện để tạo list/set/dict, nhưng khi không
cần tới list/set/dict kết quả, hãy đừng lạm dụng.

## Generator

Generator sinh ra các phần tử của list tương ứng, nhưng mỗi lần, chỉ có 1
phần tử được tạo ra, vì vậy thường dùng để tiết kiệm RAM. Cú pháp tạo generator
đơn giản chỉ là thay dấu `[]` thành `()`.

```python
In [36]: sys.getsizeof([i for i in range(5000000) if i % 3 == 0 or i % 5 == 0])
Out[36]: 19836760

In [37]: sys.getsizeof((i for i in range(5000000) if i % 3 == 0 or i % 5 == 0))
Out[37]: 88

In [38]: sum([i for i in range(5000000) if i % 3 == 0 or i % 5 == 0])
Out[38]: 5833329166668

In [39]: sum(i for i in range(5000000) if i % 3 == 0 or i % 5 == 0) # chỗ này mượn tạm luôn dấu () của sum
Out[39]: 5833329166668
```

Đã đến lúc lạm dụng **generator**!!! nó được dùng mọi nơi trong Python3 và
là một cải tiến hấp dẫn của Python3 so với Python2.

## Hết.

HVN at [https://pymi.vn](https://pymi.vn) and http://www.familug.org
