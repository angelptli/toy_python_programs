import sys
import concurrent.futures


def get_utf_stat(file_arg):
    """Opens and determine if file is UTF-8, UTF-16, or other"""
    # First determine if UTF-8
    try:
        with open(file_arg, 'r', encoding='utf-8') as f:
            f.read()
            return 'is UTF-8'
    except UnicodeDecodeError:
        pass
    except FileNotFoundError:
        return 'does not exist'

    # Then determine if UTF-16
    try:
        with open(file_arg, 'r', encoding='utf-16') as f:
            f.read()
            return 'is UTF-16'
    except UnicodeDecodeError:
        return 'is not UTF-8 nor UTF-16'


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
