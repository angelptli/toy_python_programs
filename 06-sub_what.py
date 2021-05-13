import sys
import subprocess
from functools import wraps


def result_decorator(result_func):

    @wraps(result_func)
    def wrapper_result(*args):
        """wrap args_result function"""
        print(result_func.__name__)
        print(result_func.__doc__)

        # calls function that uses subprocess and displays output
        result_func(*args)

    return wrapper_result


@result_decorator
def args_result(the_args):
    """Here is the result of your file and args using subprocess"""
    # Run the file with the indicated args
    process = subprocess.run(the_args, check=True, universal_newlines=True)
    output = process.stdout

    # display output
    return output


if __name__ == '__main__':
    try:
        # check if there are sufficient args
        input_args = sys.argv[1:]
        if len(input_args) > 1:
            args_result(input_args)
        else:
            print('Please enter the proper sys args. -> ',
                  'Example: python3 /path/file.py java file.java arg1...')

    except FileNotFoundError:
        print('Please enter the proper sys args. -> ',
              'Example: python3 /path/file.py java file.java arg1...')

    else:
        print('\nInvalid input. Please try again.')
        print('Example: python3 /path/file.py java file.java arg1...')

"""
Example usage on command line for java file
python3 06-sub_what.py /usr/local/bin/java file.java arg1 arg2 ...
"""
