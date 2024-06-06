import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017")
db = client["Sample"]
collection = db["MySampleCollection"]
print("Database created ")
# update one
# prev={'Name':'Yash'}
# Nextt={'$set':{'Age':'66'}}
# updatee=collection.update_one(prev,Nextt)

"""alll=collection.find({'Name':'Yash'})
for item in alll:
  print(item)"""


# update many
"""prev={'Name':'Yash'}
Nextt={'$set':{'Age':'66'}}
update_all=collection.update_many(prev,Nextt)

alll=collection.find({'Name':'Yash'})
for item in alll:
  print(item)"""
