import sys
from functools import reduce


def count_palindromes(file):
    """Count the instances of palindromes in the file"""
    try:
        return reduce(lambda c, x: c + x.count(x[::-1]),
                      (list(filter(lambda x: len(x) != 1,
                                   open(file).read().split()))), 0)
    except FileNotFoundError:
        return 'file not found'


def main():
    """Feed file args into count_palindromes and print labeled results"""
    files = sys.argv[1:]
    if len(files) == 0:
        print('Please enter files on the command line')

    for f in files:
        print('File:', f)
        print('Result:', count_palindromes(f), '\n')
        print('-' * 80)  # neat results divider

if __name__ == '__main__':
    main()
