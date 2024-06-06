import pymongo

if __name__ == "__main__":
    print("welcome to pymongo")
    client = pymongo.MongoClient("mongodb://localhost:27017")
    print(client)
    # alldatabses=client.list_database_names()
    # print(alldatabses)
