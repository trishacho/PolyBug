# Use Python as the base image
FROM python:3.9-slim

# Install git and other dependencies
RUN apt-get update && apt-get install -y git

# Set the working directory
WORKDIR /app

# Clone the repository - using a depth of 10000 to get a lot of history
RUN git clone --depth=10000 https://github.com/canonical/checkbox.git
WORKDIR /app/checkbox

# List available directories to help find Python packages
RUN ls -la

# Install pytest
RUN pip install pytest

# Install checkbox-ng (one of the main Python packages)
WORKDIR /app/checkbox/checkbox-ng
RUN pip install -e . || echo "Could not install checkbox-ng, trying other packages"

# Install checkbox-support
WORKDIR /app/checkbox/checkbox-support
RUN pip install -e . || echo "Could not install checkbox-support, continuing"

# Go back to the main directory
WORKDIR /app/checkbox

# Command to run pytest on a specific file
CMD ["pytest", "checkbox-support/checkbox_support/tests/test_slugify.py", "-v"]