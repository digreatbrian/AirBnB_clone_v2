#!/usr/bin/env bash

# Update package index by installing Nginx
sudo apt-get update
sudo apt-get install -y nginx

# Create necessary HTML file to test
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/

# Create a fake HTML file for testing
echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" | sudo tee /data/web_static/releases/test/index.html > /dev/null

# Create / update a symbolic link
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

# Ownership of directories to the 'ubuntu' user and group
sudo chown -R ubuntu:ubuntu /data/

# Update Nginx configuration to serve /data/web_static/current at /hbnb_static/
sudo sed -i "/server_name _;/a \\\n\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n" /etc/nginx/sites-available/default

# Restart Nginx to apply changes
sudo service nginx restart
