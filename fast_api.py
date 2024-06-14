import fastapi
from fastapi import Request , Form
import chain
import QR_gen
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse , FileResponse, RedirectResponse


app = fastapi.FastAPI()
templates = Jinja2Templates(directory = "htmlfiles")


# uviocorn main:app --reload
# python -m uvicorn fast_api:app --reload
# ctrl + c to stop local server


#first endpoint
@app.get('/',response_class=HTMLResponse)
def home(request : Request):
    context = {'request': request}
    return templates.TemplateResponse("home.html", context) 

#second endpoint
@app.post('/scanner',response_class=HTMLResponse)
async def home(request : Request):
    context = {'request': request}
    return templates.TemplateResponse("scan.html", context) 

#third endpoint
@app.post('/add_block',response_class=HTMLResponse)
async def home(request : Request):
    context = {'request': request}
    return templates.TemplateResponse("log_in.html", context) 

#4th endpoint
@app.post('/log_in', response_class=RedirectResponse)
async def e_block(request :Request, Username: str= Form(...),password : str = Form(...)):
    context = {"request": request}
    #chain.block(ID,name,price)
    #file_path = "/qrcodesImgs/"
    #c= QR_gen.QR_co.block_no
    #return RedirectResponse("/enter_block/entered_block")
    redirect_url= request.url_for('http://localhost:8000//log_in/enter_block')
    return RedirectResponse(redirect_url, status_code=status.HTTP_303_SEE_OTHERS)


@app.get('/log_in/enter_block' )
def e_b(request : Request):
    context = {"request": request}
    #file_path = "/qrcodesImgs/"
    #c= QR_gen.QR_co.block_no

    return templates.TemplateResponse("enterblock.html",context)


@app.get('/enter_block/entered_block', response_class=HTMLResponse)
async def log(ID: str= Form(...),name : str = Form(...), price : float = Form(...)):
    #context = {"request": request}
    chain.block(ID,name,price)
    context = {'request': request }
    return templates.TemplateResponse("blockEntered.html", context)

@app.get('/about', response_class=HTMLResponse)
def e_b(request: Request):
    context = {'request': request }
    return templates.TemplateResponse("about.html", context)