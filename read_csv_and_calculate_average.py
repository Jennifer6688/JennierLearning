# read_csv_and_calculate_average.py
import csv

def read_csv(file_path):
    with open(file_path, mode='r') as file:
        csv_reader = csv.reader(file)
        header = next(csv_reader)
        rows = [row for row in csv_reader]
    return header, rows

def calculate_average(rows, column_index):
    total = sum(float(row[column_index]) for row in rows)
    return total / len(rows)

if __name__ == "__main__":
    file_path = 'data.csv'
    header, rows = read_csv(file_path)
    print(f"Header: {header}")

    if 'value' in header:
        column_index = header.index('value')
        average = calculate_average(rows, column_index)
        print(f"Average value: {average:.2f}")
    else:
        print("'value' column not found in CSV file.")
