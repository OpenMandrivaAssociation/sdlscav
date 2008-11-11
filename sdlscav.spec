Summary:	Cool arcade/thinking game very much like Lode Runner
Name:		sdlscav
Version:	145
Release:	%mkrel 1
Group:		Games/Arcade
License:	GPL
URL:		http://www.xdr.com/dash/scavenger.html
Source:		http://www.xdr.com/dash/%{name}-%{version}.tar.bz2
Source10:	%{name}.16.xpm
Source11:	%{name}.32.xpm
Source12:	%{name}.48.xpm
Patch1:		sdlscav-145-datapath.patch
BuildRequires:	SDL-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
SDL Scavenger is a cool arcade/thinking game very much like Lode Runner.
You've got to run around and collect objects while avoiding enemies. Some
objects are buried and you've got to dig down to get at them. It's an
addictive game and some of the levels are devilishly (cruelly) complicated
to solve.

%prep
%setup -q
%patch1 -p1

%build
%make

%install
rm -rf %{buildroot}

mkdir -p %{buildroot}%_gamesbindir %{buildroot}%_gamesdatadir/%{name}
install -m 0755 %{name} %{buildroot}%_gamesbindir/
for f in data/*; do install -m 0644 $f %{buildroot}%_gamesdatadir/%{name}/; done

mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/%{name}.desktop <<EOF
[Desktop Entry]
Name="SDL Scavenger" \
Comment="Cool arcade/thinking game very much like Lode Runner"
Exec=%{_bindir}/%{name}
Icon=%{name}
Terminal=false
Type=Application
StartupNotify=true
Categories=Game;ArcadeGame;
EOF

mkdir -p %{buildroot}%_miconsdir
mkdir -p %{buildroot}%_liconsdir
install -m 0644 %SOURCE10 %{buildroot}%_miconsdir/%{name}.xpm
install -m 0644 %SOURCE11 %{buildroot}%_iconsdir/%{name}.xpm
install -m 0644 %SOURCE12 %{buildroot}%_liconsdir/%{name}.xpm

%if %mdkversion < 2009
%post
%{update_menus}
%endif

%if %mdkversion < 2009
%postun
%{clean_menus}
%endif

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README DOC
%_gamesbindir/*
%_gamesdatadir/%{name}
%{_datadir}/applications/*.desktop
%_miconsdir/%{name}.xpm
%_iconsdir/%{name}.xpm
%_liconsdir/%{name}.xpm
