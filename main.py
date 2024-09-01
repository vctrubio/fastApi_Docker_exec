import os
import io
import sys

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

    exec_var = {}
    try:
        old_stdout = sys.stdout
        sys.stdout = io.StringIO()
        
        exec(script, {}, exec_var)  # exec(object[, globals[, locals]])
        if "main" in exec_var and callable(exec_var["main"]):
            result = exec_var["main"]()
        else:
            result = None
            
        sys.stdout = old_stdout

        response = {"result": result, "script": script}
        log_to_file(json.dumps(response))
        return response["result"]

    except Exception as e:
        sys.stdout = old_stdout
        error_msg = {"error": str(e)}
        log_to_file(json.dumps(error_msg))
        return error_msg

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)


"""
Todos
[X] Execute the main function
    [] Test many cases of main functions
[] Handle script execution errors

"""
