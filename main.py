from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from backend_service import process_battery_input

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class BatteryInput(BaseModel):
    v_start: float
    v_end: float
    t_start: float
    t_max: float
    current: float
    time: float
    ambient_temp: float

@app.get("/")
def root():
    return {"message": "BatteryIQ Backend is Running 🚀"}

@app.post("/analyze")
def analyze_battery(data: BatteryInput):
    input_data = {
        "v_start": data.v_start,
        "v_end": data.v_end,
        "t_start": data.t_start,
        "t_max": data.t_max,
        "current": data.current,
        "time": data.time,
        "ambient_temp": data.ambient_temp
    }
    return process_battery_input(input_data)