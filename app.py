from flask import Flask, render_template, request, redirect
from datetime import date

app = Flask(__name__)

tasks = []
done_tasks = []

# ---------------- AI LOGIC ----------------
def agentic_ai_recommendation(tasks):
    if not tasks:
        return "No tasks yet 🚀"

    today = date.today()
    priority_order = {"High": 1, "Medium": 2, "Low": 3}

    sorted_tasks = sorted(
        tasks,
        key=lambda x: (
            date.fromisoformat(x["deadline"]),
            priority_order[x["priority"]]
        )
    )

    top_task = sorted_tasks[0]
    task_date = date.fromisoformat(top_task["deadline"])

    if task_date == today:
        return f"🔥 Do '{top_task['name']}' today (urgent)"
    elif task_date < today:
        return f"⚠️ '{top_task['name']}' is overdue!"
    else:
        return f"📅 Plan '{top_task['name']}' next"


# ---------------- ROUTES ----------------
@app.route("/")
def index():
    ai_suggestion = agentic_ai_recommendation(tasks)
    today = date.today()

    today_list = []
    upcoming_list = []
    overdue_list = []

    for t in tasks:
        task_date = date.fromisoformat(t["deadline"])

        if task_date == today:
            today_list.append(t)
        elif task_date > today:
            upcoming_list.append(t)
        else:
            overdue_list.append(t)

    priority_order = {"High": 1, "Medium": 2, "Low": 3}

    today_list.sort(key=lambda x: priority_order[x["priority"]])
    upcoming_list.sort(key=lambda x: (
        date.fromisoformat(x["deadline"]),
        priority_order[x["priority"]]
    ))
    overdue_list.sort(key=lambda x: (
        date.fromisoformat(x["deadline"]),
        priority_order[x["priority"]]
    ))

    # ---------------- FIXED METRICS ----------------
    total_tasks = len(tasks) + len(done_tasks)

    if total_tasks == 0:
        efficiency = 0
        on_time_rate = 0
    else:
        completed = len(done_tasks)

        efficiency = int((completed / total_tasks) * 100)

        on_time_completed = 0
        for t in done_tasks:
            task_date = date.fromisoformat(t["deadline"])
            if task_date >= today:
                on_time_completed += 1

        if completed == 0:
            on_time_rate = 0
        else:
            on_time_rate = int((on_time_completed / completed) * 100)

    return render_template(
        "index.html",
        today_tasks=today_list,
        upcoming_tasks=upcoming_list,
        done_tasks=done_tasks,
        overdue_tasks=overdue_list,
        efficiency=efficiency,
        on_time_rate=on_time_rate,
        ai_suggestion=ai_suggestion
    )


@app.route("/add", methods=["POST"])
def add():
    tasks.append({
        "id": len(tasks) + len(done_tasks) + 1,
        "name": request.form["name"],
        "priority": request.form["priority"],
        "deadline": request.form["deadline"]
    })
    return redirect("/")


@app.route("/done/<int:id>")
def done(id):
    global tasks, done_tasks
    for t in tasks:
        if t["id"] == id:
            done_tasks.append(t)
            tasks.remove(t)
            break
    return redirect("/")


@app.route("/undo/<int:id>")
def undo(id):
    global tasks, done_tasks
    for t in done_tasks:
        if t["id"] == id:
            tasks.append(t)
            done_tasks.remove(t)
            break
    return redirect("/")


@app.route("/delete/<int:id>")
def delete(id):
    global tasks, done_tasks
    tasks = [t for t in tasks if t["id"] != id]
    done_tasks = [t for t in done_tasks if t["id"] != id]
    return redirect("/")


# ---------------- RUN APP ----------------
if __name__ == "__main__":
    app.run(debug=True)