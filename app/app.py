from flask import Flask, render_template
import pymysql
import os
import time

app = Flask(__name__)

# קבלת משתני סביבה
DB_HOST = os.environ.get("DB_HOST", "db")
DB_PORT = int(os.environ.get("DB_PORT", 3306))
DB_NAME = os.environ.get("DB_NAME", "mysql_db")
DB_USER = os.environ.get("DB_USER", "nadav")
DB_PASSWORD = os.environ.get("DB_PASSWORD", "password")

# המתנה עד שה-DB מוכן
while True:
    try:
        connection = pymysql.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD,
            database=DB_NAME,
            port=DB_PORT
        )
        print("Connected to MySQL")
        break
    except pymysql.MySQLError:
        print("Waiting for MySQL...")
        time.sleep(1)

@app.route("/")
def index():
    with connection.cursor() as cursor:
        # צור טבלה אם לא קיימת
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS hits_counter (
                id INT AUTO_INCREMENT PRIMARY KEY,
                count INT NOT NULL
            )
        """)
        connection.commit()

        # בדיקה אם יש שורה קיימת
        cursor.execute("SELECT count FROM hits_counter WHERE id=1")
        result = cursor.fetchone()

        if result:
            new_count = result[0] + 1
            cursor.execute("UPDATE hits_counter SET count=%s WHERE id=1", (new_count,))
        else:
            new_count = 1
            cursor.execute("INSERT INTO hits_counter (count) VALUES (%s)", (new_count,))
        connection.commit()

    return render_template("index.html", count=new_count)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
