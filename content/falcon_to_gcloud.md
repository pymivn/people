# Cùng tạo và deploy ứng dụng API đơn giản lên Google Cloud Platform
Trong bài này, mình sử dụng Falcon framework để xây dựng API. Bạn có thể xem thêm tại [đây](http://falcon.readthedocs.io/en/stable/) hoặc bạn có thể sử dụng Flask cách làm cũng tương tự.
# Chuẩn bị:
1. Tài khoản của [Google Cloud](https://cloud.google.com/)

Đừng lo Google cho mình $300 miễn phí và có thể sử dụng được trong 12 tháng. Nhớ là phải Enable Billing và trong thẻ Visa hoặc Credit Card phải còn tối thiểu 100k (vì khi đăng ký sẽ phải cần $1) nhé.
2. Tài khoản git
3. Cài trên máy:
  - git
  - python 3 
  - mysql
  - virtualenv
# Tạo ứng dụng API đơn giản
Đầu tiên, tạo một `repositories` rỗng trên github, gitlab...bất cứ đâu cũng được và clone `repositories` về máy bạn.
Trong thư mục vừa clone về, bạn tạo các file sau nhé:
- app.py: ứng dụng API
- requirements.txt: quản lý lib python


# Deploy ứng dụng
Mình sử dụng dịch vụ Compute Engine (hay có thể gọi là VPS) nên nó sẽ hơi phức tạp so với việc sử dụng App Engine.
### WIP
https://www.digitalocean.com/community/tutorials/how-to-serve-flask-applications-with-gunicorn-and-nginx-on-ubuntu-16-04
http://falcon.readthedocs.io/en/stable/
https://viblo.asia/p/huong-dan-tao-ung-dung-web-python-don-gian-tren-google-app-engine-QpmleARnlrd

