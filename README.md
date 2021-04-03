# Tallinna Tööstushariduskeskus Bot

Tallinna Tööstushariduskeskus Bot at VK social, that gives an ability to quickly get changes, consultations and other
studies releated information about this.

## How to run?

### Basic

* #### Install requirements

```
pip install -r requirements.txt 
```

* #### Run tests

```
pytest tests.py
```

* #### Run application with Gunicorn

```
python3 main.py
```

### From Dockerfile

* #### Get Dockerfile

```
docker pull bredbrains/tthk-bot:latest
```

* #### Create Docker container with image

```
docker run bredbrains/tthk-bot
```

*Use **-d** operator to launch container in detached mode*

## Dependencies

* Python 3.9
* tthkAPI
* VK Bottle
