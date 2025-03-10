'''TASK 5
Contact BookContact Information: 
Store name, phone number, email, and address for each contact.
View Contact List: Display a list of all saved contacts with names and phone numbers.
Add Contact: Allow users to add new contacts with their details.
Search Contact: Implement a search function to find contacts by name or phone number.
Update Contact: Enable users to update contact details.
Delete Contact: Provide an option to delete a contact.
User Interface: Design a user-friendly interface for easy interaction.
This project aims to create a command-line or GUI-based application
using Python'''
import tkinter as tk
from tkinter import simpledialog, messagebox
window = tk.Tk()
window.title("Contact Book")
window.geometry("500x500")
contacts = []
contact_listbox = tk.Listbox(window, width=60, height=10)
contact_listbox.pack(pady=10)
def refresh_list():
    contact_listbox.delete(0, tk.END)
    for contact in contacts:
        contact_listbox.insert(tk.END, f"{contact['name']} - {contact['phone_number']}")
def add_contact():
    name = simpledialog.askstring("New Contact", "Enter Name:")
    phone = simpledialog.askstring("New Contact", "Enter Phone Number:")
    email = simpledialog.askstring("New Contact", "Enter Email:")
    address = simpledialog.askstring("New Contact", "Enter Address:")
    if name and phone and email and address:
        contacts.append({"name": name, "phone_number": phone, "email": email, "address": address})
        refresh_list()
    else:
        messagebox.showwarning("Input Error", "All fields are required!")
def view_contact():
    selected = contact_listbox.curselection()
    if selected:
        index = selected[0]
        contact = contacts[index]
        messagebox.showinfo("Contact Info", f"Name: {contact['name']}\nPhone: {contact['phone_number']}\nEmail: {contact['email']}\nAddress: {contact['address']}")
    else:
        messagebox.showwarning("Selection Error", "Please select a contact to view.")
def search_contact():
    search_term = simpledialog.askstring("Search Contact", "Enter Name or Phone Number:")
    if search_term:
        found_contacts = [contact for contact in contacts if search_term.lower() in contact['name'].lower() or search_term in contact['phone_number']]
        if found_contacts:
            contact_listbox.delete(0, tk.END)
            for contact in found_contacts:
                contact_listbox.insert(tk.END, f"{contact['name']} - {contact['phone_number']}")
        else:
            messagebox.showinfo("Search Result", "No contact found.")
    else:
        messagebox.showwarning("Search Error", "Please enter a search term.")
def update_contact():
    selected = contact_listbox.curselection()
    if selected:
        index = selected[0]
        contact = contacts[index]
        new_name = simpledialog.askstring("Update Contact", "Enter new Name:", initialvalue=contact['name'])
        new_phone = simpledialog.askstring("Update Contact", "Enter new Phone Number:", initialvalue=contact['phone_number'])
        new_email = simpledialog.askstring("Update Contact", "Enter new Email:", initialvalue=contact['email'])
        new_address = simpledialog.askstring("Update Contact", "Enter new Address:", initialvalue=contact['address'])
        if new_name and new_phone and new_email and new_address:
            contacts[index] = {"name": new_name, "phone_number": new_phone, "email": new_email, "address": new_address}
            refresh_list()
        else:
            messagebox.showwarning("Input Error", "All fields are required!")
    else:
        messagebox.showwarning("Selection Error", "Please select a contact to update.")
def delete_contact():
    selected = contact_listbox.curselection()
    if selected:
        index = selected[0]
        contacts.pop(index)
        refresh_list()
    else:
        messagebox.showwarning("Selection Error", "Please select a contact to delete.")
button_frame = tk.Frame(window)
button_frame.pack(pady=10)
add_button = tk.Button(button_frame, text="Add Contact", width=15, command=add_contact)
add_button.pack(side=tk.LEFT, padx=5)
view_button = tk.Button(button_frame, text="View Contact", width=15, command=view_contact)
view_button.pack(side=tk.LEFT, padx=5)
search_button = tk.Button(button_frame, text="Search Contact", width=15, command=search_contact)
search_button.pack(side=tk.LEFT, padx=5)
update_button = tk.Button(button_frame, text="Update Contact", width=15, command=update_contact)
update_button.pack(side=tk.LEFT, padx=5)
delete_button = tk.Button(button_frame, text="Delete Contact", width=15, command=delete_contact)
delete_button.pack(side=tk.LEFT, padx=5)
window.mainloop()
