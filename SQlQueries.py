
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


# In[38]:


def create_total_car(conn):
    cur = conn.cursor()
    cur.execute("CREATE TABLE if not exists totalcar(userid text,vehicalid text,od_oil int,od_fuel int,od_tyre int)")
    cur.execute("INSERT INTO totalcar values('abc','xyz',1,2,3)")
 
    #rows = cur.fetchall()
 
    #for row in rows:
        #print(row)

def find_user(conn,uid):
    cur = conn.cursor()
    cur.execute("SELECT * FROM totalcar where userid='%s'"%uid)
 
    rows = cur.fetchall()
    return rows

def insert_user(conn,uid,vid):
    cur = conn.cursor()
    cur.execute("insert into totalcar values('%s','%s',%i,%i,%i)"%(uid,vid,0,0,0))
    
def select_all_user(conn):
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

def update_od_fuel(con,userid,vehicleid, odometer, threshold):
    #filled fueltank at odometer
    cur = conn.cursor()
    cur.execute("UPDATE totalcar set od_fuel=%i where userid='%s' and vehicalid='%s'"%(odometer+threshold,userid,vehicleid))
    rows = cur.fetchall()
    for row in rows:
        print(row)

""""def update_od_oil(con,userid,vehicleid, odometer, threshold):
    cur = conn.cursor()
    cur.execute("UPDATE totalcar set od_oil=%i where userid=%s and vehicalid=%s"%(odometer+threshold,userid,vehicleid))
    
def update_od_tire(con,userid,vehicleid, odometer, threshold):
    cur = conn.cursor()
    cur.execute("UPDATE totalcar set od_tyre=%i where userid=%s and vehicalid=%s"%(odometer+threshold,userid,vehicleid))
        
def main():
    database = "/Users/admin/Desktop/Spring 2019/MyProjectIdea/pythonsqlite.db"
 
    # create a database connection
    conn = create_connection(database)
    return conn
        #create_total_car(conn)
        #select_all_tasks(conn)"""
if __name__ == '__main__':
    conn=main()
    #insert_user(conn,'xyz','abc')
    update_od_fuel(conn,'abc','xyz',100,100)
    #select_all_user(conn)

