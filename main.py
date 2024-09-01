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


def run_script_in_sandbox(script):
    exec_var = {}
    try:
        old_stdout = sys.stdout
        sys.stdout = io.StringIO()

        exec(script, {}, exec_var)

        if "main" in exec_var and callable(exec_var["main"]):
            result = exec_var["main"]()
        else:
            raise ValueError("main() function is not defined or not callable")

        sys.stdout = old_stdout

        try:
            json.dumps(result)
        except (TypeError, ValueError):
            raise ValueError("main() did not return a JSON-serializable object")

        return {"result": result, "script": script}

    except Exception as e:
        sys.stdout = old_stdout
        raise e


@app.post("/execute")
async def execute_script(request: Request):
    data = await request.json()
    script = data.get("script")

    if not script:
        return {"error": "No script provided"}

    if "def main()" not in script:
        return {"error": "No main() function found"}

    try:
        result = run_script_in_sandbox(script)
        log_to_file(json.dumps(result))
        return result["result"]

    except Exception as e:
        result = {"error": str(e), "script": script}
        log_to_file(json.dumps(result))
        return result["error"]


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)
