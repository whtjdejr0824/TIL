import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
# "mydatabase"라는 데이터베이스를 만듭니다. 
# 단, MongoDB는 실제로 데이터베이스 (및 컬렉션)를 만들기 전에 
# 최소한 하나의 문서 (레코드)가있는 컬렉션 (테이블)을 만들 때까지 생성 X
mydb = myclient["mydatabase"]

# DB 리스트 확인
# print(myclient.list_database_names())

# dblist = myclient.list_database_names()
# if "mydatabase" in dblist:
#   print("The database exists.")

# mycol = mydb["customers"]
# print(mydb.list_collection_names())

# collist = mydb.list_collection_names()
# if "customers" in collist:
#   print("The collection exists.")

mycol = mydb["customers"]

# mydict = { "name": "Peter", "address": "Lowstreet 27" }

# x = mycol.insert_one(mydict)

# print(x.inserted_id)

# mylist = [
#   { "name": "Amy", "address": "Apple st 652"},
#   { "name": "Hannah", "address": "Mountain 21"},
#   { "name": "Michael", "address": "Valley 345"},
#   { "name": "Sandy", "address": "Ocean blvd 2"},
#   { "name": "Betty", "address": "Green Grass 1"},
#   { "name": "Richard", "address": "Sky st 331"},
#   { "name": "Susan", "address": "One way 98"},
#   { "name": "Vicky", "address": "Yellow Garden 2"},
#   { "name": "Ben", "address": "Park Lane 38"},
#   { "name": "William", "address": "Central st 954"},
#   { "name": "Chuck", "address": "Main Road 989"},
#   { "name": "Viola", "address": "Sideway 1633"}
# ]

# x = mycol.insert_many(mylist)

# #print list of the _id values of the inserted documents:
# print(x.inserted_ids)

# mylist = [
#   { "_id": 1, "name": "John", "address": "Highway 37"},
#   { "_id": 2, "name": "Peter", "address": "Lowstreet 27"},
#   { "_id": 3, "name": "Amy", "address": "Apple st 652"},
#   { "_id": 4, "name": "Hannah", "address": "Mountain 21"},
#   { "_id": 5, "name": "Michael", "address": "Valley 345"},
#   { "_id": 6, "name": "Sandy", "address": "Ocean blvd 2"},
#   { "_id": 7, "name": "Betty", "address": "Green Grass 1"},
#   { "_id": 8, "name": "Richard", "address": "Sky st 331"},
#   { "_id": 9, "name": "Susan", "address": "One way 98"},
#   { "_id": 10, "name": "Vicky", "address": "Yellow Garden 2"},
#   { "_id": 11, "name": "Ben", "address": "Park Lane 38"},
#   { "_id": 12, "name": "William", "address": "Central st 954"},
#   { "_id": 13, "name": "Chuck", "address": "Main Road 989"},
#   { "_id": 14, "name": "Viola", "address": "Sideway 1633"}
# ]

# x = mycol.insert_many(mylist)

# #print list of the _id values of the inserted documents:
# print(x.inserted_ids)

# x = mycol.find_one()

# print(x)

# for x in mycol.find():
#   print(x)

# id를 제외한, 이름과 주소를 출력
# for x in mycol.find({},{ "_id": 0, "name": 1, "address": 1 }):
#   print(x)

# 주소를 제외한 나머지 값 출력
# for x in mycol.find({},{ "address": 0 }):
#   print(x)

# 동일한 객체에 0과 1값을 모두 지정하면 오류!(통일을 하거나 위의 예시처럼 해야 오류X)
# for x in mycol.find({},{ "_id": 0, "name": 1, "address": 0 }):
#   print(x)

# myquery = { "address": "Park Lane 38" }

# mydoc = mycol.find(myquery)

# for x in mydoc:
#   print(x)

# 고급 쿼리 (주소가 알파벳 S이상으로 시작하는 문서)
# myquery = { "address": { "$gt": "S" } }

#mydoc = mycol.find(myquery)

#for x in mydoc:
  #print(x)


# 정규식으로 필터링(S로만 시작하는 데이터)
myquery = { "address": { "$regex": "^S" } }

mydoc = mycol.find(myquery)

for x in mydoc:
  print(x)