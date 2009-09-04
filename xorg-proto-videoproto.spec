Summary:	Video protocol and ancillary headers
Summary(pl.UTF-8):	Nagłówki protokołu Video i pomocnicze.
Name:		xorg-proto-videoproto
Version:	2.2.2
Release:	2
License:	MIT
Group:		X11/Development/Libraries
Source0:	http://xorg.freedesktop.org/releases/individual/proto/videoproto-%{version}.tar.bz2
# Source0-md5:	44292d74a9a3c94b1ecb9d77a0da83e8
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	xorg-util-util-macros
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Video protocol and ancillary headers.

%description -l pl.UTF-8
Nagłówki protokołu Video i pomocnicze.

%package devel
Summary:	Video protocol and ancillary headers
Summary(pl.UTF-8):	Nagłówki protokołu Video i pomocnicze
Group:		X11/Development/Libraries
Requires:	xorg-proto-xproto-devel

%description devel
Video protocol and ancillary headers.

%description devel -l pl.UTF-8
Nagłówki protokołu Video i pomocnicze.

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
%{_includedir}/X11/extensions/*.h
%{_pkgconfigdir}/videoproto.pc
