from tkinter import *
from tkinter import messagebox
import pickle
from tkinter import simpledialog

class ToDoList:
    def __init__(self, master):
        self.master = master
        master.title("To-Do List")
        master.geometry("600x400")

        # Load tasks from file
        self.tasks = self.load_tasks()

        # Create task list frame
        self.task_list_frame = Frame(master)
        self.task_list_frame.pack(pady=10, padx=10)

        # Create task list label
        self.task_list_label = Label(self.task_list_frame, text="Tasks:", font=("Helvetica", 14))
        self.task_list_label.pack()

        # Create listbox for tasks
        self.task_listbox = Listbox(self.task_list_frame, width=60, height=12, font=("Helvetica", 12))
        self.task_listbox.pack(pady=5)
        self.populate_listbox()

        # Create entry field for adding tasks
        self.task_entry = Entry(master, width=50, font=("Helvetica", 12))
        self.task_entry.pack(pady=5, padx=10)

        # Create buttons frame
        self.buttons_frame = Frame(master)
        self.buttons_frame.pack(pady=10, padx=10)

        # Create button for adding tasks
        self.add_button = Button(self.buttons_frame, text="Add Task", command=self.add_task, font=("Helvetica", 12), bg="#4CAF50", fg="white")
        self.add_button.pack(side=LEFT, padx=5)

        # Create button for marking tasks complete
        self.mark_complete_button = Button(self.buttons_frame, text="Mark Complete", command=self.mark_complete, font=("Helvetica", 12), bg="#FF9800", fg="white")
        self.mark_complete_button.pack(side=LEFT, padx=5)

        # Create button for clearing completed tasks
        self.clear_completed_button = Button(self.buttons_frame, text="Clear Completed", command=self.clear_completed, font=("Helvetica", 12), bg="#F44336", fg="white")
        self.clear_completed_button.pack(side=LEFT, padx=5)

        # Create button for editing tasks
        self.edit_button = Button(self.buttons_frame, text="Edit Task", command=self.edit_task, font=("Helvetica", 12), bg="#2196F3", fg="white")
        self.edit_button.pack(side=LEFT, padx=5)

    def load_tasks(self):
        try:
            with open("tasks.pickle", "rb") as f:
                tasks = pickle.load(f)
        except FileNotFoundError:
            tasks = []
        return tasks

    def save_tasks(self):
        with open("tasks.pickle", "wb") as f:
            pickle.dump(self.tasks, f)

    def populate_listbox(self):
        self.task_listbox.delete(0, END)
        for task in self.tasks:
            self.task_listbox.insert(END, task)

    def add_task(self):
        task = self.task_entry.get().strip()
        if task:
            self.tasks.append(task + " (Incomplete)")
            self.task_entry.delete(0, END)
            self.populate_listbox()
            self.save_tasks()
        else:
            messagebox.showwarning("Warning", "You must enter a task.")

    def mark_complete(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            index = selected_index[0]
            task = self.tasks[index]
            self.tasks[index] = task.replace(" (Incomplete)", " (Completed)")
            self.populate_listbox()
            self.save_tasks()
        else:
            messagebox.showwarning("Warning", "You must select a task to mark as complete.")

    def clear_completed(self):
        completed_tasks = [index for index, task in enumerate(self.tasks) if " (Completed)" in task]
        for index in reversed(completed_tasks):
            self.tasks.pop(index)
        self.populate_listbox()
        self.save_tasks()
        if not completed_tasks:
            messagebox.showinfo("Info", "No completed tasks to clear.")

    def edit_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            index = selected_index[0]
            task = self.tasks[index]
            new_task = simpledialog.askstring("Edit Task", "Enter the new task description:", initialvalue=task)
            if new_task is not None:
                self.tasks[index] = new_task + " (Incomplete)" if " (Completed)" not in task else new_task + " (Completed)"
                self.populate_listbox()
                self.save_tasks()
        else:
            messagebox.showwarning("Warning", "You must select a task to edit.")

if __name__ == "__main__":
    root = Tk()
    app = ToDoList(root)
    root.mainloop()