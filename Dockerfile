FROM ubuntu:latest

# install deps
RUN apt-get update && apt-get install -y \
    python3.12 \
    python3-pip \
    python3-dev \
    build-essential \
    git

RUN python3 -m pip install PyYaml --break-system-packages

COPY feed.py /usr/bin/feed.py

COPY entrypoint.sh /entrypoint.sh

ENTRYPOINT [ "/entrypoint.sh" ]
