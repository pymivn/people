Title: Class inheritance trong Python
Date: 2019-06-23
Author: tung491
Tags: Python
Category: Trang chủ


Classes cùng với objects tạo nên những tính năng lõi của Python. Classes cung cấp một cách tổ chức các attributes(data) 
và methods(behaviors). Một khái niệm vô cùng quan trọng của OOP(Object Oriented Programming) là class inheritance 
(dịch đại ý là thừa kế class). Class inheritance cho phép chúng ta tạo ra một class “thừa kế" (inherit) mọi 
tính năng của base class(es)(parent class(es), super class(es)), chỉnh sửa các tính năng đó và đồng thời thêm các methods,
 attributes. Trong bài viết này, mình cùng các bạn khám phá khái niệm này trong Python.
 
# I. Cách để kế thừa một class:

Cú pháp để kế thừa một class làm base class như sau:
```python
class Parent:
    passclass Child(Parent):
    pass
```

Base class(es) được định nghĩa ở trong () sau tên của child class.<br>

Để kiểm tra base(parent) class(es) của một class là gì, chúng ta dùng cú pháp <class>.__bases__ . 
Câu lệnh sẽ trả về một tuple chứa các base class(es) của <class>. Đối với class Child, cú pháp trên sẽ trả về:
```
(__main__.Parent,) 
```

# II. Parent của các parents
Ở ví dụ trên, class Parent không được định nghĩa parent class. Vậy nó có “parent” không hay là mồ côi?

Để câu hỏi trên thì chúng ta lại dùng cú pháp `<class>.__bases__` đối với class Parent. Kết quả trả về là:
```python
(object,)   
```

Oh vậy object chính là parent của parents. Vì Python là một ngôn ngữ OO(Object Oriented) nên mọi thứ trong Python đều là 
object ngoại trừ control flow. Và `object` là base classes của mọi objects trong Python. Một ví dụ để thấy điều này đó là:
```python
In [1]: int.__bases__                                                           
Out[1]: (object,)
```

# III. Các cách mở rộng class thông qua kế thừa
Đây là parent class chúng ta sẽ dùng trong ba phần phía dưới:
```python
class Animal:
    def __init__(self, age, gender):
        self.age = age
        self.gender = gender
```
## 1. Thêm method(s) mới:
```python
class Dog(Animal):
    def bark(self):
        print("Woof Woof")


misa = Dog(1, 'gay')
misa.bark()
```

Output sẽ là:
```
Woof Woof
```

## 2. Định nghĩa lại, chỉnh sửa method(s) có sẵn của base class(es)
```python
class Chihuahua(Dog):
    def bark(self):
        print('Yab Yab')


mic = Chihuahua(2, 'male')
mic.bark()
```

Output sẽ là:
```
Yab Yab
```

## 3. Thêm attribute(s) mới
```python
class Bear(Animal):
    def __init__(self, age, gender, fur_color):
        super().__init__(age, gender)
        self.fur_color = fur_color
```
Khái niệm `super()` mình sẽ giải thích ở sau. Các bạn có thể hiểu `super()` trong context hiện tại là để gọi 
phiên bản trước — tức là class Animal. Ở ví dụ trên, đó là truyền vào __init__ của class Animal hai attributes đó là age, 
gender như định nghĩa của nó.

```python
polar_bear = Bear(1, 'male', 'white')# __dict__ trả về một dictionary chứa instance data của instance
polar_bear.__dict__
```
 
Output:
```
{'age': 1, 'gender': 'male', 'fur_color': 'white'}
```
Như các bạn thấy polar_bear có đầy đủ hai attributes của Animal đó là `age`, `gender`, và attribute `fur_color` mới được thêm vào class Bear

# IV. Quan hệ giữa các child và parent classes

Sự “thừa kế” giữa child và base class(es) sẽ tạo ra một quan hệ “huyết thống” giữa 2.

Ví dụ kiểm tra loại của polar_bear:

```python
isinstance(polar_bear, Bear)
True

isinstance(polar_bear, Animal)
True
```

Do đó, một đoạn code hoat động với instance của parent class thì nên hoạt động với instance của child class.

# Kế thừa nhiều class (Multi-inheritance)
Không như Java — ngôn ngữ chỉ cho kế thừa một class duy nhất cho một class, Python cho phép cho chúng ta kết thừa nhiều class cho một class. Ví dụ:
```python
class Father:
    pass


class Mother:
    pass


class Child(Father, Mother):
    pass
```

Kết quả của Child.__bases__ trong trường hợp này đó là:
```python
(__main__.Father, __main__.Mother)
```

# VI. Tìm attributes với kế thừa

Theo logic, quá trình tìm kiếm attributes như sau:
* Đầu tiên, tìm kiếm attributes trong local __dict__
* Nếu không có, tiếp tục tìm trong class __dict__
* Nếu vẫn không có thì tìm ở trong các classes còn lại ở __mro__

Mình sẽ làm rõ ý cuối cùng ở các phần tiếp theo của bài.


# VII. MRO
MRO là viết tắt của Method Resolution Order. Là một chuỗi inheritance mà Python tính toán và lưu 
nó ở MRO attribute trong class. Như đã nói ở trên khi tìm attributes, Python sẽ đi lần lượt qua các phần tử trong MRO.

Để xem MRO của một class, ta dùng cú pháp `<class>.__mro__` . Ví dụ:

```python
class A: pass
class B(A): pass
class C(B): pass
class D(C): pass
class E(D): pass


E.__mro__
```

Output:
```
(__main__.E, __main__.D, __main__.C, __main__.B, __main__.A, object)
```

Một ví dụ khác “khù khằm” hơn với multi inheritance:
```python
class A: pass
class B(A): pass
class C(A): pass
class D(B): pass
class E(D, C): pass


E.__mro__
```

Python sử dụng `cooperative multiple inheritance` để quy định một số luật về thứ tự của class:
* Children are always checked before parents (chilren classes luôn được kiểm tra trước parents classes)
* Parents (if multiple) are always checked in the order listed (các parents classes luôn được kiêm tra theo thứ tự được liệt kê)

Như ví dụ ở trên, sau khi kiểm tra ở E, class D sẽ được kiểm tra vì D được ghi đầu tiên trong hai base classes. Sau đó, B — parent class của D sẽ được kiểm tra. Cuối cùng, class C và parent của nó - A sẽ được kiểm tra.


Để hiểu rõ hơn, các bạn hãy thử động não, thử giải thích MRO của class E dưới đây:


```python
class A: pass
class B: pass
class C(A, B): pass
class D(B): pass
class E(C, D): pass


E.__mro__
```
Output:
```python
(__main__.E, __main__.C, __main__.A, __main__.D, __main__.B, object)
```
Thuật toán này là có tên là “C3 Linearization Algorithm” nhưng bạn không cần đi sâu vào thuật toán này. Để đơn giản và nhớ hiểu, hãy tưởng tượng đến thứ tự thoát hiểm khi một sự cố như cháy nhà, chìm tàu xảy ra:
 “Trẻ em đầu tiên, sau đó mới là người lớn" (Children first, followed by parents).


# VIII. Ví dụ về multi-inheritance
```python
class Person:
    def talks(self):
        return 'ư ư ư'


class Noisy:
    def talks(self):
        return super().talk().upper()


class NoisyPerson(Noisy, Person):
    pass
```
`super()` sẽ gọi class kế tiếp của class hiện tại trong MRO

Ví dụ:
MRO của NoisyPerson:
```python
(__main__.NoisyPerson, __main__.Noisy, __main__.Person, object)
```

Thử gọi method talks của NoisyPerson instance:
```python
girl = NoisyPerson()
girl.talks()
```

Output:
```
'Ư Ư Ư'
```

Khi talk() method của girl được gọi, do bản thân NoisyPerson không có method này nên nó sẽ tìm ở class tiếp theo trong MRO là Noisy.
Noisy có talk() method sẽ được execute. `super().talk()` sẽ tìm gọi method talk() của class kế tiếp trong MRO - Person (return 'ư ư ư').
Đoạn string 'ư ư ư' này sẽ được upper() và return. Do đó output trả về là `"Ư Ư Ư"` 


Bây giờ nếu ta đổi chỗ 2 parent classes với nhau thì sao?
```python
class NoisyPerson(Person, Noisy):
    pass
```

Chạy lại talks method:
```python
girl = NoisyPerson()
girl.talks()
```

Output:
```python
'ư ư ư'
```

Đây là MRO của NoisyPerson bây giờ:
```python
(__main__.NoisyPerson, __main__.Person, __main__.Noisy, object)
```

Ta thấy class Person được kiểm tra trước Noisy, trong khi đó Person có method talks() nên nó sẽ được execute.

# IX. Kết luận
Hy vọng qua bài viết, các bạn đã có cái kiến thức tổng quan inheritance trong Python và có thể áp dụng nó vào công việc của mình.

Reference: [https://github.com/dabeaz-course/practical-python](https://github.com/dabeaz-course/practical-python)
