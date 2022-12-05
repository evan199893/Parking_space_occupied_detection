from flask import Flask
from flask import render_template
from flask_bootstrap import Bootstrap
import pymysql

app = Flask(__name__)
bootstrap = Bootstrap(app)

@app.route('/')

def index():
    db_settings = {
        "host": "127.0.0.1",
        "port": 3306,
        "user": "root",
        "password": "ttv021015",
        "db": "parking_lot",
        "charset": "utf8"
    }
    db = pymysql.connect(**db_settings)
    cursor = db.cursor()
    sql = "SELECT * FROM information_table"
    cursor.execute(sql)
    u = cursor.fetchall()
    db.close()
    return render_template('index.html',u=u)

if __name__ == '__main__':
    app.run()