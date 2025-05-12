# Development image with full source access
FROM golang:1.24-alpine AS dev

# Install git (Alpine uses apk, not apt-get)
RUN apk add --no-cache git bash

# Clone Dapr repo (replace with your fork if needed)
WORKDIR /app
RUN git clone https://github.com/dapr/dapr.git
WORKDIR /app/dapr

# Keep container running for development
CMD ["bash", "-c", "tail -f /dev/null"]
