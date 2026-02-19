Name:           akhenaten
Version:        0.26
Release:        1%{?dist}
Summary:        Open-source city builder set in Ancient Egypt

License:        GPL-3.0-or-later
URL:            https://github.com/Keriew/akhenaten
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig

%description
Akhenaten is an open-source reimplementation of Pharaoh,
a city-building game set in Ancient Egypt.

%prep
%autosetup

%build
cd build
cmake .. \
  -DOPTION_ENABLE_TRACY=OFF \
  -DTRACY_ENABLE=OFF \
  -DCMAKE_BUILD_TYPE=Release
%cmake_build

%install
cd build
%cmake_install

%files
%license LICENSE
%doc README.md
%{_bindir}/akhenaten

