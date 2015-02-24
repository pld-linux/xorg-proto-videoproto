Summary:	Video extension headers
Summary(pl.UTF-8):	Nagłówki roszerzenia Video
Name:		xorg-proto-videoproto
Version:	2.3.2
Release:	2
License:	MIT
Group:		X11/Development/Libraries
Source0:	http://xorg.freedesktop.org/releases/individual/proto/videoproto-%{version}.tar.bz2
# Source0-md5:	e658641595327d3990eab70fdb55ca8b
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake
BuildRequires:	xorg-util-util-macros >= 1.3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Video (XVideo) extension headers.

%description -l pl.UTF-8
Nagłówki roszerzenia Video (XVideo).

%package devel
Summary:	Video extension headers
Summary(pl.UTF-8):	Nagłówki roszerzenia Video
Group:		X11/Development/Libraries
Requires:	xorg-proto-xproto-devel

%description devel
Video (XVideo) extension headers.

%description devel -l pl.UTF-8
Nagłówki roszerzenia Video (XVideo).

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
%doc COPYING ChangeLog README xv-protocol-v2.txt
%{_includedir}/X11/extensions/Xv*.h
%{_includedir}/X11/extensions/vldXvMC.h
%{_pkgconfigdir}/videoproto.pc
