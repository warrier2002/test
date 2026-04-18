# Project Submission: Flask & MongoDB Assignment

## GitHub Repository
https://github.com/warrier2002/test

---

## Part 1: Flask Application

### 1. API Route (`/api`)
Returns a JSON list read from the backend `data.json` file.

```python
@app.route('/api', methods=['GET'])
def get_api_data():
    with open('data.json', 'r') as f:
        data = json.load(f)
    return jsonify(data)
```

### 2. Submission Form (`/submit`)
Frontend form collects Name, Email, and Message. On submit:
- **Success**: Inserts into MongoDB Atlas → redirects to `/success` showing "Data submitted successfully"
- **Error**: Stays on the same page and displays the error message

```python
@app.route('/submit', methods=['POST'])
def submit():
    try:
        collection.insert_one(data)
        return redirect(url_for('success'))
    except Exception as e:
        return render_template('index.html', error=str(e))
```

### 3. To-Do List (`/todo`)
Form with Item Name, Item Description, and Item ID. Submits to `/submittodoitem` which stores in MongoDB.

### 4. Data Viewer (`/viewdata`)
Dedicated page to browse all MongoDB records with:
- Tabs to switch between Submissions and To-Do Items
- Live search/filter by any field

---

## Part 2: Git Workflow

### Step 1: Repository Setup & Branch Creation
```bash
git init
git checkout -b Harshit_Sharma
git add .
git commit -m "Part 1: Initial Flask project implementation on Harshit_Sharma branch"
git checkout main
git merge Harshit_Sharma
```
**Explanation**: Created a branch named after the user, added all Flask project files, committed, and merged into main.

### Step 2: Merge Conflict Resolution
```bash
git checkout -b Harshit_Sharma_new
# Updated data.json
git add data.json && git commit -m "Updated data.json on Harshit_Sharma_new branch"
git checkout main
# Modified data.json on main to create conflict
git add data.json && git commit -m "Modified data.json on main to create conflict"
git merge Harshit_Sharma_new
# CONFLICT in data.json
git checkout --theirs data.json
git add data.json
git commit -m "Merged Harshit_Sharma_new and resolved conflicts"
```
**Explanation**: Created a deliberate conflict by modifying the same file on both branches. Resolved by accepting changes from `Harshit_Sharma_new`.

### Step 3: Parallel Feature Development
```bash
git branch master_1 main
git branch master_2 main
git checkout master_1
# Created To-Do frontend (templates/todo.html)
git add templates/todo.html && git commit -m "Part 3: Implemented To-Do Page frontend in master_1"
git checkout master_2
# Created /submittodoitem backend route
git add app.py && git commit -m "Part 3: Implemented /submittodoitem backend route in master_2"
git checkout main
git merge master_1
git merge master_2
```
**Explanation**: Built frontend and backend in separate branches, then merged both into main.

### Step 4: Sequential Commits, Soft Reset & Rebase
```bash
git checkout master_1
git add templates/todo.html && git commit -m "Part 4: Add Item ID field"
git add templates/todo.html && git commit -m "Part 4: Add Item UUID field"
git add templates/todo.html && git commit -m "Part 4: Add Item Hash field"
git checkout main
git merge master_1
git reset --soft 931994b   # Reset to "Item ID" commit, changes remain staged
git commit -m "Part 4: Re-committed state after soft reset to Item ID commit"
git rebase main master_1   # Rebase preserving individual commits
git push -u origin main
git push origin master_1 Harshit_Sharma Harshit_Sharma_new
```
**Explanation**: Added fields one-by-one as separate commits. Used `git reset --soft` to roll back while keeping staged changes. Re-committed and rebased to maintain clean history.
