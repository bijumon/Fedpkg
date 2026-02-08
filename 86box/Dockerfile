FROM fedora:rawhide

ENV LANG=C.UTF-8
ENV LC_ALL=C.UTF-8

# Speed up DNF a bit
RUN echo "max_parallel_downloads=10" >> /etc/dnf/dnf.conf

# Base build tools
RUN dnf -y upgrade && \
    dnf -y install \
        git \
        cmake \
        ninja \
        gcc \
        gcc-c++ \
        make \
        pkgconf-pkg-config \
        python3 \
        which \
        file \
        \
        # Qt6
        qt6-qtbase-devel \
        qt6-qttools-devel \
        qt6-qtsvg-devel \
        qt6-qtbase-private-devel \
        \
        # SDL / audio / input
        SDL2-devel \
        libX11-devel \
        libXcursor-devel \
        libXinerama-devel \
        libXrandr-devel \
        libXi-devel \
        libXpresent-devel \
        libxkbcommon-devel \
        libxkbcommon-x11-devel \
        wayland-devel \
        wayland-protocols-devel \
        \
        # Graphics / fonts
        mesa-libEGL-devel \
        mesa-libGL-devel \
        mesa-libGLU-devel \
        freetype-devel \
        \
        # Misc used by 86Box
        libevdev-devel \
        alsa-lib-devel \
        pulseaudio-libs-devel \
        pipewire-jack-audio-connection-kit-devel \
        rtmidi-devel \
    && dnf clean all

WORKDIR /work
