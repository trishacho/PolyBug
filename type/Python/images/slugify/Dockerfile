# Use Python as the base image (choose your Python version)
FROM python:3.11-slim
RUN apt-get update && apt-get install -y \
    git \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Clone the repository (replace with your repository URL)
RUN git clone https://github.com/canonical/checkbox.git .

# Checkout a specific commit (replace with your commit hash)
RUN git checkout 7c3a8c7

# If your repo requires submodules, uncomment the line below
# RUN git submodule update --init --recursive

# If your Python project is in a subdirectory, navigate to it
WORKDIR /app/docs/.sphinx

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt