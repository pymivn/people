Title: Có Salt không lo chết đói
Date: 2021-06-19
Category: Trang chủ
Tags: saltstack, salt, deploy, devops, ansible, sysadmin
Slug: salt
Authors: hvnsweeting
Summary: Tự động hóa cài đặt, cấu hình (deploy) với SaltStack


## Salt là gì

SaltStack (từ đây gọi tắt là Salt) là một phần mềm mã nguồn mở, một hệ thống
thuộc nhóm Configuration management, viết bằng Python, sử dụng YAML làm ngôn
ngữ giao tiếp với người dùng.

## Salt làm gì?
Tính năng của Salt chia làm 2 phần chính: remote execution và configuration
management dựa trên nền tảng remote execution.

### Remote execution
chạy lệnh từ xa. Tức sau khi cài đặt xong salt-master (daemon đóng vai trò
server) và các salt-minion (các daemon đóng vai tròn client), từ
salt-master có thể chạy bất kì câu lệnh nào trên máy cài salt-minion.

Tưởng tượng bạn cần xoá 1 file trên 10 hay 100 máy, chỉ cần gõ 1 câu lệnh và
tất cả các minion sẽ chạy câu lệnh ấy. Sức mạnh là vô cùng khủng khiếp, giống
như nắm một mạng botnet trong tay vậy. Muốn ping 1 server từ 100 máy? gõ lệnh
``ping -c N victim``, và 100 máy sẽ cùng lúc ping đến máy đích.

### Configuration management
đảm bảo trạng thái các thành phần của hệ thống. Cần đảm bảo 1 service NGINX
chạy với file cấu hình nhất định, forward request đến gunicorn app
server trên máy ấy, đã cấu hình để chạy một web application viết bằng Python
với phiên bản mới nhất lấy từ 1 git repository? Salt làm được tất cả điều đó,
và nó có thể đảm bảo rằng mọi thay đổi bằng tay thực hiện trên những thành
phần nói trên sẽ bị thay thế bằng những gì đã định trước.

Theo [Chào Muối, em là ai? ](https://www.familug.org/2015/06/saltstack-chao-muoi-em-la-ai.html)

## Mục tiêu
Bài này cài đặt salt qua `pip`, và dùng `salt-ssh` để điều khiển máy khác.
Mục tiêu đưa ra một bài hướng dẫn thực hành đơn giản hơn bài hướng dẫn trên
trang chủ [Salt in 10 minutes](https://docs.saltproject.io/en/master/topics/tutorials/walkthrough.html#salt-in-10-minutes/)
và mang lại cảm giác giống đang dùng [Ansible](https://www.familug.org/2016/12/ansible-command.html).

Kết quả: deploy uds bot - 1 chương trình Python lên máy Ubuntu 18.04, cấu hình
systemd chạy vù vù.


## 3 phút dành cho lý thuyết
- Máy ra lệnh gọi là salt master
- Máy bị điều khiển, chạy các câu lệnh gọi là salt minion, trong bài này có IP `192.168.0.110`
- Trong bài này, master sẽ truy cập vào minion qua ssh.
- Máy master không cần quyền gì đặc biệt và đã cài đặt salt trên Python3.6+
- Máy minion chạy `*NIX` OS (Ubuntu, Debian, Fedora, .. MacOS),
  phải có quyền sudo không password hoặc root để toàn quyền điều khiển máy (như cài package qua
apt). [Salt có hỗ trợ Windows](https://docs.saltproject.io/en/latest/topics/installation/windows.html) nhưng nằm ngoài phạm vi bài viết này.

## Trên máy minion
- Tạo 1 user mới: `sudo adduser saltuser`, trả lời các câu hỏi và gõ password
- Sudo không password: them `saltuser ALL=(ALL) NOPASSWD: ALL` vào cuối file /etc/sudoers

## Trên máy master
Copy ssh pub key vào minion:

```sh
ssh-copy-id saltuser@192.168.0.110
# rồi gõ password saltuser vừa tạo
```

### Cài đặt
Tạo 1 virtualenv:

```sh
python3 -m venv saltenv
. saltenv/bin/activate
pip install salt==3002  # do bản 3003 mới nhất đang có bug
```
Cài xong kiểm tra
```sh
$ salt-ssh --version
salt-ssh 3002
```

### Cấu hình master
Có 2 file cần tạo: `master` và `roster`

Tạo 1 thư mục tên saltlab:

```sh
mkdir -p ~/saltlab/base
cd ~/saltlab
pwd
```

File `master` chứa 2 dòng, `root_dir` giá trị là đường dẫn đầy đủ tới
thư muc saltlab, `file_roots` có `base` với giá trị là đường dẫn đầy đủ
tới thư mục `base`, thư mục base sẽ chứa các file "saltstate"


```yaml
root_dir: /home/hvn/saltlab
file_roots:
  base:
    - /home/hvn/saltlab/base
```

File `roster` chứa thông tin về các máy minion:

```yaml
tv:
  host: 192.168.0.110
  user: saltuser
  sudo: True
trau:
  host: 103.x.y.z
  user: root
  port: 22022
```

ở đây định nghĩa 2 minion, 1 tên tv và 1 tên `trau`, minion `tv` sẽ là đối
tượng của bài này.

```
saltlab/
├── master
├── pillars
├── roster
└── states
    ├── template.j2
    └── uds.sls
```

File này tương tự file inventory (hay có tên là `hosts`) của Ansible.


## Chạy câu lệnh Salt
Từ master, trong venv saltenv, gõ lệnh `salt-ssh` với đối tượng `tv`, câu lệnh
salt `cmd.run`, câu lệnh chạy trên `tv` là `uname -a`:

```sh
(saltenv) $ salt-ssh --config ~/saltlab tv cmd.run 'uname -a'
tv:
    Linux MINIPC-PN50 5.8.0-55-generic #62~20.04.1-Ubuntu SMP Wed Jun 2 08:55:04 UTC 2021 x86_64 x86_64 x86_64 GNU/Linux
```

## Apply Salt state
Saltstate file là [file YAML](https://docs.saltproject.io/en/latest/topics/yaml/index.html) có đuôi `.sls`, chứa các định nghĩa (declare) về
trạng thái của hệ thống mong muốn đạt được.

```yaml
install htop:   #  ID của "state"
  pkg.installed:  # loại state - tương ứng với 1 python function
    - name: htop   # các tham số - function argument
```

Cú pháp YAML trên tương ứng với Python dict sau:

```py
{'install htop':
  {'pkg.installed': [{'name': 'htop'}]}}
```

Sau khi được `apply`, state trên sẽ cài package `htop` lên máy, sử dụng package
manager của máy minion, dù là apt trên Ubuntu hay yum/dnf trên Fedora.

Đây là một ưu điểm lớn của Salt, người dùng thậm chí không biết chính xác
câu lệnh để cài thế nào, chỉ cần liệt kê ra những gì mình cần, Salt sẽ lo tất.
Phần này nghe rất "magic", thực chất thì bên dưới pkg là 1 [Python module](https://github.com/saltstack/salt/blob/master/salt/states/pkg.py)
còn [`installed` là 1 function](https://github.com/saltstack/salt/blob/v3003/salt/states/pkg.py#L1007)
chạy đủ loại if/else kiểm tra hệ thống và chọn `apt` hay `yum` cho phù hợp.
Salt gọi đây là `state module pkg`(https://docs.saltproject.io/en/latest/ref/states/all/index.html)

Gõ trên master:

```sh
$ salt-ssh --config ~/saltlab tv state.apply htop
tv:
----------
          ID: install htop
    Function: pkg.installed
        Name: htop
      Result: True
     Comment: The following packages were installed/updated: htop
     Started: 15:09:22.550836
    Duration: 10969.17 ms
     Changes:
              ----------
              htop:
                  ----------
                  new:
                      2.2.0-2build1
                  old:

Summary for tv
------------
Succeeded: 1 (changed=1)
Failed:    0
------------
Total states run:     1
```

Xem đầy đủ các option, các function khác của `pkg state module` tại
[https://docs.saltproject.io/en/latest/ref/states/all/salt.states.pkg.html#module-salt.states.pkg](https://docs.saltproject.io/en/latest/ref/states/all/salt.states.pkg.html#module-salt.states.pkg)

### Copy/render file và chạy câu lệnh

```yaml
render a config file:
  file.managed:
    - source: salt://template.j2
    - template: jinja
    - mode: 0400
    - name: /tmp/ahihi.yml

now run a command:
  cmd.run:
    - name: cat /tmp/ahihi.yml | head
```

`cmd.run` dùng để chạy 1 câu lệnh trên minion, lệnh tùy ý. Với `cmd.run`,
ta đã có thể làm được mọi thứ, đây là cách đơn giản nhất để thay thế các
bash script mặc dù không phải tối ưu nhất. Ví dụ: nếu chạy apt-get install để
cài package thay vì pkg.installed sẽ mất đi các lợi ích pkg.installed thực hiện
- chạy trên nhiều OS khác nhau, tự động chạy apt update).
Người mới tập dùng Salt có thể dùng `cmd.run` để bắt đầu, nhưng nên tìm state
module có sẵn để thu được kết quả tốt hơn.

`file.managed` có thể tải 1 file từ internet, có thể copy 1 file từ X đến Y,
trong ví dụ này nó copy file từ salt://template.j2 tới minion rồi render với
[Jinja2 template](https://docs.saltproject.io/en/getstarted/config/jinja.html),
ghi vào `/tmp/ahihi.yml` và chmod 0400.

`salt://` trong ví dụ này là `file_roots` trong file cấu hình master, tức thư
mục `/home/hvn/saltlab/base`.

Nội dung file template.j2:

```jinja2
{%- for i in ['meo', 'bo', 'ga'] %}
  - {{ i }}
{%- endfor %}

myuser: user
mypassword: passwd

os: {{ grains['osfinger'] }}
ips: {{ grains['ipv4'] }}
```

Jinja2 có for if/else như Python, xem link hoặc học Flask để tìm hiểu thêm.

### 1 phút dành cho lý thuyết: grains pillar
1 nhược điểm của Salt là theo mốt thời 2010, đặt tên cho mọi khái niệm, và tên
đó không thực sự có nhiều ý nghĩa - đơn giản chỉ là bịa ra (theo mốt của
[Chef](https://www.chef.io/) - một đối thủ viết bằng Ruby).

Salt có 2 khái niệm:

- grains: chứa các thông tin về máy minion (OS, version, ip, ...)
- pillar: chứa các thông tin truyền từ master (thường là các thông tin bí mật như
  user/password).

#### salt  grains
Ví dụ trên có truy cập 2 thông tin từ grains là tên hệ điều hành và các IPv4 của
máy minion. state.apply

```yaml
          ID: render a config file
    Function: file.managed
        Name: /tmp/ahihi.yml
      Result: True
     Comment: File /tmp/ahihi.yml is in the correct state
     Started: 15:37:34.775460
    Duration: 46.881 ms
     Changes:
----------
          ID: now run a command
    Function: cmd.run
        Name: cat /tmp/ahihi.yml
      Result: True
     Comment: Command "cat /tmp/ahihi.yml" run
     Started: 15:37:34.824872
    Duration: 7.323 ms
     Changes:
              ----------
              pid:
                  37968
              retcode:
                  0
              stderr:
              stdout:

                    - meo
                    - bo
                    - ga

                  myuser: user
                  mypassword: passwd

                  os: Ubuntu-20.04
                  ips: ['127.0.0.1', '192.168.0.110']
```

Để liệt kê tất cả grains của minion, dùng Salt command `grains.items`

```
$ salt-ssh -c ~/saltlab tv grains.items
tv:
    ----------
    biosreleasedate:
        08/27/2020
    biosversion:
        0416
    cpu_flags:
    ...
```

#### salt pillar
Pillar chỉ nằm trên master, nên nó phân cấu trúc thư mục và map file nào
dành cho minion nào. File `top.sls`

```
base:
  '*':
    - common
  'trau':
    - uds
```

`*` tức mọi minion đều có thể truy cập các pillar item trong file `common.sls`,
chỉ `trau` mới truy cập được nội dung trong file `uds.sls`.

Các file pillar là các file `.sls` theo syntax YAML, biểu diễn các dictionary
của Python. Ví dụ: `uds.sls`:

```yaml
telegram_token: this_is_token

database:
  username: root
  password: toor
```

Để liệt kê tất cả pillar item dành cho minion, dùng Salt command `pillar.items`
(chú ý grains có s, pillar không có).

```sh
$ salt-ssh -c ~/saltlab trau pillar.items
tv:
    ----------
    database:
        ----------
        password:
            toor
        username:
            root
    telegram_token:
        this_is_token
```

Ví dụ 1 file dùng pillar:

```yaml
# /lib/systemd/system/uds.service
[Unit]
Description=UDS telegram bot

[Service]
User=uds
Environment=BOT_TOKEN={{ pillar['telegram_token'] }}
```

### Deploy 1 Python project
Link này viết 1 salt formula (tên của 1 "bộ cài bằng Salt") để cài
bot telegram `uds` chạy trên Ubuntu 18.04 với systemd.
#### TODO link here.

### Troubleshooting
Khi kêt quả chạy apply không thành công, thêm `-ldebug` để xem log chi tiết.

## Dùng Ansible "xịn hơn" không?
Không, Ansible giống Salt đến bất ngờ, cũng viết bằng Python với các module
tương ứng, cũng dùng Jinja2, cũng viết cấu hình bằng file YAML với Jinja2.

Ngày nay, Ansible phổ biến hơn nhờ nó có vẻ đơn giản hơn để bắt đầu, do ít
từ khóa hay khái niệm lạ. Năm 2015, RedHat mua lại Ansible khiến cho nó
càng trở nên phổ biến hơn.

Salt thành công trước Ansible (2012 2013), đứng sau là công ty SaltStack, đến
năm 2020 cũng được ông lớn [VMWare
mua lại](https://www.vmware.com/support/acquisitions/saltstack.html). Salt có
nhiều ưu điểm so với Ansible, cũng cấp nhiều tính năng phức tạp - dùng trong
môi trường phức tạp.

Dùng Salt chuyển sang Ansible mất nửa ngày để map lại khái niệm.

## Kết luận

## References
- [salt-ssh](https://docs.saltproject.io/en/latest/topics/ssh/)
- https://github.com/saltstack/salt/issues/59942


### Ủng hộ tác giả
HVN at [http://pymi.vn](http://pymi.vn) and [https://www.familug.org](https://www.familug.org).

- [Ủng hộ tác giả 🍺](https://www.familug.org/p/ung-ho.html)
