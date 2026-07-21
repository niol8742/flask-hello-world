from flask import Flask
import psycopg
import os
app = Flask(__name__)

@app.route("/")
def index():
    return "Hello World from Nick OLeary in 3308"

@app.route("/db_test")
def db_test():
    conn = None
    try:
        conn = psycopg.connect("postgresql://niol8742db_user:vC051v0HBBHJEroQn7HFFZhU4sR6whRO@dpg-d9fp1q3bc2fs73bl98qg-a/niol8742db")
        return "Database connection successful"
    except Exception as e:
        return f"Database connection failed: {e}"
    finally:
        if conn is not None:
            conn.close()
            
@app.route('/db_create')
def creating():
    conn = psycopg.connect("postgresql://niol8742db_user:vC051v0HBBHJEroQn7HFFZhU4sR6whRO@dpg-d9fp1q3bc2fs73bl98qg-a/niol8742db")
    cur = conn.cursor()

    cur.execute('''
        CREATE TABLE IF NOT EXISTS Basketball (
            First varchar(255),
            Last varchar(255),
            City varchar(255),
            Name varchar(255),
            Number int
        );
    ''')

    conn.commit()
    conn.close()

    return "Basketball Table Successfully Created"

@app.route('/db_insert')
def inserting():
    conn = psycopg.connect("postgresql://niol8742db_user:vC051v0HBBHJEroQn7HFFZhU4sR6whRO@dpg-d9fp1q3bc2fs73bl98qg-a/niol8742db")
    cur = conn.cursor()

    cur.execute('''
        INSERT INTO Basketball (First, Last, City, Name, Number)
        Values
        ('Jayson', 'Tatum', 'Boston', 'Celtics', 0),
        ('Stephen', 'Curry', 'San Francisco', 'Warriors', 30),
        ('Nikola', 'Jokic', 'Denver', 'Nuggets', 15),
        ('Kawhi', 'Leonard', 'Los Angeles', 'Clippers', 2);
    ''')

    conn.commit()
    conn.close()

    return "Basketball Table Successfully Populated"

@app.route('/db_select')
def selecting():
    conn = psycopg.connect("postgresql://niol8742db_user:vC051v0HBBHJEroQn7HFFZhU4sR6whRO@dpg-d9fp1q3bc2fs73bl98qg-a/niol8742db")
    cur = conn.cursor()

    cur.execute('''
        SELECT * FROM Basketball;
    ''')

    records = cur.fetchall()
    conn.close()

    response_string = ""
    response_string += "<table>"

    for player in records:
        response_string += "<tr>"

        for info in player:
            response_string += "<td>{}</td>".format(info)

        response_string += "</tr>"

    response_string += "</table>"

    return response_string