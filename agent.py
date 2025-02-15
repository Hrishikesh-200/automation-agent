import os
from Handlers.task_handlers import execute_task

# Security constraints
SECURE_DIR = "/data"

def run_task(task_description):
    # Example task description: "Sort the contacts"
    task_name = parse_task_description(task_description)

    if task_name:
        try:
            result = execute_task(task_name)
            return {"status": "success", "output": result}
        except Exception as e:
            return {"status": "error", "message": str(e)}
    else:
        return {"status": "error", "message": "Invalid task description"}

def parse_task_description(description):
    # Map natural language to task handlers
    task_map = {
        "sort contacts": "sort_contacts",
        "fetch api data": "fetch_api_data",
        "clone git repo": "clone_git_repo",
        "extract email": "extract_email",
    }
    return task_map.get(description.lower(), None)
