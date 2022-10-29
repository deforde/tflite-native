from ubuntu:22.04

ARG DEBIAN_FRONTEND=noninteractive
ENV TZ=Africa/Johannesburg

RUN apt update && apt install -y \
    cmake \
    g++ \
    git

RUN adduser --disabled-password --uid 1000 --gecos "" mruser
USER mruser

WORKDIR /home/mruser

RUN git clone --depth 1 --branch v2.9.0 https://github.com/tensorflow/tensorflow

COPY build.sh /home/mruser/build.sh

ENTRYPOINT ["/home/mruser/build.sh"]
