from pymongo import MongoClient

client = MongoClient("localhost", 27017)

db = client.get_database("Student_DB")

coll = db.get_collection("student_Data")
coll.