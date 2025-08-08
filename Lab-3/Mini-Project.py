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

while True:
    print("\nMenu:")
    print("1. Add Task")
    print("2. List Pending Tasks")
    print("3. Mark All Tasks as Completed")
    print("4. Search Tasks")
    print("5. Exit")

    choice = input("Enter choice (1-5): ").strip()

    if choice == "1":
        task_name = input("Enter task name: ").strip()
        tasks = add_task(tasks, task_name)
        print(f"Task '{task_name}' added.")
    elif choice == "2":
        pending = list_pending(tasks)
        print("Pending Tasks:")
        for t in pending:
            print(f"- {t['name']}")
        if not pending:
            print("No pending tasks.")
    elif choice == "3":
        tasks = complete_all(tasks)
        print("All tasks marked as completed.")
    elif choice == "4":
        keyword = input("Enter keyword to search: ").strip()
        results = search_tasks(tasks, keyword)
        print(f"Search Results for '{keyword}':")
        for t in results:
            status = "Completed" if t["completed"] else "Pending"
            print(f"- {t['name']} [{status}]")
        if not results:
            print("No matching tasks found.")
    elif choice == "5":
        print("Exiting. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number from 1 to 5.")
