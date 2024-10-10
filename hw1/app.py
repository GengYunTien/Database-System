import os
from flask import Flask, render_template, request, redirect, url_for
import mysql.connector
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__, static_folder='static')

db_config = {
    'user': os.getenv('MYSQL_USER'),
    'password': os.getenv('MYSQL_PASSWORD'),
    'host': os.getenv('MYSQL_HOST'),
    'database': os.getenv('MYSQL_DATABASE')
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add', methods=['POST'])
def add():
    name = request.form['name']
    team = request.form['team']
    player = request.form['player']

    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO mlb (name, team, player) VALUES (%s, %s, %s)", (name, team, player))
    conn.commit()
    cursor.close()
    conn.close()
    
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)