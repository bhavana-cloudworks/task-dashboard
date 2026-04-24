from flask import Flask, render_template, request, redirect, url_for
import sqlite3
from datetime import datetime, date

app = Flask(__name__)

def init_db():
    conn = sqlite3.connect("tasks.db")
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        priority TEXT,
        deadline TEXT,
        status TEXT
    )''')
    conn.commit()
    conn.close()

@app.route('/')
def home():
    conn = sqlite3.connect("tasks.db")
    c = conn.cursor()
    c.execute("SELECT * FROM tasks")
    tasks = c.fetchall()
    conn.close()

    today = date.today()
    today_tasks, upcoming_tasks, done_tasks = [], [], []
    completed = 0

    for t in tasks:
        if t[4] == "Done":
            done_tasks.append(t)
            completed += 1
        else:
            if t[3] and datetime.fromisoformat(t[3]).date() <= today:
                today_tasks.append(t)
            else:
                upcoming_tasks.append(t)

    efficiency = int((completed / len(tasks)) * 100) if tasks else 0

    # ✅ ADD THIS LINE (for greeting)
    now_hour = datetime.now().hour

    return render_template(
        "index.html",
        today_tasks=today_tasks,
        upcoming_tasks=upcoming_tasks,
        done_tasks=done_tasks,
        efficiency=efficiency,
        now_hour=now_hour   # ✅ PASS TO HTML
    )

@app.route('/add', methods=['POST'])
def add():
    conn = sqlite3.connect("tasks.db")
    c = conn.cursor()
    c.execute("INSERT INTO tasks VALUES(NULL,?,?,?,?)",
              (request.form['name'], request.form['priority'], request.form['deadline'], "Pending"))
    conn.commit()
    conn.close()
    return redirect(url_for('home'))

@app.route('/done/<int:id>')
def done(id):
    conn = sqlite3.connect("tasks.db")
    c = conn.cursor()
    c.execute("UPDATE tasks SET status='Done' WHERE id=?", (id,))
    conn.commit()
    conn.close()
    return redirect(url_for('home'))

@app.route('/undo/<int:id>')
def undo(id):
    conn = sqlite3.connect("tasks.db")
    c = conn.cursor()
    c.execute("UPDATE tasks SET status='Pending' WHERE id=?", (id,))
    conn.commit()
    conn.close()
    return redirect(url_for('home'))

@app.route('/delete/<int:id>')
def delete(id):
    conn = sqlite3.connect("tasks.db")
    c = conn.cursor()
    c.execute("DELETE FROM tasks WHERE id=?", (id,))
    conn.commit()
    conn.close()
    return redirect(url_for('home'))

if __name__ == '__main__':
    init_db()
    app.run(debug=True)