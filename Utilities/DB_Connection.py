import jaydebeapi
import jpype
import _jpype
import os

# ******************************************* DATABASE - CONNECTION ***********************************************
try:
    conn = jaydebeapi.connect('com.ingres.jdbc.IngresDriver'
                              , 'jdbc:ingres://i-tapaculo:CL7/sqadb'
                              , driver_args=['test', 'passmark100']
                              , jars="C:/Karthik/New_Projects/Exceptional_Entries/Sources/iijdbc.jar")
    curs = conn.cursor()
    print(curs.fetchall())
    curs.close()
    conn.close()

except:
    print('No database Connection')
