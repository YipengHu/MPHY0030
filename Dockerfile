# Dockerfile for the module tutorial and coursework

FROM ubuntu:20.04

# git and conda
RUN apt-get update && apt-get install -y wget git \
 && rm -rf /var/lib/apt/lists/*
RUN wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh \
 && mkdir /root/.conda \
 && bash Miniconda3-latest-Linux-x86_64.sh -b \
 && rm -f Miniconda3-latest-Linux-x86_64.sh
ARG PATH="/root/miniconda3/bin:$PATH"
RUN conda init bash
ENV PATH="/root/miniconda3/bin:$PATH"

# clone the repo in "/workspace"
RUN git clone https://github.com/YipengHu/MPHY0030 workspace/mphy0030
WORKDIR /workspace

# create the tutorial/coursework conda environment "mphy0030"
ARG CONDA_ENV="mphy0030"
RUN conda create -n $CONDA_ENV python=3.9 numpy scipy \
 && echo "source activate $CONDA_ENV" > ~/.bashrc 
