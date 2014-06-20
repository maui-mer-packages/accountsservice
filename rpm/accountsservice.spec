# 
# Do NOT Edit the Auto-generated Part!
# Generated by: spectacle version 0.27
# 

Name:       accountsservice

# >> macros
# << macros

Summary:    D-Bus interfaces for querying and manipulating user account information
Version:    0.6.37
Release:    1
Group:      System/Daemons
License:    GPLv3
URL:        http://www.freedesktop.org/wiki/Software/AccountsService/
Source0:    accountsservice-%{version}.tar.xz
Source100:  accountsservice.yaml
Requires:   polkit
Requires:   shadow-utils
Requires:   systemd
Requires(preun): systemd
Requires(post): systemd
Requires(postun): systemd
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(systemd)
BuildRequires:  pkgconfig(polkit-gobject-1)
BuildRequires:  pkgconfig(dbus-glib-1)
BuildRequires:  pam-devel
BuildRequires:  gobject-introspection-devel
BuildRequires:  intltool
BuildRequires:  systemd

%description
The AccountService project provides a set of D-Bus
interfaces for querying and manipulating user account
information and an implementation of these interfaces,
based on the useradd, usermod and userdel commands.


%package libs
Summary:    Client-side library to talk to accountsservice
Group:      Development/Libraries
Requires:   %{name} = %{version}-%{release}
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig

%description libs
The accountsservice-libs package contains a library that can
be used by applications that want to interact with the accountsservice
daemon.


%package devel
Summary:    Development files for accountsservice-libs
Group:      Development/System
Requires:   %{name} = %{version}-%{release}

%description devel
This accountsservice-devel package contains headers and other
files needed to build applications that use accountsservice-libs.


%prep
%setup -q -n %{name}-%{version}/upstream

# >> setup
# << setup

%build
# >> build pre
# << build pre

%autogen --disable-static
%configure --disable-static
make %{?_smp_mflags}

# >> build post
# << build post

%install
rm -rf %{buildroot}
# >> install pre
# << install pre
%make_install

# >> install post
%find_lang accounts-service
# << install post

%post libs -p /sbin/ldconfig

%postun libs -p /sbin/ldconfig

%files -f accounts-service.lang
%defattr(-,root,root,-)
%doc AUTHORS COPYING INSTALL NEWS README TODO
%{_sysconfdir}/dbus-1/system.d/org.freedesktop.Accounts.conf
%{_libexecdir}/accounts-daemon
%{_datadir}/dbus-1/interfaces/org.freedesktop.Accounts.xml
%{_datadir}/dbus-1/interfaces/org.freedesktop.Accounts.User.xml
%{_datadir}/dbus-1/system-services/org.freedesktop.Accounts.service
%{_datadir}/polkit-1/actions/org.freedesktop.accounts.policy
%dir %{_localstatedir}/lib/AccountsService/
%dir %{_localstatedir}/lib/AccountsService/users
%dir %{_localstatedir}/lib/AccountsService/icons
%{_unitdir}/accounts-daemon.service
# >> files
# << files

%files libs
%defattr(-,root,root,-)
%{_libdir}/libaccountsservice.so.*
%{_libdir}/girepository-1.0/AccountsService-1.0.typelib
# >> files libs
# << files libs

%files devel
%defattr(-,root,root,-)
%{_includedir}/accountsservice-1.0
%{_libdir}/libaccountsservice.so
%{_libdir}/pkgconfig/accountsservice.pc
%{_datadir}/gir-1.0/AccountsService-1.0.gir
# >> files devel
# << files devel
