import csv
import json
import sys


def make_pretty_json(file):
    """Create a pretty JSON formatted version of CSV file"""
    try:
        # Allow opening of files with ASCII and UTF-8 characters
        with open(file, 'r', encoding='utf-8') as f:
            # If there is a header, continue, else csv.Error occurs, so
            # handle by creating a custom header in separate try/except block
            csv.Sniffer().has_header(f.readline())
            f.seek(0)  # returns to top of file

            # Sniff out the delimiter
            delimiter = csv.Sniffer().sniff(f.read())
            f.seek(0)

            # By creating this object, header fields are assigned to row items
            dict_reader = csv.DictReader(f, dialect=delimiter)

            # Make rows into dicts and put into list
            list_of_dicts = [dict(row) for row in dict_reader]
            f.seek(0)

            # Find number of records by finding number of dicts, then create
            # labels for each record
            records = sum(1 for _ in csv.reader(f, delimiter))

            # Use list_of_dicts to make dicts_of_dicts. The labels become
            # the key for each record in dicts_of_dicts.
            dict_of_dicts = {}
            for n in range(1, records):
                label = 'Record ' + str(n)
                dict_of_dicts[label] = list_of_dicts[0]
                del list_of_dicts[0]

            # Return JSON pretty format using dumps method, which serializes
            # the dicts. Allow non-ascii characters.
            return json.dumps(dict_of_dicts, indent=4, ensure_ascii=False)

    except (FileNotFoundError, IndexError):
        return 'Please enter valid CSV files as command line arguments'
    except UnicodeDecodeError:
        return 'This program works for ASCII and UTF-8 files'
    except csv.Error:
        # Handle no-header CSV files in the next try/except block
        pass

    # Create header for CSV files without one. A blank top line means no header.
    try:
        with open(file, 'r', encoding='utf-8') as f:
            # Get delimiter from CSV file
            delimiter = csv.Sniffer().sniff(f.read())
            f.seek(0)  # returns to top of file

            # Find number of fields, which is used for creating a header list
            fields = 0
            for row in csv.reader(f, delimiter):
                if len(row) > 0:
                    fields = len(row)
                    break

            f.seek(0)
            header = ['Field ' + str(n) for n in range(1, fields + 1)]

            # Convert rows and header list into dicts, put into list
            list_of_dicts = \
                [dict(zip(header, row))
                 for row in csv.reader(f, delimiter) if len(row) > 0]
            f.seek(0)

            # Find number of records to create record labels
            records = sum(1 for _ in csv.reader(f, delimiter))

            # Use list_of_dicts to create dicts_of_dicts
            dict_of_dicts = {}
            for n in range(1, records):
                label = 'Record ' + str(n)
                dict_of_dicts[label] = list_of_dicts[0]
                del list_of_dicts[0]

            # Return JSON pretty format and allow non-ascii characters
            return json.dumps(dict_of_dicts, indent=4, ensure_ascii=False)

    except (FileNotFoundError, IndexError, csv.Error):
        return 'Please enter valid CSV files as command line arguments'
    except UnicodeDecodeError:
        return 'This program works for ASCII and UTF-8 files'


def main():
    """Call make_pretty_json function to return a pretty JSON formatted
    version of each CSV file"""
    # Allow multiple files and check for at least one arg entered
    args = sys.argv[1:]
    if len(args) == 0:
        print('Please enter at least one CSV file as a command line argument')

    # Display each CSV file in pretty print JSON format
    for arg in args:
        json_obj = make_pretty_json(arg)
        print("=========================================================")
        print(f"{arg} as JSON object:\n{json_obj}")
        print("=========================================================\n")

if __name__ == '__main__':
    main()
