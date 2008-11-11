%define name	sdlscav
%define version 145
%define	Summary	Cool arcade/thinking game very much like Lode Runner
%define release %mkrel 1
Summary:	%{Summary}
Name:		%{name}
Version:	%{version}
Release:	%{release}

Group:	Games/Arcade
URL:	http://www.xdr.com/dash/scavenger.html
License:	GPL
BuildRequires:	libSDL-devel rpm-build
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot


Source: http://www.xdr.com/dash/%name-%version.tar.bz2
Source10: %name.16.xpm
Source11: %name.32.xpm
Source12: %name.48.xpm

Patch1: sdlscav-145-datapath.patch

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
mkdir -p %buildroot%_gamesbindir %buildroot%_gamesdatadir/%name
install -m 0755 %name %buildroot%_gamesbindir/
for f in data/*
do
	install -m 0644 $f %buildroot%_gamesdatadir/%name/
done

mkdir -p %buildroot/%_menudir
cat << EOF > %buildroot/%_menudir/%name
?package(%name):command="soundwrapper %name" icon="%name.xpm" \
  needs="x11" section="Amusement/Arcade" title="SDL Scavenger" \
  longtitle="Cool arcade/thinking game very much like Lode Runner"
EOF

mkdir -p %buildroot%_miconsdir
mkdir -p %buildroot%_liconsdir
install -m 0644 %SOURCE10 %buildroot%_miconsdir/%name.xpm
install -m 0644 %SOURCE11 %buildroot%_iconsdir/%name.xpm
install -m 0644 %SOURCE12 %buildroot%_liconsdir/%name.xpm

%post
%update_menus

%postun
%clean_menus

%files
%defattr(-,root,root)
%doc README DOC
%_gamesbindir/*
%_gamesdatadir/%name
%_menudir/%name
%_miconsdir/%name.xpm
%_iconsdir/%name.xpm
%_liconsdir/%name.xpm

