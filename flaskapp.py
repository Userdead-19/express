from flask import Flask,request,jsonify,render_template
import sqlite3
app=Flask(__name__)

@app.route('/',methods=["GET"])
def hello():
     if request.method=="GET":
         return render_template("index.html")
@app.route('/iv',methods=["GET"])
def iv():
    return render_template("index2.html")

@app.route("/create",methods=["GET"])
def create():
    conn=sqlite3.connect("mydata.db")
    c=conn.cursor()
    c.execute("""CREATE TABLE fort (
         name text,
         pass text,
         pin text
    )""")
    conn.commit()
    c.close()
    return jsonify("done")


@app.route("/insert",methods=["GET"])
def insert():
    conn=sqlite3.connect("mydata.db")
    c=conn.cursor()
    data=request.args.get("message")
    passw=request.args.get("pass")
    pin=request.args.get("pin")
    c.execute("INSERT INTO fort VALUES(?,?,?)",[data,passw,pin])
    conn.commit()
    c.close()
    return jsonify("done")

@app.route("/ptch",methods=["GET"])
def check():
    if request.method=="GET":
        data=request.args.get("message")
        data1=request.args.get("pass")
        conn=sqlite3.connect("mydata.db")
        c=conn.cursor()
        c.execute("SELECT * FROM fort WHERE name LIKE ? AND pass LIKE ?",[data,data1])
        temp=c.fetchall()
        return jsonify(temp)

@app.route("/select",methods=["GET"])
def getall():
    conn=sqlite3.connect("mydata.db")
    c=conn.cursor()
    c.execute("SELECT * FROM fort")
    conn.commit()
    temp=c.fetchall()
    c.close()
    return jsonify(temp)

@app.route("/drop",methods=["GET"])
def deleter():
    conn=sqlite3.connect("mydata.db")
    c=conn.cursor()
    c.execute("DROP TABLE fort ")
    conn.commit()
    c.close()
    return jsonify("deleted successfully")

@app.route("/create/new",methods=["GET"])
def create1():
    conn=sqlite3.connect("mydata.db")
    c=conn.cursor()
    c.execute("""CREATE TABLE todo (
         items text
    )""")
    conn.commit()
    c.close()
    return jsonify("done")

@app.route("/todo/add",methods=["GET"])
def addtodo():
    conn=sqlite3.connect("mydata.db")
    c=conn.cursor()
    data=request.args.get("addtodo")
    c.execute("INSERT INTO todo VALUES(?)",[data])
    conn.commit()
    c.close()
    return jsonify("done")

@app.route("/todo/pageinput",methods=["GET"])
def givetodo():
    conn=sqlite3.connect("mydata.db")
    c=conn.cursor()
    c.execute("SELECT * FROM todo")
    conn.commit()
    temp=c.fetchall()
    c.close()
    return jsonify(temp)

if __name__=="__main__":
   app.run(debug=True,host="0.0.0.0")
