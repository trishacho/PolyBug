FROM debian:bullseye-slim

ARG DEBIAN_FRONTEND=noninteractive
ENV VCPKG_FORCE_SYSTEM_BINARIES=1
ENV HOME=/root

RUN apt update -y && \
    apt install --yes --no-install-recommends \
        g++ \
        gcc \
        git \
        curl \
        nasm \
        yasm \
        libgtk-3-dev \
        clang \
        libxcb-randr0-dev \
        libxdo-dev \
        libxfixes-dev \
        libxcb-shape0-dev \
        libxcb-xfixes0-dev \
        libasound2-dev \
        libpam0g-dev \
        libpulse-dev \
        make \
        wget \
        libssl-dev \
        unzip \
        zip \
        sudo \
        libgstreamer1.0-dev \
        libgstreamer-plugins-base1.0-dev \
        ca-certificates \
        ninja-build && \
        rm -rf /var/lib/apt/lists/*

RUN wget https://github.com/Kitware/CMake/releases/download/v3.30.6/cmake-3.30.6.tar.gz --no-check-certificate && \
    tar xzf cmake-3.30.6.tar.gz && \
    cd cmake-3.30.6 && \
    ./configure  --prefix=/usr/local && \
    make && \
    make install && \
    cd / && rm -rf cmake-3.30.6.tar.gz cmake-3.30.6

RUN git clone --branch 2023.04.15 --depth=1 https://github.com/microsoft/vcpkg && \
    /vcpkg/bootstrap-vcpkg.sh -disableMetrics && \
    /vcpkg/vcpkg --disable-metrics install libvpx libyuv opus aom

RUN curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y
ENV PATH="/root/.cargo/bin:${PATH}"

WORKDIR /root
RUN curl -LO https://raw.githubusercontent.com/c-smile/sciter-sdk/master/bin.lnx/x64/libsciter-gtk.so

WORKDIR /app
RUN git clone https://github.com/rustdesk/rustdesk . && \
    git submodule update --init --recursive

RUN cp /root/libsciter-gtk.so /app/

ENV VCPKG_ROOT=/vcpkg
RUN cd /app && \
    cargo build --release

EXPOSE 21115-21119/tcp
EXPOSE 21115-21119/udp

CMD ["/app/target/release/rustdesk"]