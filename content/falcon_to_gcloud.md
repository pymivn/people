Title: Tạo và deploy ứng dụng API đơn giản lên Google Cloud Platform  
Category: python  
Tags: python, gcp, falcon, api, deploy  
Author: kubeitsme  

Trong bài này, mình sử dụng [Falcon framework](http://falcon.readthedocs.io/en/stable/) để xây dựng API hoặc bạn có thể sử dụng Flask cách làm cũng tương tự.
## Chuẩn bị:
1. Tài khoản của [Google Cloud](https://cloud.google.com/)  
Google cho mỗi tài khoản $300 để sử dụng dịch vụ cloud trong vòng 12 tháng. Để đăng ký được thì cần phải có 1 thẻ tín dụng còn ít nhất 100.000 VNĐ trong tài khoản.
2. Tài khoản github, gitlab, bitbucket...  
3. Nên có kiến thức về:
    - Ubuntu cơ bản
    - Git
    - Cơ sở dữ liệu
4. Cài trên máy:
    - git
    - python 3 
    - mysql
    - virtualenv

## Tạo ứng dụng API đơn giản
Đầu tiên, tạo một `repository` rỗng trên github, gitlab...bất cứ đâu cũng được và clone `repository` về máy bạn.
Trong thư mục vừa clone về, bạn tạo các file sau:
- app.py: file chứa code
- requirements.txt: quản lý lib (thư viện) python  

Mở file `app.py` vừa tạo và chép đoạn mã sau vào:
```python
# Let's get this party started!
import falcon


# Falcon follows the REST architectural style, meaning (among
# other things) that you think in terms of resources and state
# transitions, which map to HTTP verbs.
class ThingsResource(object):
    def on_get(self, req, resp):
        """Handles GET requests"""
        resp.status = falcon.HTTP_200  # This is the default status
        resp.body = ('\nTwo things awe me most, the starry sky '
                     'above me and the moral law within me.\n'
                     '\n'
                     '    ~ Immanuel Kant\n\n')

# falcon.API instances are callable WSGI apps
api = falcon.API()

# Resources are represented by long-lived class instances
things = ThingsResource()

# things will handle all requests to the '/things' URL path
api.add_route('/things', things)
```
Tiếp theo mở file `requirements.txt` và chép đoạn text ở dưới vào
```
mysqlclient
falcon
gunicorn
```
Cài đặt vào chạy ứng dụng trên local:  
### 1. Cài đặt môi trường ảo
Tạo môi trường ảo (virtualenv)
```
python3 -m venv falcon-env
```
Kích hoạt môi trường ảo
```
source falcon-env/bin/activate
```
Cài đặt các lib (thư viện) cần thiết
```
pip install -r requirements.txt
```
**Trên ubuntu có thể không install được lib `mysqlclient` thì bạn chạy lệnh này trước.
```
sudo apt-get update && sudo apt-get install libmysqlclient-dev
```
Nếu không may bạn bị thoát ra khỏi môi trường ảo, thì chạy lệnh sau để kích hoạt lại môi trường ảo. Vậy làm sao để biết mình có đang trong môi trường ảo hay không?
Bạn để ý vào dấu nhắc lệnh (command prompt), mình lấy ví dụ ở Ubuntu. Đây là khi chưa kích hoạt môi trường ảo
```
username@ubuntu:~$
```
Sau khi chạy lệnh
```
source falcon-env/bin/activate
```
Môi trường ảo đã kích hoạt thì dấu nhắc lệnh (command prompt) của bạn sẽ như sau
```
(falcon-env)username@ubuntu:~$
```
- `falcon-env` là tên môi trường ảo mình đã tạo ở trên.

Tiếp tục nào, chạy lại lệnh
```
pip install -r requirements.txt
```
### 2. Chạy thử ứng dụng
```
gunicorn app:api
```
```
[2018-05-04 23:22:02 +0700] [4418] [INFO] Starting gunicorn 19.8.1
[2018-05-04 23:22:02 +0700] [4418] [INFO] Listening at: http://127.0.0.1:8000 (4418)
[2018-05-04 23:22:02 +0700] [4418] [INFO] Using worker: sync
[2018-05-04 23:22:02 +0700] [4421] [INFO] Booting worker with pid: 4421
```
Truy cập vào đường dẫn trên [http://127.0.0.1:8000/things](http://127.0.0.1:8000/things)
![first run app](images/ftg_first_run_app.png)
**Bạn có thắc mắc vì sao phải thêm `/things` vào không? Vì trong file `app.py` có dòng:
```python
api.add_route('/things', things)
```
Hiểu đơn giản là `route` có nhiệm vụ định hướng request (nôm na là URL - ở đây là `/things`) của mình tới `resource` (ThingsResource) đã được định nghĩa sẵn.
### 3. Tạo database
Bây giờ chúng ta đã có một API đơn giản hãy giờ làm cho nó phức tạp thêm. Đầu tiên phải tạo database trước
```
mysql -u root -p
Enter password: 
```
**password mặc định mình hay để trống nên mình `Enter` luôn, sau khi đăng nhập vào mysql nó sẽ như này
![mysql](images/ftg_mysql.png)
Kiểm tra coi đang có bao nhiêu databases
```sql
mysql> show databases;
+----------------------+
| Database             |
+----------------------+
| information_schema   |
| mysql                |
| performance_schema   |
| sys                  |
+----------------------+
4 rows in set (0.00 sec)
```
Giờ mình tiến hành tạo database
```sql
mysql> create database example_api;
Query OK, 1 row affected (0.01 sec)
```
Kiểm tra lại phát nào
```sql
mysql> show databases;
+----------------------+
| Database             |
+----------------------+
| information_schema   |
| example_api          |
| mysql                |
| performance_schema   |
| sys                  |
+----------------------+
5 rows in set (0.00 sec)
```
Đã có database `example_api`, muốn lưu trữ được dữ liệu thì cần phải tạo thêm table cho nó
```sql
mysql> use example_api;
Database changed
```
Xem trong database đã có tables nào chưa
```sql
mysql> show tables;
Empty set (0.00 sec)
```
Chưa có tables nào hết, tạo mới một table mới thôi
```sql
mysql> create table songs(
    -> id int,
    -> song_name varchar(255),
    -> category varchar(255),
    -> singer varchar(255)
    -> );
Query OK, 0 rows affected (0.03 sec)
```
Đã tạo thành công table tên là `songs`, kiểm tra lại lần nữa
```sql
mysql> show tables;
+-----------------------+
| Tables_in_example_api |
+-----------------------+
| songs                 |
+-----------------------+
1 row in set (0.00 sec)
```
Giờ tiến hành thêm giữ liệu vào cho nó, trước khi thêm kiểm tra xem đã có dữ liệu chưa
```sql
mysql> select * from songs;
Empty set (0.00 sec)
```
Chưa có rồi, tiến hành thêm dữ liệu vào
```sql
mysql> insert into songs (id, song_name, category, singer) 
    -> values (1, 'Đừng Như Thói Quen', 'Nhạc trẻ', 'JayKii; Sara Lưu'),
    -> (2, 'Tâm Sự Tuổi 30', 'Nhạc trẻ', 'Trịnh Thăng Bình'),
    -> (3, 'Chạm Đáy Nỗi Đau', 'Nhạc trẻ', 'Erik'),
    -> (4, 'Hey Brother', 'Electronica', 'Avicii'),
    -> (5, 'Wake me up', 'Electronica', 'Avicii');
Query OK, 5 rows affected (0.00 sec)
Records: 5  Duplicates: 0  Warnings: 0
```
Thêm dữ liệu thành công, kiểm tra lại phát nữa
```sql
mysql> select * from songs;
+--------+-------------------------+--------------+----------------------+
| id | song_name                | category     | singer               |
+--------+-------------------------+--------------+----------------------+
|      1 | Đừng Như Thói Quen      | Nhạc trẻ     | JayKii; Sara Lưu     |
|      2 | Tâm Sự Tuổi 30          | Nhạc trẻ     | Trịnh Thăng Bình     |
|      3 | Chạm Đáy Nỗi Đau        | Nhạc trẻ     | Erik                 |
|      4 | Hey Brother             | Electronica  | Avicii               |
|      5 | Wake me up              | Electronica  | Avicii               |
+--------+-------------------------+--------------+----------------------+
5 rows in set (0.00 sec)
```
Dữ liệu cũng đã có, sử dụng `\q` để thoát ra khỏi `mysql`
```
mysql> \q
Bye
```
### 4. Kết nối database và thêm resource
Mở lại file `app.py` và thay thế code cũ bằng code ở dưới
```python
# Let's get this party started!
import falcon
import json
import MySQLdb


class SongsResource(object):
    def on_get(self, req, resp):
        db = MySQLdb.connect(host='127.0.0.1',
                             user='root',
                             passwd='',
                             db='example_api',
                             use_unicode=True,
                             charset="utf8")
        c = db.cursor()
        c.execute('select * from songs')
        songs = c.fetchall()
        db.close()
        records = []
        for song in songs:
            records.append({
                'id': song[0],
                'song_name': song[1],
                'category': song[2],
                'singer': song[3],
            })
        body = {
            'status': 'ok',
            'records': records,
            'total_matched': len(songs)
        }
        resp.status = falcon.HTTP_200
        resp.body = (json.dumps(body))


# Falcon follows the REST architectural style, meaning (among
# other things) that you think in terms of resources and state
# transitions, which map to HTTP verbs.
class ThingsResource(object):
    def on_get(self, req, resp):
        """Handles GET requests"""
        resp.status = falcon.HTTP_200  # This is the default status
        resp.body = ('\nTwo things awe me most, the starry sky '
                     'above me and the moral law within me.\n'
                     '\n'
                     '    ~ Immanuel Kant\n\n')

# falcon.API instances are callable WSGI apps
api = falcon.API()

# Resources are represented by long-lived class instances
things = ThingsResource()
songs = SongsResource()

# things will handle all requests to the '/things' URL path
api.add_route('/things', things)
api.add_route('/songs', songs)
```
Tắt app đang chạy bằng cách `Control + C` (mình xài OSX), rồi chạy lại app
```
gunicorn app:api
```
Truy cập vào đường dẫn [http://127.0.0.1:8000/songs](http://127.0.0.1:8000/songs)
![response](images/ftg_response.png)
Mọi thứ đã chạy ổn trên local, giờ dùng `git` để push lên thôi. Nếu không muốn tạo lại database nữa thì chạy lệnh này để `export` ra
```
mysqldump -u root -p example_api > example_api.sql
Enter password: 
```
Xong giờ mình đã có database (để có thể mang đi khắp nơi), do đây là ví dụ nên để file `example_api.sql` trong `repository`  rồi push lên luôn (trên thực tế chẳng ai làm vậy cả vì vấn đề bảo mật).
## Deploy ứng dụng
Đây là phần hấp dẫn nhất, trong phần này mình sử dụng `Compute Engine` (hay có thể gọi là Cloud VPS) để có thể quản lý database của mình hoặc các app khác nếu mình muốn.  
Mình sẽ không hướng dẫn tạo tài khoản và `Enable Billing`, vì đã có rất nhiều bài hướng dẫn rồi hoặc bạn có thể coi từ trang [hỗ trợ](https://support.google.com/cloud/answer/6158867?hl=en) của Google.  
Bạn cũng có thể coi hướng dẫn nhanh về cách tạo và sử dụng `Compute Engine` từ Google bằng hình ảnh ở [đây](https://cloud.google.com/compute/docs/quickstart-linux).
 Dưới đây, mình sẽ hướng dẫn tạo và sử dụng `Compute Engine` bằng bộ Google Cloud SDK (gcloud).
### 1. Tải và cài đặt gcloud
Tải bộ [Google Cloud SDK](https://cloud.google.com/sdk/downloads) về và giải nén ra. Bật terminal lên và chạy lệnh
```
./google-cloud-sdk/install.sh
```
Tắt và mở lại terminal. Tiếp theo cấu hình tài khoản cho `gcloud`
```
gcloud init
```
Màn hình sẽ hiển thị chào mừng...
```
Welcome! This command will take you through the configuration of gcloud.

Your current configuration has been set to: [default]

You can skip diagnostics next time by using the following flag:
  gcloud init --skip-diagnostics

Network diagnostic detects and fixes local network connection issues.
Checking network connection...done.                                                                                           
Reachability Check passed.
Network diagnostic (1/1 checks) passed.

You must log in to continue. Would you like to log in (Y/n)?  
```
Nó bảo mình phải đăng nhập để tiếp tục, nhấn phím `Y` và `Enter`.
Sau khi nhấn `Enter`, 1 tab của trình duyệt sẽ mở lên và yêu cầu chọn tài khoản (nếu có nhiều tài khoản đã đăng nhập).
![choose-account](images/ftg_choose_account.png)
Sau khi chọn tài khoản thì nhấn nút `CHO PHÉP` để cấp quyền cho gcloud.
![permission](images/ftg_permission.png)
Bạn sẽ được chuyển tới một trang với nội dung là đã xác thực thành công.
![permission](images/ftg_auth_success.png)
Quay lại terminal bạn sẽ thấy như sau
```
Your browser has been opened to visit:

    https://accounts.google.com/o/oauth2/auth?redirect_uri=http%3A%2F%2Flocalhost%3A8085%2F&prompt=select_account&response_type=code&client_id=*********.apps.googleusercontent.com&scope=https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fuserinfo.email+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fcloud-platform+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fappengine.admin+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fcompute+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Faccounts.reauth&access_type=offline


You are logged in as: [*********@gmail.com].

This account has no projects.

Would you like to create one? (Y/n)?
```
Tiếp theo mình phải tạo một `project` để có thể sử dụng được `Compute Engine`. Nhấn `Y` và `Enter`
```
Enter a Project ID. Note that a Project ID CANNOT be changed later.
Project IDs must be 6-30 characters (lowercase ASCII, digits, or
hyphens) in length and start with a lowercase letter.
```
Đại khái là nó kêu bạn đặt tên cho `project`(chấp nhận ký tự ASCII thường, số và dấu gạch ngang)...trong bài này mình đặt tên cho `project` là `project-songs`. Sau khi đặt tên xong nhấn `Enter`
```
Your current project has been set to: [project-songs].

Not setting default zone/region (this feature makes it easier to use
[gcloud compute] by setting an appropriate default value for the
--zone and --region flag).
See https://cloud.google.com/compute/docs/gcloud-compute section on how to set
default compute region and zone manually. If you would like [gcloud init] to be
able to do this for you the next time you run it, make sure the
Compute Engine API is enabled for your project on the
https://console.developers.google.com/apis page.

Your Google Cloud SDK is configured and ready to use!

* Commands that require authentication will use *********@gmail.com by default
* Commands will reference project `project-songs` by default
Run `gcloud help config` to learn how to change individual settings

This gcloud configuration is called [default]. You can create additional configurations if you work with multiple accounts and/or projects.
Run `gcloud topic configurations` to learn more.

Some things to try next:

* Run `gcloud --help` to see the Cloud Platform services you can interact with. And run `gcloud help COMMAND` to get help on any gcloud command.
* Run `gcloud topic -h` to learn about advanced features of the SDK like arg files and output formatting
```
Đã tạo `project` thành công, để xem danh sách các `projects`
```
gcloud projects list
```
```
PROJECT_ID     NAME           PROJECT_NUMBER
project-songs  project-songs  579008193409
```
Tiếp theo mình sẽ cần tạo 1 `instance` (Compute Engine có thể tạo được nhiều instance), trước tiên phải kiểm tra xem có instances nào chưa
```
gcloud compute instances list
```
Và một thông báo lỗi sẽ xuất hiện
```
ERROR: (gcloud.compute.instances.list) Some requests did not succeed:
 - Project 579008193409 is not found and cannot be used for API calls. If it is recently created, enable Compute Engine API by visiting https://console.developers.google.com/apis/api/compute.googleapis.com/overview?project=579008193409 then retry. If you enabled this API recently, wait a few minutes for the action to propagate to our systems and retry.
```
Bạn copy link ở trên và paste vào trình duyệt web, nó sẽ dẫn bạn đến trang để `Enable Compute Engine API`
![enable-compute-api](images/ftg-enable-compute-api.png)
Nhấn vào nút `ENABLE` một popup hiện ra yêu cầu bạn phải `Enable Billing`
![enable_billing](images/ftg_enable_billing.png)
Tiếp tục nhấn vào `ENABLE BILLING` một popup khác lại hiện ra yêu cầu bạn cài đặt tài khoản thanh toán cho `project` của mình
![set_account](images/ftg_set_account.png)
Và nhấn vào `SET ACCOUNT`, đợi một tí nó sẽ chuyển bạn đến 1 trang khác giống như vậy
![enable_compute_api_done](images/enable_compute_api_done.png)
Quay lại terminal và kiểm tra xem `Compute Engine API` đã hoạt động chưa
```
gcloud compute instances list
```
```
Listed 0 items.
```
Mọi thứ đã hoạt động tốt tiến hành tạo `instance`
```
gcloud compute instances create [INSTANCE_NAME]
    --image-family [IMAGE_FAMILY]
    --image-project [IMAGE_PROJECT]
    --zone [ZONE]
    --tags http-server,https-server
```
Với:
  - [INSTANCE_NAME] tên `instance`
  - [IMAGE_FAMILY] và [IMAGE_PROJECT] nôm na là hệ điều hành để chạy trên `instance`, coi thêm ở [đây](https://cloud.google.com/compute/docs/images#os-compute-support)
  - [ZONE] nơi đặt `instance`
  - --tags http-server,https-server: cho phép truy cập bằng HTTP và HTTPS
```
gcloud compute instances create example-api --image-family ubuntu-1604-lts --image-project ubuntu-os-cloud --zone asia-southeast1-c --tags http-server,https-server
```
```
Created [https://www.googleapis.com/compute/v1/projects/project-songs/zones/asia-southeast1-c/instances/example-api].
NAME         ZONE               MACHINE_TYPE   PREEMPTIBLE  INTERNAL_IP  EXTERNAL_IP     STATUS
example-api  asia-southeast1-c  n1-standard-1               10.148.0.2   35.198.235.193  RUNNING
```
Đã tạo `intance` thành công, kiểm tra lại lần nữa cho chắc
```
gcloud compute instances list
```
```
NAME         ZONE               MACHINE_TYPE   PREEMPTIBLE  INTERNAL_IP  EXTERNAL_IP     STATUS
example-api  asia-southeast1-c  n1-standard-1               10.148.0.2   35.198.235.193  RUNNING
```
`Instance` đã có và để truy cập vào `instance` bằng trình duyệt web thông qua giao thức HTTP mình cần phải cấu hình thêm một bước nữa, xem đã `port 80` đã mở chưa
```
gcloud compute firewall-rules list
```
```
NAME                    NETWORK  DIRECTION  PRIORITY  ALLOW                         DENY
default-allow-icmp      default  INGRESS    65534     icmp
default-allow-internal  default  INGRESS    65534     tcp:0-65535,udp:0-65535,icmp
default-allow-rdp       default  INGRESS    65534     tcp:3389
default-allow-ssh       default  INGRESS    65534     tcp:22

To show all fields of the firewall, please show in JSON format: --format=json
To show all fields in table format, please see the examples in --help.
```
Chưa có rồi, thêm vào thôi
```
gcloud compute firewall-rules create rule-allow-tcp-80 --source-ranges 0.0.0.0/0 --target-tags allow-tcp-80 --allow tcp:80
```
```
Creating firewall...-Created [https://www.googleapis.com/compute/v1/projects/project-songs/global/firewalls/rule-allow-tcp-80].
Creating firewall...done.                                                                                                     
NAME               NETWORK  DIRECTION  PRIORITY  ALLOW   DENY
rule-allow-tcp-80  default  INGRESS    1000      tcp:80
```
Đã tạo xong, thêm nó vào `instance` nào
```
gcloud compute instances add-tags example-api --tags allow-tcp-80
```

```
No zone specified. Using zone [asia-southeast1-c] for instance: [example-api].
Updated [https://www.googleapis.com/compute/v1/projects/project-songs/zones/asia-southeast1-c/instances/example-api].
```
### 2. Đăng nhập và cài đặt cái gói cần thiết
Đăng nhập vào `instance`
```
gcloud compute ssh [INSTANCE_NAME]
```
```
gcloud compute ssh example-api
```
```
WARNING: The public SSH key file for gcloud does not exist.
WARNING: The private SSH key file for gcloud does not exist.
WARNING: You do not have an SSH key for gcloud.
WARNING: SSH keygen will be executed to generate a key.
Generating public/private rsa key pair.
Enter passphrase (empty for no passphrase): 
```
Do lần đầu đăng nhập chưa có `SSH key` - SDK sẽ tự tạo ra một `key` cho mình. Nhấn `Enter`
```
Enter same passphrase again: 
```
Nhấn `Enter` lần nữa, rồi đợi một tí
```
Your identification has been saved in /Users/kube/.ssh/google_compute_engine.
Your public key has been saved in /Users/kube/.ssh/google_compute_engine.pub.
The key fingerprint is:
SHA256:VIc95umck9XFwT7qpEY14bQM2dGtTJiehPVYUy8rNFw kube@letri.local
The key's randomart image is:
+---[RSA 2048]----+
|          .==+E++|
|         .o=BO.+=|
|        .  =X**oo|
|       .   .=B+=.|
|        S  oo++ .|
|           .*+   |
|          . +.   |
|           o .   |
|          .      |
+----[SHA256]-----+
No zone specified. Using zone [asia-southeast1-c] for instance: [example-api].
Updating project ssh metadata...|Updated [https://www.googleapis.com/compute/v1/projects/project-songs].                      
Updating project ssh metadata...done.                                                                                         
Waiting for SSH key to propagate.
Warning: Permanently added 'compute.6186573008226470554' (ECDSA) to the list of known hosts.
Welcome to Ubuntu 16.04.4 LTS (GNU/Linux 4.13.0-1015-gcp x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage

  Get cloud support with Ubuntu Advantage Cloud Guest:
    http://www.ubuntu.com/business/services/cloud

0 packages can be updated.
0 updates are security updates.


_____________________________________________________________________
WARNING! Your environment specifies an invalid locale.
 The unknown environment variables are:
   LC_CTYPE=UTF-8 LC_ALL=
 This can affect your user experience significantly, including the
 ability to manage packages. You may install the locales by running:

   sudo apt-get install language-pack-UTF-8
     or
   sudo locale-gen UTF-8

To see all available language packs, run:
   apt-cache search "^language-pack-[a-z][a-z]$"
To disable this message for all users, run:
   sudo touch /var/lib/cloud/instance/locale-check.skip
_____________________________________________________________________
```
Ở trên nó `CẢNH BÁO` mình cài đặt ngôn ngữ chưa hợp lệ nên làm thêm bước nữa
```
export LC_ALL="en_US.UTF-8"
```
```
export LC_CTYPE="en_US.UTF-8"
```
```
sudo dpkg-reconfigure locales
```
![locales](images/ftg_locales.png)
Ở bước này chỉ cần nhấn `Enter`, `Enter` và `Enter` thôi
```
Generating locales (this might take a while)...
  en_US.UTF-8... done
Generation complete.
```
Di chuyển vào thư mục `/`
```
cd /
```
Cập nhật và cài đặt thêm các gói (package) cần thiết
```
sudo apt-get update
```
```
sudo apt-get -y install nginx git-core libmysqlclient-dev mysql-server python3-pip python3-venv
```
Khi đang chạy sẽ xuất hiện như hình dưới, bạn cứ gõ mật khẩu mong muốn vào và `Enter`
![mysql_password](images/ftg_mysql_password.png)
Sau khi nhấn `Enter`, sẽ xuất hiện thêm màn hình nhập lại mật khẩu - bạn cứ nhập mật khẩu lúc nãy và nhấn `Enter`
![mysql_repeat_password](images/ftg_mysql_repeat_password.png)

Sau khi đã cài đặt xong, kiểm tra xem đã có python 3 chưa
```
python3 -V
```
```
Python 3.5.2
```
Lúc này bạn đang đứng ở thư mục `/`, nên di chuyển vào thư mục `/opt` 
```
cd opt/
```
Tạo một thư mục tên là `www`
```
sudo mkdir www
```
Di chuyển vào thư mục `www` vừa tạo
```
cd wwww
```
Đã có python 3 tiến hành tạo môi trường ảo cho nó
```
python3 -m venv falcon-env
```
Set quyền cho thư mục `falcon-env`
```
sudo chmod -R 777 falcon-env/
```
Kích hoạt môi trường ảo
```
source falcon-env/bin/activate
```
Nâng cấp `pip` lên phiên bản mới nhất
```
pip install --upgrade pip
```
Clone `repository` của bạn và di chuyển vào thư mục vừa clone về
```
cd `tên_repository`
```
Cài đặt cái lib của python
```
pip install -r requirements.txt
```
Tạo database cho ứng dụng
```sql
mysql -u root -p
```

```sql
mysql> create database example_api;
Query OK, 1 row affected (0.00 sec)
mysql> \q
Bye
```
Trong thư mục vừa clone về đã có database nên chỉ cần import vào
```
mysql -u root -p example_api < example_api.sql
```
Vào kiểm tra lại lần nữa cho chắc
```sql
mysql -u root -p
```
```sql
mysql> use example_api;
Reading table information for completion of table and column names
You can turn off this feature to get a quicker startup with -A
Database changed
mysql> select * from songs;
+--------+-------------------------+--------------+----------------------+
| id | song_name                | category     | singer               |
+--------+-------------------------+--------------+----------------------+
|      1 | Đừng Như Thói Quen      | Nhạc trẻ     | JayKii; Sara Lưu     |
|      2 | Tâm Sự Tuổi 30          | Nhạc trẻ     | Trịnh Thăng Bình     |
|      3 | Chạm Đáy Nỗi Đau        | Nhạc trẻ     | Erik                 |
|      4 | Hey Brother             | Electronica  | Avicii               |
|      5 | Wake me up              | Electronica  | Avicii               |
+--------+-------------------------+--------------+----------------------+
5 rows in set (0.01 sec)
mysql> \q
Bye
```
Mở file `app.py` sửa lại thông số
```
nano app.py
```
Chỉ cần thay đổi thông số của `passwd` và `db`
```python
db = MySQLdb.connect(host='127.0.0.1',
                     user='root',
                     passwd='password của bạn',
                     db='example_api',
                     use_unicode=True,
                     charset="utf8")
```
Bấm `Control + X` sau đó `shift + Y` rồi `Enter` để lưu lại.
Chạy thử app
```
gunicorn app:api
```
```
[2018-05-05 16:29:12 +0000] [19408] [INFO] Starting gunicorn 19.8.1
[2018-05-05 16:29:12 +0000] [19408] [INFO] Listening at: http://127.0.0.1:8000 (19408)
[2018-05-05 16:29:12 +0000] [19408] [INFO] Using worker: sync
[2018-05-05 16:29:12 +0000] [19411] [INFO] Booting worker with pid: 19411
```
Vậy là không có lỗi gì xảy ra, mở thêm một tab của terminal (OSX: Command + T)
```
gcloud compute instances list
```
```
NAME         ZONE               MACHINE_TYPE   PREEMPTIBLE  INTERNAL_IP  EXTERNAL_IP     STATUS
example-api  asia-southeast1-c  n1-standard-1               10.148.0.2   35.198.235.193  RUNNING
```
Mở trình duyệt web lên và nhập `EXTERNAL_IP` ở trên vào
![first_view.png](images/ftg_first_view.png)
`Compute Engine` đã chạy, thử vào app của mình xem
```
35.198.235.193/things
```
![things_not_found](images/ftg_things_not_found.png)
```
35.198.235.193/songs
```
![songs_not_found](images/ftg_songs_not_found.png)
Rõ ràng là app đã chạy rồi nhưng sao lại báo không tìm thấy? Không sao đâu do mình chưa config đó mà một vài bước nữa sẽ xong thôi.  
Tắt app đang chạy (`Control + C`).  
### 3. Cấu hình nginx
Giờ mình bắt đầu vào config `nginx` thôi. Mình không phải dân chuyên về `network` nên mình hiểu nôm na `nginx` là một web server.  
Let's do it. Đầu tiên tạo mới một file bạn có thể thay thế `example-api` nếu muốn.
```
sudo nano /etc/nginx/sites-available/example-api
```
Chép cái đống này vào và chỗ `server_name` thay thế bằng `External IP`
```dns
server {
    listen       80;
    server_name  35.198.235.193;
    location / {
        proxy_pass http://127.0.0.1:8000;
    }
}
```
`Control + X` và `Shift Y` rồi nhấn `Enter` để lưu lại.  
Sau đó chạy thêm lệnh này, bạn muốn hiểu thêm về lệnh của linux thì vào [đây](https://explainshell.com/) 
```
sudo ln -s /etc/nginx/sites-available/example-api /etc/nginx/sites-enabled/
```
Kiểm tra xem file config `nginx` mình vừa tạo có lỗi cú pháp nào không
```
sudo nginx -t
```
Nếu không có lỗi thì sẽ hiển thị như này
```
nginx: the configuration file /etc/nginx/nginx.conf syntax is ok
nginx: configuration file /etc/nginx/nginx.conf test is successful
```
Khởi động lại `nginx` thôi nào
```
sudo systemctl restart nginx
```
Mọi thứ đã xong, à mà chưa xong đâu bạn phải chạy lại app của mình
```
gunicorn app:api
```
Kiểm tra xem nào, gõ `External IP` lên trình duyệt web
![no_route](images/ftg_no_route.png)
Khi truy cập vào `External IP` sẽ có thông báo không tìm thấy page. Để giải quyết vấn đề này thì bạn có thể config lại file `nginx` hoặc có thể dùng hàm `handle_404` (`falcon` có hỗ trợ). 
Vào tiếp thằng `/things` xem nào
```
35.198.235.193/things
```
![things_ok](images/ftg_things_ok.png)
Ổn rồi, vào thằng `/songs` xem
```
35.198.235.193/songs
```
![songs_ok](images/ftg_songs_ok.png)
Đến đây có thể được coi là xong nhưng chưa hoàn chỉnh vì khi server của mình khởi động lại thì app cũng sẽ bị tắt đi. Để giải quyết được vấn đề trên giải pháp được đưa ra là sử dụng `systemd`.
### Bonus: cấu hình systemd
Như đã nói ở trên, mình không phải chuyên về mảng `network` nên mình chỉ bắt tay vào làm thôi...còn bạn muốn tìm hiểu thêm thì có thể coi ở đây ["Systemd là gì"](https://techtalk.vn/blog/posts/systemd-la-gi)
Bắt đầu nào, di chuyển vào thư mục `/etc/systemd/system`
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
