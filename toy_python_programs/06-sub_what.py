import sys
import subprocess
from functools import wraps


def result_decorator(result_func):

    @wraps(result_func)
    def wrapper_result(*args):
        """Wrap args_result function"""
        # Print input file name
        for item in args:
            print('File:', item[1])

        print(result_func.__doc__)

        # Calls function that uses subprocess and displays output
        result_func(*args)

    return wrapper_result


@result_decorator
def args_result(the_args):
    """Here is the result of your file and args using subprocess"""
    # Run the file with the indicated args
    process = subprocess.run(the_args, check=True, universal_newlines=True)
    output = process.stdout

    return output


if __name__ == '__main__':
    try:
        # check if there are sufficient args
        input_args = sys.argv[1:]
        if len(input_args) > 1:
            args_result(input_args)
        else:
            print('Please enter the proper sys args. -> ',
                  'Ex: python3 file.py /usr/local/bin/java file.java arg1...')

    except FileNotFoundError:
        print('Please enter the proper sys args. -> ',
              'Ex: python3 file.py /usr/local/bin/java file.java arg1...')
