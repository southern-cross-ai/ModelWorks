# Use Ubuntu 24.04 for stability
FROM ubuntu:24.04

# Set environment variable for non-interactive installation
ENV DEBIAN_FRONTEND=noninteractive

# Update system and install necessary packages
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

# Ensure 'python3' is recognized as 'python'
RUN ln -sf /usr/bin/python3 /usr/bin/python

# Default command (for interactive HPC usage)
CMD ["/bin/bash"]

RUN git clone https://github.com/southern-cross-ai/ModelWorks.git 

WORKDIR ModelWorks
RUN git checkout pdf_reader_bot

WORKDIR app

RUN python3 -m venv .venv

RUN .venv/bin/python

RUN .venv/bin/pip install -r requirements.txt

ENTRYPOINT [ ".venv/bin/python", "app.py" ]
