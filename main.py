import os
import pandas
import numpy
import json
from datetime import datetime
from fastapi import FastAPI, Request, Response
import uvicorn


app = FastAPI()


def log_to_file(content):
    if not os.path.exists("logs"):
        os.makedirs("logs")

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    log_filename = os.path.join("logs", f"{timestamp}.json")

    with open(log_filename, "a") as log_file:
        log_file.write(content + "\n")


@app.post("/execute")
async def execute_script(request: Request):
    data = await request.json()
    script = data.get("script")

    if not script:
        return {"error": "No script provided"}

    if "def main()" not in script:
        return {"error": "No main() function found"}

    ptr_dict = {}
    try:
        exec(script, {}, ptr_dict)  # exec(object[, globals[, locals]])
        if "main" in ptr_dict and callable(ptr_dict["main"]):
            result = ptr_dict["main"]()
        else:
            result = None
        response = {"result": result, "script": script}
        log_to_file(json.dumps(response))
        return response["result"]

    except Exception as e:
        return {"error": str(e)}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)


"""
Todos
[] Execute the main function
[] Handle script execution errors


"""
