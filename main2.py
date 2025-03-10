'''TASK 2 Design a simple calculator with basic arithmetic operations.
Prompt the user to input two numbers and an operation choice.
Perform the calculation and display the result.
This project aims to create a command-line or GUI-based application
using Python'''
import tkinter as tk
def ad(x, y):
    return x + y
def substract(x, y):
    return x - y
def mul(x, y):
    return x * y
def divde(x, y):
    if y == 0:
        return "Error! Division by zero."
    else:
        return x / y
def calculate():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
    except ValueError:
        result_label.config(text="Invalid input! Please enter numeric values.")
        return
    operation = operation_var.get()
    if operation == "add":
        result = ad(num1, num2)
    elif operation == "subtract":
        result = substract(num1, num2)
    elif operation == "multiply":
        result = mul(num1, num2)
    elif operation == "divide":
        result = divde(num1, num2)
    else:
        result_label.config(text="Invalid operation!")
        return
    result_label.config(text=f"Result: {result}")
window = tk.Tk()
window.title("Simple Calculator")
window.geometry("400x300")
label1 = tk.Label(window, text="Enter first number:")
label1.pack(pady=5)
entry1 = tk.Entry(window)
entry1.pack(pady=5)
label2 = tk.Label(window, text="Enter second number:")
label2.pack(pady=5)
entry2 = tk.Entry(window)
entry2.pack(pady=5)
operation_var = tk.StringVar()
add_button = tk.Radiobutton(window, text="Add", variable=operation_var, value="add")
add_button.pack()
sub_button = tk.Radiobutton(window, text="Subtract", variable=operation_var, value="subtract")
sub_button.pack()
mul_button = tk.Radiobutton(window, text="Multiply", variable=operation_var, value="multiply")
mul_button.pack()
div_button = tk.Radiobutton(window, text="Divide", variable=operation_var, value="divide")
div_button.pack()
calculate_button = tk.Button(window, text="Calculate", command=calculate)
calculate_button.pack(pady=20)
result_label = tk.Label(window, text="Result: ")
result_label.pack()
window.mainloop()
