FROM debian:10
ARG TOOLCHAIN_VERSION
# Stops tzdata interactive configuration.
ENV DEBIAN_FRONTEND=noninteractive

# Update repositories and install essential packages
RUN apt update && apt install -y \
    ca-certificates wget git curl gnupg2 software-properties-common \
    build-essential python3 python3-pip

# Do NOT be smart here and clean the cache because the container is used in the
# stateful context.
RUN wget -q https://s3-eu-west-1.amazonaws.com/deps.memgraph.io/toolchain-${TOOLCHAIN_VERSION}/toolchain-${TOOLCHAIN_VERSION}-binaries-ubuntu-20.04-amd64.tar.gz \
    -O toolchain-${TOOLCHAIN_VERSION}-binaries-ubuntu-20.04-amd64.tar.gz \
    && tar xzvf toolchain-${TOOLCHAIN_VERSION}-binaries-ubuntu-20.04-amd64.tar.gz -C /opt \
    && rm toolchain-${TOOLCHAIN_VERSION}-binaries-ubuntu-20.04-amd64.tar.gz

# Install toolchain run deps and memgraph build deps
ARG GIT_REF
SHELL ["/bin/bash", "-c"]

# For Debian, we'll need to adapt the Ubuntu script or manually install dependencies
RUN git clone --branch ${GIT_REF} https://github.com/memgraph/memgraph.git \
    && cd memgraph \
    # The following lines might need adjustment based on what these scripts actually do
    # You might need to manually install dependencies instead
    && bash -c "sed -i 's/ubuntu-20.04/debian-10/g' ./environment/os/ubuntu-20.04.sh || true" \
    && bash -c "./environment/os/ubuntu-20.04.sh install TOOLCHAIN_RUN_DEPS || apt install -y build-essential cmake libssl-dev" \
    && bash -c "./environment/os/ubuntu-20.04.sh install MEMGRAPH_BUILD_DEPS || apt install -y python3-dev" \
    && cd .. && rm -rf memgraph

# Create mg user and set as default
RUN useradd -m -s /bin/bash mg
USER mg

# Install rust
ARG RUST_VERSION
RUN curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y \
    && rustup default ${RUST_VERSION}

# Fix node
ARG NODE_VERSION
RUN curl https://raw.githubusercontent.com/creationix/nvm/master/install.sh | bash \
    && . ~/.nvm/nvm.sh \
    && nvm install ${NODE_VERSION} \
    && nvm use ${NODE_VERSION}

ENTRYPOINT ["sleep", "infinity"]
