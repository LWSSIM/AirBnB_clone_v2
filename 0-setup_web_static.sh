#!/usr/bin/env bash
# sets up your web servers for the deployment of web_static
command -v nginx &>/dev/null || sudo apt-get update && sudo apt-get install nginx -y

dirs=(
	"/data/web_static/releases/test"
	"/data/web_static/shared"
)
for dir in "${dirs[@]}"; do
	if [ ! -d "$dir" ]; then
		sudo mkdir -p "$dir"
	fi
done

sudo tee /data/web_static/releases/test/index.html >/dev/null <<EOF
<html>
<head></head>
<body>Welcome habibi to lwssim.tech</body>
</html>
EOF

sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

sudo chown -R ubuntu:ubuntu /data/

sudo sed -i "/server_name _;/a \ \n\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n" /etc/nginx/sites-available/default

sudo service nginx restart
