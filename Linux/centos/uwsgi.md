pip3 install uwsgi

ln -sf /usr/local/python3/bin/uwsgi /usr/local/bin/uwsgi


kill -9 1573

ps -aux | grep uwsgi.ini 
ps -aux | grep nginx
nginx -s quit

uwsgi -d --ini uwsgi.ini 
netstat -lnp|grep 80

uwsgi -d --ini /srv/jiuguai/qhj/uwsgi.ini 
nginx /etc/nginx/conf.d/qhj


[uwsgi]

chdir = /srv/jiuguai/qhj

wsgi-file = /srv/jiuguai/qhj/app.py

callable = app


home = /root/Envs/flask

master = true

processes = 3

http = :9090

# socket = /srv/jiuguai/qhj/qhj.sock

socket = 127.0.0.1:8080
# socket = 127.0.0.1:8080

# chmod-socket = 666
# vacuum = true
