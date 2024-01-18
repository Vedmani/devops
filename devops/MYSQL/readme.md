create network:
sudo docker network create mysql_net

create Dockerfile:
nano Dockerfile

create app.py file
nano app.py

app_docker:
sudo docker build -t mysql_app .
sudo docker run -ti --network mysql_net --rm mysql_app

mysql DB :
sudo docker run --name mysqldb --network mysql_net -e MYSQL_ROOT_PASSWORD=password -e MYSQL_ROOT_USER=mysql1 -ti --rm mysql
