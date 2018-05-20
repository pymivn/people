Title: Xây dựng REST API đơn giản với Python và Falcon - Phần 4 
Category: python  
Tags: python, gcp, falcon, api, deploy  
Author: kube.its.me  


Đến đây có thể được coi là xong nhưng chưa hoàn chỉnh vì khi server của mình khởi động lại thì ứng dụng sẽ bị tắt đi mà không tự động chạy lại. Để giải quyết được vấn đề trên giải pháp được đưa ra là sử dụng `systemd`.
## Cấu hình systemd
Như đã nói ở trên, mình không phải chuyên về mảng `network` nên mình chỉ bắt tay vào làm thôi...còn bạn muốn tìm hiểu thêm thì có thể coi ở đây ["Systemd là gì"](https://techtalk.vn/blog/posts/systemd-la-gi).  
Bắt đầu nào, di chuyển vào thư mục `/etc/systemd/system` (lưu ý: nhớ đăng nhập vào `instance` đã tạo ở phần 3 trước khi làm)
```
cd /etc/systemd/system
```
Tạo một file với phần mở rộng là `.service` ở đây mình tạo file tên `api-webserver.service`
```
sudo nano api-webserver.service
```
Chép nội dung ở dưới vào
```
[Unit]
Description=API web server
After=network.target

[Service]
User=root
Group=root
WorkingDirectory=/opt/www/example-api
Environment="PATH=/opt/www/falcon-env/bin"
ExecStart=/opt/www/falcon-env/bin/gunicorn app:api

[Install]
WantedBy=multi-user.target
```
Với:
  - WorkingDirectory: đường dẫn tới thư mục chứa file app
  - Environment: đường dẫn tới môi trường ảo
  - ExecStart: lệnh muốn chạy

Nhấn `Control + X` rồi `Shift + Y` sau đó nhấn `Enter` để lưu lại.  
Chạy và kích hoạt `service`
```
sudo systemctl start api-webserver
sudo systemctl enable api-webserver
```
Kiểm tra lại `service` đã được kích hoạt chưa
```
sudo systemctl list-unit-files | grep api-webserver
```
```
api-webserver.service                      enabled 
```
Vậy là `service` đã được kích hoạt, kiểm tra tiếp coi ứng dụng của mình đã chạy chưa
```
systemctl status api-webserver
```
```
● api-webserver.service - API web server
   Loaded: loaded (/etc/systemd/system/api-webserver.service; enabled; vendor preset: enabled)
   Active: active (running) since Sun 2018-05-13 15:47:17 UTC; 4min 24s ago
 Main PID: 1142 (gunicorn)
    Tasks: 2
   Memory: 27.6M
      CPU: 376ms
   CGroup: /system.slice/api-webserver.service
           ├─1142 /opt/www/falcon-env/bin/python3 /opt/www/falcon-env/bin/gunicorn app:api
           └─1254 /opt/www/falcon-env/bin/python3 /opt/www/falcon-env/bin/gunicorn app:api

May 13 15:47:17 example-api systemd[1]: Started API web server.
May 13 15:47:18 example-api gunicorn[1142]: [2018-05-13 15:47:18 +0000] [1142] [INFO] Starting gunicorn 19.8.1
May 13 15:47:18 example-api gunicorn[1142]: [2018-05-13 15:47:18 +0000] [1142] [INFO] Listening at: http://127.0.0.1:8000 (1142
May 13 15:47:18 example-api gunicorn[1142]: [2018-05-13 15:47:18 +0000] [1142] [INFO] Using worker: sync
May 13 15:47:18 example-api gunicorn[1142]: [2018-05-13 15:47:18 +0000] [1254] [INFO] Booting worker with pid: 1254
lines 1-16/16 (END)
```
Ứng dụng cũng đã chạy tốt và nhấn `q` để thoát ra.  
Hết.
