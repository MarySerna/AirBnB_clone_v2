#!/usr/bin/env bash
#Bash script that sets up your web servers for the deployment of web_static

# Install nginx web server:
sudo apt-get -y update
sudo apt-get install -y nginx

# Create folders if don't exist:
sudo mkdir -p "/data/"
sudo mkdir -p "/data/web_static/"
sudo mkdir -p "/data/web_static/releases/"
sudo mkdir -p "/data/web_static/shared/"
sudo mkdir -p "/data/web_static/releases/test/"

# Create a fake HTML file:
sudo touch /data/web_static/releases/test/index.html 
echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" > /data/web_static/releases/test/index.html

# Create a symbolic link
sudo ln -sfn /data/web_static/releases/test/ /data/web_static/current

# Give ownership of the /data/ folder to the ubuntu user AND group
sudo chown -R ubuntu:ubuntu /data/

# Update the Nginx configuration to serve the content of /data/web_static/current/ to hbnb_static
sed -i "32i location  /hbnb_static/ {" /etc/nginx/sites-available/default
sed -i "33i alias /data/web_static/current/;" /etc/nginx/sites-available/default
sed -i "34i autoindex off;" /etc/nginx/sites-available/default
sed -i "35i }" /etc/nginx/sites-available/default

# Restart nginx:
sudo service nginx restart
