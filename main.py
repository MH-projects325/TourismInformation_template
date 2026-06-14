import sqlite3
from datetime import datetime

from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
app.secret_key = 'super_secret_key'


def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

db=get_db_connection()

db.execute('''
CREATE TABLE IF NOT EXISTS comments_spain (
id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT,
comment TEXT,
time TEXT
)
''')

db.execute('''
CREATE TABLE IF NOT EXISTS comments_france (
id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT,
comment TEXT,
time TEXT
)
''')

db.execute('''
CREATE TABLE IF NOT EXISTS comments_turkey (
id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT,
comment TEXT,
time TEXT
)
''')

db.commit()
db.close()



@app.route('/',methods=['GET','POST'])
def Spain():

    if request.method == 'POST':
        name = request.form['name']
        comment = request.form['comment']
        time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        db = get_db_connection()
        db.execute('INSERT INTO comments_spain (name, comment, time) VALUES (?,?,?)',(name,comment,time))

        db.commit()
        db.close()

        return  redirect(url_for('Spain'))
    db = get_db_connection()
    comments = db.execute('SELECT * FROM comments_spain').fetchall()
    db.close()


    return render_template("Spain.html",comments=comments)

@app.route('/france',methods=['GET','POST'])
def France():

    if request.method == 'POST':
        name = request.form['name']
        comment = request.form['comment']
        time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        db = get_db_connection()
        db.execute('INSERT INTO comments_france (name,comment,time) VALUES (?,?,?)',(name,comment,time))

        db.commit()
        db.close()

        return redirect(url_for('France'))

    db = get_db_connection()
    comments = db.execute('SELECT * FROM comments_france').fetchall()
    db.close()




    return render_template("France.html",comments=comments)

@app.route('/turkey',methods=['GET','POST'])
def Turkey():
    if request.method == 'POST':
        name = request.form['name']
        comment = request.form['comment']
        time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        db = get_db_connection()
        db.execute('INSERT INTO comments_turkey (name,comment,time) VALUES (?,?,?)', (name, comment, time))

        db.commit()
        db.close()

        return redirect(url_for('Turkey'))

    db = get_db_connection()
    comments = db.execute('SELECT * FROM comments_turkey').fetchall()
    db.close()


    return render_template("Turkey.html",comments=comments)


if __name__ == '__main__':
    app.run(debug=True)

else:
    pass