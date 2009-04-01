%define name enhance
%define version 0.0.1
%define release %mkrel 3

%define major 0
%define libname %mklibname %{name} %major
%define libnamedev %mklibname %{name} %major -d

Summary:	Library that takes advantage of Glade's
Name:		%name
Version:	%version
Epoch:		1
Release:	%release
License: 	BSD
Group:		System/Libraries
URL: 		http://www.enlightenment.org/
Source: 	ftp://ftp.enlightenment.org/pub/enhance/%{name}-%{version}.tar.bz2
BuildRequires: 	ecore-devel >= 0.9.9.050
Buildrequires: 	etk-devel >= 0.1.0.042, exml-devel >= 0.1.1
BuildRoot: 	%{_tmppath}/%{name}-%{version}-root
provides: 	%{name}-devel = %version
provides: 	%{name}-devel = %epoch:%version

%description
Enhance is a library that takes advantage of Glade's .glade XML files, EXML,
and Etk to easy application GUI development and cut down on its time.

After using Glade to design a GUI, you can save generate the .glade XML file
that describes the interface design and use it in Enhance to generate an Etk
equivalent. Enhance works at runtime, ie, it does not generate C code. It
will parse the XML at application launch and will do the appropriate work to
create the GUI and the required callbacks for you. There are several examples
in the examples directory for you to take a look at.

Please note that Etk does not support all of the GTK+ widgets. As widgets are
added to Etk, Enhance will be updated to support those new widgets.


%package -n %libname
Summary: %{name} libraries
Group:		System/Libraries
Provides: %{name} = %{version}-%{release}

%description -n %libname
%name libraries

%package -n %libnamedev
Summary: %{name} headers, static libraries, documentation and test programs
Group:		System/Libraries
Requires: %libname = %{epoch}:%{version}-%{release}
Requires: ecore-devel >= 0.9.9.050
Provides: %{name}-devel = %{version}-%{release}

%description -n %libnamedev
Headers, static libraries, test programs and documentation for enhance

%prep
rm -rf $RPM_BUILD_ROOT
%setup -q

%build
%configure2_5x
%make

%install
%makeinstall

%if %mdkversion < 200900
%post -n %libname -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %libname -p /sbin/ldconfig
%endif

%clean
test "x$RPM_BUILD_ROOT" != "x/" && rm -rf $RPM_BUILD_ROOT

%files -n %libname
%defattr(-, root, root)
%doc AUTHORS INSTALL README
%{_libdir}/*.so.%{major}*

%files -n %libnamedev
%defattr(-, root, root)
%{_libdir}/*a
%{_libdir}/pkgconfig/*.pc
%{_bindir}/%name-config
%{_libdir}/*.so
%{_includedir}/*
