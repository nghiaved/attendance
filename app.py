from flask import Flask, render_template, request, flash
from werkzeug.utils import redirect
from PIL import Image
import numpy as np
import mysql.connector
from barcode.writer import ImageWriter
from barcode import Code128

app = Flask(__name__)
app.secret_key = 'secret_key'

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="attendance"
)


def get_students():
    cursor = db.cursor()
    cursor.execute("SELECT * FROM students")

    students = []
    for row in cursor:
        students.append({
            "id": row[0],
            "name": row[1],
            "code": row[2]
        })

    return students
    

@app.route("/")
def index():
    return render_template("index.html", students=get_students())


@app.route('/create', methods = ['POST'])
def insert():
    if request.method == "POST":
        code = request.form['code']
        name = request.form['name']
        cursor = db.cursor()

        barcode = Code128(code, writer=ImageWriter())
        barcode_path = 'static/img/' + code
        barcode.save(barcode_path)
        
        cursor.execute("INSERT INTO students (code, name, path) VALUES (%s, %s, %s)", (code ,name, barcode_path + '.png'))
        db.commit()

        flash("Data Inserted Successfully")
        return redirect('/')


@app.route('/delete/<string:id_data>', methods = ['GET'])
def delete(id_data):
    cursor = db.cursor()
    cursor.execute("DELETE FROM students WHERE id=" + id_data)
    db.commit()

    flash("Record Has Been Deleted Successfully")
    return redirect('/')


@app.route('/update', methods= ['POST', 'GET'])
def update():
    if request.method == 'POST':
        id_data = request.form['id']
        code = request.form['code']
        name = request.form['name']

        cursor = db.cursor()
        cursor.execute("""
        UPDATE students SET code=%s, name=%s
        WHERE id=%s
        """, (code, name, id_data))
        db.commit()

        flash("Data Updated Successfully")
        return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)