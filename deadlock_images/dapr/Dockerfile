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
