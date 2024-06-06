import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017")
db = client["Sample"]
collection = db["MySampleCollection"]
print("Databases connected ")
"Delete one record"
# dell=collection.delete_one({'Name':'Saiyam Tuteja'})
# print("data deletd suceesfuill ")
"""for view the database"""
# one=collection.find({'Name':'Saiyam Tuteja'})
# for i in one:
#     print(i)
"delete all record "
# dell=collection.delete_many({'Name':'Saiyam Tuteja'})
# print("data deletd suceesfuill ")
