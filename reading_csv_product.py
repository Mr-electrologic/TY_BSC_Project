import pandas as pd
import chain
import pymongo

class starting:

    name=[]
    id=[]
    price=[]
    date=[]
    alldoc = []
    
    def print_testing(self):
        client = pymongo.MongoClient("mongodb://localhost:27017")
        print("reading DB for products")
        db = client['BLOCK_CHAIN']
        collection = db['PRODUCTS ENTERED']
        alldoc = collection.find({})

            
        for val in alldoc:
            self.name.append(val['name'])


        for val in alldoc:
            self.id.append(val['_id'])


        for val in alldoc:
            self.price.append(val['price'])


        for val in alldoc:
            self.date.append(str(val['date']))
        
        chain.l1.list1.clear()
        
        objs = []
        for m in range(len(self.name)):
            objs.append(chain.block(self.name[m],self.id[m],self.price[m],self.date[m]))
            print(m)
        
        