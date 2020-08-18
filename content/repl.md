Title: Viết code dễ đổi, dễ test như thế nào?
Date: 2020-08-17
Category: Trang chủ
Tags: python, best-practice
Slug: repl
Authors: hvnsweeting
Summary: Tận dụng tối đa REPL của Python, tính năng mà C, Java, Golang không có

Các lập trình viên chuyển sang code Python từ các ngôn ngữ lập trình khác như
Java, C, Golang... thường bắt đầu code bằng việc bật một cái IDE to đùng
(PyCharm) lên,
rồi viết chục dòng code, sau đó bấm nút "tam giác" để chạy từ trên xuống dưới.
Đó là cách làm phổ biến, tiêu chuẩn khi viết code C, Java, Golang... nhưng là
một cách làm rất không ... Python.

Khi học Python, việc đầu tiên ta làm là bật `python` từ terminal, rồi gõ trực
tiếp các dòng code vào đó, enter để thấy kết quả:

```python
$ python3
Python 3.6.9 (default, Apr 18 2020, 01:56:04)
[GCC 8.4.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> str(21 * 2) + " is the answer of life."
'42 is the answer of life.'
```

Còn khi đi làm, viết code Python? Cũng vậy!

Khả năng gõ code trực tiếp, enter thấy ngay kết quả như trên, là một tính năng
cực kỳ hấp dẫn/quan trọng của Python cũng như các ngôn ngữ lập trình có `REPL`
như Ruby, Clojure, JavaScript, LISP, Ocaml, Elixir, F#... nó cho phép người
dùng khám phá,
vui chơi thoải mái với dữ liệu một cách tương tác, thấy kết quả nhanh nhất, thay
vì phải ngồi tưởng tượng, đoán, chờ compile,
và dựa vào IDE trợ giúp như các ngôn ngữ không có REPL.

![xkcd303](https://imgs.xkcd.com/comics/compiling.png)

Đây là chế độ ["interactive mode"](https://docs.python.org/3/tutorial/interpreter.html)
của Python interpreter, khái niệm này có cái tên khác chung hơn là: REPL.

(Chú ý: Golang có các project như [`gore`](https://github.com/motemen/gore) hay
 `yaegi` nhưng đều rất hạn chế so với REPL của các ngôn ngữ kể trên).

## REPL
REPL - Read Eval Print Loop, là môi trường nhận đầu vào từ người dùng (`Read`),
chạy input đó (`Eval`), in kết quả ra màn hình (`Print`), và cứ tiếp tục vậy
(`Loop`).

Khái niệm này bắt nguồn từ ngôn ngữ lập trình cổ thứ 2 thế giới: [LISP](https://pp.pymi.vn/article/scm1/).

Việc viết code khi dùng các ngôn ngữ có REPL thường theo các bước:

- bật REPL lên
- gõ code thử cho tới khi thu được kết quả mong muốn
- copy code đó vào editor/IDE

## Ví dụ
Đoạn code Python 3 sau sẽ truy cập API của GitHub, lấy các repo của Pymivn về,
lọc ra các repo có > 0 star, sắp xếp giảm dần theo số star,
rồi in ra output ở dạng dễ đọc.

```python
# githubstars.py
from urllib.request import urlopen
import json


def main():
    with urlopen("https://api.github.com/users/pymivn/repos") as f:
        repos = json.load(f)

    has_stars = []
    for repo in repos:
        if repo["stargazers_count"] > 0:
            has_stars.append((
                repo["stargazers_count"], repo["html_url"]
                ))

    has_stars.sort(reverse=True)
    for stars, url in has_stars:
        output = "{} - {}".format(stars, url)
        print(output)


if __name__ == "__main__":
    main()
```

Nếu viết theo kiểu này, rồi cho vào IDE, bấm nút tam giác để chạy, những nhược
điểm sau sẽ xuất hiện:

- Mỗi lần chạy, code sẽ truy cập vào API GitHub 1 lần, việc này ngoài chậm,
phụ thuộc vào mạng internet mỗi lần chạy,
còn thêm nhược điểm nữa là sẽ dùng tốn "quota" hàng ngày của bạn (VD GitHub chỉ
cho phép gọi API n lần 1 ngày).
- Trừ khi bạn code 1 lần chuẩn luôn, còn không thì mất khoảng 5 7 lần mới ra
đoạn code trên.
- Không test từng phần (bước) của đoạn code được.

Thay vì vậy, viết lại một phần code như sau

```python
from urllib.request import urlopen
import json

def getrepos():
    with urlopen("https://api.github.com/users/pymivn/repos") as f:
        repos = json.load(f)
    return repos

def main():
    pass
```
Lưu vào file `github.py`, rồi vào terminal, bật `python3` lên, gõ:

```python
>>> import github
>>> repos = github.getrepos()
>>> type(repos), len(repos)
(<class 'list'>, 23)
>>> one = repos[0]
>>> one.keys()
dict_keys(['id', 'node_id', 'name', 'full_name', 'private', 'owner', 'html_url', 'description', 'fork', 'url', 'forks_url', 'keys_url', 'collaborators_url', 'teams_url', 'hooks_url', 'issue_events_url', 'events_url', 'assignees_url', 'branches_url', 'tags_url', 'blobs_url', 'git_tags_url', 'git_refs_url', 'trees_url', 'statuses_url', 'languages_url', 'stargazers_url', 'contributors_url', 'subscribers_url', 'subscription_url', 'commits_url', 'git_commits_url', 'comments_url', 'issue_comment_url', 'contents_url', 'compare_url', 'merges_url', 'archive_url', 'downloads_url', 'issues_url', 'pulls_url', 'milestones_url', 'notifications_url', 'labels_url', 'releases_url', 'deployments_url', 'created_at', 'updated_at', 'pushed_at', 'git_url', 'ssh_url', 'clone_url', 'svn_url', 'homepage', 'size', 'stargazers_count', 'watchers_count', 'language', 'has_issues', 'has_projects', 'has_downloads', 'has_wiki', 'has_pages', 'forks_count', 'mirror_url', 'archived', 'disabled', 'open_issues_count', 'license', 'forks', 'open_issues', 'watchers', 'default_branch'])
>>> one['stargazers_count']
0
>>> has_stars = [p for p in repos if p['stargazers_count'] > 0]
>>> len(has_stars)
8
>>> stars_urls = [(p['stargazers_count'], p['html_url']) for p in has_stars]
>>> stars_urls
[(7, 'https://github.com/pymivn/awesome'), (2, 'https://github.com/pymivn/cpuisfast'), (1, 'https://github.com/pymivn/hoidap-python'), (1, 'https://github.com/pymivn/lekhome'), (4, 'https://github.com/pymivn/math-stats-ml'), (3, 'https://github.com/pymivn/people'), (1, 'https://github.com/pymivn/pyjobs_crawlers'), (4, 'https://github.com/pymivn/Python_Hanoi_Meetup')]
>>> stars_urls.sort(reverse=True)
>>> fmt = "{} - {}"
>>> for i in stars_urls:
...     print(fmt.format(*i))
...
7 - https://github.com/pymivn/awesome
4 - https://github.com/pymivn/math-stats-ml
4 - https://github.com/pymivn/Python_Hanoi_Meetup
3 - https://github.com/pymivn/people
2 - https://github.com/pymivn/cpuisfast
1 - https://github.com/pymivn/pyjobs_crawlers
1 - https://github.com/pymivn/lekhome
1 - https://github.com/pymivn/hoidap-python
```

Với cách làm này, chỉ cần gọi GitHub API duy nhất 1 lần, còn sau đó thử
thoải mái cho đến khi thu được kết quả mong muốn thì copy vào file cuối cùng:

```python
import json
from urllib.request import urlopen


def getrepos():
    with urlopen("https://api.github.com/users/pymivn/repos") as f:
        repos = json.load(f)
    return repos


def has_stars(repo):
    return repo["stargazers_count"] > 0


def filter_repos_have_stars(repos):
    return [p for p in repos if has_stars(p)]


def get_star_url(p):
    return (p["stargazers_count"], p["html_url"])


def main():
    repos = getrepos()
    repos_have_stars = filter_repos_have_stars(repos)
    stars_urls = [get_star_url(p) for p in repos_have_stars]
    stars_urls.sort(reverse=True)
    fmt = "{} - {}"
    for i in stars_urls:
        print(fmt.format(*i))


if __name__ == "__main__":
    main()
```

Sau này nếu code có bug, lại bật REPL lên, gọi các function để debug trực tiếp
dễ dàng, từng bước một.

```python
$ ipython
Python 3.6.9 (default, Jul 17 2020, 12:50:27)
Type 'copyright', 'credits' or 'license' for more information
IPython 7.9.0 -- An enhanced Interactive Python. Type '?' for help.

In [1]: import github
In [2]: repos = github.getrepos()

In [3]: have_stars = github.filter_repos_have_stars(repos)

In [4]: len(have_stars)
Out[4]: 8

In [5]: [github.get_star_url(p) for p in have_stars]
Out[5]:
[(7, 'https://github.com/pymivn/awesome'),
 (2, 'https://github.com/pymivn/cpuisfast'),
 (1, 'https://github.com/pymivn/hoidap-python'),
 (1, 'https://github.com/pymivn/lekhome'),
 (4, 'https://github.com/pymivn/math-stats-ml'),
 (3, 'https://github.com/pymivn/people'),
 (1, 'https://github.com/pymivn/pyjobs_crawlers'),
 (4, 'https://github.com/pymivn/Python_Hanoi_Meetup')]

In [8]: sorted([github.get_star_url(p) for p in have_stars], reverse=True)

Out[8]:
[(7, 'https://github.com/pymivn/awesome'),
 (4, 'https://github.com/pymivn/math-stats-ml'),
 (4, 'https://github.com/pymivn/Python_Hanoi_Meetup'),
 (3, 'https://github.com/pymivn/people'),
 (2, 'https://github.com/pymivn/cpuisfast'),
 (1, 'https://github.com/pymivn/pyjobs_crawlers'),
 (1, 'https://github.com/pymivn/lekhome'),
 (1, 'https://github.com/pymivn/hoidap-python')]
```


## Dev với IPython
IPython (`pip install ipython`) cung cấp thêm các tính năng giúp cách code này
hiệu quả hơn.

IPython có màu mè, auto-indent tự thụt sau for/if giúp gõ nhanh hơn.

Magic command `%hist` sẽ hiện full history những gì user đã gõ, giúp copy code
để paste ra IDE/Editor dễ hơn, không bao gồm output.

Magic command `%edit` sẽ mở hẳn editor ra để sửa code, sau khi đóng lại, code
sẽ được chạy, các biến sẽ tồn tại trong môi trường đang code.

Ví dụ này gõ `%edit` lần đầu định nghĩa list `ns`, rồi gõ `%edit` lần 2 để
print ra list ns định nghĩa trước đó:

```python
$ ipython
Python 3.6.9 (default, Apr 18 2020, 01:56:04)
Type 'copyright', 'credits' or 'license' for more information
IPython 7.9.0 -- An enhanced Interactive Python. Type '?' for help.

In [1]: %edit
IPython will make a temporary file named: /tmp/ipython_edit_2v90rimj/ipython_edit_wf_rn_nc.py
Editing... done. Executing edited code...
Out[1]: '\nns = [1,2,3,4]\n'

In [2]: ns
Out[2]: [1, 2, 3, 4]

In [3]: %edit
IPython will make a temporary file named: /tmp/ipython_edit_qb43pml6/ipython_edit_tph7_5x6.py
Editing... done. Executing edited code...
[1, 2, 3, 4]
Out[3]: 'print(ns)\n'
```

### Đổi editor
ra shell, gõ `echo $EDITOR` xem đang đặt
là gì, thay bằng câu lệnh mở editor mình muốn, ví dụ
```sh
$ export EDITOR=nano
$ ipython
```

### Chạy file rồi bật REPL
Python hay IPython đều hỗ trợ [option
`-i`](https://pp.pymi.vn/article/pythoni/), sau khi chạy với 1 file code
sẽ tự động vào chế độ interactive mode

## Jupyter
Code trên Jupyter (`pip install jupyter`) cũng cho khả năng linh hoạt tương tự.
Code xong File > Save As Python file.

## Unittest
Trong các ngôn ngữ không có REPL, cách thử 1 đoạn code nhanh nhất là viết
1 function cần thử, rồi viết unittest, rồi chạy test thay vì chạy cả 1 chương
trình ngàn dòng.
Với Python, ta chỉ cần bật REPL lên, import module vào và khám phá.

Code viết theo mới trên vừa dễ gõ trực tiếp trong REPL, vừa dễ viết unittest,
ví dụ viết nhanh unittest chạy bằng `pytest` (`pip install pytest`) như sau:

```python
# test_github.py
import github


def test():
    bad = {"stargazers_count": 0, "html_url": "bad_repo"}
    good = {
        "stargazers_count": 69,
        "html_url": "https://github.com/pymivn/awesome",
        "blah": "blo",
    }
    sample_repos = [bad, good]
    assert github.filter_repos_have_stars(sample_repos) == [good]
    assert github.get_star_url(good) == (
        good["stargazers_count"],
        good["html_url"],
    )
    assert github.has_stars(bad) is False
    assert github.has_stars(good) is True
```

Viết code bằng REPL hay bằng [unittest
TDD](https://en.wikipedia.org/wiki/Test-driven_development) đều mang tới một
kết quả chung: code dễ sửa, dễ test.

Tất nhiên REPL không thay thế hoàn toàn cho unittest, nhưng nó mang lại môi
trường thử nghiệm nhanh chóng <del>tương đương như</del> hơn nhiều unittest ở
các ngôn ngữ khác.

## Hành động của chúng ta
Cài ngay IPython, Jupyter rồi bật lên mỗi khi muốn code Python.

## Kết luận
Đừng đọc tiếng Anh theo kiểu Tiếng Việt, đừng code Python theo kiểu Java.
REPL là một phát minh có sức mạnh khủng khiếp mà các Pythonista nên vận dụng,
sử dụng, và lạm dụng hết mình.
