sudo rm /etc/nginx/sites-enabled/default
sudo rm /etc/gunicorn.d/test.conf
sudo ln -sf /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/default       
sudo /etc/init.d/nginx restart                                                  
sudo ln -sf /home/box/web/etc/django.py /etc/gunicorn.d/test.conf

