Title: Đọc code chương trình pycodestyle, pep8
Date: 2024-04-25
Category: Trang chủ
Tags: python, architecture, codewalk
Slug: pep8
Authors: hvnsweeting
Summary: Tham khảo thiết kế, cách tổ chức code của chương trình kiểm tra PEP8

[PEP8](https://peps.python.org/pep-0008/) là tài liệu hướng dẫn style coding cho code Python, viết bởi tác giả của Python Guido van Rossum từ năm 2001 (23 năm trước!).

Code Python từ đó đều luôn tuân theo chuẩn PEP8, được gọi là "PEP8 compliant".
Nhưng tài liệu PEP8 rất dài, có hàng chục mục khác nhau, vì vậy [năm 2006, Johann C. Rocholl](https://github.com/PyCQA/pycodestyle/blob/2.11.1/LICENSE#L1) đã viết ra chương trình tên là `pep8` để kiểm tra PEP8 tự động.
Chương trình này, hiển nhiên, trở nên vô cùng phổ biến và được chạy trong hầu hết các hệ thống CI kiểm tra code Python.

Để cài đặt, gõ `pip install pep8`.

Năm [2016, Guido đề nghị đổi tên chương trình `pep8`](https://github.com/PyCQA/pycodestyle/issues/466), từ đó nó có tên mới là `pycodestyle`.

Bài viết này tham khảo kiến trúc, thiết kế của chương trình pycodestyle, sau hàng chục năm dùng mà chưa 1 lần đọc code.
### Tải code về máy
Dùng `git clone` tải bản mới nhất hiện tại (`2.11.1`) về máy.

```
$ git clone https://github.com/PyCQA/pycodestyle/ --branch 2.11.1 --single-branch
Cloning into 'pycodestyle'...
remote: Enumerating objects: 5413, done.
remote: Counting objects: 100% (794/794), done.
remote: Compressing objects: 100% (375/375), done.
remote: Total 5413 (delta 453), reused 689 (delta 393), pack-reused 4619
Receiving objects: 100% (5413/5413), 1.72 MiB | 3.11 MiB/s, done.
Resolving deltas: 100% (3369/3369), done.
Note: switching to 'cefd59cf8e8a199a978da491e75a37fe4d37de82'.
...
```

### Cấu trúc chương trình
File `setup.py` để hỗ trợ việc cài đặt qua pip

```
from setuptools import setup
setup()
```

chương trình `pycodestyle` nằm gọn trong 1 file `pycodestyle.py`, dài 2655 dòng.
```
$ cd pycodestyle
$ wc -l *.py
 2655 pycodestyle.py
    2 setup.py
 2657 total
```

Một chương trình hơn 1000 dòng nằm gọn trong 1 file không phải chuyện **thường thấy**, các project thường sẽ chia nhỏ ra các file chứa code làm nhiệm vụ khác nhau.

`pycodestyle` không phải chương trình **bình thường**. Nó có tính năng ổn định, ít thay đổi (chỉ khi Python ra bản mới giới thiệu các cú pháp mới như `async/await`, `:=` hay `switch`, ...), cần dễ dàng distribute, thậm chí không cần dùng tới pip, chỉ cần copy file `pycodestyle.py` là chạy được, nó không có dependencies nào khác ngoài các standard library.

### Kiến trúc phần mềm
Mô tả ngắn gọn, `pycodestyle` làm những việc sau:

1. đọc config file, options từ dòng lệnh
2. chạy các check với các file đầu vào
3. in ra màn hình kết quả


#### Kiến trúc class, function

Để thực hiện bước 2, các chương trình sẽ thường cần chứa danh sách các check (có đầu vào khác nhau), rồi chạy lần lượt từng check cho từng file.

Các ngôn ngữ lập trình hướng đối tượng OOP sẽ thường tạo class và dùng inheritance (kế thừa):

```py
class BaseCheck():
    def check(self, arg1, arg2):
        pass

class Check1(BaseCheck):
    def check(...)
        pass

class Check2(BaseCheck):
    def check(...)
        pass
```

`pycodestyle` không dùng class để làm việc này mà dùng các function.
Bỏ qua các function nhận input `_line` (các check), ta có các function và class của chương trình:

```py
$ grep -E '^def |^class ' pycodestyle.py | grep -v _line
def _get_parameters(function):
def register_check(check, codes=None):
def module_imports_on_top_of_file(
def _is_binary_operator(token_type, text):
def _break_around_binary_operators(tokens):
def readlines(filename):
def stdin_get_value():
def expand_indent(line):
def mute_string(text):
def parse_udiff(diff, patterns=None, parent='.'):
def normalize_paths(value, parent=os.curdir):
def filename_match(filename, patterns, default=True):
def update_counts(s, counts):
def _is_eol_token(token):
class Checker:
class BaseReport:
class FileReport(BaseReport):
class StandardReport(BaseReport):
class DiffReport(StandardReport):
class StyleGuide:
def get_parser(prog='pycodestyle', version=__version__):
def read_config(options, args, arglist, parser):
def process_options(arglist=None, parse_argv=False, config_file=None,
def _parse_multi_options(options, split_token=','):
def _main():
```

Chương trình chạy bằng cách gọi function `_main()`:

```py
$ tail -n2 pycodestyle.py
if __name__ == '__main__':
    _main()
```


#### Các thành phần chính của chương trình

function `_main` code ngắn gọn:

```py
def _main():
    """Parse options and run checks on Python source."""
    import signal

    # Handle "Broken pipe" gracefully
    try:
        signal.signal(signal.SIGPIPE, lambda signum, frame: sys.exit(1))
    except AttributeError:
        pass    # not supported on Windows

    style_guide = StyleGuide(parse_argv=True)
    options = style_guide.options

    if options.doctest or options.testsuite:
        from testsuite.support import run_tests
        report = run_tests(style_guide)
    else:
        report = style_guide.check_files()

    if options.statistics:
        report.print_statistics()

    if options.benchmark:
        report.print_benchmark()

    if options.testsuite and not options.quiet:
        report.print_results()

    if report.total_errors:
        if options.count:
            sys.stderr.write(str(report.total_errors) + '\n')
        sys.exit(1)
```

function `_main` làm 2 việc chính:

- tạo objects `StyleGuide`
- chạy function `style_guide.check_files()`
- thực hiện report dựa trên các option tương ứng rồi kết thúc.

#### class StyleGuide
Khi gọi StyleGuide(), method `__init__` thực hiện đọc các options rồi setup checker, runner, options, report:

```py
class StyleGuide:
    def __init__(self, *args, **kwargs):
        self.checker_class = kwargs.pop('checker_class', Checker)
        ...
        options, self.paths = process_options(
            arglist, parse_argv, config_file, parser, verbose)
        ...
        self.runner = self.input_file
        self.options = options
        if not options.reporter:
            options.reporter = BaseReport if options.quiet else StandardReport
        ...
        options.physical_checks = self.get_checks('physical_line')
        options.logical_checks = self.get_checks('logical_line')
        options.ast_checks = self.get_checks('tree')
        self.init_report()
```

class Checker thực hiện load file cần check, tokenize rồi chạy các check để check coding style:

```
class Checker:
    """Load a Python source file, tokenize it, check coding style."""
```

`self.runner` được gán giá trị `self.input_file`, là 1 method của `StyleGuide`:

```py
def input_file(self, filename, lines=None, expected=None, line_offset=0):
    """Run all checks on a Python source file."""
    if self.options.verbose:
        print('checking %s' % filename)
    fchecker = self.checker_class(
        filename, lines=lines, options=self.options)
    return fchecker.check_all(expected=expected, line_offset=line_offset)
```

method `input_file` khởi tạo instance của class Checker rồi chạy method `check_all` để chạy các check với 1 Python source file.
Method `check_all` sẽ được xem lại sau.

`self.options` chứa mọi option của chương trình.

`reporter` mặc định dùng class `StandardReport`.
#### method `check_files`

method `check_files` thực hiện chạy check cho **các** file cần kiểm tra PEP8, trả về `report`

```py
    def check_files(self, paths=None):
        """Run all checks on the paths."""
        if paths is None:
            paths = self.paths
        report = self.options.report
        runner = self.runner
        report.start()
        try:
            for path in paths:
                if os.path.isdir(path):
                    self.input_dir(path)
                elif not self.excluded(path):
                    runner(path)
        except KeyboardInterrupt:
            print('... stopped')
        report.stop()
        return report
```

`path` là đường dẫn, có thể tới 1 file hay 1 thư mục, với file, chương trình sẽ check luôn nhờ gọi `runner` (method `input_file`), với thư mục, gọi method `input_dir(path)` để xử lý logic tìm các file trong thư mục rồi chạy `runner` với từng file.

#### class Checker
Logic của từng check nằm ở mỗi check funtion, nhưng việc load các check này vào, chạy khi nào, với option nào được gọi bởi Checker object.

##### register checks
Có 30 function check, mỗi function có số lượng argument khác nhau:

```py
$ grep -E '^def ' pycodestyle.py | grep _line
def tabs_or_spaces(physical_line, indent_char):
def tabs_obsolete(physical_line):
def trailing_whitespace(physical_line):
def trailing_blank_lines(physical_line, lines, line_number, total_lines):
def maximum_line_length(physical_line, max_line_length, multiline,
def _is_one_liner(logical_line, indent_level, lines, line_number):
def blank_lines(logical_line, blank_lines, indent_level, line_number,
def extraneous_whitespace(logical_line):
def whitespace_around_keywords(logical_line):
def missing_whitespace_after_keyword(logical_line, tokens):
def indentation(logical_line, previous_logical, indent_char,
def continued_indentation(logical_line, tokens, indent_level, hang_closing,
def whitespace_before_parameters(logical_line, tokens):
def whitespace_around_operator(logical_line):
def missing_whitespace(logical_line, tokens):
def whitespace_around_comma(logical_line):
def whitespace_around_named_parameter_equals(logical_line, tokens):
def whitespace_before_comment(logical_line, tokens):
def imports_on_separate_lines(logical_line):
def compound_statements(logical_line):
def explicit_line_join(logical_line, tokens):
def break_before_binary_operator(logical_line, tokens):
def break_after_binary_operator(logical_line, tokens):
def comparison_to_singleton(logical_line, noqa):
def comparison_negative(logical_line):
def comparison_type(logical_line, noqa):
def bare_except(logical_line, noqa):
def ambiguous_identifier(logical_line, tokens):
def python_3000_invalid_escape_sequence(logical_line, tokens, noqa):
def maximum_doc_length(logical_line, max_doc_length, noqa, tokens):
```

parameter đầu tiên của các check đều được chuẩn hóa, với tên:

- `physical_line`
- `logical_line`

Đây cũng là 2 **kind** (loại) check trong tổng 3 loại mà `pycodestyle` hỗ trợ:

```py
_checks = {'physical_line': {}, 'logical_line': {}, 'tree': {}}

class StyleGuide():
    def __init__(...):
        ...
        options.physical_checks = self.get_checks('physical_line')
        options.logical_checks = self.get_checks('logical_line')
        options.ast_checks = self.get_checks('tree')
```

Các check được lưu vào 1 global dict tên `_checks` sau khi define các check function, nhờ sử dụng decorator `register_check`:

```py
def register_check(check, codes=None):
    """Register a new check object."""
    def _add_check(check, kind, codes, args):
        if check in _checks[kind]:
            _checks[kind][check][0].extend(codes or [])
        else:
            _checks[kind][check] = (codes or [''], args)
    if inspect.isfunction(check):
        args = _get_parameters(check)
        if args and args[0] in ('physical_line', 'logical_line'):
            if codes is None:
                codes = ERRORCODE_REGEX.findall(check.__doc__ or '')
            _add_check(check, args[0], codes, args)
    elif inspect.isclass(check):
        if _get_parameters(check.__init__)[:2] == ['self', 'tree']:
            _add_check(check, 'tree', codes, None)
    return check

@register_check
def tabs_or_spaces(physical_line, indent_char):
    pass
```

Đoạn code này là một **magic**, sử dụng tính dynamic linh hoạt của Python, dùng `inspect` để đọc từ các function object: tên, parameters, rồi `_add_check` vào từng nhóm `kind` dựa trên tên của parameter đầu tiên.

```py
    _add_check(check, args[0], codes, args)
```

Thử viết 1 function với 2 parameter, rồi dùng code `inspect` tìm xem parameter đầu tiên tên gì:
```py
>>> def sum_two(x, y):
...     pass
...
>>> import inspect
>>> inspect.signature(sum_two)
<Signature (x, y)>
>>> S = inspect.signature(sum_two)
>>> S.
S.bind(              S.empty()            S.parameters         S.return_annotation
S.bind_partial(      S.from_callable(     S.replace(
>>> S.parameters
mappingproxy(OrderedDict([('x', <Parameter "x">), ('y', <Parameter "y">)]))
>>> S.parameters.values()
odict_values([<Parameter "x">, <Parameter "y">])
>>> list(S.parameters.values())[0].name
'x'
```

```py
    _add_check(check, args[0], codes, args)
```

`codes` ở đây là mã error như W101 E201, lọc ra từ docstring của mỗi check function qua `check.__doc__`.

```py
ERRORCODE_REGEX = re.compile(r'\b[A-Z]\d{3}\b')
if codes is None:
    codes = ERRORCODE_REGEX.findall(check.__doc__ or '')
```

Dùng grep để liệt kê tất cả các mã error:

```
$ grep -Eo '\b[A-Z][0-9]{3}\b' pycodestyle.py | sort | uniq | xargs printf '%s '
E101 E111 E112 E113 E114 E115 E116 E121 E122 E123 E124 E125 E126 E127 E128 E129 E131 E133 E201 E202 E203 E211 E221 E222 E223 E224 E225 E226 E227 E228 E231 E241 E242 E251 E252 E261 E262 E265 E266 E271 E272 E273 E274 E275 E301 E302 E303 E304 E305 E306 E401 E402 E501 E502 E701 E702 E703 E704 E711 E712 E713 E714 E721 E722 E731 E741 E742 E743 E901 E902 W191 W291 W292 W293 W391 W503 W504 W505 W605
```

Sửa code trong `_main` rồi chạy:

```py
    style_guide = StyleGuide(parse_argv=True)
    # them 2 dong nay
    for kind, checks in _checks.items():
        print(kind, len(checks))
```

Output:

```
$ python pycodestyle.py pycodestyle.py
physical_line 5
logical_line 25
tree 0
```

`pycodestyle` mặc định có 5 physical checks và 25 logical checks, không có ast (tree) check nào.

Việc thêm check mới đơn giản là viết 1 function, chọn 1 trong 3 type nói trên rồi decorate với `@register_check`.

#### physical check và logical check
physical check kiểm tra từng dòng code mà người dùng nhìn thấy trước khi Python load vào, giống như đọc từng dòng trong file.

```py
def tabs_or_spaces(physical_line, indent_char):
def tabs_obsolete(physical_line):
def trailing_whitespace(physical_line):
def trailing_blank_lines(physical_line, lines, line_number, total_lines):
def maximum_line_length(physical_line, max_line_length, multiline,...)
```

5 physical check trên kiểm tra dòng chứa tab hay space, cuối dòng có whitespace không, blank line có whitespace không và độ dài mỗi dòng, đều có thể dựa trên nội dung text của từng dòng.

logical check kiểm tra các thành phần trong 1 dòng code mà Python hiểu. Ví dụ

Đây là 1 dòng physical

```py
if 2 > 1 and length > 80:
```

Đây là 2 dòng physical nhưng là 1 dòng logical:

```py
if (2 > 1
    and length > 80):
```

Việc kiểm tra độ dài của dòng rõ ràng thuộc về physical check.

#### `check_all`
Method **"core"** của chương trình là `check_all`, nơi **thực sự** chạy các check và thu thập kết quả vào `Report`.
45 dòng:

```py
def check_all(self, expected=None, line_offset=0):
    """Run all checks on the input file."""
    self.report.init_file(self.filename, self.lines, expected, line_offset)
    self.total_lines = len(self.lines)
    if self._ast_checks:
        self.check_ast()
    self.line_number = 0
    self.indent_char = None
    self.indent_level = self.previous_indent_level = 0
    self.previous_logical = ''
    self.previous_unindented_logical_line = ''
    self.tokens = []
    self.blank_lines = self.blank_before = 0
    parens = 0
    for token in self.generate_tokens():
        self.tokens.append(token)
        token_type, text = token[0:2]
        if self.verbose >= 3:
            if token[2][0] == token[3][0]:
                pos = '[{}:{}]'.format(token[2][1] or '', token[3][1])
            else:
                pos = 'l.%s' % token[3][0]
            print('l.%s\t%s\t%s\t%r' %
                  (token[2][0], pos, tokenize.tok_name[token[0]], text))
        if token_type == tokenize.OP:
            if text in '([{':
                parens += 1
            elif text in '}])':
                parens -= 1
        elif not parens:
            if token_type in NEWLINE:
                if token_type == tokenize.NEWLINE:
                    self.check_logical()
                    self.blank_before = 0
                elif len(self.tokens) == 1:
                    # The physical line contains only this token.
                    self.blank_lines += 1
                    del self.tokens[0]
                else:
                    self.check_logical()
    # HVN note: only for last line of file
    if self.tokens:
        self.check_physical(self.lines[-1])
        self.check_logical()
    return self.report.get_file_results()
```

thực hiện:

- khởi tạo report
- chạy các `ast_checks` nếu có (mặc định là không)
- duyệt qua từng token, chạy `check_logical`
- kết thúc, gọi report lấy kết quả cuối cùng để print ra màn hình.

Không thấy `check_physical` ở đâu? bởi `check_physical` được gọi khi `generate_tokens`.

```py
def generate_tokens(self):
    """Tokenize file, run physical line checks and yield tokens."""
    if self._io_error:
        self.report_error(1, 0, 'E902 %s' % self._io_error, readlines)
    tokengen = tokenize.generate_tokens(self.readline)
    try:
        prev_physical = ''
        for token in tokengen:
            if token[2][0] > self.total_lines:
                return
            self.noqa = token[4] and noqa(token[4])
            self.maybe_check_physical(token, prev_physical)
            yield token
            prev_physical = token[4]
    except (SyntaxError, tokenize.TokenError):
        self.report_invalid_syntax()
```
method này gọi `tokenize.generate_tokens` để thực hiện tokenize code, rồi `maybe_check_physical` để có thể gọi `check_physical` nếu cần thiết.

Tokenize là việc chia 1 dòng code thành các thành phần nhỏ nhất: token. Ví dụ dòng `def sum_two(a, b):` có 9 token: `def`, `sum_two`, `(`, `a`, `,`, `b`, `)`, `:`, `\n` xuống dòng.

Thừ xem `tokenize.tokenize` xử lý file code sau:

```py
# foo.py
1 def sum_two(a, b):
2     c = a + b
3
4     return c
```

Chạy tokenize:
```py
>>> import tokenize
>>> f = tokenize.open("foo.py")
>>> for t in tokenize.generate_tokens(f.readline):
...     print(t)
...
TokenInfo(type=1 (NAME), string='def', start=(1, 0), end=(1, 3), line='def sum_two(a, b):\n')
TokenInfo(type=1 (NAME), string='sum_two', start=(1, 4), end=(1, 11), line='def sum_two(a, b):\n')
TokenInfo(type=54 (OP), string='(', start=(1, 11), end=(1, 12), line='def sum_two(a, b):\n')
TokenInfo(type=1 (NAME), string='a', start=(1, 12), end=(1, 13), line='def sum_two(a, b):\n')
TokenInfo(type=54 (OP), string=',', start=(1, 13), end=(1, 14), line='def sum_two(a, b):\n')
TokenInfo(type=1 (NAME), string='b', start=(1, 15), end=(1, 16), line='def sum_two(a, b):\n')
TokenInfo(type=54 (OP), string=')', start=(1, 16), end=(1, 17), line='def sum_two(a, b):\n')
TokenInfo(type=54 (OP), string=':', start=(1, 17), end=(1, 18), line='def sum_two(a, b):\n')
TokenInfo(type=4 (NEWLINE), string='\n', start=(1, 18), end=(1, 19), line='def sum_two(a, b):\n')
TokenInfo(type=5 (INDENT), string='    ', start=(2, 0), end=(2, 4), line='    c = a + b\n')
TokenInfo(type=1 (NAME), string='c', start=(2, 4), end=(2, 5), line='    c = a + b\n')
TokenInfo(type=54 (OP), string='=', start=(2, 6), end=(2, 7), line='    c = a + b\n')
TokenInfo(type=1 (NAME), string='a', start=(2, 8), end=(2, 9), line='    c = a + b\n')
TokenInfo(type=54 (OP), string='+', start=(2, 10), end=(2, 11), line='    c = a + b\n')
TokenInfo(type=1 (NAME), string='b', start=(2, 12), end=(2, 13), line='    c = a + b\n')
TokenInfo(type=4 (NEWLINE), string='\n', start=(2, 13), end=(2, 14), line='    c = a + b\n')
TokenInfo(type=62 (NL), string='\n', start=(3, 0), end=(3, 1), line='\n')
TokenInfo(type=1 (NAME), string='return', start=(4, 4), end=(4, 10), line='    return c\n')
TokenInfo(type=1 (NAME), string='c', start=(4, 11), end=(4, 12), line='    return c\n')
TokenInfo(type=4 (NEWLINE), string='\n', start=(4, 12), end=(4, 13), line='    return c\n')
TokenInfo(type=6 (DEDENT), string='', start=(5, 0), end=(5, 0), line='')
TokenInfo(type=0 (ENDMARKER), string='', start=(5, 0), end=(5, 0), line='')
>>> list(t)
[0, '', (5, 0), (5, 0), '']
```
`tokenize` trả về các `TokenInfo` object, chứa 5 thông tin về token:

- type của token
- string biểu diễn token
- vị trí start (dòng, cột), chú ý dòng bắt đầu từ 1, cột bắt đầu từ 0.
- vị trí end kết thúc token
- line: nội dung dòng vật lý

các attribute này có thể truy cập bằng cú pháp attribute như `t.start` hay dùng index như `t[2]`.
Chú ý rằng file `foo.py` có 4 dòng vật lý, thì token cuối cùng lại có start là dòng 5, nên mới có điều kiện dừng generator:

```py
def generate_tokens(self):
    ...
    for token in tokengen:
        if token[2][0] > self.total_lines:
            return
        ...
        yield token
```

mỗi object Checker biểu diễn việc kiểm tra 1 file, có attribute `.lines` chứa các dòng của file đó. Các check sẽ lấy dòng số mấy dựa theo token start/stop rồi truy cập dòng bằng `self.lines[n]`.

### run physical check
Vậy mỗi physical check được gọi như thế nào?

```py
    def run_check(self, check, argument_names):
        """Run a check plugin."""
        arguments = []
        for name in argument_names:
            arguments.append(getattr(self, name))
        return check(*arguments)

    def init_checker_state(self, name, argument_names):
        """Prepare custom state for the specific checker plugin."""
        if 'checker_state' in argument_names:
            self.checker_state = self._checker_states.setdefault(name, {})

    def check_physical(self, line):
        """Run all physical checks on a raw input line."""
        self.physical_line = line
        for name, check, argument_names in self._physical_checks:
            self.init_checker_state(name, argument_names)
            result = self.run_check(check, argument_names)
            if result is not None:
                (offset, text) = result
                self.report_error(self.line_number, offset, text, check)
                if text[:4] == 'E101':
                    self.indent_char = line[0]
```

Với mỗi `name, check, argument_names` chứa trong `self._physical_checks`, gọi `run_check(check, argument_names)`, method này lấy tên của các argument, rồi lấy giá trị của chúng chưa trong attribute của Checker, sau đó gọi function `check(*arguments)`. Hãy xem thử với check độ dài của dòng:

```py
def maximum_line_length(physical_line, max_line_length, multiline, line_number, noqa):
```
ở phần register_check, argument đầu tiên `physical_line` đã bị tách ra để làm kind của check, còn lại
`arguments = [max_line_length, multiline, line_number, noqa]`, các argument này đều có attribute tương ứng trong Checker

```py
class Checker:
    def __init__(self, filename=None, lines=None,
                 options=None, report=None, **kwargs):
        self.max_line_length = options.max_line_length
        self.multiline = False  # in a multiline string?
        self.noqa = False
        ...
```
`line_number` được set khi chạy `check_all` và được update mỗi khi đọc 1 dòng

```py
    def check_all(self, expected=None, line_offset=0):
        ...
        self.line_number = 0
        ...
        for token in self.generate_tokens():
            ...
```
Như vậy các parameter của function checker đều có attribute tương ứng trong Checker class chứ không phải tùy ý.

#### xem 1 check đơn giản nhất: dòng chứa Tab
Dùng regex tìm trong dòng có chứa ký tự `\t` khi indent không, nếu có, trả về tuple 2 phần tử (index của ký tự tab và nội dung error "W191")

```py
@register_check
def tabs_obsolete(physical_line):
    r"""On new projects, spaces-only are strongly recommended over tabs.

    Okay: if True:\n    return
    W191: if True:\n\treturn
    """
    indent = INDENT_REGEX.match(physical_line).group(1)
    if '\t' in indent:
        return indent.index('\t'), "W191 indentation contains tabs"
```
### coding style
#### global var is okay
pycodestyle sử dụng nhiều biến global như `_checks`, việc sử dụng biến global thường bị xem như "code smell", nhưng biến global này chỉ để đọc (sau khi đã set giá trị) mà không update, nên các nhược điểm do sử dụng global không ảnh hưởng ở đây.
Ngoài ra pycodestyle cũng chỉ chạy mội vài giây (phút) rồi kết thúc chứ không chạy cả ngày như 1 web app nên việc sử dụng global var hoàn toàn OK.
#### main làm ít việc
function main (`_main`) của pycodestyle đơn giản, chủ yếu gọi các function khác, đúng như những gì ta thấy trong [refactor]({filename}/refactor.md)
#### dùng class khi cần class, còn đa số là function
class Checker giúp tạo ra các object checker để quản lý state và thực hiện chạy check cho mỗi file.

Các class Report thực hiện kế thừa BaseReport vì có nhiều điểm giống nhau.

class StyleGuide chứa mọi thứ cần có về chương trình pycodestyle.

các check là các function.

### Kết luận
pycodestyle hay pep8 là chương trình thuộc top phổ biến của python

requests: 450 triệu download/tháng, pycodestyle: 40 triệu download/tháng.

có code nằm trong 1 file duy nhất với 2600 dòng, với tính năng ổn định, code đơn giản, sử dụng tính dynamic linh hoạt của Python để tạo các check. Code dễ dàng thêm các check mới bằng việc tạo function rồi chạy register.
Dùng global var, hàm main ít code, dùng class khi cần.


Hết!

HVN at [http://pymi.vn](http://pymi.vn) and [https://www.familug.org](https://www.familug.org).

- [Ủng hộ tác giả 🍺](https://www.familug.org/p/ung-ho.html)
