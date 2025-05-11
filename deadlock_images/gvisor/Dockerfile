FROM debian:bullseye-slim

# Install all required dependencies including unzip
RUN apt-get update && \
    apt-get install -y \
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
        unzip \
        zip && \
    rm -rf /var/lib/apt/lists/*

# Install Go 1.21 (required by gVisor)
RUN wget https://go.dev/dl/go1.21.6.linux-amd64.tar.gz && \
    tar -C /usr/local -xzf go1.21.6.linux-amd64.tar.gz && \
    rm go1.21.6.linux-amd64.tar.gz
ENV PATH=$PATH:/usr/local/go/bin
ENV GOPATH=/go

# Install Bazel 6.4.0 (known working version)
RUN wget https://github.com/bazelbuild/bazel/releases/download/6.4.0/bazel-6.4.0-installer-linux-x86_64.sh && \
    chmod +x bazel-6.4.0-installer-linux-x86_64.sh && \
    ./bazel-6.4.0-installer-linux-x86_64.sh && \
    rm bazel-6.4.0-installer-linux-x86_64.sh

# Clone specific gVisor release
WORKDIR /gvisor
RUN git clone --depth=1 --branch=release-20240603.0 https://github.com/google/gvisor.git . && \
    git submodule update --init --recursive

# Setup environment
ENV CC=/usr/bin/gcc
ENV CXX=/usr/bin/g++

# Build runsc with conservative resources
RUN bazel build --jobs=2 --local_ram_resources=2048 //runsc

# Install runsc
RUN cp bazel-bin/runsc/linux_amd64_pure_stripped/runsc /usr/local/bin/ && \
    chmod +x /usr/local/bin/runsc

# Configure Docker
RUN mkdir -p /etc/docker && \
    echo '{"runtimes":{"runsc":{"path":"/usr/local/bin/runsc","runtimeArgs":[]}}}' > /etc/docker/daemon.json

# Install Docker
RUN curl -fsSL https://download.docker.com/linux/debian/gpg | gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg && \
    echo "deb [arch=amd64 signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/debian $(lsb_release -cs) stable" | tee /etc/apt/sources.list.d/docker.list > /dev/null && \
    apt-get update && \
    apt-get install -y docker-ce docker-ce-cli containerd.io && \
    rm -rf /var/lib/apt/lists/*

# Create startup script
RUN echo '#!/bin/bash\n\
service docker start\n\
runsc install --runtime=runsc\n\
systemctl restart docker\n\
echo "gVisor ready! Test with: docker run --runtime=runsc hello-world"\n\
tail -f /dev/null' > /start.sh && \
    chmod +x /start.sh

EXPOSE 2375
CMD ["/start.sh"]