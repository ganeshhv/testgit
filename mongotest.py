import pymongo

client = pymongo.MongoClient("mongodb+srv://ganeshhv:5620@cluster0.zdjswjw.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d = {
    'name': 'ganesh',
    'email': 'ganeshhv800@gmail.com',
    'age': 27
}

# db name
db1 = client['mongotest']
# collection/ table name
coll = db1['test']
coll.insert_one(d)