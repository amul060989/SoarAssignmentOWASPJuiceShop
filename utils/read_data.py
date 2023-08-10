import csv

def getData(filename):
    rows = []
    file = open(filename)
    reader = csv.reader(file)
    next(reader)

    for row in reader:
        rows.append(row)

    return rows