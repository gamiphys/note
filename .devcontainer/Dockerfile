FROM mcr.microsoft.com/vscode/devcontainers/cpp:0-ubuntu-20.04

# Install LaTeX
RUN apt-get update \
    && export DEBIAN_FRONTEND=noninteractive \
    && apt-get -y install --no-install-recommends texlive-latex-base texlive-fonts-recommended texlive-fonts-extra texlive-latex-extra \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*
