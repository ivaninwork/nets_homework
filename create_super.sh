sudo docker exec -it $1 python manage.py migrate --noinput
#sudo docker exec -it $1 python manage.py createsuperuser
#echo $1
sudo docker exec -it $1 bash -c "cat default_creation.py | python manage.py shell"
