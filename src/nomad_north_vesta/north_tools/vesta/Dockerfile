ARG IMAGE_TAG=main
ARG BASE_IMAGE=ghcr.io/fairmat-nfdi/nomad-north-desktop-base
ARG PLUGIN_NAME=nomad-north-apmtools

FROM ${BASE_IMAGE}:${IMAGE_TAG} AS base

# Fix: https://github.com/hadolint/hadolint/wiki/DL4006
# Fix: https://github.com/koalaman/shellcheck/wiki/SC3014
SHELL ["/bin/bash", "-o", "pipefail", "-c"]

USER root

RUN apt update \
 && apt install --no-install-recommends -y \
      wget \
      libgl1 \
      libglu1-mesa \
      libglu1-mesa-dev \
 && rm -rf /var/lib/apt/lists/*

# Switch back to jovyan to avoid accidental container runs as root
USER ${NB_UID}
# WORKDIR "${HOME}"
WORKDIR "${HOME}/vesta"

# 3.5.8 is the latest version, was released in 2022, maybe feature complete
RUN wget https://jp-minerals.org/vesta/archives/3.5.8/VESTA-gtk3.tar.bz2 \
 && tar -xvf VESTA-gtk3.tar.bz2 \
 && rm -f VESTA-gtk3.tar.bz2

COPY --chown=${NB_UID}:${NB_GID} "src/nomad_north_vesta/north_tools/vesta/config/Vesta.desktop" "${HOME}/.config/autostart/Vesta.desktop"

#       git \
#       cmake \
#       build-essential \
#       libblas-dev \
#       liblapack-dev \
#       libxc-dev \
#       libgtk-3-dev \
#       libgl1-mesa-dri
