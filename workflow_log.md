# Workflow Log

## Commands Executed

### Part 1: Initial Setup
```
git init
git checkout -b Harshit_Sharma
git add .
git commit -m "Part 1: Initial Flask project implementation on Harshit_Sharma branch"
git checkout main
git merge Harshit_Sharma
```

### Part 2: Conflict Resolution
```
git checkout -b Harshit_Sharma_new
git add data.json && git commit -m "Updated data.json on Harshit_Sharma_new branch"
git checkout main
git add data.json && git commit -m "Modified data.json on main to create conflict"
git merge Harshit_Sharma_new
git checkout --theirs data.json
git add data.json
git commit -m "Merged Harshit_Sharma_new and resolved conflicts"
```

### Part 3: Feature Branches
```
git branch master_1 main
git branch master_2 main
git checkout master_1
git add templates/todo.html && git commit -m "Part 3: Implemented To-Do Page frontend in master_1"
git checkout master_2
git add app.py && git commit -m "Part 3: Implemented /submittodoitem backend route in master_2"
git checkout main
git merge master_1
git merge master_2
```

### Part 4: Soft Reset & Rebase
```
git checkout master_1
git add templates/todo.html && git commit -m "Part 4: Add Item ID field"
git add templates/todo.html && git commit -m "Part 4: Add Item UUID field"
git add templates/todo.html && git commit -m "Part 4: Add Item Hash field"
git checkout main
git merge master_1
git reset --soft 931994b
git commit -m "Part 4: Re-committed state after soft reset to Item ID commit"
git rebase main master_1
```

### Push to Remote
```
git remote add origin git@github.com:warrier2002/test.git
git push -u origin main
git push origin master_1 Harshit_Sharma Harshit_Sharma_new
```
