from fastapi import FastAPI

from data import get_team_from_fake_db, get_all_teams_from_fake_db

app = FastAPI()

@app.get("/")
def index():
    return{"message" : "Bienvenue sur F1 2021"}

@app.get("/teams")
def get_teams():
    return get_all_teams_from_fake_db()
