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
            sql = f"INSERT OR IGNORE INTO shein_tweets VALUES {value}"
            cur.execute(sql)

            # Commit the changes to the database
            conn.commit()
        # Close the connection to the SQLite database
        conn.close()
