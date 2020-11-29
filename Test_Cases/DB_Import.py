import csv
import pandas as pd
from Utilities import DB_Connection
from Utilities.DB_Connection import conn

# curs = conn.cursor()
# curs.execute("select * FROM entries WHERE scn =123456762")
# print(curs.fetchall())


# with open('C:/Karthik/Execeptional_entries.csv', 'r') as f:
#     reader = csv.reader(f)
#     header = next(reader)
#     rows = [header] + [[int(row[0]), row[1], row[2], [int(row[3])]] for row in reader if row]
# for row in rows:
#     print(row)

# ----------------------------WORKING-----------------------------------------------
# with open('C:/Karthik/Execeptional_entries.csv', 'r') as csv_file:
#     csv_file = csv.reader(csv_file)
#     all_value = []
#     for row in csv_file:
#         # value = (row[0], row[1], row[2], row[3])
#
#         value = [(str(row[0])), row[1], row[2], [str(row[3])]]
#         all_value.append(value)
#
# query = "INSERT INTO entries (centre_id, product_code, product_level, scn) VALUES (?,?,?,?)"
# curs = conn.cursor()
# curs.executemany(query, all_value)
# conn.commit()
# -------------------------------WORKING----------------------------------------
df = pd.read_csv('C:/Karthik/Execeptional_entries.csv', header=0)
# # print(df)
# query = (df.iloc[:, [2]])
# for x in query:
#     print(query)
curs = conn.cursor()
row_count = 0
curs.execute("select * FROM entries WHERE scn = 'query'")

#     # print(curs.fetchall())
#
#     # Insert DataFrame to Table
#     for row in df.itertuples():
#         use = 'python'
#         curs.execute('''
#                     INSERT INTO entries (product_code, product_level, completion_date, scn)
#                     VALUES (%s,%s,%s,%s)
#                     ''',
#                      row.product_code,
#                      row.product_level,
#                      row.completion_date,
#                      row.scn
#                      )
#     conn.commit()


