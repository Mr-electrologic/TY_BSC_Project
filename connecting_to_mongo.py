import pymongo


class enter_products_to_mongo:
    def __init__(self,proof_of_work,id,date,name,prev_hash,hash,block_no,price):
        client = pymongo.MongoClient("mongodb://localhost:27017")
        print("entering products")
        db = client['BLOCK_CHAIN']
        collection = db['PRODUCTS ENTERED']
        dictonary = {'_id': id,'block_no':block_no, 'name':name,'date':date,'price':price,'proof_of_work':proof_of_work, 'prev_hash':prev_hash,'current_hash':hash}
        try:
            collection.insert_one(dictonary)
        except:
            print("entering to mongoDB failed")

class enter_used_products_to_mongo:
    def __init__(self,id,prev_hash,date,proof_of_work,hash):
        client = pymongo.MongoClient("mongodb://localhost:27017")
        print("entering used products")
        db = client['BLOCK_CHAIN']
        collection = db['USED PRODUCTS ENTERED']
        dictonary = {'_id': id,'date':date,'proof_of_work':proof_of_work, 'prev_hash':prev_hash,'current_hash':hash}
        try:
            collection.insert_one(dictonary)
        except:
            print("entering to mongoDB failed")


class enter_user_to_mongo:
    def __init__(self,username,password,id,key2):
        client = pymongo.MongoClient("mongodb://localhost:27017")
        print('entering user')
        db = client['BLOCK_CHAIN']
        collection = db['USERS LIST']
        dictonary = {'USERNAME':username,'password':password, 'key':key2}
        try:
            collection.insert_one(dictonary)
        except:
            print("entering to mongoDB failed")
