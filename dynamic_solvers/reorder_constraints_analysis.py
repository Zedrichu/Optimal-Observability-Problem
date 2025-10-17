import operator
import os
import csv
import argparse

TIMEOUT = 180

def main():
    parser = argparse.ArgumentParser(description='Count solved instances in CSV files.')
    parser.add_argument('directory', help='Path to the directory containing CSV files')
    args = parser.parse_args()

    directory = args.directory
    results = []

    for filename in os.listdir(directory):
        if filename.endswith('.csv'):
            filepath = os.path.join(directory, filename)
            solved = 0
            duration = 0.0
            total = 0
            with open(filepath, newline='') as csvfile:
                reader = csv.reader(csvfile)
                reader.__next__() # Skip header
                for row in reader:
                    total += 1
                    status = row[6].strip().strip().upper()
                    if status != "UNKNOWN":
                        solved += 1
                        duration += float(row[4].strip())
            results.append((filename, solved, total, duration))

    # Sort files by solved count descending
    results.sort(key = lambda x: (x[1], -x[2]), reverse=True)

    for i, (filename, solved, total, duration) in enumerate(results):
        file_id = str(i+1).rjust(2, ' ')
        print(f'{file_id} {filename}: {solved} ({(solved/total*100):.2f}%) solved instances in {duration:.2f}s')

if __name__ == '__main__':
    main()
