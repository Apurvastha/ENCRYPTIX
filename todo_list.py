from tkinter import *
from tkinter import messagebox

class ToDoList:
    def __init__(self, master):
        self.master = master
        master.title("To-Do List")
        master.geometry("400x300")

        # Create task list frame
        self.task_list_frame = Frame(master)
        self.task_list_frame.pack(pady=10)

        # Create task list label
        self.task_list_label = Label(self.task_list_frame, text="Tasks:", font=("Helvetica", 14))
        self.task_list_label.pack()

        # Create listbox for tasks
        self.task_listbox = Listbox(self.task_list_frame, width=50, height=10, font=("Helvetica", 12))
        self.task_listbox.pack()

        # Create entry field for adding tasks
        self.task_entry = Entry(master, width=40, font=("Helvetica", 12))
        self.task_entry.pack(pady=5)

        # Create buttons frame
        self.buttons_frame = Frame(master)
        self.buttons_frame.pack(pady=10)

        # Create button for adding tasks
        self.add_button = Button(self.buttons_frame, text="Add Task", command=self.add_task, font=("Helvetica", 12), bg="#4CAF50", fg="white")
        self.add_button.pack(side=LEFT, padx=5)

        # Create button for marking tasks complete
        self.mark_complete_button = Button(self.buttons_frame, text="Mark Complete", command=self.mark_complete, font=("Helvetica", 12), bg="#FF9800", fg="white")
        self.mark_complete_button.pack(side=LEFT, padx=5)

        # Create button for clearing completed tasks
        self.clear_completed_button = Button(self.buttons_frame, text="Clear Completed", command=self.clear_completed, font=("Helvetica", 12), bg="#F44336", fg="white")
        self.clear_completed_button.pack(side=LEFT, padx=5)

        # Initialize tasks list
        self.tasks = []

    def add_task(self):
        task = self.task_entry.get().strip()
        if task:
            self.tasks.append(task + " (Incomplete)")
            self.task_listbox.insert(END, task + " (Incomplete)")
            self.task_entry.delete(0, END)
        else:
            messagebox.showwarning("Warning", "You must enter a task.")

    def mark_complete(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            index = selected_index[0]
            task = self.tasks[index]
            self.tasks[index] = task.replace(" (Incomplete)", " (Completed)")
            self.task_listbox.delete(index)
            self.task_listbox.insert(index, self.tasks[index])
        else:
            messagebox.showwarning("Warning", "You must select a task to mark as complete.")

    def clear_completed(self):
        completed_tasks = [index for index, task in enumerate(self.tasks) if " (Completed)" in task]
        for index in reversed(completed_tasks):
            self.tasks.pop(index)
            self.task_listbox.delete(index)
        if not completed_tasks:
            messagebox.showinfo("Info", "No completed tasks to clear.")

if __name__ == "__main__":
    root = Tk()
    app = ToDoList(root)
    root.mainloop()
