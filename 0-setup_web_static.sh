#!/usr/bin/env bash
# sets up your web servers for the deployment of web_static

# Install Nginx if it not already installed
if ! command -v nginx &> /dev/null; then
	apt-get update
	apt install nginx -y
fi

# Create the folder /data/ if it doesn’t already exist
if ! [ -d "/data/" ]; then
	mkdir "/data/"
fi

# Create the folder /data/web_static/ if it doesn’t already exist
if ! [ -d "/data/web_static/" ]; then
        mkdir "/data/web_static/"
fi

# Create the folder /data/web_static/releases/ if it doesn’t already exist
if ! [ -d "/data/web_static/releases/" ]; then
        mkdir "/data/web_static/releases/"
fi

# Create the folder /data/web_static/shared/ if it doesn’t already exist
if ! [ -d "/data/web_static/shared/" ]; then
        mkdir "/data/web_static/shared/"
fi

# Create the folder /data/web_static/releases/test/ if it doesn’t already exist
if ! [ -d "/data/web_static/releases/test/" ]; then
        mkdir "/data/web_static/releases/test/"
fi

# Create a fake HTML file /data/web_static/releases/test/index.html (with simple content, to test your Nginx configuration)
touch /data/web_static/releases/test/index.html

PATH_FILE=/data/web_static/releases/test/index.html

content="<html>
<head>
</head>
<body>
	<h1>Testing Nginx configuration</h1>
</body>
</html>"

echo "$content" | sudo tee "$PATH_FILE"

# Create a symbolic link /data/web_static/current linked to the /data/web_static/releases/test/ folder. If the symbolic link already exists, it should be deleted and recreated every time the script is ran.
ln -sfn /data/web_static/releases/test/ /data/web_static/current

# Give ownership of the /data/ folder to the ubuntu user AND group (you can assume this user and group exist). This should be recursive; everything inside should be created/owned by this user/group.
chown -R ubuntu:ubuntu /data/

# Update the Nginx configuration to serve the content of /data/web_static/current/ to hbnb_static (ex: https://mydomainname.tech/hbnb_static
# Add the location configuration to the Nginx
CONF_PATH=/etc/nginx/sites-enabled/default

sudo sed -i "/listen 80 default_server;/a\\\tlocation /hbnb_static/ {\n\talias /data/web_static/current/;\n\t}" "$CONF_PATH"

service nginx restart
