
# Smart Task Dashboard

Prioritize smarter. Execute faster.  
A Flask-based productivity system that transforms static to-do lists into a dynamic execution engine using a deterministic scoring model (urgency × priority × deadline proximity).

Live Demo: https://smart-task-dashboard-l0wo.onrender.com/

![Backend](https://img.shields.io/badge/Backend-Flask-blue)
![Database](https://img.shields.io/badge/Database-SQLite-lightgrey)
![UI](https://img.shields.io/badge/UI-Responsive-orange)

---

## One-Line Problem Statement
Most to-do apps store tasks. This system decides execution order.

---

## Preview
### Real-time task prioritization dashboard:
<img width="1909" height="914" alt="image" src="https://github.com/user-attachments/assets/88598b91-b213-48ff-b069-7f53e599531a" />


---

## Highlights
* Dynamic Prioritization Engine → Ranks tasks in real time using urgency × priority × deadline proximity.
* Productivity Tracking → Monitor completion rates and performance insights.
* Rule-Based Recommendation System → Deterministic logic inspired by scheduling heuristics.
* Clean Responsive UI → Minimalist, distraction-free interface.
* Lightweight Architecture → Deployable Flask app with SQLite persistence.

---

## Overview
Smart Task Dashboard is a productivity-focused task manager built with Flask. It replaces static task lists with a real-time ranking system that helps users focus on high-impact tasks first, reducing decision fatigue and improving execution efficiency.

---

## Task Intelligence Engine
A deterministic scoring system inspired by scheduling heuristics:

Score = Priority Weight × Urgency Factor × Deadline Proximity

### Example Output
* Submit report (High priority, due today) → Rank #1  
* Read documentation (Low priority, no deadline) → Rank #5

---

## Tech Stack
* Backend: Flask (Python, REST-style routing)
* Frontend: HTML5, CSS3 (Responsive UI)
* Storage: In-memory Python lists

---

## Project Structure
```text
task-dashboard/
├── app.py           # Application logic and routing
├── static/          # CSS and frontend assets
├── templates/       # HTML layouts
└── README.md        # Documentation
````

---

## Installation & Setup

```bash
git clone https://github.com/bhavana-cloudworks/task-dashboard.git
cd task-dashboard
pip install -r requirements.txt
python app.py
```

Access the application at: [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## Usage

* Add tasks with specific priority and deadlines.
* View the automatically ranked task list.
* Track completion status in real time.
* Use system-generated recommendations to plan your workday.

---

## Impact

* Eliminates decision fatigue in daily task planning.
* Improves focus by prioritizing high-impact tasks automatically.
* Encourages consistent execution over simple task accumulation.

---

## Future Enhancements

* User authentication and multi-user support.
* Cloud database hosting for persistent data.
* Advanced analytics and visualization dashboards.
* Mobile-responsive PWA version.

---

## What This Project Demonstrates
- Backend system design using Flask
- Real-time decision-making logic (scoring engine)
- Clean separation of frontend and backend
- Deployment using cloud platform (Render)
- Product-thinking beyond CRUD applications

---

## Author

Bhavana
