#docker build -t django-app .
#docker run -p 8000:8000 django-app
sudo chmod -R 777 data/db
docker-compose build
docker-compose up
