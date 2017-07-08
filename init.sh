sudo ln -sf /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart
sudo ln -s /home/box/web/hello.py /usr/local/lib/python2.7/hello.py
sudo gunicorn -b 0.0.0.0:8080 hello
