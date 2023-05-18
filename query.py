import sqlite3
from datetime import datetime 

class sqliteHandle:

    def __init__(self) -> None:
        self.conn = sqlite3.connect('test.db',check_same_thread=False)
        self.cur = self.conn.cursor()
        self.__checktable()


    def __createTable(self):
        self.conn.execute('''CREATE TABLE data
         (time TEXT PRIMARY KEY     NOT NULL,
         temp           INT    NOT NULL,
         moisture            INT     NOT NULL,
         smoisture         INT      NOT NULL);''')
        
    def __checktable(self):
        try:
            self.cur.execute("SELECT * FROM data")
        except : 
            self.__createTable()

    def addData(self , dicto : dict) : 
        records =  [datetime.now().strftime("%m/%d/%Y, %H:%M:%S")]
        for keys in dicto : 
            records.append(dicto[keys])

        self.cur.execute("INSERT INTO data VALUES (?,?,?,?)", records)
        self.conn.commit()
        print(dicto)