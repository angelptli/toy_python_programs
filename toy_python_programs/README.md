# Toy Python Programs
**Note:** The toy python programs are command line friendly. They have been tested in Linux. Usage examples are easily translated for testing in Windows and Mac.
#
### [01-count_lambs.py](01-count_lambs.py)

**Goal:** Feed file content to reduce and lambda functions to count certain words

**Applications:**
- Convert file contents to a list
- Identify palindrome words
- Exclude one-character labels (e.g. a, b, 1, 2)
- Use counter with default value of 0

**Usage:**
```
$ python3 count_lambs.py [file]
```
```
$ python3 count_lambs.py [file1] [file2] [file3] ...
```
#
### [02-zig_zag.py](02-zig_zag.py)

**Goal:** Simulate a symmetrical zig zag pattern using itertools module's chain function

**Applications:**
- Customize main pattern (7-8 characters)
- Customize pole pattern (1-2 characters)
- Specify various ranges of spacing
- Essentiate symmetrical pattern with pole pattern
- Chain separate range sequences into a single long sequence

**Usage:**
```
$ python3 test.py [main_pattern] [pole_pattern]
```
#
### [03-columnize.py](03-columnize.py)

**Goal:** Columnize file content using the re and textwrap modules

**Applications:**
- Substitute all initial spacing with one-spaces
- Keep words intact without breakage
- Format content into one continuous column

**Usage:**
```
$ python3 columnize.py [file]
```
#
### [04-math_dates.py](04-math_dates.py)

**Goal:** Practice unit testing and output assertion with dates

**Applications:**
- Place date math functions into its own class
- Do simple math using datetime module's timedelta function
- Perform tests in a separate class
- Self assert output using unittest module's assertEqual function

**Usage:**
```
python3 math_dates
```
#
### [05-utf_id.py](05-utf_id.py)

**Goal:** Calculate the average bytes that characters in a file require

**Applications:**
- Accept ASCII and UTF-8 files
- Get the total byte count for a file
- Get the total character count for a file
- Calculate average by dividing total bytes with total characters 

**Usage:**
```
$ python3 utf_id.py [file]
```
```
$ python3 utf_id.py [file1] [file2] [file3] ...
```
#
### [06-sub_what.py](06-sub_what.py)

**Goal:** Utilize python's subprocessing to run programs in different languages

**Applications:**
- Accept programs written in any programming language
- Receive any number of arguments following the file's name
- Run the program using the subprocess module's functions
- Decorate results using functools module's wraps function

**Usage:**<br/>
Example for running java subprocess
```
python3 sub_what.py [/usr/local/bin/java] [filename] [arg1] [arg2] ...
```
Example for running bash subprocess
```
python3 sub_what.py [/usr/local/bin/bash] [./filename] [arg1] [arg2] ...
```
#
### [07-file_checks.py](07-file_checks.py)

**Goal:** Check for UTF file status using concurrent processing

**Applications:**
- Check if file is UTF-8, UTF-16, or other
- Implement concurrent pool processing feature
- Process quickly with ProcessPoolExecutor class

**Usage:**
```
$ python3 file_checks.py [file]
```
```
$ python3 file_checks.py [file1] [file2] [file3] ...
```
#
### [08-turn_json.py](08-turn_json.py)

**Goal:** Convert objects from CSV files to pretty print JSON objects

**Applications:**
- Use sniffer to identify dialect and delimiter
- Add root label to keep track or records
- Create header for empty-header files

**Usage:**
```
$ python3 turn_json.py [file]
```
```
$ python3 turn_json.py [file1] [file2] [file3] ...
```
#
### [09-id_byte_str.py](09-id_byte_str.py)

**Goal:** Extract byte strings from file(s) and determine their UTF encoding

**Applications:**
- Work with files containing only byte strings
- Preserve byte string type using ast modules's literal_eval helper
- Attempt decoding in UTF-8, -16, and 32
- Include feature for returning decoded byte strings as strings

**Usage:**
```
$ python3 id_byte_str.py [file1] [file2] [file3] ...
```
#
# Docs
Almost every program here uses the [sys](https://docs.python.org/3/library/sys.html) module for passing command line arguments into the program. Specific definition link: [sys.argv](https://docs.python.org/3/library/sys.html#sys.argv).

### [01-count_lambs.py](01-count_lambs.py)<br/>
[functools](https://docs.python.org/3/library/functools.html)<br/>
&nbsp;&nbsp;&nbsp;&nbsp; &mdash; [functools.reduce](https://docs.python.org/3/library/functools.html#functools.reduce)

### [02-zig_zag.py](02-zig_zag.py)<br/>
[itertools](https://docs.python.org/3/library/itertools.html)<br/>
&nbsp;&nbsp;&nbsp;&nbsp; &mdash; [itertools.chain](https://docs.python.org/3/library/itertools.html#itertools.chain)

### [03-columnize.py](03-columnize.py)<br/>
[re](https://www.w3schools.com/python/python_regex.asp)<br/>
&nbsp;&nbsp;&nbsp;&nbsp; &mdash; [re.sub](https://docs.python.org/3/library/re.html#re.sub)<br/>

[textwrap](https://www.geeksforgeeks.org/textwrap-text-wrapping-filling-python/)<br/>
&nbsp;&nbsp;&nbsp;&nbsp; &mdash; [textwrap.TextWrapper](https://docs.python.org/3/library/textwrap.html#textwrap.TextWrapper)<br/>
&nbsp;&nbsp;&nbsp;&nbsp; &mdash; [textwrap.fill](https://docs.python.org/3/library/textwrap.html#textwrap.fill)

### [04-math_dates.py](04-math_dates.py)
[unittest](https://docs.python.org/3/library/unittest.html)<br/>
&nbsp;&nbsp;&nbsp;&nbsp; &mdash; [assertEqual](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertEqual)<br/>
&nbsp;&nbsp;&nbsp;&nbsp; &mdash; [self.assertEqual examples](https://docs.python.org/3/library/unittest.html#basic-example)<br/>

[datetime](https://docs.python.org/3/library/datetime.html)<br/>
&nbsp;&nbsp;&nbsp;&nbsp; &mdash; [datetime.timedelta](https://docs.python.org/3/library/datetime.html#datetime.timedelta)<br/>
&nbsp;&nbsp;&nbsp;&nbsp; &mdash; [datetime.date](https://docs.python.org/3/library/datetime.html#datetime.date)

### [05-utf_id.py](05-utf_id.py)<br/>
&nbsp;&nbsp;&nbsp;&nbsp; &mdash; N/A

### [06-sub_what.py](06-sub_what.py)<br/>
[subprocess](https://docs.python.org/3/library/subprocess.html)<br/>
&nbsp;&nbsp;&nbsp;&nbsp; &mdash; [subprocess.run](https://docs.python.org/3/library/subprocess.html#subprocess.run)<br/>
&nbsp;&nbsp;&nbsp;&nbsp; &mdash; [stdout](https://docs.python.org/3/library/subprocess.html#subprocess.run)<br/>

[functools](https://docs.python.org/3/library/functools.html)<br/>
&nbsp;&nbsp;&nbsp;&nbsp; &mdash; [@functools.wraps](https://docs.python.org/3/library/functools.html#functools.wraps)

### [07-file_checks.py](07-file_checks.py)<br/>
[concurrent.futures](https://docs.python.org/3/library/concurrent.futures.html)<br/>
&nbsp;&nbsp;&nbsp;&nbsp; &mdash; [concurrent.futures.ProcessPoolExecutor](https://docs.python.org/3/library/concurrent.futures.html#concurrent.futures.ProcessPoolExecutor)

### [08-turn_json.py](08-turn_json.py)<br/>
[csv](https://docs.python.org/3/library/csv.html)<br/>
&nbsp;&nbsp;&nbsp;&nbsp; &mdash; [csv.Sniffer.has_header](https://docs.python.org/3/library/csv.html#csv.Sniffer)<br/>
&nbsp;&nbsp;&nbsp;&nbsp; &mdash; [csv.Sniffer.sniff](https://docs.python.org/3/library/csv.html#csv.Sniffer)<br/>
&nbsp;&nbsp;&nbsp;&nbsp; &mdash; [csv.DictReader](https://docs.python.org/3/library/csv.html#csv.DictReader)<br/>
&nbsp;&nbsp;&nbsp;&nbsp; &mdash; [csv.reader](https://docs.python.org/3/library/csv.html#csv.reader)<br/>

[json](https://docs.python.org/3/library/json.html)<br/>
&nbsp;&nbsp;&nbsp;&nbsp; &mdash; [json.dumps](https://docs.python.org/3/library/json.html#json.dumps)

### [09-id_byte_str.py](09-id_byte_str.py)<br/>
[ast](https://docs.python.org/3/library/ast.html)<br/>
&nbsp;&nbsp;&nbsp;&nbsp; &mdash; [ast.literal_eval](https://docs.python.org/3/library/ast.html#ast.literal_eval)<br/>

[concurrent.futures](https://docs.python.org/3/library/concurrent.futures.html)<br/>
&nbsp;&nbsp;&nbsp;&nbsp; &mdash; [concurrent.futures.ProcessPoolExecutor](https://docs.python.org/3/library/concurrent.futures.html#concurrent.futures.ProcessPoolExecutor)

## Credits
This is a work in process by Angel Li [@angelptli](https://github.com/angelptli)