import tkinter as tk
from tkinter import messagebox
from pymongo import MongoClient
from bson import ObjectId, errors

# Database setup
client = MongoClient("mongodb://localhost:27017")
db = client["Sample"]
collection = db["MySampleCollection"]


# GUI setup
class DatabaseApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Database Management App")

        # List Data
        self.list_frame = tk.Frame(root)
        self.list_frame.pack(pady=20)
        self.list_button = tk.Button(
            self.list_frame, text="List All Data", command=self.list_data
        )
        self.list_button.pack()

        # Add Data
        self.add_frame = tk.Frame(root)
        self.add_frame.pack(pady=20)
        self.add_id_label = tk.Label(self.add_frame, text="ID")
        self.add_id_label.grid(row=0, column=0)
        self.add_id_entry = tk.Entry(self.add_frame)
        self.add_id_entry.grid(row=0, column=1)
        self.add_name_label = tk.Label(self.add_frame, text="Name")
        self.add_name_label.grid(row=1, column=0)
        self.add_name_entry = tk.Entry(self.add_frame)
        self.add_name_entry.grid(row=1, column=1)
        self.add_age_label = tk.Label(self.add_frame, text="Age")
        self.add_age_label.grid(row=2, column=0)
        self.add_age_entry = tk.Entry(self.add_frame)
        self.add_age_entry.grid(row=2, column=1)
        self.add_marks_label = tk.Label(self.add_frame, text="Marks")
        self.add_marks_label.grid(row=3, column=0)
        self.add_marks_entry = tk.Entry(self.add_frame)
        self.add_marks_entry.grid(row=3, column=1)
        self.add_button = tk.Button(
            self.add_frame, text="Add Data", command=self.add_data
        )
        self.add_button.grid(row=4, columnspan=2)

        # Update Data
        self.update_frame = tk.Frame(root)
        self.update_frame.pack(pady=20)
        self.update_id_label = tk.Label(self.update_frame, text="ID")
        self.update_id_label.grid(row=0, column=0)
        self.update_id_entry = tk.Entry(self.update_frame)
        self.update_id_entry.grid(row=0, column=1)
        self.update_name_label = tk.Label(self.update_frame, text="New Name")
        self.update_name_label.grid(row=1, column=0)
        self.update_name_entry = tk.Entry(self.update_frame)
        self.update_name_entry.grid(row=1, column=1)
        self.update_age_label = tk.Label(self.update_frame, text="New Age")
        self.update_age_label.grid(row=2, column=0)
        self.update_age_entry = tk.Entry(self.update_frame)
        self.update_age_entry.grid(row=2, column=1)
        self.update_button = tk.Button(
            self.update_frame, text="Update Data", command=self.update_data
        )
        self.update_button.grid(row=3, columnspan=2)

        # Delete Data
        self.delete_frame = tk.Frame(root)
        self.delete_frame.pack(pady=20)
        self.delete_id_label = tk.Label(self.delete_frame, text="ID")
        self.delete_id_label.grid(row=0, column=0)
        self.delete_id_entry = tk.Entry(self.delete_frame)
        self.delete_id_entry.grid(row=0, column=1)
        self.delete_button = tk.Button(
            self.delete_frame, text="Delete Data", command=self.delete_data
        )
        self.delete_button.grid(row=1, columnspan=2)

    def list_data(self):
        data = collection.find()
        list_window = tk.Toplevel(self.root)
        list_window.title("List of Data")
        text = tk.Text(list_window)
        text.pack()
        for item in data:
            text.insert(
                tk.END,
                f"Id: {item['_id']}, Name: {item.get('Name', 'N/A')}, Age: {item.get('Age', 'N/A')}, Marks: {item.get('marks', 'N/A')}\n",
            )

    def add_data(self):
        _id = self.add_id_entry.get()
        Name = self.add_name_entry.get()
        Age = self.add_age_entry.get()
        marks = self.add_marks_entry.get()
        try:
            collection.insert_one(
                {"_id": _id, "Name": Name, "Age": Age, "marks": marks}
            )
            messagebox.showinfo("Success", "Record added successfully")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def update_data(self):
        _id = self.update_id_entry.get()
        new_Name = self.update_name_entry.get()
        new_Age = self.update_age_entry.get()
        try:
            _id = ObjectId(_id)
        except (errors.InvalidId, TypeError):
            pass
        collection.update_one(
            {"_id": _id}, {"$set": {"Name": new_Name, "Age": new_Age}}
        )
        messagebox.showinfo("Success", "Record updated successfully")

    def delete_data(self):
        _id = self.delete_id_entry.get()
        try:
            _id = ObjectId(_id)
        except (errors.InvalidId, TypeError):
            pass
        collection.delete_one({"_id": _id})
        messagebox.showinfo("Success", "Record deleted successfully")


root = tk.Tk()
app = DatabaseApp(root)
root.mainloop()
