Summary:	Cool arcade/thinking game very much like Lode Runner
Name:		sdlscav
Version:	145
Release:	5
Group:		Games/Arcade
License:	GPL
URL:		http://www.xdr.com/dash/scavenger.html
Source:		http://www.xdr.com/dash/%{name}-%{version}.tar.bz2
Source10:	%{name}.16.xpm
Source11:	%{name}.32.xpm
Source12:	%{name}.48.xpm
Patch0:		%{name}-145-optflags.patch
Patch1:		%{name}-145-datapath.patch
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
%patch0 -p1
%patch1 -p1

%build
%make OPT="%{optflags}"

%install
rm -rf %{buildroot}

mkdir -p %{buildroot}%_gamesbindir %{buildroot}%_gamesdatadir/%{name}
install -m 0755 %{name} %{buildroot}%_gamesbindir/
for f in data/*; do install -m 0644 $f %{buildroot}%_gamesdatadir/%{name}/; done

mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/%{name}.desktop <<EOF
[Desktop Entry]
Name=SDL Scavenger
Comment=Cool arcade/thinking game very much like Lode Runner
Exec=%{_gamesbindir}/%{name}
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

%if %mdkversion < 200900
%post
%{update_menus}
%endif

%if %mdkversion < 200900
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


%changelog
* Sun Sep 20 2009 Thierry Vignaud <tvignaud@mandriva.com> 145-4mdv2010.0
+ Revision: 445093
- rebuild

* Fri Dec 05 2008 Zombie Ryushu <ryushu@mandriva.org> 145-3mdv2009.1
+ Revision: 310699
- Fix odds quotation that don't belong.
- Fix Desktop shortcut

* Wed Nov 12 2008 Zombie Ryushu <ryushu@mandriva.org> 145-2mdv2009.1
+ Revision: 302450
- Release Increment
- Fix xdg menu again
- Fix MDV Compiance for XDG Menu
- Fix Menu Entry and Build Requires
- First Mandriva Package of SDL Port of xscavenger
- First Mandriva Package of SDL Port of xscavenger
- import sdlscav

  + Tomasz Pawel Gajc <tpg@mandriva.org>
    - Patch0: build with %%optflags
    - make it mdv compiliant


* Fri Nov 6 2008 Zombie Ryushu <ryushu@mandriva.org> 145
- 145
- First Mandriva Package with Zombie as full maintner

* Fri Jul 20 2007 Sergey V Turchin <zerg at altlinux dot org> 144-alt2
- fix data locations

* Thu Jul 19 2007 Sergey V Turchin <zerg at altlinux dot org> 144-alt1
- new version

* Thu Dec 25 2003 Sergey V Turchin <zerg at altlinux dot org> 137-alt3
- fix menu to launch via soundwrapper
- cleanup spec
- rebuild

* Tue Sep 24 2002 Sergey V Turchin <zerg@altlinux.ru> 137-alt2
- rebuild with gcc3.2

* Fri Jul 06 2001 Sergey V Turchin <zerg@altlinux.ru> 137-alt1
- first ALT release
