import sys
import textwrap
import re


def col_text(text, width_value):
    """Return text in a column with a given width value"""
    # convert multiple spaces in the text into single spaces
    one_spaced_text = re.sub(r'\s+', ' ', text)

    # wrapper for making column with specified with
    wrapper = textwrap.TextWrapper(width=width_value)

    # wraps text and makes it into a single string
    wrapped_text = wrapper.fill(text=one_spaced_text)

    return wrapped_text


def main():
    """Get content of one file and specify a 79-character width for column"""
    try:
        # Check if file exists
        arg = sys.argv[1]
        open(arg)
    except FileNotFoundError:
        print('File does not exist')
    except IndexError:
        print('Please enter one file to columnize')
    else:
        # Get content from one file. (Use loop if batching files)
        arg = sys.argv[1]
        with open(arg, 'r') as file:
            content = file.read()
            file.close()

        # Pass file contents and column width value to col_text()
        print(col_text(content, 79))

if __name__ == '__main__':
    main()
