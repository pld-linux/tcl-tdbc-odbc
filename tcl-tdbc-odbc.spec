Summary:	TDBC driver to access databases via ODBC
Summary(pl.UTF-8):	Sterownik TDBC służący do dostępu do baz danych poprzez ODBC
Name:		tcl-tdbc-odbc
Version:	1.0.4
Release:	1
License:	Tcl (BSD-like)
Group:		Libraries
Source0:	http://downloads.sourceforge.net/tcl/tdbcodbc%{version}.tar.gz
# Source0-md5:	fd8385b3b7af7873e45ea8a0b11a6f34
URL:		http://tdbc.tcl.tk/
BuildRequires:	tcl-devel >= 8.6
BuildRequires:	tcl-tdbc-devel >= %{version}
Requires:	tcl >= 8.6
Requires:	tcl-tdbc >= %{version}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Tcl TDBC MySQL module is the driver for Tcl Database Connectivity
(TDBC) to access databases via ODBC interface.

%description -l pl.UTF-8
Moduł Tcl TDBC MySQL to sterownik szkieletu Tcl Database Connectivity
(TDBC) służący do dostępu do baz danych poprzez interfejs ODBC.

%prep
%setup -q -n tdbcodbc%{version}

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# internal headers
%{__rm} $RPM_BUILD_ROOT%{_includedir}/{fakesql,odbcStubs}.h

# allow dependency generation
chmod 755 $RPM_BUILD_ROOT%{_libdir}/tdbcodbc%{version}/*.so

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README license.terms
%dir %{_libdir}/tdbcodbc%{version}
%attr(755,root,root) %{_libdir}/tdbcodbc%{version}/libtdbcodbc%{version}.so
%{_libdir}/tdbcodbc%{version}/*.tcl
%{_mandir}/mann/tdbc_odbc.n*
