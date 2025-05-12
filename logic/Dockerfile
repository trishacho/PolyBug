# Use Python as the base image
FROM python:3.10

# Install git and other dependencies
RUN apt-get update && apt-get install -y git

# Set the working directory
WORKDIR /app

# Clone the repository - using a depth of 10000 to get a lot of history
RUN git clone --depth=10000 https://github.com/data-apis/array-api-extra.git
WORKDIR /app/array-api-extra

# Install the package in development mode
# This ensures the package is installed while allowing edits to affect the installed package
RUN pip install -e .

# Install required dependencies
RUN pip install pytest numpy hypothesis

# Command to run pytest on a specific file
CMD ["pytest", "tests/test_funcs.py::TestIsClose", "-v"]