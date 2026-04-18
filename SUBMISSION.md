# Project Submission: Flask & MongoDB Assignment
**Author**: Harshit Sharma

## 1. Project Implementation
The application is a Flask-based web service that integrates with MongoDB Atlas. It features a modern Glassmorphism UI for high visual impact.

### Setup Commands:
```bash
# Initialize local environment
git init
python3 -m pip install Flask pymongo python-dotenv
```

### Route: `/api`
Returns a JSON record list read from a backend `data.json` file.
```python
@app.route('/api', methods=['GET'])
def get_api_data():
    with open('data.json', 'r') as f:
        data = json.load(f)
    return jsonify(data)
```

### Route: `/submit` (Form Submission)
Inserts data into MongoDB Atlas and redirects to a success page.
- **Success**: Redirects to `/success`.
- **Error**: Displays error on the same page.

---

## 2. Git Workflow Demonstration

### Part 1 & 2: Initial Branching & Merge Conflicts
- Created branch `Harshit_Sharma`.
- Resolved a conflict in `data.json` by favoring the `Harshit_Sharma_new` branch.
```bash
# Resolution command
git checkout --theirs data.json
git add data.json
git commit -m "Resolved conflicts"
```

### Part 3: Feature Branching
- **master_1**: Implemented the To-Do frontend form.
- **master_2**: Implemented the `/submittodoitem` backend API.
- Successfully merged both into `main`.

### Part 4: Advanced History Management
- **Commit Sequence**: Added Item ID, UUID, and Hash fields in 3 distinct, sequential commits on `master_1`.
- **Soft Reset**: Rolled back the `main` branch to the "Item ID" state using `git reset --soft` and re-committed to maintain a clean linear history.
- **Rebase**: Rebased `master_1` onto `main` ensuring individual change history is preserved.

---

## 3. Final Repository Status
**Branch**: `main`
**Commit Trace**:
1. `8395eb7` - Initial Project
2. `b19872d` - Merged and Resolved Conflicts
3. `56e2580` - Part 3 Completion
4. `931994b` - Part 4: Add Item ID field
5. `54539d9` - Part 4: Reset and Re-committed State (Current Tip)

**GitHub Repository Link**: [Insert Link Here]
