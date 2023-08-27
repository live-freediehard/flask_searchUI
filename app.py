#app.py
from flask import Flask, render_template, request, jsonify
import sqlite3
import pandas as pd
     
app = Flask(__name__)
     
app.secret_key = "j998qwm3298234jn"

dbval = pd.read_csv("data.csv")
print(dbval)
db = sqlite3.connect("file::memory:?cache=shared", uri=True)
dbval.to_sql('dbdata', con=db)
createIndex = "CREATE unique INDEX index_f_name ON dbdata(filename)"
sqliteCursor = db.cursor()
print(sqliteCursor.execute(createIndex))

print("index")
print(sqliteCursor)

@app.route('/')
def index():
    return render_template('index.html')
  
@app.route("/ajaxlivesearch",methods=["POST","GET"])
def ajaxlivesearch():
    
    global sqliteCursor
    db = sqlite3.connect("file::memory:?cache=shared", uri=True)
    cur = db.cursor()
    print("ajax")
    print(cur.execute('select * from dbdata').fetchall())


    if request.method == 'POST':
        search_word = request.form['query']
        print(search_word)
        if search_word == '':
            query = "SELECT * from dbdata"
            cur.execute(query)
            fdata = cur.fetchall()
            print("inside search_Blank")
            print(fdata)
        else:
            tr='SELECT * FROM dbdata where filename like \'%'+search_word+'%\'' 
            print(tr)	    
            cur.execute(tr)
            
            fdata = cur.fetchall()
            numrows = len(fdata)
            print("inside search VALUES -->"+str(numrows))
            print(fdata)
    return jsonify({'htmlresponse': render_template('response.html', fdata=fdata, numrows=numrows)})
     
if __name__ == "__main__":
    app.run(debug=True)