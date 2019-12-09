#!/usr/bin/env bash
source /home/fenbi/django-env-1.11/bin/activate
cmd=$1
if [ ${cmd} == "start" ]
then
    uwsgi --ini django_socket_school.ini
    tail -f uwsgi.log
elif [ ${cmd} == "stop" ]
then
    uwsgi --stop uwsgi.pid
    tail -f uwsgi.log
elif [ ${cmd} == "reload" ]
then
    uwsgi --reload uwsgi.pid
    tail -f uwsgi.log
else
    echo 'Usage: reload/start/stop'
fi