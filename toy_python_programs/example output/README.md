## Example Output
**Note:** The toy python programs are command line friendly. They have been tested in Linux. Usage examples are easily translated for testing in Windows and Mac.
#
### [01-count_lambs.py](../01-count_lambs.py)
```
$ python3 count_lambs.py novel.txt chapter.txt
File: novel.txt
Result: 4319

--------------------------------------------------------------------------------
File: chapter.txt
Result: 7

--------------------------------------------------------------------------------
```
#
### [02-zig_zag.py](../02-zig_zag.py)
```
$ python3 zig_zag.py 'ლ(ಠ益ಠ)ლ', '¡'
ლ(ಠ益ಠ)ლ,
            ¡
   ლ(ಠ益ಠ)ლ,
            ¡
      ლ(ಠ益ಠ)ლ,
            ¡
         ლ(ಠ益ಠ)ლ,
            ¡
            ლ(ಠ益ಠ)ლ,
            ¡
               ლ(ಠ益ಠ)ლ,
            ¡
               ლ(ಠ益ಠ)ლ,
            ¡
            ლ(ಠ益ಠ)ლ,
            ¡
         ლ(ಠ益ಠ)ლ,
            ¡
      ლ(ಠ益ಠ)ლ,
            ¡
   ლ(ಠ益ಠ)ლ,
            ¡
ლ(ಠ益ಠ)ლ,
            ¡
ლ(ಠ益ಠ)ლ,
            ¡
   ლ(ಠ益ಠ)ლ,
            ¡
      ლ(ಠ益ಠ)ლ,
            ¡
         ლ(ಠ益ಠ)ლ,
            ¡
            ლ(ಠ益ಠ)ლ,
            ¡
               ლ(ಠ益ಠ)ლ,
            ¡
               ლ(ಠ益ಠ)ლ,
            ¡
            ლ(ಠ益ಠ)ლ,
            ¡
         ლ(ಠ益ಠ)ლ,
            ¡
      ლ(ಠ益ಠ)ლ,
            ¡
   ლ(ಠ益ಠ)ლ,
            ¡
ლ(ಠ益ಠ)ლ,
            ¡
ლ(ಠ益ಠ)ლ,
            ¡
   ლ(ಠ益ಠ)ლ,
            ¡
      ლ(ಠ益ಠ)ლ,
            ¡
         ლ(ಠ益ಠ)ლ,
            ¡
            ლ(ಠ益ಠ)ლ,
            ¡
               ლ(ಠ益ಠ)ლ,
            ¡
               ლ(ಠ益ಠ)ლ,
            ¡
            ლ(ಠ益ಠ)ლ,
            ¡
         ლ(ಠ益ಠ)ლ,
            ¡
      ლ(ಠ益ಠ)ლ,
            ¡
   ლ(ಠ益ಠ)ლ,
            ¡
ლ(ಠ益ಠ)ლ,
            ¡
```
#
### [03-columnize.py](../03-columnize.py)
```
$ python3 columnize.py words.txt
word word word word word word word word word word word word word word word word
word word word word word word word word word word word word word word word word
word word word word word word word word word word word word word word word word
word word word word word word word word word word word word word word word word
word word word word word word word word word word word word word word word word
word word word word word word word word word word word word word word word word
word word word word word word word word word word word word word word word word
word word word word word word word word word word word word word word word word
word word word word word word
```
#
### [04-math_dates.py](../04-math_dates.py)
```
$ python3 math_dates.py
Adding 20 days to 2021-12-01 should result in 2021-12-21
Subtracting 20 days from 2021-12-01 should result in 2021-11-11

Unittest Results:
test_add_days (__main__.TestDateMath)
Confirm that the result of adding 20 days returned 2021-12-21 ... ok
test_minus_days (__main__.TestDateMath)
Confirm that the result of taking away 20 days returned 2021-11-11 ... ok

----------------------------------------------------------------------
Ran 2 tests in 0.001s

OK
```
#
### [05-utf_id.py](../05-utf_id.py)
```
$ python3 utf_id.py utf8_file file.py utf16_file utf32_file
Average Bytes Required for Each Character in utf8_file: 1.7925636007827788
Average Bytes Required for Each Character in file.py: 1.0
This program only accepts valid ASCII and UTF-8 files.
This program only accepts valid ASCII and UTF-8 files.
```
#
### [06-sub_what.py](../06-sub_what.py)
```
$ python3 sub_what.py /usr/local/bin/java hwjava.java printed some words here
File: hwjava.java
Here is the result of your file and args using subprocess:
printed
some
words
here
```
```
$ python3 sub_what.py /usr/bin/bash ./double.sh 30 40 100
File: ./double.sh
Here is the result of your file and args using subprocess:
Integer input doubled:
60
80
200
```
#
### [07-file_checks.py](../07-file_checks.py)
```
$ python3 file_checks.py utf8_file utf16_file utf32_file file.py
File: utf8_file ... is encoded in UTF-8
--------------------------------------------------------------------------------
File: utf16_file ... is encoded in UTF-16
--------------------------------------------------------------------------------
File: utf32_file ... is encoded in UTF-32
--------------------------------------------------------------------------------
File: file.py ... is encoded in UTF-8
--------------------------------------------------------------------------------
```
#
### [08-turn_json.py](../08-turn_json.py)
```
$ python3 test.py greetings.csv no_header.csv
=========================================================
greetings.csv as JSON object:
{
    "Record 1": {
        "Greeting": "Hi",
        "First Name": "SamÆ",
        "Question": "Do you like",
        "Quantity": "much",
        "Food Item": "tuna"
    },
    "Record 2": {
        "Greeting": "Howdy",
        "First Name": "Bobbië",
        "Question": "Would you like",
        "Quantity": "some",
        "Food Item": "celery"
    },
    "Record 3": {
        "Greeting": "Hey",
        "First Name": "Anderson",
        "Question": "Do you like",
        "Quantity": "a lot of",
        "Food Item": "beef"
    }
}
=========================================================

=========================================================
no_header.csv as JSON object:
{
    "Record 1": {
        "Field 1": "Hi",
        "Field 2": "SamÆ",
        "Field 3": "Do you like",
        "Field 4": "much",
        "Field 5": "tuna"
    },
    "Record 2": {
        "Field 1": "Howdy",
        "Field 2": "Bobbië",
        "Field 3": "Would you like",
        "Field 4": "some",
        "Field 5": "celery"
    },
    "Record 3": {
        "Field 1": "Hey",
        "Field 2": "Anderson",
        "Field 3": "Do you like",
        "Field 4": "a lot of",
        "Field 5": "beef"
    }
}
=========================================================

```
#
### [09-id_byte_str.py](../09-id_byte_str.py)
Get UTF status using program's get_status() function
```
$ python3 test.py byte_str byte_str_utf16 byte_str_utf32
byte_str
---------
UTF-8 byte strings
Decoded: 跑到縣衙 跑到縣衙

byte_str_utf16
---------------
UTF-16 byte strings
Decoded: popcorn

byte_str_utf32
---------------
UTF-32 byte strings
Decoded: popcorn! popcorn! Eat popcorn during the movie.
```
#
[Return to top of page](#example-output)
#