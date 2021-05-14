## Toy Python Programs
###### Note: These toy python programs are command line friendly. All programs have been tested in Linux. Usage examples are easily translatable to test in Windows and Mac.
#
[01-count_lambs.py](01-count_lambs.py)

**Goal**
- Feed file content to reduce and lambda functions to get count of word(s)

**Application**
- Convert file contents to a list
- Identify palindrome words
- Exclude one-character labels (e.g. a, b, 1, 2)
- Use counter with default value of 0

**Usage**
```
$ python3 count_lambs.py [file]
```
```
$ python3 count_lambs.py [file1] [file2] [file3] ...
```
#
[02-zig_zag.py](02-zig_zag.py) <br/>
**Goal**
- Simulate a symmetrical zig zag pattern using itertools module's chain function

**Application**
- Customize main pattern (7-8 characters)
- Customize pole pattern (1-2 characters)
- Specify various ranges of spacing
- Essentiate symmetrical pattern with pole pattern
- Chain separate range sequences into a single long sequence
**Usage**
```
$ python3 test.py [main_pattern] [pole_pattern]
```
#
[03-columnize.py](03-columnize.py) <br/>
**Goal**
- Columnize file content using the re and textwrap modules

**Application**
- Substitute all initial spacing with one-spaces
- Keep words intact without breakage
- Format content into one continuous column

**Usage**
```
$ python3 columnize.py [file]
```
#
[04-math_dates.py](04-math_dates.py) <br/>
**Goal**
TBA <br/>
**Application**
TBA <br/>
**Usage**
TBA
#
[05-utf_id.py](05-utf_id.py) <br/>
***Goal***:
TBA <br/>
**Application** 
TBA <br/>
**Usage**
TBA
#
[06-sub_what.py](06-sub_what.py) <br/>
**Goal**
TBA <br/>
**Application**
TBA <br/>
**Usage**
TBA
#
[07-file_checks.py](07-file_checks.py) <br/>
**Goal**
- Check for UTF file types with concurrent processing

**Application**
- Check if file is UTF-8, UTF-16, or other
- Implement concurrent pool processing feature
- Process quickly with ProcessPoolExecutor class

**Usage**
```
$ python3 file_checks.py [file]
```
```
$ python3 file_checks.py [file1] [file2] [file3] ...
```
#
[08-turn_json.py](08-turn_json.py) <br/>
**Goal**
Convert CSV objects to pretty JSON objects

**Application**
- Use sniffer to identify dialect and delimiter
- Add root label to keep track or records
- Create header for empty-header files

**Usage**
```
$ python3 turn_json.py [file]
```
```
$ python3 turn_json.py [file1] [file2] [file3] ...
```
#
[09-id_byte_str.py](09-id_byte_str.py) <br/>
**Goal**
- Extract byte strings from file(s) and determine encoding

**Application**
- Work with files containing only byte strings
- Preserve byte string type using ast modules's literal_eval helper
- Attempt decoding in UTF-8, -16, and 32
- Include feature for returning decoded byte strings as strings

**Usage**
```
$ python3 id_byte_str.py [file1] [file2] [file3] ...
```
#
### Docs
To be added
