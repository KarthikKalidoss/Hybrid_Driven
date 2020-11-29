import csv
import pandas as pd

with open('C:/Karthik/Execeptional_entries_empty.csv', 'r') as csv_file:
    csv_dict = [row for row in csv.DictReader(csv_file)]
    if len(csv_dict) == 0:
        print('CSV IS EMPTY')
    else:
        print('CSV IS NOT EMPTY')

df = pd.read_csv('C:/Karthik/Execeptional_entries_empty.csv')
if df.empty:
    print('DATAFRAME - CSV FILE IS EMPTY')
else:
    print('DATAFRAME- CSV FILE IS NOT EMPTY')

csv_row = len(df.axes[0])
print('TOTAL NUMBER OF ROWS IN THE CSV FILE : ', csv_row)
csv_column = len(df.axes[1])
print('TOTAL NUMBER OF COLUMN IN THE CSV FILE : ', csv_column)
