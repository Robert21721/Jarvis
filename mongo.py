from pymongo import MongoClient

CONNECTION_STRING = "mongodb+srv://User:Password@cluster0.lsv82vu.mongodb.net/?retryWrites=true&w=majority"

client = MongoClient(CONNECTION_STRING)
print("Connection Successful")

JarvisDB = client["JarvisDB"]
contacts = JarvisDB["contacts"]

p1 = {
    "name" : "Name",
    "phone_nr" : "0123456789"
}


contacts.insert_one(p1)

# for x in contacts.find():
#     if (x["name"] == "MyName"):
#         print(x["phone_nr"])

client.close()