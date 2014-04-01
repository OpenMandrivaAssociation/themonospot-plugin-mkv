Summary: Matroska plugin for themonospot system
Name:    themonospot-plugin-mkv
Version: 0.1.1
Release: 2
License: GPLv2
Group:   Video
Source:  http://www.integrazioneweb.com/repository/SOURCES/themonospot-plugin-mkv-%{version}.tar.gz
Url:     http://www.integrazioneweb.com/themonospot

#BuildArch : noarch
%define debug_package %{nil}

BuildRequires: mono-devel
BuildRequires: themonospot-base-devel

%description
themonospot-plugin-mkv is a matroska plugin package for themonospot system. 
It install:
    - themonospot-plugin-mkv mono assembly (use from themonospot-base)

%prep
%setup -q

%build
%configure2_5x
%make

%install
%makeinstall_std

%files
%doc copying.gpl
%{_libdir}/themonospot/plugins/%{name}/
