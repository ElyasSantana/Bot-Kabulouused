# Based on Ubuntu 22.04 LTS
FROM ubuntu:18.04
# RUN apt-get update
# RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-key FDC247B7
# RUN echo 'deb https://repo.windscribe.com/ubuntu bionic main' | tee /etc/apt/sources.list.d/windscribe-repo.list
# RUN apt-get install windscribe-cli
RUN apt -y update && apt -y dist-upgrade && apt install -y gnupg apt-utils ca-certificates expect iptables iputils-ping && \
  apt-key adv --keyserver keyserver.ubuntu.com --recv-key FDC247B7 && echo 'deb https://repo.windscribe.com/ubuntu bionic main' | tee /etc/apt/sources.list.d/windscribe-repo.list && \
  echo "resolvconf resolvconf/linkify-resolvconf boolean false" | debconf-set-selections && \
  apt -y update && apt -y dist-upgrade && apt install -y windscribe-cli && \
  apt install -y curl net-tools iputils-tracepath && \
  apt -y autoremove && apt -y clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
ADD . /app
WORKDIR /app
RUN pip install -r requirements.txt