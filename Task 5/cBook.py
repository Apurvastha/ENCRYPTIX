import tkinter as tk
from tkinter import ttk, messagebox

contacts = {}

class ContactBook(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Contact Book")
        self.geometry("600x400")

        self.create_widgets()

    def create_widgets(self):
        # Create frames
        input_frame = tk.Frame(self)
        input_frame.pack(pady=10)

        contacts_frame = tk.Frame(self)
        contacts_frame.pack(pady=10)
        # self.contacts_tree.column("Name", width=100)
        # self.contacts_tree.column("Phone", width=100)
        # self.contacts_tree.column("Email", width=150)
        # self.contacts_tree.column("Address", width=200)

        # Create input fields
        name_label = tk.Label(input_frame, text="Name:")
        name_label.grid(row=0, column=0, padx=5, pady=5)
        self.name_entry = tk.Entry(input_frame)
        self.name_entry.grid(row=0, column=1, padx=5, pady=5)

        phone_label = tk.Label(input_frame, text="Phone:")
        phone_label.grid(row=0, column=2, padx=5, pady=5)
        self.phone_entry = tk.Entry(input_frame)
        self.phone_entry.grid(row=0, column=3, padx=5, pady=5)

        email_label = tk.Label(input_frame, text="Email:")
        email_label.grid(row=1, column=0, padx=5, pady=5)
        self.email_entry = tk.Entry(input_frame)
        self.email_entry.grid(row=1, column=1, padx=5, pady=5)

        address_label = tk.Label(input_frame, text="Address:")
        address_label.grid(row=1, column=2, padx=5, pady=5)
        self.address_entry = tk.Entry(input_frame)
        self.address_entry.grid(row=1, column=3, padx=5, pady=5)

        # Create buttons
        add_button = tk.Button(input_frame, text="Add", command=self.add_contact)
        add_button.grid(row=2, column=0, padx=5, pady=5)

        update_button = tk.Button(input_frame, text="Update", command=self.update_contact)
        update_button.grid(row=2, column=1, padx=5, pady=5)

        remove_button = tk.Button(input_frame, text="Remove", command=self.remove_contact)
        remove_button.grid(row=2, column=2, padx=5, pady=5)

        # Create search bar
        search_frame = tk.Frame(self)
        search_frame.pack(pady=5)

        search_label = tk.Label(search_frame, text="Search:")
        search_label.pack(side=tk.LEFT)

        self.search_entry = tk.Entry(search_frame, width=30)
        self.search_entry.pack(side=tk.LEFT, padx=5)
        self.search_entry.bind("<KeyRelease>", self.search_contacts)

        # Create contacts list
        contacts_label = tk.Label(contacts_frame, text="Contacts:")
        contacts_label.pack(side=tk.TOP, pady=5)

        self.contacts_tree = ttk.Treeview(contacts_frame, columns=("Name", "Phone", "Email", "Address"), show="headings")
        self.contacts_tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.contacts_tree.heading("Name", text="Name")
        self.contacts_tree.heading("Phone", text="Phone")
        self.contacts_tree.heading("Email", text="Email")
        self.contacts_tree.heading("Address", text="Address")

        self.contacts_tree.bind("<ButtonRelease-1>", self.select_contact)

        

    def add_contact(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        email = self.email_entry.get()
        address = self.address_entry.get()

        if name and phone:
            contacts[name] = {"Name": name,"Phone": phone, "Email": email, "Address": address}
            self.clear_entries()
            self.update_contacts_tree()
            messagebox.showinfo("Success", "Contact added successfully!")
        else:
            messagebox.showerror("Error", "Please enter a name and phone number.")

    def update_contact(self):
        selected_item = self.contacts_tree.focus()
        if selected_item:
            name = self.contacts_tree.item(selected_item)["text"]
            new_name = self.name_entry.get()
            new_phone = self.phone_entry.get()
            new_email = self.email_entry.get()
            new_address = self.address_entry.get()

            if new_name:
                contacts[new_name] = contacts.pop(name)
                contacts[new_name]["Phone"] = new_phone if new_phone else contacts[new_name]["Phone"]
                contacts[new_name]["Email"] = new_email if new_email else contacts[new_name]["Email"]
                contacts[new_name]["Address"] = new_address if new_address else contacts[new_name]["Address"]
                self.clear_entries()
                self.update_contacts_tree()
                messagebox.showinfo("Success", "Contact updated successfully!")
            else:
                messagebox.showerror("Error", "Please enter a name.")
        else:
            messagebox.showerror("Error", "Please select a contact to update.")

    def remove_contact(self):
        selected_item = self.contacts_tree.focus()
        if selected_item:
            name = self.contacts_tree.item(selected_item)["text"]
            confirm = messagebox.askyesno("Confirm", f"Are you sure you want to remove '{name}'?")
            if confirm:
                del contacts[name]
                self.clear_entries()
                self.update_contacts_tree()
                messagebox.showinfo("Success", "Contact removed successfully!")
        else:
            messagebox.showerror("Error", "Please select a contact to remove.")

    def select_contact(self, event):
        selected_item = self.contacts_tree.focus()
        if selected_item:
            name = self.contacts_tree.item(selected_item)["text"]
            contact = contacts[name]
            self.name_entry.delete(0, tk.END)
            self.name_entry.insert(0, name)
            self.phone_entry.delete(0, tk.END)
            self.phone_entry.insert(0, contact["Phone"])
            self.email_entry.delete(0, tk.END)
            self.email_entry.insert(0, contact.get("Email", ""))
            self.address_entry.delete(0, tk.END)
            self.address_entry.insert(0, contact.get("Address", ""))

    def clear_entries(self):
        self.name_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.address_entry.delete(0, tk.END)

    def update_contacts_tree(self):
        self.contacts_tree.delete(*self.contacts_tree.get_children())
        for name, contact in contacts.items():
            self.contacts_tree.insert("", tk.END, text=name, values=(name, contact["Phone"], contact.get("Email", ""), contact.get("Address", "")))

    def search_contacts(self, event):
        search_term = self.search_entry.get().lower()
        self.contacts_tree.delete(*self.contacts_tree.get_children())
        for name, contact in contacts.items():
            if search_term in name.lower() or search_term in contact["Phone"].lower() or search_term in contact.get("Email", "").lower() or search_term in contact.get("Address", "").lower():
                self.contacts_tree.insert("", tk.END, text=name, values=(name, contact["Phone"], contact.get("Email", ""), contact.get("Address", "")))

if __name__ == "__main__":
    app = ContactBook()
    app.mainloop()