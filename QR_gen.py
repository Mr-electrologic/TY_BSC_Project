import qrcode
import shutil
import os
import pandas as pd
import connecting_to_mongo

class QR_co:
    block_no : str
    path_1 : str
    d : str
    brand_name : str
    
    def __init__(self,proof_of_work,id,date,name,prev_hash,hash,block_no,price):
        g.A.append(str((block_no)))
        g.b.append(str((id)))
        g.c.append(str((date)))
        g.d.append(str((name)))
        g.e.append(str((proof_of_work)))
        g.f.append(str((prev_hash)))
        g.G.append(str((hash)))
        g.h.append(str((price)))
        a= connecting_to_mongo.enter_products_to_mongo(proof_of_work,id,date,name,prev_hash,hash,block_no,price)
        features = qrcode.QRCode(version=1, box_size=10, border=3)
        a= (f" proof of work: {proof_of_work}\ndate: {date}\n hash: {hash}\n prev_hash: {prev_hash}\n id: {id}")
        features.add_data(a)
        features.make_image(fit=True)
        b = features.make_image(fill_color = "black", back_color = "white")
        lop = True
        while(lop):
            c= ("BLOCK-"+str(block_no)+".jpg")
            e= os.path.abspath(c)
            d="../qrcodesImgs/"
            f = os.path.join(e, d)
            pt = os.path.join(f,c)
            if os.path.exists(pt):
                block_no = block_no + 1
            else:
                lop = False
                b.save(c)
                shutil.move(c, "D:/BLOCKCHAIN/qrcodesImgs/")
                self.d=c
        
            

    def get_ad(self):
        self.c = ("D:/BLOCKCHAIN/qrcodesImgs/"+self.d)
        return self.c

    def get_name(self):
        return self.d

class user_qr:
    def __init__(self,u_n,id,password,key) -> None:
        U_csv.A.append(u_n)
        U_csv.b.append(id)
        U_csv.c.append(password)
        U_csv.d.append(key)
        U_csv.print_to_file(U_csv)
        features = qrcode.QRCode(version=1, box_size=10, border=3)
        a= (f"user name: {u_n}\n ID: {id}\n password: {password}\n key: {key}")
        features.add_data(a)
        features.make_image(fit=True)
        b = features.make_image(fill_color = "black", back_color = "blue")
        c= ("USER-"+str(u_n)+key+".jpg")
        b.save(c)
        shutil.move(c, "D:/BLOCKCHAIN/user_qr/")
        self.block_no=c
        self.path_1= ("D:/BLOCKCHAIN/user_qr/"+str(c))
    
    def get_path(self):
        return self.path_1
    

class write_to_execl_product:
    list1 = []
    A=[]
    b=[]
    c=[]
    d=[]
    e=[]
    f=[]
    G=[]
    h=[]
    def print_to_file(self):
        df = pd.DataFrame.from_dict({'block_no': g.A, 'ID': g.b, 'date': g.c, 'name': g.d, 'proof_of_work': g.e, 'prev hash': g.f, 'current hash': g.G,'price':g.h})
        df.to_csv('products.csv', index=False)
    

g= write_to_execl_product

class write_to_execl_user:
    list1 = []
    A=[]
    b=[]
    c=[]
    d=[]
    

    def print_to_file(self):
        df = pd.DataFrame.from_dict({'ID': U_csv.c,'user_name': U_csv.A,  'password': U_csv.b, 'key': U_csv.d})
        df.to_csv('users.csv', index=False)
    
U_csv= write_to_execl_user