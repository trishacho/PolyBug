FROM ubuntu:20.04

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y \
    build-essential \
    git \
    curl \
    wget \
    libncurses5-dev \
    libncursesw5-dev \
    python3 \
    python3-dev \
    python3-pip \
    ruby \
    lua5.3 \
    liblua5.3-dev \
    libperl-dev \
    vim \
    nano \
    && rm -rf /var/lib/apt/lists/*

# clone vim
RUN git clone https://github.com/vim/vim.git /vim
WORKDIR /vim/src

# configure and build vim
RUN ./configure --with-features=huge \
    --enable-multibyte \
    --enable-python3interp \
    --enable-perlinterp \
    --enable-rubyinterp \
    --enable-luainterp \
    --enable-cscope && \
    make

# run only 30state_pen.test file
CMD make test TESTFILE=src/libvterm/t/30state_pen.test