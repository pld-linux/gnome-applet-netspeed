%define		_realname	netspeed_applet
Summary:	Show how much traffic occurs on a network device
Summary(pl.UTF-8):	Pokazywanie wielkości ruchu występującego na urządzeniu sieciowym
Name:		gnome-applet-netspeed
Version:	0.15
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://www.wh-hms.uni-ulm.de/~mfcn/netspeed/packages/%{_realname}-%{version}.tar.gz
# Source0-md5:	6aacaac946b17b3a95a0b366c6dbe850
URL:		http://www.gnome.org/projects/netspeed/
BuildRequires:	GConf2-devel
BuildRequires:	autoconf >= 2.52
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	gnome-doc-utils
BuildRequires:	gnome-panel-devel >= 2.4.0
BuildRequires:	intltool >= 0.35.0
BuildRequires:	libgtop-devel >= 2.14.2
BuildRequires:	libiw-devel >= 1:28-0.pre9.1
BuildRequires:	libtool
BuildRequires:	rpmbuild(find_lang) >= 1.23
BuildRequires:	rpmbuild(macros) >= 1.311
Requires(post,postun):	gtk+2
Requires(post,postun):	hicolor-icon-theme
Requires(post,postun):	scrollkeeper
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Netspeed applet is just a little applet that shows how much traffic
occurs on a specified network device.

%description -l pl.UTF-8
Netspeed jest po prostu niewielkim apletem pokazującym wielkość ruchu
występującego na określonym urządzeniu sieciowym.

%prep
%setup -q -n %{_realname}-%{version}

%build
%{__libtoolize}
%{__intltoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang netspeed_applet --with-gnome --with-omf

%clean
rm -rf $RPM_BUILD_ROOT

%post
%scrollkeeper_update_post
%update_icon_cache hicolor

%postun
%scrollkeeper_update_postun
%update_icon_cache hicolor

%files -f netspeed_applet.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_libdir}/netspeed_applet2
%{_libdir}/bonobo/servers/GNOME_NetspeedApplet.server
%{_iconsdir}/hicolor/*/*/*
