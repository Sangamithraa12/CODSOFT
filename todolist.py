def show_menu():
    print("\nTo-Do List Menu:")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Mark Task as Done")
    print("4. Exit")

def view_tasks(tasks):
    if not tasks:
        print("\nNo tasks yet!")
    else:
        print("\nYour Tasks:")
        for idx, (task, done) in enumerate(tasks, start=1):
            status = "Done" if done else "Pending"
            print(f"{idx}. {task} - {status}")

def add_task(tasks):
    task = input("\nEnter a new task: ")
    tasks.append((task, False))
    print("Task added!")

def mark_task_done(tasks):
    view_tasks(tasks)
    try:
        task_num = int(input("\nEnter the task number to mark as done: "))
        task, _ = tasks[task_num - 1]
        tasks[task_num - 1] = (task, True)
        print("Task marked as done!")
    except (ValueError, IndexError):
        print("Invalid task number!")

def main():
    # Preloaded tasks
    tasks = [
        ("Buy groceries", False),
        ("Finish homework", False),
        ("Call mom", False),
        ("Clean the house", False),
        ("Read a book", False),
    ]

    print("\nPreloaded tasks have been added to your To-Do List!")

    while True:
        show_menu()
        choice = input("Choose an option: ")
        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            mark_task_done(tasks)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again!")

if __name__ == "__main__":
    main()
