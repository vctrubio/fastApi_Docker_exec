# Docker CMDS

docker build -t fastapi-app .
docker run -d -p 8080:8080 fastapi-app
docker run -it fastapi-app /bin/sh
docker logs [id]
docker stop [id]

## GCR CMDS

gcr.io: The main domain used by Google Container Registry for storing container images. It’s commonly used for global availability and is tied to the Google Cloud region you select.

gcr.io/[PROJECT-ID]/[IMAGE-NAME]:[TAG]
gcr.io/ozu-tokenise/fastapi-app:latest
