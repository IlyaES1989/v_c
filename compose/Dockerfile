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

COPY ./compose/install_lib /install_lib
RUN sed -i 's/\r$//g' /install_lib
RUN chmod +x /install_lib
RUN /install_lib

COPY ./main.py /app/main.py

COPY ./compose/start /start
RUN sed -i 's/\r$//g' /start
RUN chmod +x /start

WORKDIR /app
