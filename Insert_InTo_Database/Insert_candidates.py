import csv
import warnings
warnings.filterwarnings("ignore")
from Utilities.DB_Connection import conn

# ********************************* INSERT INTO CANDIDATE TABLE ***************************************
curs = conn.cursor()
with open('C:/Karthik/New_Projects/Hybrid_Driven/Test_Data/Insert_Candidates.csv', 'r') as f:
    reader = csv.reader(f)
    all_value = []
    next(reader)  # SKIP THE HEADER
    for row in reader:
        curs.execute('INSERT INTO test.candidate VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)', row)
        conn.commit()
