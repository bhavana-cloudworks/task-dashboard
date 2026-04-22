from flask import Flask, render_template, request, redirect
import sqlite3
from datetime import datetime, date

app = Flask(__name__)

# ---------- DB ----------
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

# ---------- SCORE ----------
def task_score(task):
    id, name, priority, deadline, status = task

    score = {"High":5, "Medium":3, "Low":1}.get(priority,1)

    if deadline:
        d = datetime.fromisoformat(deadline).date()
        days = (d - date.today()).days

        if days < 0:
            score += 5
        elif days == 0:
            score += 4
        elif days == 1:
            score += 2

    return score

# ---------- AI ----------
def get_focus(tasks):
    pending = [t for t in tasks if t[4] != "Done"]

    if not pending:
        return None, None

    pending.sort(key=lambda t: -task_score(t))

    today = date.today()

    today_tasks = [t for t in pending if t[3] and datetime.fromisoformat(t[3]).date() <= today]
    upcoming = [t for t in pending if t not in today_tasks]

    return (
        today_tasks[0] if today_tasks else None,
        upcoming[0] if upcoming else None
    )

# ---------- HOME ----------
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

    today_focus, upcoming_focus = get_focus(tasks)

    return render_template("index.html",
        today_tasks=today_tasks,
        upcoming_tasks=upcoming_tasks,
        done_tasks=done_tasks,
        efficiency=efficiency,
        today_focus=today_focus,
        upcoming_focus=upcoming_focus,
        today=today.isoformat()
    )

# ---------- ADD ----------
@app.route('/add', methods=['POST'])
def add():
    conn = sqlite3.connect("tasks.db")
    c = conn.cursor()

    c.execute("INSERT INTO tasks VALUES(NULL,?,?,?,?)",
              (request.form['name'],
               request.form['priority'],
               request.form['deadline'],
               "Pending"))

    conn.commit()
    conn.close()
    return redirect('/')

# ---------- DONE ----------
@app.route('/done/<int:id>')
def done(id):
    conn = sqlite3.connect("tasks.db")
    c = conn.cursor()
    c.execute("UPDATE tasks SET status='Done' WHERE id=?", (id,))
    conn.commit()
    conn.close()
    return redirect('/')

# ---------- UNDO ----------
@app.route('/undo/<int:id>')
def undo(id):
    conn = sqlite3.connect("tasks.db")
    c = conn.cursor()
    c.execute("UPDATE tasks SET status='Pending' WHERE id=?", (id,))
    conn.commit()
    conn.close()
    return redirect('/')

# ---------- RUN ----------
if __name__ == '__main__':
    init_db()
    app.run(debug=True)