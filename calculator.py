import tkinter as tk
from tkinter import ttk
import math

# Function definitions
def button_click(value):
    current = input_field.get()
    if value == "C":
        input_field.delete(0, tk.END)
    elif value == "=":
        try:
            result = eval(current)
            input_field.delete(0, tk.END)
            input_field.insert(0, str(result))
        except:
            input_field.delete(0, tk.END)
            input_field.insert(0, "Error")
    elif value == "π":
        input_field.insert(tk.END, str(math.pi))
    elif value == "e":
        input_field.insert(tk.END, str(math.e))
    elif value == "√x":
        try:
            result = math.sqrt(float(current))
            input_field.delete(0, tk.END)
            input_field.insert(0, str(result))
        except:
            input_field.delete(0, tk.END)
            input_field.insert(0, "Error")
    elif value == "log":
        try:
            result = math.log10(float(current))
            input_field.delete(0, tk.END)
            input_field.insert(0, str(result))
        except:
            input_field.delete(0, tk.END)
            input_field.insert(0, "Error")
    elif value == "←":
        input_field.delete(len(current) - 1, tk.END)
    else:
        input_field.insert(tk.END, value)

def clear_field():
    input_field.delete(0, tk.END)

def calculate_result():
    try:
        result = eval(input_field.get())  # Evaluate the mathematical expression
        input_field.delete(0, tk.END)
        input_field.insert(0, str(result))
    except:
        input_field.delete(0, tk.END)
        input_field.insert(0, "Error")

def calculate_square_root():
    try:
        result = math.sqrt(float(input_field.get()))
        input_field.delete(0, tk.END)
        input_field.insert(0, str(result))
    except:
        input_field.delete(0, tk.END)
        input_field.insert(0, "Error")

def calculate_log_base_10():
    try:
        result = math.log10(float(input_field.get()))
        input_field.delete(0, tk.END)
        input_field.insert(0, str(result))
    except:
        input_field.delete(0, tk.END)
        input_field.insert(0, "Error")

def calculate_sine():
    try:
        result = math.sin(math.radians(float(input_field.get())))
        input_field.delete(0, tk.END)
        input_field.insert(0, str(result))
    except:
        input_field.delete(0, tk.END)
        input_field.insert(0, "Error")

def calculate_cosine():
    try:
        result = math.cos(math.radians(float(input_field.get())))
        input_field.delete(0, tk.END)
        input_field.insert(0, str(result))
    except:
        input_field.delete(0, tk.END)
        input_field.insert(0, "Error")

def calculate_tangent():
    try:
        result = math.tan(math.radians(float(input_field.get())))
        input_field.delete(0, tk.END)
        input_field.insert(0, str(result))
    except:
        input_field.delete(0, tk.END)
        input_field.insert(0, "Error")

def calculate_pi():
    input_field.delete(0, tk.END)
    input_field.insert(0, str(math.pi))

def calculate_e():
    input_field.delete(0, tk.END)
    input_field.insert(0, str(math.e))

def calculate_inverse():
    try:
        value = 1 / float(input_field.get())
        input_field.delete(0, tk.END)
        input_field.insert(0, str(value))
    except:
        input_field.delete(0, tk.END)
        input_field.insert(0, "Error")

def calculate_abs():
    try:
        value = abs(float(input_field.get()))
        input_field.delete(0, tk.END)
        input_field.insert(0, str(value))
    except:
        input_field.delete(0, tk.END)
        input_field.insert(0, "Error")

def calculate_exponent():
    try:
        base = float(input_field.get())
        input_field.delete(0, tk.END)
        input_field.insert(0, f"{base}^")
    except:
        input_field.delete(0, tk.END)
        input_field.insert(0, "Error")

def backspace():
    current = input_field.get()
    input_field.delete(len(current) - 1, tk.END)

def toggle_theme():
    current_theme = style.theme_use()
    if current_theme == "clam":
        style.theme_use("alt")
    else:
        style.theme_use("clam")

# Create the main window
root = tk.Tk()
root.title("Scientific Calculator")
root.geometry("400x600")
root.resizable(True, True)

# Define the styling
style = ttk.Style(root)
style.theme_use("clam")
style.configure("TButton", font=("Arial", 14), padding=5, relief="raised")
style.configure("TEntry", font=("Arial", 16))
style.configure("TFrame", background="#2e3b4e")  # Frame background color

# Input field
input_field = ttk.Entry(root, font=("Arial", 20), justify="right")
input_field.grid(row=0, column=0, columnspan=5, padx=10, pady=20, sticky="nsew")

# Create a frame for the buttons
frame = tk.Frame(root)
frame.grid(row=1, column=0, columnspan=5, padx=10, pady=10)

# Button labels
buttons = [
    "2nd", "π", "e", "C", "←", 
    "x²", "1/x", "|x|", "EXP", "mod", 
    "√x", "(", ")", "n!", "/", 
    "xʸ", "7", "8", "9", "x", 
    "10ˣ", "4", "5", "6", "-", 
    "log", "1", "2", "3", "+", 
    "ln", "+/-", "0", ".", "="
]

# Button actions
button_actions = {
    "2nd": lambda: None,  # This could trigger a mode change, implemented as needed
    "π": calculate_pi,
    "e": calculate_e,
    "C": clear_field,
    "←": backspace,  # Backspace button
    "x": lambda: button_click("*"),
    "x²": lambda: button_click("**2"),
    "1/x": calculate_inverse,
    "|x|": calculate_abs,
    "EXP": lambda: button_click("**"),
    "mod": lambda: button_click("%"),
    "√x": calculate_square_root,
    "(": lambda: button_click("("),
    ")": lambda: button_click(")"),
    "n!": lambda: button_click("math.factorial("),
    "/": lambda: button_click("/"),
    "xʸ": lambda: button_click("**"),
    "7": lambda: button_click("7"),
    "8": lambda: button_click("8"),
    "9": lambda: button_click("9"),
    "x": lambda: button_click("*"),
    "10ˣ": lambda: button_click("10**"),
    "4": lambda: button_click("4"),
    "5": lambda: button_click("5"),
    "6": lambda: button_click("6"),
    "-": lambda: button_click("-"),
    "log": calculate_log_base_10,
    "1": lambda: button_click("1"),
    "2": lambda: button_click("2"),
    "3": lambda: button_click("3"),
    "+": lambda: button_click("+"),
    "ln": lambda: button_click("math.log("),
    "+/-": lambda: button_click("-"),
    "0": lambda: button_click("0"),
    ".": lambda: button_click("."),
    "=": calculate_result
}

# Create button with animations
def on_enter(event):
    event.widget.configure(relief="sunken", background="#5c8aff")
        
def on_leave(event):
    event.widget.configure(relief="raised", background="SystemButtonFace")

# Add buttons to the grid
for i, label in enumerate(buttons):
    action = button_actions.get(label, lambda: button_click(label))  # Default to button click if no specific action
    btn = tk.Button(frame, text=label, width=5, height=2, command=action)
    btn.grid(row=i // 5, column=i % 5, padx=5, pady=5)
    btn.bind("<Enter>", on_enter)
    btn.bind("<Leave>", on_leave)

# Theme toggle button
theme_button = ttk.Button(root, text="Toggle Theme", command=toggle_theme)
theme_button.grid(row=6, column=0, columnspan=5, sticky="nsew", padx=5, pady=5)

# Run the application
root.mainloop()
