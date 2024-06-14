import pandas as pd


class products:
    block_no = 0
    ID : str
    name : str
    price : float
    date : str
    prev_hash : str
    current_hash : str 
    proof_of_work : int
    
    
    def __init__(self,i,ph,d,pow,h):
        self.block_no = self.block_no + 1
        self.ID = i
        self.date=d
        self.prev_hash=ph
        self.current_hash=h
        self.proof_of_work=pow
        l1.add_block(self)
        return None
    
class writetofile:
    list1 =[]
    def add_block(b = products):
        l1.list1.append(b)
        file = open('usedblocks.txt','w')
        for i in l1.list1:
            file.write("**************************-block ")
            file.write(str((i.block_no)))
            Up_csv.A.append(i.block_no)
            file.write("-*************************\n")
            file.write("ID: ")
            file.write(str(i.ID))
            Up_csv.b.append(i.ID)
            file.write("\n")
            file.write("date of manufacturing: ")
            file.write(str(i.date))
            Up_csv.c.append(i.date)
            file.write("\n")
            file.write("proof of work: ")
            file.write(str(i.proof_of_work))
            Up_csv.d.append(i.proof_of_work)
            file.write("\n")
            file.write("prev_hash: ")
            file.write( str(i.prev_hash))
            Up_csv.e.append(i.prev_hash)
            file.write("\n")
            file.write("current_hash: ")
            file.write(str(i.current_hash))
            Up_csv.f.append(i.current_hash)
            file.write("\n ")
            file.write("************************************************************\n\n")
        file.close()
        Up_csv.print_to_file(Up_csv)
    
l1 = writetofile

class write_to_execl_user:
    list1 = []
    A=[]
    b=[]
    c=[]
    d=[]
    e=[]
    f=[]

    def print_to_file(self):
        df = pd.DataFrame.from_dict({'block_no': Up_csv.A, 'ID': Up_csv.b, 'date': Up_csv.c, 'proof_of_work': Up_csv.d, 'prev_hash': Up_csv.e, 'current_hash': Up_csv.f})
        df.to_csv('Usedproducts.csv', index=False)
    
Up_csv= write_to_execl_user