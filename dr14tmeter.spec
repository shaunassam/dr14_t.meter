Name: dr14_t.meter
Version: 1.0.16
Release: 4
Summary: Compute the dynamic range DR14 value of the givens audio files
BuildArch: noarch

Group: Applications/Sound
License: GPLv3	
URL: http://dr14tmeter.sourceforge.net	
Source: https://github.com/simon-r/dr14_t.meter/archive/v1.0.16.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: python3
BuildRequires: bash

Requires: python3
Requires: python3-numpy
Requires: flac
Requires: lame
Requires: faad2
Requires: ffmpeg
Requires: vorbis-tools


%description
Compute the DR14 value of the given audio files according to the algorithm decribed by the Pleasurize Music Foundation

%prep
rm -rf $RPM_BUILD_DIR/%{name}-%{version}
zcat $RPM_SOURCE_DIR/v1.0.16.tar.gz | tar -xvf -

%build
cd $RPM_BUILD_DIR/%{name}-%{version}
python3 setup.py build


%install
#rm -rf %{buildroot}
cd $RPM_BUILD_DIR/%{name}-%{version}
python3 setup.py install --root=%{buildroot} --prefix=usr --optimize=1


%clean
#rm -rf %{buildroot}


%files
%defattr(-,root,root)
%{_bindir}/*
/usr/lib/*
%{_mandir}/man1/*



%changelog
* Mon Sept 18 2023 Shaun Assam <sassam [at] fedoraproject.org> - 1.0.16-4
- Rebuild for EL9, Fedora 37 and Fedora 38
* Wed Nov 6 2019 Shaun Assam <sassam [at] fedoraproject.org> - 1.0.16-2
- Update specs for Python 3

