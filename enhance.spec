%define name enhance
%define version 0.0.1
%define release %mkrel 1

%define major 1
%define libname %mklibname %{name} %major
%define libnamedev %mklibname %{name} %major -d

Summary:	Enhance is a library that takes advantage of Glade's
Name:		%name
Version:	%version
Release:	%release
License: BSD
Group: System Environment/Libraries
URL: http://www.enlightenment.org/
Source: ftp://ftp.enlightenment.org/pub/enhance/%{name}-%{version}.tar.bz2
BuildRequires: libxml2-devel, ecore-devel >= 0.9.9.038
BuildRoot: %{_tmppath}/%{name}-%{version}-root

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
Summary: %name libraries
Group: System Environment/Libraries
Requires: %{name} = %{version}
Requires: libxml2-devel, ecore-devel

%description -n %libname
%name libraries

%package -n %libnamedev
Summary: %name headers, static libraries, documentation and test programs
Group: System Environment/Libraries
Requires: %{name} = %{version}
Requires: ecore-devel >= 0.9.9.038

%description -n %libnamedev
Headers, static libraries, test programs and documentation for enhance

%prep
rm -rf $RPM_BUILD_ROOT
%setup -n %name-%version

%build
%configure2_5x
%make

%install
%makeinstall

%post -n %libname -p /sbin/ldconfig
%postun -n %libname -p /sbin/ldconfig

%clean
test "x$RPM_BUILD_ROOT" != "x/" && rm -rf $RPM_BUILD_ROOT

%files -n %libname
%defattr(-, root, root)
%doc AUTHORS COPYING INSTALL NEWS README
%{_libdir}/*.so*

%files -n %libnamedev
%defattr(-, root, root)
%doc doc/html
%{_libdir}/*a
%{_libdir}/pkgconfig/*.pc
%{_bindir}/%name-config
%{_includedir}/*
