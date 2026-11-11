print("Welcome to Task Manager")
tasks = []

while True:
    print("\n===== TASK MANAGER =====")
    print("1. Add Task")
    print("2. Display Tasks")
    print("3. Search Task")
    print("0. Exit")

    choice = input("Choose an option: ")
    if choice == "0":
        print("Goodbye!")
        break
    elif choice == "1":
        task = input("Enter task title: ")

        if task.strip() == "":
            print("Task title cannot be empty.")
        else:
            tasks.append(task)
            print("Task added successfully.")
    elif choice == "2":

        if len(tasks) == 0:
            print("No tasks found.")
        else:
            print("\nTasks:")

            for index, task in enumerate(tasks, start=1):
                print(f"{index}. {task}")
    elif choice == "3":

        keyword = input("Enter keyword: ")

        found = False

        for task in tasks:
            if keyword.lower() in task.lower():
                print(task)
                found = True

        if not found:
            print("No matching tasks found.")
    else:
        print("Invalid option. Try again.")
