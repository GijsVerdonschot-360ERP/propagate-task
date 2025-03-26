# 🛠️ Task Branch Propagation Tool

This tool helps automate the repetitive Git workflow of propagating a task branch across multiple customer versions (e.g., `17.0`, `17.0-staging`, `18.0`, `main`, etc.), including staging branches.

## 💡 Problem

For each task, developers often need to:
- Create a branch per version (`17.0-task-1234`, `18.0-task-1234`, etc.)
- Cherry-pick the same changes
- Push each branch separately

This becomes tedious and error-prone, especially when customers have different branching structures.

## ✅ Solution

This Python script automates that workflow:
- Detects your current task branch (e.g. `17.0-task-1234`)
- Interactively asks which base branches to target
- Creates the appropriate task branches (e.g. `18.0-task-1234-staging`)
- Cherry-picks your commit(s)
- Pushes to origin

## 🚀 Usage

1. From your task branch (e.g. `17.0-task-1234`), run:

   ```bash
   nano propagate_task.py

2. Paste the script into the file and save it
- Press ```CTRL+X```
- Press ```Y``` to confirm saving
- Press ```ENTER``` to write the file

3. Then run:

   ```bash
   python3 propagate_task.py

4. Follow the prompts:
- Select which base branches to apply the task to
- Provide the commit hash or range to cherry-pick
