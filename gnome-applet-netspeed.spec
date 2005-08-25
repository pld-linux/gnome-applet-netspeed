%define		_realname	netspeed_applet
Summary:	Show how much traffic occurs on a network device
Summary(pl):	Pokazywanie wielkości ruchu występującego na urządzeniu sieciowym
Name:		gnome-applet-netspeed
Version:	0.13
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://www.wh-hms.uni-ulm.de/~mfcn/shared/netspeed/%{_realname}-%{version}.tar.gz
# Source0-md5:	b5c5332993ed779c3653433c6f3b6a9a
URL:		http://mfcn.ilo.de/netspeed_applet/
BuildRequires:	automake
BuildRequires:	gnome-desktop-devel >= 2.4.0
BuildRequires:	gnome-panel-devel >= 2.4.0
BuildRequires:	intltool >= 0.21
BuildRequires:	libglade2-devel >= 2.0.1
BuildRequires:	libgnomeui-devel >= 2.8.0
BuildRequires:	libgtop-devel >= 2.10.0
BuildRequires:	rpmbuild(macros) >= 1.197
BuildRequires:	scrollkeeper
Requires(post,postun):	scrollkeeper
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Netspeed applet is just a little applet that shows how much traffic
occurs on a specified network device.

%description -l pl
Netspeed jest po prostu niewielkim apletem pokazującym wielkość ruchu
występującego na określonym urządzeniu sieciowym.

%prep
%setup -q -n %{_realname}-%{version}

%build
cp -f /usr/share/automake/config.sub .
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	localedir=%{_datadir}/locale

%find_lang netspeed-applet --with-gnome --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%post
%scrollkeeper_update_post

%postun
%scrollkeeper_update_postun

%files -f netspeed-applet.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_libdir}/%{_realname}2
%{_libdir}/bonobo/servers/*.server
%{_omf_dest_dir}/%{_realname}
%{_pixmapsdir}/%{_realname}
%{_pixmapsdir}/*.png
