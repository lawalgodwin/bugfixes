#!/bin/python3

from flask import Flask, render_template, request, abort
from flask_mysqldb import MySQL

app = Flask(__name__)

# configuring mysql

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'nedutechboy'
app.config['MYSQL_DB'] = 'flask'

mysql = MySQL(app)


@app.route('/form')
def form():
    return render_template('form.html')


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'GET':
        return "Login via the login Form"

    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        try:
            cursor = mysql.connection.cursor()
            query = "INSERT INTO info_table(name, age) VALUES(%s,%s)"
            data = (name, age)
            cursor.execute(query, data)
            mysql.connection.commit()
            cursor.close()
            return 'Done!!'
        except Exception as ex:
            print(f"Error connecting the DB: ${ex}")
            abort(500)


if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)
