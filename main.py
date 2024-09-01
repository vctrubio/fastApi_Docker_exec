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


def extract_context(script):
    try:
        main_start = script.index("def main()")

        main_content = script[
            main_start:
        ]  ## Needs to check for the return and not include the rest

        return {"main_function_content": main_content}

    except Exception as e:
        return {"error": f"Failed to extract main(): {str(e)}"}


@app.post("/execute")
async def execute_script(request: Request):
    data = await request.json()
    script = data.get("script")

    if not script:
        return {"error": "No script provided"}

    if "def main()" not in script:
        return {"error": "No main() function found"}

    i = extract_context(script)

    response = {
        "result": "script executed successfully",
        "context": i,
        "script": script,
    }
    log_to_file(json.dumps(response))

    return response


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)
