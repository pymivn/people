Title: Viết một chatbot đơn giản với Python3
Date: 2018-05-25
Author: tung491
Tags: Python, chatbot
Category: Trang chủ

Đầu tiên, bạn cần hiểu chatbot là gì? Chatbot là một chương trình thực hiện cuộc hội thoại qua phương pháp gửi nhận văn bản hoặc các object như hình ảnh, file, ...

Có bao giờ sắp đến giao thừa hay một dịp gì đấy mà bạn muốn nhắn tin cho nhiều người vào một mốc thời gian (VD: 12h đêm) mà bạn không thể dậy được vào lúc đó, hoặc bạn quá lười để làm một việc lặp đi lặp lại? Câu trả lời của mình khi đó là viết một chatbot và hẹn giờ cho nó.

Thôi chém nữa, bắt đầu thôi!

Trong bài viết này mình sử dụng 2 lib của bên thứ 3 là [fbchat](https://fbchat.readthedocs.io/en/master/), [schedule](https://schedule.readthedocs.io/en/stable/) do đó bạn cần tạo virtualenv trước tiên, sau đó dùng pip để cài 2 lib trên. Sau đó tạo một file chatbot.py hay một tên nào đó tuỳ bạn.

Đầu tiên, import những lib mình cần đã 🎉

```
import logging
import os
import time
from threading import Thread
from fbchat import Client
from fbchat.models import Message, ThreadType
import schedule
```

Sau đó tạo một class `Bot` kế thừa `Client` :

`class Bot(Client):`

Tạo 1 function trong class `Bot` để thực hiện gửi tin nhắn, dưới đây là code của mình:

```
class Bot(Client):
    def do_something(self): 
        #Đổi tên function cho phù hợp
        logging.basicConfig(level=logging.INFO)
        lst_id = [...] # List chứa fb id của những người bạn muốn gửi
        for user_id in lst_id:    
            self.send(Message(text="Chúc mừng năm mới"),
                      thread_id=user_id, thread_type=ThreadType.USER)
            self.sendLocalImage('/home/dosontung007/Pictures/wallpaper.png', message=Message(text='Chúc mừng năm mới'),
                                thread_id=user_id, thread_type=ThreadType.USER)
            logging.info('Sent success to %s' % str(user_id))
```

Và để nhận được tin nhắn từ những người gửi cho mình cho mình , ta viết function `onMessage` trong class `Bot` và xử lí các tin nhắn đó:

```
def onMessage(self, message_object, author_id, thread_id, thread_type, **kwargs):
    lst_msg = list('Chúc mừng năm mới')
    if author_id != self.uid and message_object.text in lst_msg:
        self.send(Message(text='Năm mới chúc .....'),
                  thread_id=author_id,
                  thread_type=thread_type)
```

Tham khảo thêm tại https://fbchat.readthedocs.io/en/master/

Job thực hiện việc gửi tin nhắn trong này đó là:

`Bot(os.environ['USERNAME_'], os.environ['PASSWORD']).do_something()`


Class `Bot` kế thừa `Client` do đó 2 args cần truyền vào đó là username và password của Facebook của bạn. Do đó bạn cần set value cho 2 var `USERNAME_` và `PASSWORD` bằng câu lệnh `export var=value`. Lưu ý `USERNAME_` chứ không phải `USERNAME`.

Bây giờ còn một công việc duy nhất là hẹn giờ cho job làm việc thôi!

```
def job():
    Bot(os.environ['USERNAME_'], os.environ['PASSWORD']).do_something()


def send_msg():
    schedule.every().day.at('00:00').do(job_that_executes_once))
    
    while True:
        schedule.run_pending()
        time.sleep(1)
```

Thay đổi `00:00` bằng thời gian mà bạn muốn hẹn giờ.

Để nhận được message, ta sử dụng function `listen` từ `Client` , về cơ bản `listen` khi chạy sẽ truyền các arguments vào `onMessage` mỗi lần Facebook bạn có event mới (VD: có người nhắn cho bạn, bạn nhắn cho người khác hoặc tin nhắn trong nhóm, ...):

```
def reply_msg():
    Bot(os.environ['USERNAME_'], os.environ['PASSWORD']).listen()
```

Ở function main, mình sử dụng lib threading để chạy song song 2 job là reply_msg và send_msg :

```
def main():
    Thread(target=send_msg).start()
    Thread(target=reply_msg).start()
```

Cuối cùng cũng xong 🎉.Sau tất cả, đây là một con chatbot hoàn chỉnh :

```
import logging
import os
import time
from threading import Thread

from fbchat import Client
from fbchat.models import Message, ThreadType
import schedule


class Bot(Client):
    def onMessage(self, message_object, author_id, thread_id, thread_type, **kwargs):
        lst_msg = list('Chúc mừng năm mới')
        if author_id != self.uid and message_object.text in lst_msg:
            self.send(Message(text='Năm mới chúc .....'),
                      thread_id=author_id,
                      thread_type=ThreadType.USER)


    def do_something(self):
        logging.basicConfig(level=logging.INFO)
        lst_id = ['100012610305665']
        for user_id in lst_id:    
            self.send(Message(text="Chúc mừng năm mới"),
                      thread_id=user_id, thread_type=ThreadType.USER)
            self.sendLocalImage('/home/dosontung007/Pictures/wallpaper.png', message=Message(text='Chúc mừng năm mới'),
                                thread_id=user_id, thread_type=ThreadType.USER)
            logging.info('Sent success to %s' % "100012610305665")


def job_that_executes_once():
    Bot(os.environ['USERNAME_'], os.environ['PASSWORD']).something()
    return schedule.CancelJob


def reply_msg():
    Bot(os.environ['USERNAME_'], os.environ['PASSWORD']).listen()


def send_msg():
    schedule.every().day.at('00:00').do(job_that_executes_once))
    while True:
        schedule.run_pending()
        time.sleep(1)


def main():
    Thread(target=send_msg).start()
    Thread(target=reply_msg).start()


if __name__ == '__main__':
    main()

```

Bây giờ chỉ cần chạy thôi. Và đây là thành quả:

![img]: (/home/dosontung007/Downloads/imageedit_2_6324647083.png)

Nếu bạn muốn chạy luôn mà không cần hẹn giờ thì chỉ cần xoá function `job_that_executes_once` và thay function `send_msg` bằng:

```
def send_msg():
    Bot(os.environ['USERNAME_'],os.environ['PASSWORD']).do_something()
```

HẾT.

TUNG491 at http://pymi.vn/
