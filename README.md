# Harshit Sharma - Flask & MongoDB Integration Assignment

A premium Flask-based web application demonstrating complex Git workflows, MongoDB Atlas integration, and modern UI design.

## 🚀 Overview
This project fulfills a comprehensive assignment requiring a backend API server, a frontend data-entry portal, and a sophisticated version control history including branching, merging, conflict resolution, and soft resets.

## 🛠 Tech Stack
- **Backend**: Flask (Python)
- **Database**: MongoDB Atlas (Pymongo)
- **Frontend**: HTML5, Vanilla CSS (Premium Glassmorphism Design)
- **Cloud Tools**: python-dotenv for secure environment management

## ✨ Features
- **API Endpoint**: `/api` returns dynamic records from a backend JSON file.
- **Data Submission**: Interactive form that validates inputs and stores records in a MongoDB Atlas cluster.
- **To-Do Management**: Dedicated module for task tracking with unique ID, UUID, and Hashing functionality.
- **Error Handling**: Graceful error displays on same-page forms with redirect-to-success logic.

## 📊 Git Workflow History
This repository maintains a detailed commit history split across several branches:
- `Harshit_Sharma`: Initial core development.
- `Harshit_Sharma_new`: Demonstration of merge conflict resolution.
- `master_1`: Frontend feature development (UI/UX).
- `master_2`: Backend API development (Routes/Data).
- `main`: Optimized production branch following advanced Git Reset and Rebase patterns.

## ⚙️ Setup & Installation
1. **Clone the repository**:
   ```bash
   git clone git@github.com:warrier2002/test.git
   ```
2. **Install dependencies**:
   ```bash
   pip install Flask pymongo python-dotenv
   ```
3. **Configure MongoDB**:
   Create a `.env` file or update `app.py` with your `MONGO_URI`.
4. **Run the application**:
   ```bash
   python3 app.py
   ```
   The app will be available at `http://localhost:5001`.

---
**Author**: Harshit Sharma
