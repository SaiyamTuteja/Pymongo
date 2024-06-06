import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017")
db = client["Sample"]
collection = db["MySampleCollection"]
print("Databases connected")
"Read One record from database"
# one=collection.find_one({'Name':'Shikha'})
# print(one)
"read all records from the database"
alldocs = collection.find({"Name": "Muskan"}, {"Name": 1, "Age": 1, "_id": 0})
# {'Name':1,'Age':1,'_id':0} -------------------> this will use to show thw value which is having the value as 1 and 0 will be excluded output----->{'Name': 'Muskan', 'Age': 20}
if alldocs:
    for i in alldocs:
        print(i)
else:
    print("Not Availabel")
