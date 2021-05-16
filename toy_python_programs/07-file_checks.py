import sys
import concurrent.futures


def get_utf_stat(file_arg):
    """Opens and determine if file is UTF-8, UTF-16, or other"""
    # First check if UTF-32 file
    try:
        with open(file_arg, 'r', encoding='utf-32') as f:
            f.read()
            return 'is encoded in UTF-32'
    except (UnicodeDecodeError, UnicodeError):
        pass
    except FileNotFoundError:
        return 'does not exist'
    except IsADirectoryError:
        return 'is a directory'

    # Then check if UTF-16 file
    try:
        with open(file_arg, 'r', encoding='utf-16') as f:
            f.read()
            return 'is encoded in UTF-16'
    except (UnicodeDecodeError, UnicodeError):
        pass

    # Then check if UTF-8 file
    try:
        with open(file_arg, 'r', encoding='utf-8') as f:
            f.read()
            return 'is encoded in UTF-8'
    except UnicodeDecodeError:
        return 'is not a UTF file'


def main():
    """Give files to concurrent processing for determining file status"""
    # "You shall not pass" if not enough command line arguments - Gandalf
    args = sys.argv[1:]
    if len(args) == 0:
        print("\"YOU SHALL NOT PASSSS!!!!\" - Gandalf")
        print('Please enter at least one pathname command line argument')

    # Pass each arg (file) into check_for_utf
    with concurrent.futures.ProcessPoolExecutor() as executor:
        for file, encode_result in zip(args, executor.map(get_utf_stat, args)):
            print('File: {} ... {}'.format(file, encode_result))
            print('-' * 80)  # neat line to divide results

if __name__ == '__main__':
    main()
