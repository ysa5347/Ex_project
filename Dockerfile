FROM ubuntu

WORKDIR /Ex_finder_server
ARG DEBIAN_FRONTEND=noninteractive
ENV TZ=Asia/Seoul

RUN apt-get -y upgrade && apt-get -y update
RUN ln -sf /usr/share/zoneinfo/Asia/Seoul /etc/localtime

RUN apt-get install -y git\
    dnsutils\
    tzdata\
    libmysqlclient-dev\
    screen
RUN apt install -y python3\
    python3-pip\
    git clone -b backend https://github.com/ysa5347/Ex_project

COPY /.env /Ex_finder_server/Ex_project/project/backend/django_react_api/

RUN pip install -r requirements.txt

ENTRYPOINT sh ./server.sh