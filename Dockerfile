FROM ubuntu:latest
# install deps
RUN apt-get update && apt-get install -y \\
    python3 \\
    python3-pip \\
    git

RUN pip3 install --no-cache-dir PyYaml

COPY feed.py /usr/bin/feed.py

COPY entrypoint.sh /entrypoint.sh

ENTRYPOINT [ "/entrypoint.sh" ]
