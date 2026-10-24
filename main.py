from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

stations = [
    {
        "id": 1,
        "name": "Aurora Station",
        "orbit": "Mars",
        "crew": 5,
    },
    {
        "id": 2,
        "name": "Ceres Base",
        "orbit": "Moon",
        "crew": 5,
    },
    {
        "id": 3,
        "name": "Lumenis Colony",
        "orbit": "LHS 1140b",
        "crew": 5,
    },
    {
        "id": 4,
        "name": "Название станции",
        "orbit": "Орбита или объект",
        "crew": 5,
    },
]

class Station(BaseModel):
    id: int
    name: str
    orbit: str
    crew: int

class StationCreate(BaseModel):
    name: str
    orbit: str
    crew: int

@app.get("/station" , response_model=list[Station])
def get_stations():
    return stations

@app.post("/station" , response_model=Station , status_code=201)
def create_station(station: StationCreate):
    new_station = station.model_dump()
    new_station["id"] = len(stations) + 1
    stations.append(new_station)
    return new_station

