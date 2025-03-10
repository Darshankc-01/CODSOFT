'''TASK 3
PASSWORD GENERATOR: A password generator is a useful tool that generates strong and random passwords for users. 
This project aims to create a password generator application using Python, 
allowing users to specify the length and complexity of the password.
User Input: Prompt the user to specify the desired length of the password.
Generate Password: Use a combination of random characters to generate a password of the specified length.
Display the Password: Print the generated password on the screen.
This project aims to create a command-line or GUI-based application
using Python'''
import tkinter as tk
import random
import string
lowercase_letters = string.ascii_lowercase
uppercase_letters = string.ascii_uppercase
numbers = string.digits
symbols = "!@#$%^&*()_-+={[}]|:;\"'<>,.?/~`"
avoid_ambiguous = "0OlI1"
usable_characters = set(lowercase_letters + uppercase_letters + numbers + symbols)
usable_characters -= set(avoid_ambiguous)
usable_characters_list = list(usable_characters)
def generate_password(length=16):
    if length < 16:
        result_label.config(text="Password length must be greater than or equal to 16 characters.")
        return
    if length > len(usable_characters_list):
        result_label.config(text=f"Password length cannot be greater than {len(usable_characters_list)} characters.")
        return
    password = random.sample(usable_characters_list, length)
    random.shuffle(password)
    return ''.join(password)
def on_generate():
    try:
        password_length = int(length_entry.get())
        if password_length < 16:
            result_label.config(text="Password length must be greater than or equal to 16 characters.")
        else:
            password = generate_password(password_length)
            if password:
                result_label.config(text=f"Generated Password: {password}")
    except ValueError:
        result_label.config(text="Please enter a valid number for the password length.")
window = tk.Tk()
window.title("Password Generator")
window.geometry("400x300")
length_label = tk.Label(window, text="Enter desired password length (>= 16):")
length_label.pack(pady=10)
length_entry = tk.Entry(window)
length_entry.pack(pady=5)
generate_button = tk.Button(window, text="Generate Password", command=on_generate)
generate_button.pack(pady=20)
result_label = tk.Label(window, text="Generated Password will appear here.", wraplength=350)
result_label.pack(pady=10)
window.mainloop()
