Summary:	gvid lets you change video modes under X
Summary(pl):	Aplikacja pozwalaj±ca zmieniaæ tryby graficzne pod X
Name:		gnome-applet-gvid
Version:	0.3
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://kvand.mit.edu/gvid/gvid-%{version}.tar.gz
# Source0-md5:	12e1cc0a683c601b5df902f16f782d20
URL:		http://kvand.mit.edu/gvid/
BuildRequires:	autoconf
BuildRequires:	gnome-libs-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir	/etc/X11/GNOME

%description
Essentially, gvid lets you change video modes under X. That's it.
It'll display a little monitor icon your gnome panel. Click on the
monitor icon to pop up a list of available modes. If you are running
dual or multi-head displays, it will give you a list of screens so you
can select the appropriate one.

%description -l pl
gvid pozwala zmieniaæ tryby graficzne pod X. Wy¶wietla ma³± ikonê
z monitorem w panelu GNOME. Po klikniêciu pokazuje listê dostêpnych
trybów. W przypadku pracy na wielu monitorach pozwala wybraæ, którego
ma dotyczyæ zmiana.

%prep
%setup -q -n gvid-%{version}

%build
%{__autoconf}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_sysconfdir}/CORBA/servers} \
	$RPM_BUILD_ROOT%{_datadir}/applets/Utility

install gvid $RPM_BUILD_ROOT%{_bindir}
install gvid.gnorba $RPM_BUILD_ROOT%{_sysconfdir}/CORBA/servers
install gvid.desktop $RPM_BUILD_ROOT%{_datadir}/applets/Utility

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%attr(755,root,root) %{_bindir}/*
%{_sysconfdir}/CORBA/servers/*
%{_datadir}/applets/Utility/*
