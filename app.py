from flask import Flask
import psycopg2
import os
app = Flask(__name__)
conn = None
cur = None
try:
    conn = psycopg2.connect("postgresql://niol8742db_user:vC051v0HBBHJEroQn7HFFZhU4sR6whRO@dpg-d9fp1q3bc2fs73bl98qg-a/niol8742db")
    cur = conn.cursor()

    # SQL work goes here

    conn.commit()
    return "Success message here"
except Exception as e:
    if conn is not None:
        conn.rollback()
    return f"Database error: {e}"
finally:
    if cur is not None:
        cur.close()
    if conn is not None:
        conn.close()


@app.route("/")
def index():
    return "Hello World from Nick OLeary in 3308"

@app.route("/db_test")
def db_test():
    conn = None
    try:
        conn = psycopg2.connect("postgresql://niol8742db_user:vC051v0HBBHJEroQn7HFFZhU4sR6whRO@dpg-d9fp1q3bc2fs73bl98qg-a/niol8742db")
        return "Database connection successful"
    except Exception as e:
        return f"Database connection failed: {e}"
    finally:
        if conn is not None:
            conn.close()
