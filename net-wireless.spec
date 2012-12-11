%define name net-wireless
%define version 0.2
%define release %mkrel 14

%define nsusr nagios
%define nsgrp nagios
%define cmdusr apache
%define cmdgrp apache

Summary: Wireless access for NetSaint
Name: %{name}
Version: %{version}
Release: %{release}
License: GPL
URL: http://mobileengines.com/net-wireless/
Group: Networking/Other
Source0: %{name}.%{version}.tar.bz2
Patch0: net-wireless-nagios.patch.bz2
BuildRoot: %{_tmppath}/%{name}-root
Requires: nagios nagios-www

%description
The Wireless Network Tools package uses a Web-enabled phone (or an emulator) to
provide traceroute, ping, and port scanning. If you use netsaint, it ties into
it nicely and provides real-time status of your hosts/network. This should be
considered pre-alpha, but it does do what it is intended to do.

%prep

%setup -n %{name}
%patch0 -p1

%build
echo "no compiling is needed"

%install
[ -n "%{buildroot}" -a "%{buildroot}" != / ] && rm -rf %{buildroot}

install -d %{buildroot}/etc/httpd/conf
install -d %{buildroot}%{_libdir}/nagios/cgi/
install -d %{buildroot}%{_datadir}/nagios
install -m644 wireless.cfg %{buildroot}/etc/httpd/conf/
install -m755 *.cgi %{buildroot}%{_libdir}/nagios/cgi/
install -m644 index.wml %{buildroot}%{_datadir}/nagios/

%clean
[ -n "%{buildroot}" -a "%{buildroot}" != / ] && rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc CHANGES EMULATORS INSTALL README THANKS
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/httpd/conf/wireless.cfg
%attr(0755,root,root) %dir %{_libdir}/nagios/cgi
%attr(0755,%{nsusr},%{cmdgrp}) %{_libdir}/nagios/cgi/*
%attr(0755,root,root) %dir %{_datadir}/nagios
%attr(0644,root,root) %{_datadir}/nagios/*



%changelog
* Fri Sep 04 2009 Thierry Vignaud <tvignaud@mandriva.com> 0.2-14mdv2010.0
+ Revision: 430170
- rebuild

* Fri Aug 08 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.2-13mdv2009.0
+ Revision: 268261
- rebuild early 2009.0 package (before pixel changes)

* Sun May 11 2008 Nicolas Lécureuil <neoclust@mandriva.org> 0.2-12mdv2009.0
+ Revision: 205688
- Should not be noarch ed

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request

* Wed Dec 12 2007 Thierry Vignaud <tvignaud@mandriva.com> 0.2-11mdv2008.1
+ Revision: 117858
- use %%mkrel
- import net-wireless


* Tue Apr 26 2005 Lenny Cartier <lenny@mandriva.com> 0.2-10mdk
- rebuild

* Mon Feb 23 2004 Lenny Cartier <lenny@mandrakesoft.com> 0.2-9mdk
- rebuild

* Mon Jan 27 2003 Lenny Cartier <lenny@mandrakesoft.com> 0.2-8mdk
- rebuild

* Fri Aug 30 2002 Oden Eriksson <oden.eriksson@kvikkjokk.net> 0.2-7mdk
- Arghh!!! Requires: nagios, not nagois :-)

* Fri Aug 30 2002 Oden Eriksson <oden.eriksson@kvikkjokk.net> 0.2-6mdk
- since nagios replaces netsaint, require nagios.
- relocate to real nagios cgi-bin
- misc spec file fixes
- fix P0

* Thu Aug 29 2002 Lenny Cartier <lenny@mandrakesoft.com> 0.2-5mdk
- rebuild

* Wed Aug 22 2001  Lenny Cartier <lenny@mandrakesoft.com> 0.2-4mdk
- rebuild

* Mon Jan 22 2001 Lenny Cartier <lenny@mandrakesoft.com> 0.2-3mdk
- rebuild

* Fri Jul 28 2000 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.2-2mdk
- BM

* Wed Jun 07 2000 Stefan van der Eijk <stefan.van.der.eijk@cmg.nl> 0.2-1mdk
- Updated to 0.2

* Thu Jan 20 2000 Stefan van der Eijk <stefan.van.der.eijk@cmg.nl>
- Altered configuration file / cgi's to fit the file locations
- Made wml-ping.cgi, nokia 7110 doesn't handle hdml (?)

* Wed Jan 19 2000 Stefan van der Eijk <stefan.van.der.eijk@cmg.nl>
- First build
