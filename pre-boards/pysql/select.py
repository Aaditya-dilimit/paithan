#select
import pymysql

# Connect to the MySQL database
con = pymysql.connect(
    host='your_host', 
    user='your_user', #root
    password='your_password',
    database='your_database',
)

cur = con.cursor()

your_table = input("Table name")

sql_query = f"SELECT * FROM {your_table}"
cur.execute(sql_query)
results = cur.fetchall()

for row in results:
    print(row)

cur.close()
con.close()
