docker-compose build -t tools_vikki_in .
sudo docker run -d -p 8085:8085 --name tools.vikki.in tools_vikki.in python tools/manage.py runserver 0.0.0.0:8085