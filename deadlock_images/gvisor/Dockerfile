FROM debian:bullseye-slim

# Install dependencies
RUN apt-get update && apt-get install -y \
    git \
    curl \
    build-essential \
    python3 \
    python3-pip \
    wget \
    gnupg \
    lsb-release \
    apt-transport-https \
    ca-certificates \
    software-properties-common \
    pkg-config \
    && rm -rf /var/lib/apt/lists/*

# Install Go (required for building gVisor)
RUN wget https://go.dev/dl/go1.21.6.linux-amd64.tar.gz && \
    tar -C /usr/local -xzf go1.21.6.linux-amd64.tar.gz && \
    rm go1.21.6.linux-amd64.tar.gz
ENV PATH=$PATH:/usr/local/go/bin

# Install Docker (for testing gVisor)
RUN curl -fsSL https://download.docker.com/linux/debian/gpg | gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg && \
    echo "deb [arch=amd64 signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/debian $(lsb_release -cs) stable" | tee /etc/apt/sources.list.d/docker.list > /dev/null && \
    apt-get update && apt-get install -y docker-ce docker-ce-cli containerd.io && \
    rm -rf /var/lib/apt/lists/*

# Clone gVisor repository
WORKDIR /gvisor
RUN git clone https://github.com/google/gvisor .

# Build gVisor
RUN cd /gvisor && \
    ./tools/make.sh

# Add the built binaries to PATH
ENV PATH=$PATH:/gvisor/bazel-bin/runsc

# Create a directory for gVisor configuration
RUN mkdir -p /etc/docker

# Create a configuration file for Docker to use gVisor
RUN echo '{\n  "runtimes": {\n    "runsc": {\n      "path": "/gvisor/bazel-bin/runsc/linux_amd64_pure_stripped/runsc"\n    }\n  }\n}' > /etc/docker/daemon.json

# Expose Docker port
EXPOSE 2375

# Start script
RUN echo '#!/bin/bash\n\
service docker start\n\
echo "gVisor is ready!"\n\
echo "You can run containers with gVisor using: docker run --runtime=runsc ..."\n\
tail -f /dev/null' > /start.sh && \
    chmod +x /start.sh

CMD ["/start.sh"]