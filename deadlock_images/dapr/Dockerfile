# Development image with full source access
FROM golang:1.24-alpine AS dev

# Install git, make, and bash
RUN apk add --no-cache git make bash

# Clone Dapr repo (replace with your fork if needed)
WORKDIR /app
RUN git clone https://github.com/dapr/dapr.git . \
    && git checkout v1.15.3  # Optional: Pin a specific version

# Keep container running for development
CMD ["bash", "-c", "tail -f /dev/null"]

'''
TO RUN (IN TERMInAL)
# Build the image
docker build -t dapr-dev .

# Run with interactive shell
docker run -it --name dapr-dev-container dapr-dev

# Inside the container:
cd /app
make build  # Build Dapr
./dist/linux_amd64/release/daprd --app-id myapp  # Run
'''