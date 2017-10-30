#
# Conditional build:
%bcond_without	static_libs	# don't build static library

Summary:	libnslog library for NetSurf
Summary(pl.UTF-8):	Biblioteka libnslog dla projektu NetSurf
Name:		libnslog
Version:	0.1.0
Release:	1
License:	MIT
Group:		Libraries
Source0:	http://download.netsurf-browser.org/libs/releases/%{name}-%{version}-src.tar.gz
# Source0-md5:	69520a7133c9d13e11d164492d1bbe60
URL:		http://www.netsurf-browser.org/projects/libutf8proc/
BuildRequires:	netsurf-buildsystem >= 1.6
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libnslog

%package devel
Summary:	libnslog library headers
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libutf8proc
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
This package contains the include files and other resources you can
use to incorporate libnslog into applications.

%description devel -l pl.UTF-8
Pliki nagłówkowe pozwalające na używanie biblioteki libnslog w
swoich programach.

%package static
Summary:	libnslog static library
Summary(pl.UTF-8):	Statyczna biblioteka libnslog
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
This is package with static libnslog library.

%description static -l pl.UTF-8
Statyczna biblioteka libnslog.

%prep
%setup -q

%build
export AR="%{__ar}"
export CC="%{__cc}"
export CFLAGS="%{rpmcflags}"
export LDFLAGS="%{rpmldflags}"

%{__make} \
	Q= \
	PREFIX=%{_prefix} \
	COMPONENT_TYPE=lib-shared

%if %{with static_libs}
%{__make} \
	Q= \
	PREFIX=%{_prefix} \
	COMPONENT_TYPE=lib-static
%endif

%install
rm -rf $RPM_BUILD_ROOT

export AR="%{__ar}"
export CC="%{__cc}"
export CFLAGS="%{rpmcflags}"
export LDFLAGS="%{rpmldflags}"

%{__make} install \
	PREFIX=%{_prefix} \
	LIBDIR=%{_lib} \
	COMPONENT_TYPE=lib-shared \
	DESTDIR=$RPM_BUILD_ROOT

%if %{with static_libs}
%{__make} install \
	PREFIX=%{_prefix} \
	LIBDIR=%{_lib} \
	COMPONENT_TYPE=lib-static \
	DESTDIR=$RPM_BUILD_ROOT
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libnslog.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libnslog.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libnslog.so
%{_includedir}/nslog
%{_pkgconfigdir}/libnslog.pc

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libnslog.a
%endif
