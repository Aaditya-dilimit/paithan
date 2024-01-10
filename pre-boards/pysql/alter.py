#Alter table

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

# Replace 'your_table' and the column modifications with your actual table and alterations
alter_table_query = """
ALTER TABLE your_table
    ADD COLUMN new_column VARCHAR(255),
    MODIFY COLUMN existing_column INT,
    DROP COLUMN column_to_remove;
"""

# Execute the query to alter the table
cur.execute(alter_table_query)

# Commit the changes to the database
con.commit()

# Close the cursor and connection
cur.close()
con.close()

'''
Other commands

`ADD COLUMN new_column VARCHAR(255)` adds a new column to the table.
`MODIFY COLUMN existing_column INT` modifies the data type of an existing column.
`DROP COLUMN column_to_remove` removes an existing column from the table.
'''