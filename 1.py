users_choice = -1

tasks = []
tasks.append("Go to the bank")
tasks.append("Clean the garage")
tasks.append("Feed the cat")
tasks.append("Work on the project")


while users_choice != 5:
    print("1. Show tasks")
    print("2. Add tasks")
    print("3. Delete task")
    print("4. Save changes to a file")
    print("5. Exit")
    print()

    users_choice = int(input("Choose an option"))

    def show_tasks():
        task_index =  0
        for task in tasks:
            print(task + " " + "[" + str(task_index) + "]")
            task_index += 1

    def add_task():
        users_added_task = input("Enter tasks name: ")
        tasks.append(users_added_task)
        print("Task added")

    def delete_task():
        user_delete = int(input("Choose a number of task to delete it"))
        if user_delete < 0 or user_delete > len(tasks) - 1:
            print("Such task does not exist")
            return

        tasks.pop(user_delete)
        print("Task deleted")


    def save_tasks():
        file = open("Tasks.txt", "w")
        for task in tasks:
            file.write(task + "\n")
        file.close()



    if users_choice == 1:
        show_tasks()
        print()

    if users_choice ==2:
        add_task()

    if users_choice == 3:
        delete_task()

    if users_choice == 4:
        save_tasks()






