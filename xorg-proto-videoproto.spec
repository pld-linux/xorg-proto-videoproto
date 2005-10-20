Summary:	Video protocol and ancillary headers
Summary(pl):	Nag³ówki protoko³u Video i pomocnicze.
Name:		xorg-proto-videoproto
Version:	2.2.1
Release:	0.1
License:	MIT
Group:		X11/Development/Libraries
Source0:	http://xorg.freedesktop.org/releases/X11R7.0-RC1/proto/videoproto-%{version}.tar.bz2
# Source0-md5:	83245b434f77aeef2ba69b88153422a2
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	pkgconfig >= 0.19
BuildRequires:	xorg-util-util-macros
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Video protocol and ancillary headers.

%description -l pl
Nag³ówki protoko³u Video i pomocnicze.

%package devel
Summary:	Video protocol and ancillary headers
Summary(pl):	Nag³ówki protoko³u Video i pomocnicze
Group:		X11/Development/Libraries
Requires:	xorg-proto-xproto-devel

%description devel
Video protocol and ancillary headers.

%description devel -l pl
Nag³ówki protoko³u Video i pomocnicze.

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
%{_includedir}/X11/extensions/*.h
%{_pkgconfigdir}/videoproto.pc
