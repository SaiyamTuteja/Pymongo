from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")
db = client["Sample"]
collection = db["MySampleCollection"]
print("Database Setup")


def list_data():
    for item in collection.find():
        


def add_data(_id, name, age, marks):
    collection.insert_one({"_id": _id, "Name": name, "age": age, "marks": marks})
    print("Add the record sucessfull")


def Update_data(id, name):
    pass


def Delete_data(_id, name):
    pass


def main():
    while True:
        print("\n Database Management App")
        print("1. List all Data")
        print("2. Add a new Data")
        print("3. Update a Data")
        print("4. Delete a Data")
        print("5. Exit the app")
        choice = input("Enter your Choice:")

        if choice == "1":
            list_data()
        elif choice == "2":
            _id = input("Enter the ID:")
            name = input("Enter the Name:")
            age = input("Enter the Age:")
            marks = input("Enter the Marks:")
            add_data(id, name, age, marks)
        elif choice == "3":
            _id = input("Enter the Id for update:")
            name = input("Enter the Name for update:")
            Update_data(_id, name)
        elif choice == "4":
            _id = input("Enter the id to delete :")
            Delete_data(_id, name)
        elif choice == "5":
            break
        else:
            print("invalid selectiion enter valid choice")


if __name__ == "__main__":
    main()
