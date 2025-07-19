
class Task:
    def __init__(self, description, done=False):
        self.description = description
        self.done = done

    def mark_done(self):
        self.done = True

    def __str__(self):
        status = "[✔]" if self.done else "[ ]"
        return f"{status} {self.description}"


class ToDoList:
    def __init__(self, filename="tasks.txt"):
        self.tasks = []
        self.filename = filename
        self.load_tasks()

    def add_task(self, description):
        self.tasks.append(Task(description))
        print("✅ Task added!")

    def view_tasks(self):
        if not self.tasks:
            print("📭 No tasks are found.")
            return
        for i, task in enumerate(self.tasks, 1):
            print(f"{i}. {task}")

    def mark_task_done(self, index):
        if 0 < index <= len(self.tasks):
            self.tasks[index - 1].mark_done()
            print("✔️ Task marked as done!")
        else:
            print("❌ Invalid task number. Please choose valid number")

    def delete_task(self, index):
        if 0 < index <= len(self.tasks):
            removed = self.tasks.pop(index - 1)
            print(f"🗑️ Removed: {removed.description}")
        else:
            print("❌ Invalid task number. Please choose valid number")

    def save_tasks(self):
        with open(self.filename, 'w') as f:
            for task in self.tasks:
                f.write(f"{task.done}|{task.description}\n")

    def load_tasks(self):
        try:
            with open(self.filename, 'r') as f:
                for line in f:
                    done_str, description = line.strip().split('|', 1)
                    self.tasks.append(Task(description, done_str == "True"))
        except FileNotFoundError:
            pass  


def main():
    todo = ToDoList()

    while True:
        print("\n--------📋To-Do List Menu:--------")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Done")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            desc = input("Enter task description: ")
            todo.add_task(desc)

        elif choice == "2":
            todo.view_tasks()

        elif choice == "3":
            idx = int(input("Enter task number to mark done: "))
            todo.mark_task_done(idx)

        elif choice == "4":
            idx = int(input("Enter task number to delete: "))
            todo.delete_task(idx)

        elif choice == "5":
            todo.save_tasks()
            print("💾 Your Tasks are saved Successfully.")
            break

        else:
            print("❌ Invalid choice. Please select appropriate choice")


if __name__ == "__main__":
    main()
