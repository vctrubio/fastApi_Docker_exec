start:
	docker-compose up -d fastapi-app

stop:
	docker-compose down

build:
	docker buildx create --use
	docker buildx build --platform linux/amd64 -t gcr.io/ozu-tokenise/fastapi-app:latest --push .
	docker push gcr.io/ozu-tokenise/fastapi-app:latest

test:
	docker run -p 8080:8080 gcr.io/ozu-tokenise/fastapi-app:latest

deploy:
	gcloud run deploy fastapi-app \
   --image gcr.io/ozu-tokenise/fastapi-app:latest \
   --platform managed \
   --region europe-west1 \
   --allow-unauthenticated \
   --port 8080

