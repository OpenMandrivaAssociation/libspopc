%define	major 0
%define libname %mklibname spopc %{major}
%define develname %mklibname spopc -d

Summary:	POP3 client library
Name:		libspopc
Version:	0.7.8
Release:	%mkrel 1
License:	LGPLv2+
Group:		System/Libraries
URL:		http://brouits.free.fr/libspopc/
Source0:	http://brouits.free.fr/libspopc/releases/%{name}-%{version}.tar.gz
Patch0:		libspopc-shared.diff
BuildRequires:	openssl-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-root

%description
'libspopc' is a simple-to-use POP3 client library. It provides an easy and
quick way to host a POP3 client within a program to C developers without
exposing them to socket programming. However, the socket layer is also
accessible. libspopc allows mail programs to connect to many POP accounts and
manage email. It implements the client side of RFC 1939. The email client can
download email headers before downloading the entire message. 

%package -n	%{libname}
Summary:	POP3 client library
Group:          System/Libraries
Obsoletes:	%{name}
Provides:	%{name}

%description -n	%{libname}
'libspopc' is a simple-to-use POP3 client library. It provides an easy and
quick way to host a POP3 client within a program to C developers without
exposing them to socket programming. However, the socket layer is also
accessible. libspopc allows mail programs to connect to many POP accounts and
manage email. It implements the client side of RFC 1939. The email client can
download email headers before downloading the entire message. 

%package -n	%{develname}
Summary:	Development library and header files for %{name}
Group:		Development/C
Requires:	%{libname} = %{version}
Provides:	%{libname}-devel = %{version}
Obsoletes:	%{libname}-devel
Provides:	spopc-devel = %{version}
Obsoletes:	spopc-devel

%description -n	%{develname}
'libspopc' is a simple-to-use POP3 client library. It provides an easy and
quick way to host a POP3 client within a program to C developers without
exposing them to socket programming. However, the socket layer is also
accessible. libspopc allows mail programs to connect to many POP accounts and
manage email. It implements the client side of RFC 1939. The email client can
download email headers before downloading the entire message. 

This package contains the development library and header files for %{name} 

%prep

%setup -q -n %{name}-%{version}
%patch -p0

# fix attribs 
chmod 644 AUTHORS ChangeLog doc/README* README* doc/*.txt doc/*.html examples/*

%build

make

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

install -d %{buildroot}%{_includedir}
install -d %{buildroot}%{_libdir}

install -m0755 libspopc.so.%{version} %{buildroot}%{_libdir}/
ln -snf libspopc.so.%{version} %{buildroot}%{_libdir}/libspopc.so.0.7
ln -snf libspopc.so.%{version} %{buildroot}%{_libdir}/libspopc.so.0
ln -snf libspopc.so.%{version} %{buildroot}%{_libdir}/libspopc.so

install -m0755 libspopc.a %{buildroot}%{_libdir}/
install -m0644 libspopc.h %{buildroot}%{_includedir}/

cp doc/README README.examples

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files -n %{libname}
%defattr(-,root,root)
%doc AUTHORS ChangeLog README doc/*.txt doc/*.html
%{_libdir}/*.so.*

%files -n %{develname}
%defattr(-,root,root)
%doc README.examples examples
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/*.a
