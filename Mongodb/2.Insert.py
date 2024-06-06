import pymongo

if __name__ == "__main__":
    print("welcome to pymongo")
    client = pymongo.MongoClient("mongodb://localhost:27017")
    print(client)
    db = client["Sample"]
    collection = db["MySampleCollection"]
    "List of collection in the databasses "
    # allcollection=db.list_collection_names()
    # print(allcollection)
    "insert_one data entery "
    # dictionary={'Name':'Saiyam Tuteja','marks': 56,'Age':22}
    # collection.insert_one(dictionary)
    # dictionary={'Name':'Shikha ','marks': 63,'Age':21}
    # collection.insert_one(dictionary)
    # dictionary={'Name':'Muskan','marks': 10,'Age':20}
    # collection.insert_one(dictionary)
    # print("database Createed ")
    "Insert_many" "function for insert no of document in it "
    # insert_these = [
    #     {"Name": "Saiyam Tuteja", "marks": 56, "Age": 21},
    #     {"Name": "Shiikha", "marks": 67, "Age": 22},
    #     {"Name": "Yash", "marks": 46, "Age": 20},
    #     {"Name": "Pryag", "marks": 60, "Age": 23},
    # ]
    # collection.insert_many(insert_these)
    # print("Data Inserted sucessfull")
    "inserted link"
    # dictionary={'_id':1,'Image':'E:/lenovo thinkcenter/saiyam.jpg'}
    # collection.insert_one(dictionary)
