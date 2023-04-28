import sqlite3
import os
import pandas as pd



class DbUtils:
    def __init__(self, db_name):
        self.db = db_name
    
    def get_db(self):
        # eastablish connection with db
        db_path = os.getcwd() + "/database/{}".format(self.db)
        # db_path = os.getcwd() + "/database/{}".format(db)
        conn = sqlite3.connect(db_path,check_same_thread=False)
        cursor = conn.cursor()
        return conn, cursor

    def append_sqlite_table(self,df,table_name):
        conn , cur = self.get_db() 
        # convert the dataframe to a list of tuples
        tuple_list = [tuple(row) for row in df.values.tolist()]
        # loop through list
        for value in tuple_list:
        # Construct the SQL statement
            sql = f"INSERT OR IGNORE INTO {table_name} VALUES {value}"
            cur.execute(sql)

            # Commit the changes to the database
            conn.commit()
        # Close the connection to the SQLite database
        conn.close()

    def get_id_list(self, table_name):
        # Connect to the SQLite database
        conn , cur = self.get_db() 

        # Create a cursor object
        cur = conn.cursor()

        # Execute a SELECT statement to retrieve the 'id' column data from the specified table
        cur.execute(f"SELECT id FROM {table_name}")

        # Fetch all rows returned by the SELECT statement
        rows = cur.fetchall()

        # Extract the 'id' values from the rows and store them in a list
        id_list = [row[0] for row in rows]

        # Close the cursor and connection
        cur.close()
        conn.close()
        # Return the list of 'id' values
        return id_list
    
    def get_recent_sentiments(self, table_name):
        # Connect to the SQLite database
        conn , cur = self.get_db() 

        # Query for the 10 most recent positive texts
        query = f'''
            SELECT text, sentiment_label
            FROM  {table_name}
            WHERE sentiment_label IN ('pos', 'neg')
            ORDER BY created_at DESC
            LIMIT 20
        '''
        cur.execute(query)
        text = cur.fetchall()
        # Close the cursor and connection
        cur.close()
        conn.close()
        return text
    
    def get_id_text(self, table_name, id_list):
        # Connect to the SQLite database
        conn , cur = self.get_db() 

        # Query for the 10 most recent positive texts
        query = f'''
            SELECT text, sentiment_label
            FROM {table_name}
            WHERE id IN {id_list}
        '''
        cur.execute(query)
        text = cur.fetchall()
        # Close the cursor and connection
        cur.close()
        conn.close()
        return text
    
# db_utils = DbUtils("tweet.db")
# print(db_utils.get_recent_sentiments("shein_tweets"))