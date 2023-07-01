from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/main")
def index():
    return{"message" : "Bienvenue sur FastApi"}

@app.get("/items")
def get_items():
    return[{"id": 1, "Description":"Items1"},
           {"id": 1, "Description": "Items1"},
           {"id": 1, "Description": "Items1"}
           ]

if __name__ == '__main__':
    uvicorn.run(app)