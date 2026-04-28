AI-Powered Smart Task Dashboard for Productivity Optimization

A productivity-focused task management system built with Flask that combines structured task tracking with a lightweight agentic AI engine for intelligent task prioritization and actionable insights.

---

## Overview

Smart Task Dashboard helps users manage tasks efficiently by tracking deadlines, measuring performance, and providing data-driven recommendations.

The system extends beyond a basic to-do list by incorporating a logic-based AI layer that assists users in deciding what to work on next.

---

## UI Preview


<img width="1909" height="914" alt="image" src="https://github.com/user-attachments/assets/b4751aed-fcd4-438d-87ce-02900fbb124b" />


---

## Key Features

* Task creation, tracking, and completion management
* Deadline-aware scheduling and prioritization
* Productivity score based on task performance
* On-time completion rate monitoring
* AI-powered task recommendations and insights
* Clean, responsive user interface

---

## AI Insight Engine

The application includes a lightweight agentic AI module that enhances decision-making by:

* Evaluating task deadlines and priority levels
* Identifying overdue and high-impact tasks
* Suggesting the next best action for improved efficiency
* Generating real-time productivity insights

**Logic Spotlight:**
The AI system uses a rule-based scoring mechanism to dynamically rank tasks based on urgency (deadline proximity) and importance (priority level).

Example insight:

> "Focus on high-priority tasks nearing their deadline to maintain a strong completion rate."

---

## Tech Stack

* Backend: Flask (Python)
* Frontend: HTML, CSS
* Database: SQLite

---

## Project Structure

```
task-dashboard/
│
├── app.py
├── tasks.db
├── static/
│   └── style.css
├── templates/
│   └── index.html
└── README.md
```

---

## Installation and Setup

```bash
git clone https://github.com/bhavana-cloudworks/task-dashboard.git
cd task-dashboard
pip install -r requirements.txt
python app.py
```

Access the application at:
http://127.0.0.1:5000

---

## Usage

* Add tasks with priority and deadlines
* Track progress and completion status
* Monitor productivity metrics in real time
* Use AI-generated suggestions to optimize workflow

---

## Future Enhancements

* User authentication and multi-user support
* Cloud deployment with persistent hosting
* Advanced analytics and visualization
* Integration with external AI APIs

---

## Author

Bhavana
