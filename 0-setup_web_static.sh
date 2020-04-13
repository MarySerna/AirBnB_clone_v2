#!/usr/bin/env bash
#Bash script that sets up your web servers for the deployment of web_static

sudo apt-get -y update
sudo apt-get install -y nginx
sudo mkdir -p "/data/"
sudo mkdir -p "/data/web_static/"
sudo mkdir -p "/data/web_static/current/"
sudo mkdir -p "/data/web_static/releases/"
sudo mkdir -p "/data/web_static/shared/"
sudo mkdir -p "/data/web_static/releases/test/"
sudo touch /data/web_static/releases/test/index.html 
echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" > /data/web_static/releases/test/index.html

sudo ln -sfn /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/

sed -i "32i location  /hbnb_static/ {" /etc/nginx/sites-available/default
sed -i "33i alias /data/web_static/current/;" /etc/nginx/sites-available/default
sed -i "34i autoindex off;" /etc/nginx/sites-available/default
sed -i "35i }" /etc/nginx/sites-available/default

sudo service nginx restart
