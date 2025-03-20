## START: Set by rpmautospec
## (rpmautospec version 0.3.5)
## RPMAUTOSPEC: autorelease
%define autorelease(e:s:pb:n) %{?-p:0.}%{lua:
    release_number = 1;
    base_release_number = tonumber(rpm.expand("%{?-b*}%{!?-b:1}"));
    print(release_number + base_release_number - 1);
}%{?-e:.%{-e*}}%{?-s:.%{-s*}}%{!?-n:%{?dist}}
## END: Set by rpmautospec

## START: Set by rpmautospec
## (rpmautospec version 0.3.5)
## RPMAUTOSPEC: autorelease
%define autorelease(e:s:pb:n) %{?-p:0.}%{lua:
    release_number = 1;
    base_release_number = tonumber(rpm.expand("%{?-b*}%{!?-b:1}"));
    print(release_number + base_release_number - 1);
}%{?-e:.%{-e*}}%{?-s:.%{-s*}}%{!?-n:%{?dist}}
## END: Set by rpmautospec

## START: Set by rpmautospec
## (rpmautospec version 0.3.1)
## RPMAUTOSPEC: autorelease, autochangelog
%define autorelease(e:s:pb:n) %{?-p:0.}%{lua:
    release_number = 2;
    base_release_number = tonumber(rpm.expand("%{?-b*}%{!?-b:1}"));
    print(release_number + base_release_number - 1);
}%{?-e:.%{-e*}}%{?-s:.%{-s*}}%{!?-n:%{?dist}}
## END: Set by rpmautospec

%define _lto_cflags %{nil}

Name:           libfprint-tod

Version:        1.94.5
Release:        %autorelease
Summary:        Toolkit for fingerprint scanner

Provides:       libfprint == 1.94.5
Obsoletes:      libfprint == 1.94.5

License:        LGPLv2+
URL:            http://www.freedesktop.org/wiki/Software/fprint/libfprint
Source0:        https://gitlab.freedesktop.org/3v1n0/libfprint/-/archive/v%{version}+tod1/libfprint-v%{version}+tod1.tar.gz
ExcludeArch:    s390 s390x

BuildRequires:  meson
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  git
BuildRequires:  pkgconfig(glib-2.0) >= 2.50
BuildRequires:  pkgconfig(gio-2.0) >= 2.44.0
BuildRequires:  pkgconfig(gusb) >= 0.3.0
BuildRequires:  pkgconfig(nss)
BuildRequires:  pkgconfig(pixman-1)
BuildRequires:  gtk-doc
BuildRequires:  libgudev-devel
# For the udev.pc to install the rules
BuildRequires:  systemd
BuildRequires:  gobject-introspection-devel
# For internal CI tests; umockdev 0.13.2 has an important locking fix
BuildRequires:  python3-cairo python3-gobject cairo-devel
BuildRequires:  umockdev >= 0.13.2

%description
libfprint offers support for consumer fingerprint reader devices.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%autosetup -S git -n libfprint-v%{version}+tod1

%build
# Include the virtual image driver for integration tests
%meson -Ddrivers=all --buildtype release
%meson_build 

%install
%meson_install

%ldconfig_scriptlets

%check
%meson_test -t 4

%files
%license COPYING
%doc NEWS THANKS AUTHORS README.md
%{_libdir}/*.so.*
%{_libdir}/girepository-1.0/*.typelib
%{_udevhwdbdir}/60-autosuspend-libfprint-2.hwdb
%{_udevrulesdir}/70-libfprint-2.rules

%files devel
%doc HACKING.md
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/libfprint-2.pc
%{_libdir}/pkgconfig/libfprint-2-tod-1.pc
%{_datadir}/gir-1.0/*.gir
%{_datadir}/gtk-doc/html/libfprint-2/

%changelog
* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.94.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Nov 22 2022 Bastien Nocera <hadess@hadess.net> - 1.94.5-1
- Update to 1.94.5

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.94.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jul 11 2022 Benjamin Berg <bberg@redhat.com> - 1.94.4-1
- Update to 1.94.4

* Mon Feb 14 2022 Benjamin Berg <bberg@redhat.com> - 1.94.3-1
- Update to 1.94.3

* Mon Feb 14 2022 Benjamin Berg <bberg@redhat.com> - 1.94.2-4
- Don't set removed x11-examples option

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.94.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Nov 03 2021 Benjamin Berg <bberg@redhat.com> - 1.94.2-1
- Update to 1.94.2 (#1977842)

* Fri Sep 24 2021 Benjamin Berg <bberg@redhat.com> - 1.94.1-1
- Update to 1.94.1

* Fri Aug 20 2021 Benjamin Berg <bberg@redhat.com> - 1.94.0-1
- Update to 1.94.0 (#1977842)
  Related: #1894694

* Mon Jul 26 2021 Benjamin Berg <bberg@redhat.com> - 1.92.0-3
- Add patch disabling timeouts in virtual-device to enable fedora CI
- Increase timeout of tests by factor 4

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.92.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Jul 01 2021 Benjamin Berg <bberg@redhat.com> - 1.92.0-1
- Update to 1.92.0 (#1977842)

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.90.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jan 13 13:33:12 CET 2021 Benjamin Berg <bberg@redhat.com> - 1.90.7-1
- Update to 1.90.7 (#1902256)

* Wed Dec 09 2020 Benjamin Berg <bberg@redhat.com> - 1.90.6-1
- New upstream release 1.90.6 (#1902256)

* Tue Dec 01 2020 Benjamin Berg <bberg@redhat.com> - 1.90.5-1
- New upstream release 1.90.5 (#1902256)

* Fri Nov 27 2020 Benjamin Berg <bberg@redhat.com> - 1.90.4-1
- New upstream release 1.90.4 (#1902256)
  Resolves #1889384

* Mon Sep 14 2020 Benjamin Berg <bberg@redhat.com> - 1.90.3-1
- Update to libfprint 1.90.3 (#1878746)

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.90.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jun 08 2020 Benjamin Berg <bberg@redhat.com> - 1.90.2-1
- Update to libfprint 1.90.2
- Resolves #1832229
- Resolves #1841834
- Resolves #1841965

* Fri Feb 14 2020 Bastien Nocera <bnocera@redhat.com> - 1.90.1-2
+ libfprint-1.90.1-2
- Rebuilt for F32

* Mon Feb 10 2020 Benjamin Berg <bberg@redhat.com> - 1.90.1-1
- Update to libfprint 1.90.1

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Aug 14 2019 Benjamin Berg <bberg@redhat.com> - 1.0-1
+ libfprint-1.0-1
- Update to 1.0

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 20 2018 Bastien Nocera <bnocera@redhat.com> - 0.8.2-2
+ libfprint-0.8.2-2
- Fix build with newer meson (#1604585)

* Tue Jul 17 2018 Bastien Nocera <bnocera@redhat.com> - 0.8.2-1
+ libfprint-0.8.2-1
- Update to 0.8.2
- Add required gcc and gcc-c++ BR

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 12 2018 Bastien Nocera <bnocera@redhat.com> - 0.8.1-1
+ libfprint-0.8.1-1
- Update to 0.8.1 to fix the build

* Tue Jun 12 2018 Bastien Nocera <bnocera@redhat.com> - 0.8.0-1
+ libfprint-0.8.0-1
- Update to 0.8.0
- Port to meson, gtk-doc

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Feb 03 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.7.0-4
- Switch to %%ldconfig_scriptlets

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon May 15 2017 Bastien Nocera <bnocera@redhat.com> - 0.7.0-1
+ libfprint-0.7.0-1
- Update to 0.7.0

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Feb 03 2015 Bastien Nocera <bnocera@redhat.com> 0.6.0-1
- Update to 0.6.0

* Wed Dec 17 2014 Rex Dieter <rdieter@fedoraproject.org> - 0.5.1-5
- error opening ATTR{/sys/devices/pci0000:00/0000:00:1a.0/usb1/1-1/1-1.3/1-1.3:1.0/power/control} for writing (#950205)
- %%build: --disable-silent-rules

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Jan 16 2014 Ville Skytt√§ <ville.skytta@iki.fi> - 0.5.1-2
- Drop INSTALL from docs.

* Sun Aug 11 2013 Bastien Nocera <bnocera@redhat.com> 0.5.1-1
- Update to 0.5.1

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Dec 03 2012 Bastien Nocera <bnocera@redhat.com> 0.5.0-1
- Update to 0.5.0
- Re-add not useless udev rules

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri May 18 2012 Matthias Clasen <mclasen@redhat.com> - 0.4.0-4
- Drop broken and useless udev rules (#744637)

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Nov 21 2011 Adam Jackson <ajax@redhat.com> 0.4.0-2
- Rebuild without Requires: ConsoleKit, going away in F17

* Thu Nov 10 2011 Bastien Nocera <bnocera@redhat.com> 0.4.0-1
- Update to 0.4.0

* Mon Nov 07 2011 Adam Jackson <ajax@redhat.com> 0.3.0-3
- Rebuild for libpng 1.5

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Sep 08 2010 Bastien Nocera <bnocera@redhat.com> 0.3.0-1
- Update to 0.3.0

* Thu Aug 19 2010 Bastien Nocera <bnocera@redhat.com> 0.2.0-1
- Update to 0.2.0

* Wed Jun 30 2010 Matthew Garrett <mjg@redhat.com> 0.1.0-16.pre3
- Fix #505438 to avoid message on boot on some systems

* Tue Jun 01 2010 Bastien Nocera <bnocera@redhat.com> 0.1.0-16.pre2
- Add README to package

* Wed Jan 20 2010 Bastien Nocera <bnocera@redhat.com> 0.1.0-15.pre2
- Require hal-filesystem for the fdi file

* Tue Dec 01 2009 Bastien Nocera <bnocera@redhat.com> 0.1.0-14.pre2
- Update AES1610 patch

* Mon Nov 30 2009 Bastien Nocera <bnocera@redhat.com> 0.1.0-13.pre2
- Add aes1610 driver (#499732)

* Thu Oct 01 2009 Bastien Nocera <bnocera@redhat.com> 0.1.0-12.pre2
- Update udev autosuspend rules and disable SGS Thomson reader

* Fri Aug 21 2009 Tomas Mraz <tmraz@redhat.com> - 0.1.0-11.pre2
- rebuilt with new openssl

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.0-10.pre2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Jul 21 2009 Bastien Nocera <bnocera@redhat.com> 0.1.0-9.pre2
- Use gdk-pixbuf for image manipulation instead of ImageMagick (#472103)

* Sat Jun 20 2009 Bastien Nocera <bnocera@redhat.com> 0.1.0-8.pre2
- Update to 0.1.0-pre2

* Tue Jun 09 2009 Matthew Garrett <mjg@redhat.com> 0.1.0-7.pre1
- fprint-add-udev-rules.patch - build udev rules for autosuspend
- move hal fdi into the main package rather than -devel
- add autoreconf as a build depend while carrying the udev diff

* Tue Apr 21 2009 Karsten Hopp <karsten@redhat.com> 0.1.0-6.pre1.1
- Excludearch s390 s390x, we don't have USB devices there and this package
  doesn't build without USB support

* Mon Mar 09 2009 pingou <pingou@pingoured.fr> - 0.1.0-6.pre1
- Rebuilt for rawhide

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.0-5.pre1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Jan 17 2009 Tomas Mraz <tmraz@redhat.com> - 0.1.0-4.pre1
- rebuild with new openssl

* Tue Nov 25 2008 - Bastien Nocera <bnocera@redhat.com> - 0.1.0-3.pre1
- Fix possible crasher in libfprint when setting up the fds for polling

* Mon Nov 24 2008 - Bastien Nocera <bnocera@redhat.com> - 0.1.0-2.pre1
- And add some API docs

* Tue Nov 18 2008 - Bastien Nocera <bnocera@redhat.com> - 0.1.0-1.pre1
- Fix build

* Tue Nov 04 2008 - Bastien Nocera <bnocera@redhat.com> - 0.1.0-0.pre1
- Update to 0.1.0-pre1

* Tue May 13 2008  Pingou <pingoufc4@yahoo.fr> 0.0.5-6
- Correction on the Build Requires

* Tue May 13 2008  Pingou <pingoufc4@yahoo.fr> 0.0.5-5
- Correction on the Build Requires

* Tue May 13 2008  Pingou <pingoufc4@yahoo.fr> 0.0.5-4
- Update the Build Requires due to the change on ImageMagick

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.0.5-3
- Autorebuild for GCC 4.3

* Sat Jan 05 2008 Pingou <pingoufc4@yahoo.fr> 0.0.5-2
- Change on the BuildRequires

* Sat Jan 05 2008 Pingou <pingoufc4@yahoo.fr> 0.0.5-1
- Update to version 0.0.5

* Sat Dec 01 2007 Pingou <pingoufc4@yahoo.fr> 0.0.4-3
- Changes on the Requires

* Sun Nov 25 2007 Pingou <pingoufc4@yahoo.fr> 0.0.4-2
- Changes on the Requires

* Sat Nov 24 2007 Pingou <pingoufc4@yahoo.fr> 0.0.4-1
- First release

