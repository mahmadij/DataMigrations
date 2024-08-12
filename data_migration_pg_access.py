import psycopg2
import pyodbc 

conn = psycopg2.connect(
  host="host_name",
  database="db_name",
  user="username",
  password="password",
  port=0 # this is an optional parametr and it is an integer
)
cursor = conn.cursor()
cursor.execute("select column1,column2,column3 from source_table")
data = cursor.fetchall()

conn_str = (
    r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
    r'DBQ=the_path_to_your_access_database.accdb;'
)
access_conn = pyodbc.connect(conn_str)
access_cursor = access_conn.cursor()

for row in data:
    access_cursor.execute(
        "INSERT INTO target_table (column1,column2,column3,data_extracted_DT) VALUES (?,?,?,Date())", row
    )

access_conn.commit()
cursor.close()
conn.close()
access_cursor.close()
access_conn.close()