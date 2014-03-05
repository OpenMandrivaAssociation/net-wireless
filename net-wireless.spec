%define debug_package %{nil}

%define nsusr nagios
%define nsgrp nagios
%define cmdusr apache
%define cmdgrp apache

Summary: Wireless access for NetSaint
Name:    net-wireless
Version: 0.2
Release: 15
License: GPL
URL:     http://mobileengines.com/net-wireless/
Group:   Networking/Other
Source0: %{name}.%{version}.tar.bz2
Patch0:  net-wireless-nagios.patch.bz2
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
install -d %{buildroot}/etc/httpd/conf
install -d %{buildroot}%{_libdir}/nagios/cgi/
install -d %{buildroot}%{_datadir}/nagios
install -m644 wireless.cfg %{buildroot}/etc/httpd/conf/
install -m755 *.cgi %{buildroot}%{_libdir}/nagios/cgi/
install -m644 index.wml %{buildroot}%{_datadir}/nagios/

%files
%doc CHANGES EMULATORS INSTALL README THANKS
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/httpd/conf/wireless.cfg
%attr(0755,root,root) %dir %{_libdir}/nagios/cgi
%attr(0755,%{nsusr},%{cmdgrp}) %{_libdir}/nagios/cgi/*
%attr(0755,root,root) %dir %{_datadir}/nagios
%attr(0644,root,root) %{_datadir}/nagios/*
