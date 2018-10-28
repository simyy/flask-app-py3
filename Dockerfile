FROM python:apline

COPY /root/python/flask_app/src /home/

RUN echo "http://mirrors.aliyun.com/alpine/v3.8/main/" >> /etc/apk/repositories
RUN echo "http://mirrors.aliyun.com/alpine/v3.8/community/" >> /etc/apk/repositories

RUN apk add --no-cache --virtual .build-deps gcc musl-dev
RUN pip install -i https://pypi.tuna.tsinghua.edu.cn/simple cython
RUN pip installpip install -U setuptool

RUN sh /home/pip_install.sh
