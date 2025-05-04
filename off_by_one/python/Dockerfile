FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

RUN apt-get update && apt-get install -y \
    build-essential \
    git \
    curl \
    vim \
    nano \
    && rm -rf /var/lib/apt/lists/*

# install poetry (which is what langflow uses)
RUN curl -sSL https://install.python-poetry.org | python3 - && \
    ln -s /root/.local/bin/poetry /usr/local/bin/poetry

RUN git clone https://github.com/langflow-ai/langflow.git . && \
    git checkout main

# updating the pyproject.toml file bc it doesn't run unless I say >=3.10,<3.14 for the python version
RUN sed -i 's/^requires-python = ">=3.10,<3.14"/requires-python = ">=3.10,<3.13"/' pyproject.toml

# poetry dependencies
RUN poetry config virtualenvs.create false && \
    poetry install --no-interaction --no-ansi --no-root

# installing a lot of other dependencies that I copied into a txt file bc it was so long
COPY requirements-dev.txt .
RUN poetry run pip install -r requirements-dev.txt

# run only test_loop.py file
CMD ["poetry", "run", "pytest", "src/backend/tests/unit/components/logic/test_loop.py"]