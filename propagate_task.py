import subprocess
import re
import sys

def run(cmd):
    return subprocess.check_output(cmd, shell=True).decode().strip()

def get_current_branch():
    return run("git rev-parse --abbrev-ref HEAD")

def get_available_branches():
    output = run("git branch -r")
    branches = [b.strip().replace("origin/", "") for b in output.splitlines()]
    return sorted(set(branches))

def prompt_branch_selection(all_branches):
    print("\nAvailable base branches:")
    for i, branch in enumerate(all_branches):
        print(f"{i+1}: {branch}")

    choices = input("Select branches to apply task to (comma-separated indices): ")
    selected = [all_branches[int(i)-1] for i in choices.split(",") if i.strip().isdigit()]
    return selected

def get_commit_range():
    return input("Enter commit hash or range to cherry-pick (e.g., abc123 or abc123^..abc123): ")

def extract_task_id(branch_name):
    match = re.search(r'(?:task|ticket)-(\d+)', branch_name)
    return match.group(1) if match else None


def main():
    current_branch = get_current_branch()
    task_id = extract_task_id(current_branch)

    if not task_id:
        print("Error: Current branch doesn't include a task ID (e.g., task-1111).")
        sys.exit(1)

    print(f"Detected task ID: {task_id} from branch '{current_branch}'")

    branches = get_available_branches()
    base_branches = [b for b in branches if not b.startswith(current_branch)]

    selected_bases = prompt_branch_selection(base_branches)
    commit_range = get_commit_range()

    for base in selected_bases:
        task_branch = f"{base.split('-')[0]}-task-{task_id}"
        if "staging" in base:
            task_branch += "-staging"

        print(f"\nCreating branch {task_branch} from {base}")
        run(f"git checkout {base}")
        run(f"git pull origin {base}")
        run(f"git checkout -b {task_branch}")
        run(f"git cherry-pick {commit_range}")
        run(f"git push -u origin {task_branch}")
        print(f"✅ Pushed {task_branch}")

    print("\n🎉 All done!")

if __name__ == "__main__":
    main()
