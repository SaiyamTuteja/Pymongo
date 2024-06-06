
# Pymongo 📚

Pymongo is a powerful and flexible library that bridges MongoDB with Python, enabling seamless database management and operations.

![image](https://github.com/SaiyamTuteja/Pymongo/assets/119167105/372f46ba-b44a-4ed8-bda5-bea7e86f9639)

## Table of Contents 📑

- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Examples](#examples)
- [Contributing](#contributing)
- [License](#license)

## Installation 💻

To install Pymongo, use the following command:

```bash
pip install pymongo
```

## Usage 🚀

This repository contains the following files to manage MongoDB operations using Python:

1. **connection.py**: Connects to MongoDB Compass.
2. **insert.py**: Inserts records into the database.
3. **read.py**: Fetches records from the database.
4. **update.py**: Updates records in the database.
5. **delete.py**: Deletes records from the database.
6. **main_project.py**: Combines all features into a single file for ease of use.

## Features ✨

- **Easy Connection**: Effortlessly connect to MongoDB Compass using `connection.py`.
- **CRUD Operations**: Perform Create, Read, Update, and Delete operations with dedicated scripts.
- **Unified Project**: Use `main_project.py` to access all functionalities in one place.

## Examples 🔍

### Connecting to MongoDB

```python
# connection.py
from pymongo import MongoClient

def connect_to_mongodb():
    client = MongoClient('mongodb://localhost:27017/')
    return client

# Usage
client = connect_to_mongodb()
print("Connected to MongoDB Compass!")
```

### Inserting a Record

```python
# insert.py
from connection import connect_to_mongodb

def insert_record(data):
    client = connect_to_mongodb()
    db = client['your_database']
    collection = db['your_collection']
    collection.insert_one(data)
    print("Record inserted successfully!")

# Usage
insert_record({"name": "John Doe", "age": 30})
```

### Fetching Records

```python
# read.py
from connection import connect_to_mongodb

def fetch_records():
    client = connect_to_mongodb()
    db = client['your_database']
    collection = db['your_collection']
    records = collection.find()
    for record in records:
        print(record)

# Usage
fetch_records()
```

### Updating a Record

```python
# update.py
from connection import connect_to_mongodb

def update_record(query, new_values):
    client = connect_to_mongodb()
    db = client['your_database']
    collection = db['your_collection']
    collection.update_one(query, {'$set': new_values})
    print("Record updated successfully!")

# Usage
update_record({"name": "John Doe"}, {"age": 31})
```

### Deleting a Record

```python
# delete.py
from connection import connect_to_mongodb

def delete_record(query):
    client = connect_to_mongodb()
    db = client['your_database']
    collection = db['your_collection']
    collection.delete_one(query)
    print("Record deleted successfully!")

# Usage
delete_record({"name": "John Doe"})
```

### Main Project
# Main_project.py

## Contributing 🤝

Contributions are welcome! Please open an issue or submit a pull request with your improvements.

## License 📜

This project is licensed under the MIT License.

