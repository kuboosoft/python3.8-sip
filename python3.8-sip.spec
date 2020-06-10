%define debug_package %{nil}

Summary: SIP - Python/C++ Bindings Generator
Name: python3.8-sip
Version: 4.19.23
Release: 1%{?dist}

# sipgen/parser.{c.h} is GPLv3+ with exceptions (bison)
License: GPLv2 or GPLv3 and (GPLv3+ with exceptions)
Url: https://riverbankcomputing.com/software/sip/intro
Source0: https://riverbankcomputing.com/static/Downloads/sip/%{version}/sip-%{version}%{?snap:.%{snap}}.tar.gz


BuildRequires: gcc-c++
BuildRequires: sed
BuildRequires: python3.8-devel 
BuildRequires: dbus-python-devel
BuildRequires: python3.8-dbus

%global _description\
SIP is a tool for generating bindings for C++ classes so that they can be\
accessed as normal Python classes. SIP takes many of its ideas from SWIG but,\
because it is specifically designed for C++ and Python, is able to generate\
tighter bindings. SIP is so called because it is a small SWIG.\
\
SIP was originally designed to generate Python bindings for KDE and so has\
explicit support for the signal slot mechanism used by the Qt/KDE class\
libraries. However, SIP can be used to generate Python bindings for any C++\
class library.

%description %_description


%prep
%setup -n sip-4.19.23

%build
python3.8 configure.py CFLAGS="$CFLAGS" LFLAGS="$LDFLAGS"
   
  make

%install
  make DESTDIR=%{buildroot} install


%files
%exclude /usr/bin/sip
%{_libdir}/python3.8/site-packages/sip-4.19.23.dist-info
%{_libdir}/python3.8/site-packages/__pycache__
%{_libdir}/python3.8/site-packages/sip.pyi
%{_libdir}/python3.8/site-packages/sip.so
%{_libdir}/python3.8/site-packages/sipconfig.py
%{_libdir}/python3.8/site-packages/sipdistutils.py
/usr/include/python3.8/sip.h

%changelog
