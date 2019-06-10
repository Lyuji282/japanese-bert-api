FROM nginx

ENV main_dir /etc/nginx

RUN apt-get update &&\
    apt-get install -y vim &&\
    apt-get install htop

COPY ./ ${main_dir}