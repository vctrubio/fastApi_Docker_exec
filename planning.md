# Sunday 1 Sept

You are building a service that enables customers to execute arbitrary python code on a cloud server. The user sends a python script and the execution result of the main() function gets returned.

Build an API service that takes any python script as input and returns the result of the script execution as output.

## Bullet point step by step

- Build api endpoint
    -excute endpoint that accepts multiline JSON request
    -{"script": "def main(): ..."}
        -validations [no function main, does not return a JSON] ->throw error

- build the docker image

- deploy on google cloud run as an api

## get_time_now()

- 10.30AM [start]
- 12PM [FastAPI/Backend]
- 12.30 [DockerBuild]
- 13.00 [Gcloud]
- 13.30 [Finished] -- bug did not remove __main__ uvicorn and took for.ev.er

