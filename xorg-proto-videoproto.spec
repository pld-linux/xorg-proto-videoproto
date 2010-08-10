Summary:	Video extension headers
Summary(pl.UTF-8):	Nagłówki roszerzenia Video
Name:		xorg-proto-videoproto
Version:	2.3.1
Release:	1
License:	MIT
Group:		X11/Development/Libraries
Source0:	http://xorg.freedesktop.org/releases/individual/proto/videoproto-%{version}.tar.bz2
# Source0-md5:	c3b348c6e2031b72b11ae63fc7f805c2
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	xorg-util-util-macros >= 1.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Video extension headers.

%description -l pl.UTF-8
Nagłówki roszerzenia Video.

%package devel
Summary:	Video extension headers
Summary(pl.UTF-8):	Nagłówki roszerzenia Video
Group:		X11/Development/Libraries
Requires:	xorg-proto-xproto-devel

%description devel
Video extension headers.

%description devel -l pl.UTF-8
Nagłówki roszerzenia Video.

%prep
%setup -q -n videoproto-%{version}

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	pkgconfigdir=%{_pkgconfigdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files devel
%defattr(644,root,root,755)
%doc COPYING ChangeLog
%{_includedir}/X11/extensions/Xv*.h
%{_includedir}/X11/extensions/vldXvMC.h
%{_pkgconfigdir}/videoproto.pc
