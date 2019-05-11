#!/bin/bash
echo "stop"
killall uwsgi
## 休眠一会，不然killall仍然起作用
sleep 5
echo "start"
uwsgi --ini conf/uwsgiconfig.ini

