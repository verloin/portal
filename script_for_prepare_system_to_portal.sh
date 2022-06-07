#!/usr/bin/bash
cp /var/www/portal/configs/gunicorn.socket /etc/systemd/system/
cp /var/www/portal/configs/gunicorn.service /etc/systemd/system/
sudo systemctl start gunicorn.socket
sudo systemctl enable gunicorn.socket
echo "GUNICORN sucessfully started"
cp /var/www/portal/configs/portal /etc/nginx/sites-available/
sudo ln -s /etc/nginx/sites-available/portal /etc/nginx/sites-enabled
sudo nginx -t && sudo systemctl restart nginx
echo "NGINX sucessfully started"