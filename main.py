from flask import Flask , request
import query

app = Flask("__name__")
connection = query.sqliteHandle()

@app.route("/retData", methods = ['POST'])
def retrieveData():
    if request.method != "POST" : 
        return "Not Accepted"

    return "Data"

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

