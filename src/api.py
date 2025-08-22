from fastapi import FastAPI
from pydantic import BaseModel
from src.agent  import WaterIntakeAgent
from src.logger import log_message, log_error
from src.database import log_intake , get_intake_history


app = FastAPI()
agent = WaterIntakeAgent()

class WaterIntakeRequest(BaseModel):
    user_id : str
    intake_ml: int

@app.post ("/log-intake")
async def log_water_intake(request: WaterIntakeRequest):
    log_intake(request.user_id, request.intake_ml)
    analysis=agent.analyze_intake(request.intake_ml)
    log_message(f"user {request.user_id} has logged with water intake {request.intake_ml}")
    return {"message":"the water intake is successfully logged","analysis":analysis}

@app.get("/histroy/{user_id}")
async def get_water_history(user_id:str):
    history = get_intake_history(user_id)
    return {"user_id":user_id, "history":history}

    