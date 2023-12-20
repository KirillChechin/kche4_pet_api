from fastapi import FastAPI
import random

app = FastAPI()

@app.get("/")
def read_root():
    choice = ["Tails","Heads"]
    chance = random.randint(0,len(choice)-1)
    result = choice[chance]
    return {"result": result}
