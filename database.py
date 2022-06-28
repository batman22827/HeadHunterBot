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
        industry TEXT,
        region TEXT, 
        earnings TEXT,
        exp TEXT,
        employment TEXT,
        schedule TEXT,
        resume TEXT

        )""")

cursor.execute("""create table if not exists vacancy_urls
       (url TEXT,
       checked bool

        )""")        
connection.commit()



def get_config(config):
        res = cursor.execute(f"select {config} from config").fetchone()
        if res is None:
                return None
        return cursor.execute(f"select {config} from config").fetchone()[0] 

def get_all_urls():
        return cursor.execute("select url from vacancy_urls where checked=?",[False]).fetchall()

def write_config(row,value):
        res = cursor.execute(f"select {row} from config").fetchone()
        if res is None:
                cursor.execute(f"INSERT OR IGNORE INTO config ({row}) VALUES (?)", (value,))
        else:
                cursor.execute(f"update config set {row} = ?", [value]) 
        connection.commit()    


def write_url(url,check):
        res = cursor.execute(f"select url from vacancy_urls where url=?",[url]).fetchone()
        if res is None:
                cursor.execute(f"INSERT OR IGNORE INTO vacancy_urls (url,checked) VALUES (?,?)", (url,check))
        else:
                cursor.execute(f"update vacancy_urls set checked = ?", [check]) 
        connection.commit()    