docker build -t fastapi-app .
docker run -d -p 8080:8080 fastapi-app
docker run -it fastapi-app /bin/sh
docker logs [id]
docker stop [id]