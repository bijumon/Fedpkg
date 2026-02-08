# Fedora RPM spec file for 86Box
#
# To create RPM files from this spec file, run the following commands:
#  sudo dnf install rpm-build
#  mkdir -p ~/rpmbuild/{BUILD,RPMS,SOURCES,SPECS,SRPMS}
#
# copy this 86Box.spec file to ~/rpmbuild/SPECS and run the following commands:
#  cd ~/rpmbuild
#  sudo dnf builddep SPECS/86Box.spec
#  rpmbuild --undefine=_disable_source_fetch -ba SPECS/86Box.spec
#
# After a successful build, you can install the RPM as follows:
#  sudo dnf install RPMS/$(uname -m)/86Box-5*

Name:		86Box
Version:	5.3
Release:	1%{?dist}
Summary:	Classic PC emulator
License:	GPLv2+
URL:		https://86box.net

Source0:	https://github.com/86Box/86Box/archive/refs/tags/v%{version}.tar.gz
ExclusiveArch:  x86_64 aarch64

BuildRequires: cmake
BuildRequires: desktop-file-utils
BuildRequires: extra-cmake-modules
BuildRequires: fluidsynth-devel
BuildRequires: freetype-devel
BuildRequires: gcc-c++
BuildRequires: libFAudio-devel
BuildRequires: libappstream-glib
BuildRequires: libatomic
BuildRequires: libevdev-devel
BuildRequires: libslirp-devel
BuildRequires: libxkbcommon-x11-devel
BuildRequires: libXi-devel
BuildRequires: ninja-build
BuildRequires: openal-soft-devel
BuildRequires: qt6-linguist
BuildRequires: qt6-qtbase-private-devel
BuildRequires: qt6-qtbase-static
BuildRequires: rtmidi-devel
BuildRequires: wayland-devel
BuildRequires: SDL2-devel
BuildRequires: zlib-ng-compat-static
BuildRequires: libserialport-devel

Requires: hicolor-icon-theme
Requires: fluid-soundfont-gm

%description
86Box is a hypervisor and IBM PC system emulator that specializes in
running old operating systems and software designed for IBM
PC systems and compatibles from 1981 through fairly recent
system designs based on the PCI bus.

It supports various models of PCs, graphics and sound cards, and CPUs.

%prep
%autosetup -p1

%build
%ifarch x86_64
  %cmake -DRELEASE=on -DUSE_QT6=TRUE
%else
  %cmake -DRELEASE=on -DNEW_DYNAREC=on -DUSE_QT6=TRUE
%endif
%cmake_build

%install
# install base package
%cmake_install

# install icons
for i in 48 64 72 96 128 192 256 512; do
  mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/${i}x${i}/apps
  cp src/unix/assets/${i}x${i}/net.86box.86Box.png $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/${i}x${i}/apps
done

# install desktop file
desktop-file-install --dir=%{buildroot}%{_datadir}/applications src/unix/assets/net.86box.86Box.desktop

# install metadata
mkdir -p %{buildroot}%{_metainfodir}
cp src/unix/assets/net.86box.86Box.metainfo.xml %{buildroot}%{_metainfodir}
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/net.86box.86Box.metainfo.xml

%files
%license COPYING
%{_bindir}/86Box
%{_datadir}/applications/net.86box.86Box.desktop
%{_metainfodir}/net.86box.86Box.metainfo.xml
%{_datadir}/icons/hicolor/*/apps/net.86box.86Box.png

%changelog
* Mon Nov 17 2025 Robert de Rooy <rderooy@users.noreply.github.com> 5.2-2
- Rebuild against latest QT6
* Sun Oct 26 2025 Robert de Rooy <rderooy@users.noreply.github.com> 5.2-1
- Bump release
* Tue Sep 16 2025 Robert de Rooy <rderooy@users.noreply.github.com> 5.1-2
- Switch to QT6
* Sun Sep 14 2025 Robert de Rooy <rderooy@users.noreply.github.com> 5.1-1
- Bump release
