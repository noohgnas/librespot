Summary:        librespot is an open source client library for Spotify.
Name:           librespot
Version:        1.0.2.ddfc28f
Release:        1%{?dist}
Group:          Applications/Multimedia
License:        MIT
URL:            https://github.com/plietar/librespot
Source0:        %{name}-%{version}.tar.gz
Source1:        librespot.service
Source2:        librespot.conf
BuildRequires:  cargo, portaudio-devel, make, gcc

%description
librespot is an open source client library for Spotify. It enables
applications to use Spotify's service, without using the official
but closed-source libspotify. Additionally, it will provide extra
features which are not available in the official library.


%prep
%setup -q

%build
cargo build --release --no-default-features --features alsa-backend

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/bin
mkdir -p $RPM_BUILD_ROOT/etc/sysconfig
mkdir -p $RPM_BUILD_ROOT/usr/lib/systemd/system
%{__install} -p -m0755 target/release/librespot $RPM_BUILD_ROOT/usr/bin
%{__install} -p -m0644  %{SOURCE1} $RPM_BUILD_ROOT/usr/lib/systemd/system
cp -fa %{SOURCE2} $RPM_BUILD_ROOT/etc/sysconfig/librespot

%files
%{_bindir}/%{name}
%attr(0666, root, root) "/etc/sysconfig/librespot"
%attr(0644, root, root) "/usr/lib/systemd/system/librespot.service"

%changelog
* Fri Aug 25 2017 Sanghoon LEE <noohgnas@gmail.com> - 1.0.2
- ddfc28f

