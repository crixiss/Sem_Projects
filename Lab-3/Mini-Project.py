def add_task(task_list, task_name):
    task_list.append({"name": task_name, "completed": False})
    return task_list

def list_pending(task_list):
    return list(filter(lambda task: not task["completed"], task_list))

def complete_all(task_list):
    return list(map(lambda task: {**task, "completed": True}, task_list))

def search_tasks(task_list, keyword):
    return list(filter(lambda task: keyword.lower() in task["name"].lower(), task_list))

tasks = []
tasks = add_task(tasks, "Buy groceries")
tasks = add_task(tasks, "Finish assignment")
tasks = add_task(tasks, "Call friend")

print("Pending Tasks:", list_pending(tasks))

tasks = complete_all(tasks)

print("Search Result:", search_tasks(tasks, "call"))
