import hashlib


class g_b_h:

    block_no : int 
    ID : str
    name : str
    price : float
    date : str
    prev_hash : str
    current_hash : str 
    proof_of_work: int


    def __init__(self,block_no,ID,name,price,date,prev_hash) -> None:
        self.block_no = block_no
        self.ID = ID
        self.name = name
        self.price = price
        self.date = date
        self.prev_hash =prev_hash
    


    def cal_hash(self):
        ite= 0
        self.proof_of_work= 0
        val = False
        while (not val):
            d= (f"proof of work: {self.proof_of_work}\n date: {self.date}\n name: {self.name}\n prev_hash: {self.prev_hash}")
            self.current_hash = hashlib.sha256(d.encode('utf-8')).hexdigest()
            if(self.current_hash[:4]=="0000"):
                val=True
                return self.current_hash
            else:
                ite=ite+1
                self.proof_of_work= (self.block_no**2+(ite*2)**2+(self.price*3))

    def get_proof_val(self):
        return self.proof_of_work

a1 = g_b_h      