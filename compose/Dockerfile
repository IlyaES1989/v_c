FROM python:3.10-alpine

RUN apk update \
  && apk add \
   python3-dev \
   musl-dev \
   build-base\
   cmake\
   linux-headers \
  # git
  && apk add git \
  && apk add curl

COPY ./requirements.txt requirements.txt
RUN pip install -r /requirements.txt

RUN pip install --target=/custom_folder/flask/1.1.4 flask==1.1.4
RUN pip install --target=/custom_folder/flask/2.0.2 flask==2.0.2

COPY ./main.py /app/main.py

COPY ./compose/start /start
RUN sed -i 's/\r$//g' /start
RUN chmod +x /start

WORKDIR /app
