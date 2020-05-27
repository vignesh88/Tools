docker-compose build -t tools_vikki_in .
sudo docker run -d -p 8085:8085 --name tools.vikki.in vignesh88/tools:latest python tools/manage.py runserver 0.0.0.0:8085
sudo docker run -d -p 8081:8081 --name staging.vikki.in vignesh88/tools:tools-cdn python tools/manage.py runserver 0.0.0.0:8081