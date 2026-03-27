from datetime import datetime
from fastapi import FastAPI, HTTPException
from typing import Any

app = FastAPI(root_path="/api/v1")

@app.get("/")
async def root():
    return {"message": "Hello world"}

data : Any = [
    {
        "campaign_id": 1,
        "name": "WorkOn",
        "due_date": datetime.now(),
        "created_at": datetime.now(),
    },
    {
        "campaign_id": 2,
        "name": "BlackMiddle",
        "due_date": datetime.now(),
        "created_at": datetime.now(),
    },
]

@app.get("/campaigns")
async def read_campaigns():
    return {"campaigns": data}

@app.get("/campaigns/{id}")
async def read_campaign(id: int):
    for campaign in data:
        if campaign.get("campaign_id") == id:
            return {"campaign": campaign}
    raise HTTPException(status_code=404)
