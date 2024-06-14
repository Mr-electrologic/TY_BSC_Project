import cv2
import usedproduct
import connecting_to_mongo
import pandas as pd
import pymongo

class d_data:
    hash: str
    prev: str
    date : str
    proof_of_work: str
    id: str
    a:str

    
    def __init__(self) -> None:
        pass
        
    def data(self):
        detector= cv2.QRCodeDetector()
        reval,points,s_qr= detector.detectAndDecode(cv2.imread('name.jpg'))
        return reval

class verif:
    
    proof_of_work: float
    hash2: str
    prev2: str
    date2 : str
    proof_of_work2: str
    id2: str
    a = False
    b = False
    C = "not found"

    def __init__(self,hash,prev,date,proof_of_work,id):
        self.hash2=hash
        self.prev2=prev
        self.proof_of_work2=proof_of_work
        self.date2=date
        self.id2=id
        self.proof_of_work=float(self.proof_of_work2)
        #print(self.hash,self.prev,self.proof_of_work,self.date,self.id)
        self.find_block()

    def veri(self):
        return self.C

    def find_block(self):
        #reading database for the product
        client = pymongo.MongoClient("mongodb://localhost:27017")
        db = client['BLOCK_CHAIN']
        collection = db['PRODUCTS ENTERED']
        print('finding product')
        one = collection.find_one({'_id': self.id2,'date':self.date2,'proof_of_work':self.proof_of_work, 'prev_hash':self.prev2,'current_hash':self.hash2})
        c= True
        if(one == None):
            c = False
        
        #reading database for the used product
        collection2 = db['USED PRODUCTS ENTERED']
        print('finding product in used list')
        two = collection2.find_one({'_id': self.id2,'date':self.date2,'proof_of_work':self.proof_of_work2, 'prev_hash':self.prev2,'current_hash':self.hash2})
        c2= True
        if(two == None):
            c2 = False
            print("FALSE")
        
        if(c and c2):
            self.C = "used"
        
        if(c and (not c2)):
            self.C = "found"
            print("found")
        
        if(self.C=="found"):
            abc =usedproduct.products(self.id2,self.prev2,self.date2,self.proof_of_work2,self.hash2)
            ABC = connecting_to_mongo.enter_used_products_to_mongo(self.id2,self.prev2,self.date2,self.proof_of_work2,self.hash2)

#abc = verif("00002a1ed4e1d1fb4562628271c21ff2e9b18b28f1edd073dcf623d329eda792","0","27-11-2020","817435.0","i5")
#print(abc.a)