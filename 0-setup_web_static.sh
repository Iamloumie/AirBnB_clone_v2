#!/usr/bin/env bash
# Sets up the web servers for the deployment of web static

# install nginx if it doesn't exist
sudo apt-get -y update
sudo apt-get -y upgrade
sudo apt-get -y install nginx

# creates necessary parent directories and writes a content to one of its fake files
sudo mkdir -p /data/web_static/releases/test /data/web_static/shared
echo "Do not fret.... This is a test" | sudo tee /data/web_static/releases/test/index.html

# create symbolic links btw releases and current
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

# give recursive (created and owned) ownership to user and group
sudo chown -hR ubuntu:ubuntu /data/

# update the nginx configuration to server the /current folder to hbnb_static
sudo sed -i '38i\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n' /etc/nginx/sites-available/default

# restart nginx
sudo service nginx start
