#update

import pymysql

# Replace these values with your actual database information
host = 'your_host'
user = 'your_user'  # Usually 'root'
password = 'your_password'
database = 'your_database'

# Connect to the MySQL database
con = pymysql.connect(
    host=host,
    user=user,
    password=password,
    database=database,
)

cur = con.cursor()

# Example UPDATE query
sql_query = "UPDATE your_table SET column1 = %s WHERE condition"
new_value = 'new_value'
cur.execute(sql_query, (new_value,))

# Commit the changes to the database
con.commit()

# Close the cursor and connection
cur.close()
con.close()
