# flask_app
flask_app is a example using  blueprint of flask.

## structure

> [English](http://exploreflask.com/en/latest/), [中文](https://spacewander.github.io/explore-flask-zh/index.html)

```
flask_app/
    __init__.py
    manage.py
    config.py
    requirements.txt
    core/
        __init__.py
        app.py              # register blueprint
        base.py
        response.py
        exception.py
    tests/
        __init__.py
        test.py
    demo/                   # this is a application
        __init__.py
        models/             # models of demo
            __init__.py
            task.py
        views/              # views of demo
            __init__.py
            index.py
            errors.py
        static/             # static of demo
            hello.js
        templates/          # templates of demo
            index.html
```



## usage
**NEED**: `python3.6`, `virtualenv`.


### Step.1 virtualevn
```
virtualenv --no-site-packages -p /usr/local/Cellar/python3/3.6.3/bin/python3 flask_app
```

### Step.2 git clone & install
```
git clone xxx src
source bin/activate
pip install < src/requirements.txt
```

### Step.3 run
```
cd src
python manage.py runserver --env debug
```
> **env**: debug or product.

### Step.4 more
run a Python shell inside Flask application context.
```
python manage.py shell
```


