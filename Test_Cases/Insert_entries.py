import csv
import warnings
import pandas as pd
from Utilities.DB_Connection import conn

warnings.filterwarnings('ignore')

# ********************************* SELECT QUERY - ENTRIES TABLE ***************************************
curs = conn.cursor()
data = pd.read_csv('C:/Karthik/New_Projects/Hybrid_Driven/Test_Data/Exceptional_Entries.csv', index_col=False)
# curs.execute("select * from entries WHERE centre_id = 1032 AND product_code='G1J6' AND product_level=16 AND "
#              "scn=123456866")
csv_scn = (data.iloc[:, 4])
print('hai karthik',csv_scn)

curs.execute("select * from entries WHERE centre_id = 1032 AND product_code='G1J6' AND product_level=16 AND scn=csv_scn")
rows = curs.fetchall()
print(rows)

# print(df.iloc[:, 4])
# a = (df.iloc[:, 4])
# for row in rows:
#     print(row[13])
#     print(data.iloc[:, 4])

# with open('C:/Karthik/New_Projects/Hybrid_Driven/Test_Data/Exceptional_Entries.csv', 'r') as f:
#     reader = csv.reader(f)
#
# all_value = [] for row in reader: query = curs.execute("select scn, centre_id, product_code, product_level,
# completion_date, result from entries " "where scn = 'row[4]'") data = curs.fetchall() print(data)


# ********* READ THE NUMBER OF ROWS IN THE CSV FILE ******************
# value = len(list(reader))
# print('TOTAL NUMBER OF ROWS IN THE CSV FILE', value)
