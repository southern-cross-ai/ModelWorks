FROM ubuntu:24.04

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    vim \
    git \
    wget \
    curl \
    htop \
    nvtop \
    python3 \
    python3-pip \
    python3-venv \
    python3-dev \
    openssh-client \
    git-lfs \
    && rm -rf /var/lib/apt/lists/*  

RUN ln -sf /usr/bin/python3 /usr/bin/python

# Copy code
COPY app/ /app
WORKDIR /app

# Setup virtual environment
RUN python3 -m venv .venv
RUN .venv/bin/pip install -r requirements.txt

# Run the app
# ENTRYPOINT [".venv/bin/python", "app.py"]
