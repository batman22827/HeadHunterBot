import os
import sqlite3




outpath = os.path.join(os.getcwd(), 'data')

connection = sqlite3.connect("data/db.sqlite3",check_same_thread=False) 
cursor = connection.cursor() 
# profiles table
cursor.execute("""create table if not exists config
        (vacancy TEXT, 
        only_name bool, 
        only_name_company bool,
        only_description bool, 
        specialization TEXT, 
        region TEXT, 
        earnings TEXT,
        exp TEXT,
        employment TEXT,
        schedule TEXT

        )""")
connection.commit()



def get_config(config):
        res = cursor.execute(f"select {config} from config").fetchone()
        if res is None:
                return None
        return cursor.execute(f"select {config} from config").fetchone()[0] 



def write_config(row,value):
        res = cursor.execute(f"select {row} from config").fetchone()
        if res is None:
                cursor.execute(f"INSERT OR IGNORE INTO config ({row}) VALUES (?)", (value,))
        else:
                cursor.execute(f"update config set {row} = ?", [value]) 
        connection.commit()    

