Summary   : Matroska plugin for themonospot system
Name      : themonospot-plugin-mkv
Version   : 0.1.1
Release   : %mkrel 1
License   : GPLv2
Group     : Video
Source    : http://www.integrazioneweb.com/repository/SOURCES/themonospot-plugin-mkv-%{version}.tar.gz
BuildRoot : %{_tmppath}/%{name}-%{version}-%{release}-buildroot
URL       : http://www.integrazioneweb.com/themonospot

#BuildArch : noarch

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
rm -fr %{buildroot}
%makeinstall_std


%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%doc copying.gpl
%{_libdir}/themonospot/plugins/%{name}/


%changelog
* Wed Dec 30 2009 Armando Basile <hmandevteam@gmail.com> 0.1.1-1mdv2010.1
- removed GAC use

* Mon Dec 14 2009 Armando Basile <hmandevteam@gmail.com> 0.1.0-1mdv2010.1
- first release of new matroska plugin component
