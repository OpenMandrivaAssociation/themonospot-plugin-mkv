Summary   : Matroska plugin for themonospot system
Name      : themonospot-plugin-mkv
Version   : 0.1.0
Release   : %mkrel 1
License   : GPLv2
Group     : Video
Source    : http://www.integrazioneweb.com/repository/SOURCES/themonospot-plugin-mkv-%{version}.tar.gz
BuildRoot : %{_tmppath}/%{name}-%{version}-%{release}-buildroot
URL       : http://www.integrazioneweb.com/themonospot

#BuildArch : noarch

BuildRequires: mono >= 1.2.3
BuildRequires: pkgconfig
BuildRequires: themonospot-base >= 0.8.1

Requires: mono >= 1.2.3
Requires: themonospot-base >= 0.8.1

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
rm -fr %{buildroot}
%makeinstall_std


%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%{_datadir}/themonospot/plugins/%{name}/

%changelog
* Mon Dec 14 2009 Armando Basile <hmandevteam@gmail.com> 0.1.0-1mdv2010.1
- first release of new matroska plugin component
