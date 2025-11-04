todo_list = []

def add_task():
    task = input("Enter a task: ")
    todo_list.append({"Task":task, "Status":"Pending"})
    save_task_to_file()
    print(f"New task \'{task}\' Added succesfully\n")

def view_task():
    print("Your Todo Lists: ")

    if len(todo_list) == 0:
        print("No pending task")
    else:
        for index, task in enumerate(todo_list, 1):
            print(f"{index} : {task['Task']} - {task['Status']}")

    print()


def remove_task():
    if len(todo_list) == 0:
        print("List is Empty!")
    else:
        try:
            search_index = int(input("Enter the task number that you want to remove: ")) - 1
            
            if 0 <= search_index < len(todo_list):
                removed_task = todo_list.pop(search_index)
                save_task_to_file()
                print(f"Task removed is {removed_task['Task']}")
            else:
                print("Invalid Task Number")

        except ValueError:
            print("Please enter a valid task number")


def mark_done():
    if len(todo_list) == 0:
        print("List is Empty!")
    else:
        try:
            search_index = int(input("Enter the task number that you want to mark as done: ")) - 1

            if 0 <= search_index < len(todo_list):
                todo_list[search_index]['Status'] = 'Done'
                save_task_to_file()
                print(f"Task {todo_list[search_index]['Task']} had been marked as Done")
            else:
                print("Invalid Task Number")

        except ValueError:
            print("Please enter a valid task number")


def save_task_to_file():
    with open("todo_list_data.txt","w") as file:

        for task in todo_list:
            file.write(f"{task['Task']} - {task['Status']}\n")


def load_task_from_file():
    try:
        with open("todo_list_data.txt","r") as file:
            for line in file:
                if " - " in line:
                    task_name, status = line.strip().split(" - ")
                    todo_list.append({"Task": task_name, "Status" : status})
    except FileNotFoundError:
        pass

def menu():

    while True:

        print("*** Main Menu ***")
        print("Enter 1. Add a New Task")
        print("Enter 2. View all Task")
        print("Enter 3. Remove a Task")
        print("Enter 4. Mark a Task as Completed")
        print("Enter 5. Exit")

        choice = int(input("Enter your Choice: "))

        if choice == 1:
            add_task()
        elif choice == 2:
            view_task()
        elif choice == 3:
            remove_task()
        elif choice == 4:
            mark_done()
        elif choice == 5:
            print("Exiting the application")
            exit()
        else:
            print("Invalid choice!!! Try Again!!! ")

load_task_from_file()
menu()