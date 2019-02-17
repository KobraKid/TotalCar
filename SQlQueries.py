
# coding: utf-8

# In[7]:


import sqlite3
from sqlite3 import Error
 
def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
 
    return None


# In[14]:


def create_total_car(conn):
    cur = conn.cursor()
    cur.execute("CREATE TABLE if not exists totalcar(userid text,vehicalid text,od_oil int,od_fuel int,od_tyre int)")
    cur.execute("INSERT INTO totalcar values('abc','xyz',1,2,3)")
 
    #rows = cur.fetchall()
 
    #for row in rows:
        #print(row)

def select_all_tasks(conn):
    """
    Query all rows in the tasks table
    :param conn: the Connection object
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM totalcar")
 
    rows = cur.fetchall()
 
    for row in rows:
        print(row)
        
def main():
    database = "/Users/admin/Desktop/Spring 2019/MyProjectIdea/pythonsqlite.db"
 
    # create a database connection
    conn = create_connection(database)
    with conn:
        create_total_car(conn)
        print("1. Query task by priority:")
        select_all_tasks(conn)
if __name__ == '__main__':
    main()

