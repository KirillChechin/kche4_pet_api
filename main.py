from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

from pathlib import Path
import random

app = FastAPI()


@app.get("/repeat2/{target}")
def repeat(target: str):
    return {'repeat2':target*2, "times_repeated":2}

@app.get("/coffie/")
def coffie(name:str = "latte", size:float=0.4, toppings:str|None = None):
    top = f" with {toppings}" if toppings else ""
    msg = f"You ordered {size} {name}"+ top +", have a nice day!"
    return {'msg':msg, "name":name, "size":size, "toppings":toppings}


def coin_toss():
    choice = ["Tails","Heads"]
    chance = random.randint(0,len(choice)-1)
    result = choice[chance]

@app.get("/coin")
def read_root():
    choice = ["Tails","Heads"]
    chance = random.randint(0,len(choice)-1)
    result = choice[chance]
    file = result+".png"
    return {"coin": result, "file": file}

templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    coin = read_root()
    context = {"request": request, "coin": coin["coin"], "file": coin["file"]}
    return templates.TemplateResponse("coin.html", context)

