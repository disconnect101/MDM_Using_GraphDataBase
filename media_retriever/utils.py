import csv

def csv_reader(path):
    fields = []
    rows = []

    with open(path, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        fields = next(csvreader)
        for row in csvreader:
            rows.append(row)

    return fields, rows
