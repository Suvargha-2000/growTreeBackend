from flask import Flask , request
import sqlite3
from datetime import datetime 

class sqliteHandle:

    def __init__(self) -> None:
        self.conn = sqlite3.connect('test.db',check_same_thread=False)
        self.cur = self.conn.cursor()
        self.__checktable()


    def __createTable(self):
        self.conn.execute('''CREATE TABLE data
         (time TIMESTAMP PRIMARY KEY     NOT NULL,
         temp           INT    NOT NULL,
         moisture            INT     NOT NULL,
         smoisture         INT      NOT NULL);''')
        
    def __checktable(self):
        try:
            self.cur.execute("SELECT * FROM data")
        except : 
            self.__createTable()

    def addData(self , dicto : dict) : 
        records =  [datetime.now()]
        for keys in dicto : 
            records.append(dicto[keys])

        self.cur.execute("INSERT INTO data VALUES (?,?,?,?)", records)
        self.conn.commit()
        print(dicto)

    def retData(self , dates):
        data = self.cur.execute("SELECT * FROM data where time between DATE(?) and DATE(?)" , (dates[0] , dates[1]))
        return data

app = Flask("__name__")
connection = sqliteHandle()

@app.route("/retData", methods = ['POST'])
def retrieveData():
    if request.method != "POST" : 
        return "Not Accepted"

    data = [request.get_json()["sDate"] , request.get_json()["eDate"]]
    
    data = connection.retData(data)
    x = []
    for i in data : 
        x.append(i)

    return x

@app.route("/postData" , methods = ['POST'])
def postData():
    if request.method != "POST" : 
        return "Not Accepted"
    dicto = {}
    dicto["temp"] = request.get_json()["temp"]
    dicto["moisture"] = request.get_json()["moisture"]
    dicto["smoisture"] = request.get_json()["smoisture"]
    connection.addData(dicto)
    return "recv"


if __name__ == "__main__" :
    app.run()

