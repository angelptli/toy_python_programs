import sys
import itertools as it


def print_zig_zag(main_pattern, pole_pattern):
    """Use multiple ranges and types of spacing to print strings in a zig zag"""
    print(*(map(lambda x: (x * '   ') + main_pattern + '\n\t    ' + pole_pattern,
                it.chain(range(6), range(5, -1, -1),
                         range(6), range(5, -1, -1),
                         range(6), range(5, -1, -1)))), sep='\n')


def main():
    """
    Specify main pattern and pole pattern for printing.
    
    Recommend:
    7-8 characters for first (main) pattern.
    1-2 characters for second (pole) pattern.
    """
    first_pattern = sys.argv[1]
    second_pattern = sys.argv[2]
    print_zig_zag(first_pattern, second_pattern)

if __name__ == '__main__':
    main()
