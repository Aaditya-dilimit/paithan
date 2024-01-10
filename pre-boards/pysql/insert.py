#insert values

import pymysql

# Replace these values with your actual database information
host = 'your_host'
user = 'your_user'  # Usually 'root'
password = 'your_password'
database = 'your_database'
table = 'your_table'

# Connect to the MySQL database
con = pymysql.connect(
    host=host,
    user=user,
    password=password,
    database=database,
)

cur = con.cursor()

# Example values for the new row
column1_value = 'value1'
column2_value = 'value2'
# Add more columns and values as needed

# Construct the INSERT query
sql_query = f"INSERT INTO {table} (column1, column2) VALUES ('{column1_value}', '{column2_value}')"
# Make sure to replace 'column1', 'column2' with your actual column names

# Execute the query
cur.execute(sql_query)

# Commit the changes to the database
con.commit()

# Close the cursor and connection
cur.close()
con.close()
