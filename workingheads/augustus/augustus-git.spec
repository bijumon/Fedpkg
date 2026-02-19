%global forgeurl https://github.com/Keriew/augustus
%global date     %(date +%%Y%%m%%d)
%global commit   HEAD
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           augustus
Version:        4.0.0
Release:        %{date}git%{shortcommit}%{?dist}
Summary:        An open source re-implementation of Caesar III
License:        AGPLv3+
URL:            %{forgeurl}

Source0:        %{forgeurl}/archive/%{commit}/%{name}-%{shortcommit}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  SDL2-devel
BuildRequires:  SDL2_mixer-devel
BuildRequires:  zlib-devel
BuildRequires:  libpng-devel
BuildRequires:  hicolor-icon-theme
BuildRequires:  desktop-file-utils

Requires:       SDL2
Requires:       SDL2_mixer
Requires:       hicolor-icon-theme

%description
Augustus is a fully playable open source re-implementation of Caesar III.
Note: You need the original Caesar III assets to play.

%prep
%autosetup -n %{name}-%{commit} -c -p1
if [ -d */ ]; then
    mv */* .
    rmdir */ 2>/dev/null || :
fi

%build
%cmake .
%cmake_build

%install
%cmake_install

%files
%license LICENSE.txt
%doc README.md
%{_bindir}/%{name}
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/*/apps/*.png
%{_datadir}/metainfo/*.xml
# This line includes the assets folder that caused the previous crash
%{_datadir}/augustus-game/

%changelog
* %(date "+%a %b %d %Y") User <user@example.com> - %{version}-%{release}
- Fixed unpackaged assets error
