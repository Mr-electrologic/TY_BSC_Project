import fastapi

from os import getcwd
import os
import reading_csv_product
import reading_DB
from fastapi import Request ,Depends, HTTPException, Form, UploadFile,File
import chain
import my_qr_scan
import all_user
import client
#import server
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse , FileResponse, RedirectResponse
from fastapi.security import OAuth2AuthorizationCodeBearer, OAuth2PasswordBearer




app = fastapi.FastAPI()

def hell():
    try:
        abcd = reading_csv_product.starting
        abcd.print_testing(abcd)
    except:
        print("couldn't read from product CSV")
    try:
        ABCD= reading_DB.starting
    except:
        print("couldn't read from used products CSV")

    
#ser = serverEDIT.server_start()
templates = Jinja2Templates(directory = "htmlfiles")
staticfiles = StaticFiles(directory="./qrcodesImgs/")
app.mount("/static", StaticFiles(directory="qrcodesImgs"), name="static")
oauth2_schema = OAuth2PasswordBearer(tokenUrl="/log_in")

async def get_current_user(token :str = Depends(oauth2_schema)):
    pass


# uviocorn main:app --reload
# python -m uvicorn fast_api:app --reload
# ctrl + c to stop local server


#first endpoint
@app.get('/',response_class=HTMLResponse)
def home(request : Request):
    context = {'request': request}
    return templates.TemplateResponse("home.html", context) 

@app.post('/',response_class=HTMLResponse)
def home(request : Request):
    context = {'request': request}
    return templates.TemplateResponse("home.html", context) 

#second endpoint
@app.post('/add_block',response_class=HTMLResponse)
async def home2(request : Request):
    context = {'request': request}
    return templates.TemplateResponse("log_in.html", context) 

#third endpoint
@app.post('/sign_in', response_class=HTMLResponse)
async def sign_in(request : Request):
    context = {"request": request}
    return templates.TemplateResponse("sing_up.html", context)

#fourth endpoint
@app.post('/sign_up', response_class=HTMLResponse)
async def sign_up(request :Request, Username: str= Form(...),password : str = Form(...),):
    context = {"request": request}
    z= reading_DB.user_finding.searching(Username)
    val = Username + " already taken"
    if(z):
        a= all_user.users(Username,password,'ff5877')
        key2=all_user.users.get_key2(a)
        path : str 
        return templates.TemplateResponse("sign_up_confirm.html",{"request": request, "un":Username, "p": password,"k":key2 } )
    else:
        return templates.TemplateResponse("sing_up.html", {"request": request,'val':val})
        
#fifth endpoint
@app.post('/enter_block')
async def e_block(request :Request, name: str= Form(...),id : str = Form(...), price: float = Form(...),date: str = Form(...)):
    n1 =chain.block(name,id,price,date)
    context = {"request": request}
    b= chain.block.get_block_no(n1)
    c = chain.block.get_add(n1)
    d = c.split("/")
    e= d[3]    
    #return FileResponse(f"./qrcodesImgs/{a}")
    return templates.TemplateResponse("blockEntered.html",{"request": request, "f":e, "e": c ,"e":c})


#sixth endpoint
@app.post('/log_in', response_class=HTMLResponse)
async def log_in(request :Request, Username: str= Form(...),password : str = Form(...), key: str = Form(...)):
    a= all_user.list_of_users.verify_user(100,Username,password,key)
    context = {"request": request}
    if(a):
        return templates.TemplateResponse("enterblock.html",{"request": request, "n":Username} )
    else:
        return templates.TemplateResponse("1.html",{"request": request, "value": Username}) 

#seventh endpoint     
@app.post('/verify_product',response_class=HTMLResponse)
def verify(request : Request):
    context = {'request': request}
    return templates.TemplateResponse("scan.html", context) 

#eigth endpoint
@app.post('/sign_up_confirm/{un}', response_class=HTMLResponse)
async def sign_up2(request :Request):
    return templates.TemplateResponse("enterblock.html",{"request": request} )


@app.post('/about',response_class=HTMLResponse)
def about(request : Request):
    context = {'request': request}
    return templates.TemplateResponse("about.html", context) 

@app.post('/scan',response_class=HTMLResponse)
async def scan_code(request :Request, qr_file: UploadFile = File(...)):
    a= (qr_file.filename)
    c = a.split(".")
    d = c[0]
    file_name = "name.jpg"

    file_location = f"D:/BLOCKCHAIN/{file_name}"

    with open(file_location, "wb+") as file_object:
      file_object.write(qr_file.file.read())
    try:
        e = my_qr_scan.d_data()
        f = my_qr_scan.d_data.data(e)
        dat= str(f)
        dat2= dat.split('\n')
        dat3 = dat2[0].split(': ')
        print(dat3)
        proof_of_work = dat3[1]
        dat3 = dat2[1].split(': ')
        date = dat3[1]
        dat3 = dat2[2].split(': ')
        hash = dat3[1]
        dat3 = dat2[3].split(': ')
        prev_hash = dat3[1]
        dat3 = dat2[4].split(': ')
        id = dat3[1]
        g = my_qr_scan.verif(hash,prev_hash,date,proof_of_work,id)
        my_qr_scan.verif.veri(g)
        val= my_qr_scan.verif.veri(g)
        z="BLOCK FOUND"
        y="details of the product..."
        if (val=="found"):
            return templates.TemplateResponse("blockEntered2.html", {'request': request, 'hash':hash, 'prev_hash':prev_hash, 'id':id, 'date':date,'proof_of_work':proof_of_work,'e':z,'f':y}) 
        if(val == "used"):
            return templates.TemplateResponse("blockEntered2.html", {'request': request, 'hash':"product scaned previously", 'prev_hash':"product scaned previously", 'id':"product scaned previously", 'date':"product scaned previously",'proof_of_work':"product scaned previously",'e':"this product was scanned previously",'f':"please contact the your product seller..."}) 
        else:
            return templates.TemplateResponse("blockEntered2.html", {'request': request, 'hash':"invalid details", 'prev_hash':"invalid details", 'id':"invalid details", 'date':"invalid details",'proof_of_work':"invalid details",'e':"this product is not in out data",'f':"please contact the your product seller..."}) 
    
    except:
        return templates.TemplateResponse("blockEntered2.html", {'request': request, 'hash':"invalid details", 'prev_hash':"invalid details", 'id':"invalid details", 'date':"invalid details",'proof_of_work':"invalid details",'e':"this product is not in out data",'f':"please contact the your product seller..."}) 



@app.get("/file/{name_file}")
def get_file(name_file: str):
    c= os.path.abspath(name_file)
    d="../qrcodesImgs/"
    abs_file_path = os.path.join(c, d)
    print(abs_file_path)
    return FileResponse(abs_file_path+name_file)
  #chain.block(ID,name,price)
    #file_path = "/qrcodesImgs/"
    #c= QR_gen.QR_co.block_no
    #return RedirectResponse("/enter_block/entered_block")

