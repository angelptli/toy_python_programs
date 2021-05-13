import sys


def count_avg_bytes(file):
    """Gets the byte count of every character in a file and find average"""
    try:
        # Counters to get total bytes and chars in a file
        total_bytes = 0
        total_chars = 0

        # Open file and specify utf8 encoding, read one char at a time
        with open(file, encoding="utf8") as f:
            while True:
                char = f.read(1)
                if char:
                    total_bytes += len(str.encode(char))
                    total_chars += 1
                else:
                    # Breaks when reaches end of file
                    break

        # Divide total_bytes with total_chars and return result
        return (f"Mean Number of Bytes Per Character in "
                f"{file}: {total_bytes/total_chars}")

    except UnicodeDecodeError:
        return 'This program only accepts valid ASCII and UTF-8 files.'


def main():
    try:
        # Allow accepting of more than one file
        args = sys.argv[1:]
        if len(args) > 0:
            # Unpack from generated results
            print(*(count_avg_bytes(arg) for arg in args), sep='\n')
        else:
            print('Please enter valid files as command line args')

    except FileNotFoundError:
        print('Please enter valid files as command line args')

if __name__ == '__main__':
    main()
