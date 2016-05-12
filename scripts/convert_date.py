import csv
from datetime import datetime, timedelta
from os import path

def get_csv():
    csv_path = path.join('static', '2016-05-11-seattle-911.csv')
    with open(csv_path, newline='') as csv_file:
        csv_obj = csv.DictReader(csv_file)
        return list(csv_obj)

def write_csv(rows):
    csv_path = path.join('static', 'data.csv')
    with open(csv_path, 'w') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=rows[0].keys())
        writer.writeheader()
        for row in rows:
            writer.writerow(row)

if __name__ == '__main__':
    rows = get_csv()
    for row in rows:
        original = row['Datetime']
        dt = datetime.strptime(original[:-6], '%m/%d/%Y %I:%M:%S %p')
        dt -= timedelta(hours=7)
        row['Datetime'] = dt
    rows.sort(key=lambda row: row['Datetime'])
    for row in rows:
        row['Time'] = row['Datetime'].strftime('%I:%M:%S %p')
        del row['Datetime']
    write_csv(rows)
