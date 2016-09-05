FROM python:3.6-alpine

RUN apk --update add git

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY requirements.txt /usr/src/app/
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install git+https://github.com/docker/docker-py.git

COPY . /usr/src/app

CMD [ "python", "./app.py" ]