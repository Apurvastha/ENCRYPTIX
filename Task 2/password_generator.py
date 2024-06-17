import random
import string
import tkinter as tk
from tkinter import messagebox

def generate_password(length=12, use_lower=True, use_upper=True, use_digits=True, use_symbols=True):
    # Define the character sets to include in the password based on toggles
    lower = string.ascii_lowercase if use_lower else ''
    upper = string.ascii_uppercase if use_upper else ''
    digits = string.digits if use_digits else ''
    symbols = string.punctuation if use_symbols else ''
    
    # Combine all selected character sets
    all_characters = lower + upper + digits + symbols

    if not all_characters:
        messagebox.showwarning("Invalid Selection", "At least one character set must be selected.")
        return ''

    # Ensure the password contains at least one character from each selected set
    password = []
    if use_lower:
        password.append(random.choice(lower))
    if use_upper:
        password.append(random.choice(upper))
    if use_digits:
        password.append(random.choice(digits))
    if use_symbols:
        password.append(random.choice(symbols))

    # Fill the rest of the password length with random characters from the combined set
    password += random.choices(all_characters, k=length - len(password))

    # Shuffle the resulting list to avoid predictable sequences
    random.shuffle(password)

    # Convert the list to a string and return it
    return ''.join(password)

def generate_password_gui():
    try:
        length = int(length_entry.get())
        if length < 4:
            messagebox.showwarning("Invalid Length", "Password length must be at least 4.")
        else:
            use_lower = lower_var.get()
            use_upper = upper_var.get()
            use_digits = digits_var.get()
            use_symbols = symbols_var.get()
            password = generate_password(length, use_lower, use_upper, use_digits, use_symbols)
            password_entry.config(state=tk.NORMAL)
            password_entry.delete(0, tk.END)
            password_entry.insert(0, password)
            password_entry.config(state='readonly')
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number for the password length.")

# Setup GUI
root = tk.Tk()
root.title("Password Generator")

# Main frame
main_frame = tk.Frame(root, padx=10, pady=10)
main_frame.pack(pady=10)

# Length Frame
length_frame = tk.Frame(main_frame)
length_frame.grid(row=0, column=0, columnspan=2, pady=10)

# Length Label and Entry
length_label = tk.Label(length_frame, text="Password Length:")
length_label.grid(row=0, column=0, padx=5, pady=5, sticky='e')
length_entry = tk.Entry(length_frame)
length_entry.grid(row=0, column=1, padx=5, pady=5)
length_entry.insert(0, "12")  # Default length

# Options Frame
options_frame = tk.Frame(main_frame)
options_frame.grid(row=1, column=0, columnspan=2, pady=10)

# Toggle Buttons
lower_var = tk.BooleanVar(value=True)
upper_var = tk.BooleanVar(value=True)
digits_var = tk.BooleanVar(value=True)
symbols_var = tk.BooleanVar(value=True)

lower_check = tk.Checkbutton(options_frame, text="Include Lowercase", variable=lower_var)
lower_check.grid(row=0, column=0, padx=5, pady=5, sticky='w')
upper_check = tk.Checkbutton(options_frame, text="Include Uppercase", variable=upper_var)
upper_check.grid(row=0, column=1, padx=5, pady=5, sticky='w')
digits_check = tk.Checkbutton(options_frame, text="Include Digits", variable=digits_var)
digits_check.grid(row=1, column=0, padx=5, pady=5, sticky='w')
symbols_check = tk.Checkbutton(options_frame, text="Include Symbols", variable=symbols_var)
symbols_check.grid(row=1, column=1, padx=5, pady=5, sticky='w')

# Password Frame
password_frame = tk.Frame(main_frame)
password_frame.grid(row=2, column=0, columnspan=2, pady=10)

# Password Label and Entry (read-only)
password_label = tk.Label(password_frame, text="Generated Password:")
password_label.grid(row=0, column=0, padx=5, pady=5, sticky='e')
password_entry = tk.Entry(password_frame, state='readonly')
password_entry.grid(row=0, column=1, padx=5, pady=5)

# Generate Button
generate_button = tk.Button(main_frame, text="Generate Password", command=generate_password_gui)
generate_button.grid(row=3, column=0, columnspan=2, pady=10)

# Start the GUI event loop
root.mainloop()
