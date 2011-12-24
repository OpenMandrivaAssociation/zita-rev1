Name:            zita-rev1
Version:         0.2.1

Release:         2


Summary:        Hall-type stereo reverb with GUI
Source:         http://kokkinizita.linuxaudio.org/linuxaudio/downloads/%{name}-%{version}.tar.bz2
URL:            http://kokkinizita.linuxaudio.org
License:        GPLv2
Group:          Sound
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:  gtk2-devel
BuildRequires:  cairo-devel
BuildRequires:  clxclient-devel
BuildRequires:  jackit-devel

%description
Zita-REV1 is a reworked version of the reverb originally developed for
the Aeolus Virtual Pipe Organ by Fons "Kokkinizita" Adriaensen.
Its character is more 'hall' than 'plate', but it can be used on a wide
variety of instruments or voices. It is not a spatialiser - the early
reflections are different for the L and R inputs, but do not correspond
to any real room. They have been tuned to match left and right sources
to some extent.

%prep
%setup -q

perl -pi -e 's/\/usr\/local/\/usr/g' source/Makefile
perl -pi -e 's/-march=native//g' source/Makefile

%build
cd source
%make

%install
rm -rf %{buildroot}
install -d %{buildroot}/%{_datadir}/%{name}
install -d %{buildroot}/%{_bindir}
cd source
%makeinstall_std

#install html documentation page
install -d %{buildroot}%{_datadir}/doc/%{name}/html/
install -m 755 ../doc/* %{buildroot}%{_datadir}/doc/%{name}/html

mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=Zita-REV1
Comment=Stereo reverb
Exec=%{_bindir}/%{name}
Icon=sound_section
Terminal=false
Type=Application
Categories=X-MandrivaLinux-Multimedia-Sound;AudioVideo;
Encoding=UTF-8
EOF


%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README
%doc doc/*
%{_bindir}/*
%{_datadir}/%{name}/*
%{_datadir}/applications/mandriva-%{name}.desktop

