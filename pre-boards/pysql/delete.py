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

# Example DELETE query
sql_query = "DELETE FROM your_table WHERE condition"
cur.execute(sql_query)

# Commit the changes to the database
con.commit()

# Close the cursor and connection
cur.close()
con.close()
