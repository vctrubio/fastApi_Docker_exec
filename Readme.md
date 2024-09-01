# FastAPI Application - Safe Python Script Execution Service

## Terminal Input

gcloud run deploy fastapi-app \
--image gcr.io/ozu-tokenise/fastapi-app:latest \
--platform managed \
--region europe-west1 \
--allow-unauthenticated \
--port 8080

## Output

Deploying container to Cloud Run service [fastapi-app] in project [ozu-tokenise] region [europe-west1]

```bash
curl -X POST "https://fastapi-app-[hash]-ew.a.run.app/execute" \
-H "Content-Type: application/json" \
-d "{\"script\": \"def main():\\n    return {'result': 4}\"}"
```




## Note

I did not experiment with nsjail
