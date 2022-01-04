sudo docker exec -it $1 python manage.py makemigrations
sudo docker exec -it $1 python manage.py migrate
sudo docker exec -it $1 python manage.py makemigrations simple_app
sudo docker exec -it $1 python manage.py migrate simple_app
#sudo docker exec -it $1 python manage.py createsuperuser
#echo $1
sudo docker exec -it $1 bash -c "cat default_creation.py | python manage.py shell"
