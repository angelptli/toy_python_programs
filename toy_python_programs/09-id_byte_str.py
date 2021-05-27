import sys
import ast
from concurrent.futures import ProcessPoolExecutor


def get_file_content(file_name):
    """Extract the byte strings from a file.

    The file_name parameter is treated as a file. With file_name opened, its
    byte strings content is extracted with type preserved. This is made
    possible with the imported ast module's literal_eval method.

    :param str file_name: File containing byte strings
    :return: list of byte strings
    :rtype: list
    :raises FileNotFoundError: if file is not found
    :raises ValueError, SyntaxError: if file does not contain only byte strings
    """
    try:
        with open(file_name, 'r') as f:
            # Places byte strings into a list
            return [ast.literal_eval(line) for line in f]

    except FileNotFoundError:
        print('File does not exist')
    except (ValueError, SyntaxError):
        print('File contains non-byte strings')


def get_status(bytes_list):
    """Attempt decoding of byte strings in UTF-8, -16, and 32.

    :param list bytes_list: The list of byte strings for decoding
    :return: the file's status message
    :rtype: str
    :raises UnicodeDecodeError: if bytes_list does not contain UTF-encoded
        byte strings
    :raises AttributeError, TypeError: if FileNotFoundError and ValueError
        are raised in the get_file_content function
    """
    try:
        for item in bytes_list:
            item.decode('utf8')
        return 'UTF-8 byte strings'

    except UnicodeDecodeError:
        pass
    except (AttributeError, TypeError):
        # Raises along with FileNotFoundError and ValueError, no msg required
        pass

    # Attempt UTF-32 decoding before next since it can be decoded with UTF-16
    try:
        for item in bytes_list:
            item.decode('utf32')
        return 'UTF-32 byte strings'

    except UnicodeDecodeError:
        pass
    except (AttributeError, TypeError):
        pass

    try:
        for item in bytes_list:
            item.decode('utf16')
        return 'UTF-16 byte strings'

    except UnicodeDecodeError:
        print('Is NOT a proper UTF file')
    except (AttributeError, TypeError):
        print()


def get_decoded_str(bytes_list):
    """Return the decoded bytes strings in string.

    :param list bytes_list: The list of byte strings for decoding
    :return: decoded byte strings as a string
    :rtype: str
    :raises UnicodeDecodeError: if bytes_list does not contain UTF-encoded
        byte strings
    :raises AttributeError, TypeError: if FileNotFoundError and ValueError
        are raised in the get_file_content function
    """
    string = ''

    try:
        for item in bytes_list:
            string += item.decode('utf8')
        return string

    except UnicodeDecodeError:
        pass
    except (AttributeError, TypeError):
        # Raises along with FileNotFoundError and ValueError, no msg required
        pass

    try:
        for item in bytes_list:
            string += item.decode('utf32')
        return string

    except UnicodeDecodeError:
        pass
    except (AttributeError, TypeError):
        pass

    try:
        for item in bytes_list:
            string += item.decode('utf16')
        return string
        
    except UnicodeDecodeError:
        print('Is NOT a proper UTF file')
    except (AttributeError, TypeError):
        print()


def main():
    """Apply concurrent processing to return the file UTF status"""
    args = sys.argv[1:]
    if args:
        for arg in args:
            print(arg, ('-' * (len(arg) + 1)), sep='\n')  # underlines file

            executor = ProcessPoolExecutor(5)

            # Open file and extract byte strings
            bytes_strings = executor.submit(get_file_content, arg)
            bytes_strings = bytes_strings.result()

            # Determine file's UTF status by attempts at decoding and
            # get decoded byte strings
            utf_result = executor.submit(get_status, bytes_strings)
            decode_result = executor.submit(get_decoded_str, bytes_strings)

            # Return results
            if utf_result.result() is not None:
                print(utf_result.result())
            if decode_result.result() is not None:
                print('Decoded:', decode_result.result() + '\n')

    else:
        print('Enter at least one file as a command line argument')

    # Here's an example of a simple usage to determine status of one file
    # content = get_file_content(sys.argv[1])
    # result = get_status(content)
    #
    # if result is not None:
    #     print(result)


if __name__ == '__main__':
    main()
