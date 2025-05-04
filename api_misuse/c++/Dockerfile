# zephyr's official developer image
FROM ghcr.io/zephyrproject-rtos/zephyr-build:latest

ENV DEBIAN_FRONTEND=noninteractive
WORKDIR /workdir

# cloning zephyr repo and navigating to proper directory
RUN git clone https://github.com/zephyrproject-rtos/zephyr.git
ENV ZEPHYR_BASE=/workdir/zephyr
WORKDIR /workdir/zephyr

# initialize zephyr's west workspace and update modules
RUN west init -l . && \
    west update

# python dependencies
RUN pip install -r scripts/requirements.txt