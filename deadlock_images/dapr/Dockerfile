# Development image with full source access
FROM golang:1.24-alpine AS dev

# Clone Dapr repo (replace with your fork if needed)
WORKDIR /app
RUN apt-get update && apt-get install -y git && \
    git clone hhttps://github.com/dapr/dapr.git && \
    cd dapr

WORKDIR /app/dapr

# Keep container running for development
CMD ["bash", "-c", "tail -f /dev/null"]

FROM golang:latest

WORKDIR /app



CMD ["go", "test", "-race", "-v", "-run", "TestRandomUint16DataRace"]

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