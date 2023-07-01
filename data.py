from typing import Union

#2021 formulas one time
f1_teams =[
    {
        "team": "Mercedes",
        "drivers" : ["Lewis Hamilton", "Veleris Bottas"],
        "engine" : "Mercedes"
    },
    {
        "team": "Red Bull Racing",
        "drivers" : ["Max Verstappen","Sergio Perez"],
        "engine" : "Honda"
    },
    {
        "team": "Aston Martin",
        "drivers" : ["Sebastien Vettel", "Lance Stroll"],
        "engine" : "Mercedes"
    },
    {
        "team": "McLaren",
        "drivers" : ["Daniel Ricciano","Lando Norris"],
        "engine" : "Mercedes"
    },
    {
        "team": "Alpha Tauri",
        "drivers" : ["Pierre Gasly","Yuki Tsunoda"],
        "enginer" : "Honda"
    },
    {
        "team": "Ferrari",
        "drivers" : ["Charles Leclerc","Carlos Sainz"],
        "enginer" : "Ferrari"
    },
    {
        "team": "Alpine",
        "drivers" : ["Fernando Alonso","Esteban Ocon"],
        "enginer" : "Renaul"
    },
    {
        "team": "Alfa Romeo",
        "drivers" : ["Charles Leclerc","Carlos Sainz"],
        "enginer" : "Ferrari"
    },
    {
        "team": "Haas",
        "drivers" : ["Nikita Mazepi","Mick Shumarcher"],
        "engine" : "Ferrari"
    },
    {
        "team": "Williams",
        "drivers" : ["George Rusell", "Nicholas Latifi"],
        "engine" : "Mercedes"
    }
    ]

def get_all_teams_from_fake_db() -> list:
    """Return a team from F1 2021"""
    return f1_teams

def get_team_from_fake_db(team: str) -> Union[dict, None]:
    for f1_team in f1_teams:
        if team.lower() == f1_team.get('team').lower():
            return f1_team

    return None

