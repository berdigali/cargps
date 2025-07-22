from fastapi import FastAPI
from datetime import datetime

app = FastAPI()

@app.get("/")
def read_root():
    return {"status": "ok", "time": datetime.now().isoformat()}

@app.get("/ping")
def ping():
    return {"message": "pong"}

@app.get("/status")
def status():
    return {"service": "CarGPS FastAPI Bot", "status": "running"}
