#create table
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

# Replace 'your_table' and the column definitions with your actual table and column names
table_creation_query = """
CREATE TABLE your_table (
    id INT AUTO_INCREMENT PRIMARY KEY,
    column1 VARCHAR(255),
    column2 INT,
    column3 DATE
    -- Add more columns as needed
);
"""

# Execute the query to create the table
cur.execute(table_creation_query)

# Commit the changes to the database
con.commit()

# Close the cursor and connection
cur.close()
con.close()
