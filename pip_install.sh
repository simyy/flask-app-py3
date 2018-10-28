#!/bin/bash

apk add libevent

pip_list="werkzeug flask flask_script flask_migrate gevent"

for var in list; do
    pip install -i https://pypi.tuna.tsinghua.edu.cn/simple $var
done
