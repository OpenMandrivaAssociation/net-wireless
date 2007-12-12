%define name net-wireless
%define version 0.2
%define release %mkrel 11

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
BuildArch: noarch

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

