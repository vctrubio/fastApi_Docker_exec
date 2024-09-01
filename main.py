import os
import pandas
import numpy

from fastapi import FastAPI, Request, Response
import uvicorn


app = FastAPI()

@app.post("/execute")
async def execute_script():
    return {"message": "Script will executed"}



if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)
