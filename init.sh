sudo ln -sf /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart

sudo ln -sf /home/box/web/etc/gunicorn.conf.py /etc/gunicorn.d/gunicorn.conf.py
gunicorn -c /etc/gunicorn.d/gunicorn.conf.py ask.wsgi:application

sudo /etc/init.d/mysql start

curl -v http://127.0.0.1/
