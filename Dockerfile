FROM yusanish/jumanpp_knp

ENV main_dir /tmp

RUN apt-get update &&\
    apt-get install htop

ADD ./codes/requirements.txt  ${main_dir}
RUN mkdir -p ${main_dir}
WORKDIR ${main_dir}
RUN pip install -r requirements.txt

COPY ./codes ${main_dir}

CMD sh setup.sh