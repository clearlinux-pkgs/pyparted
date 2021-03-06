#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x62977BB9C841B965 (dcantrel@redhat.com)
#
Name     : pyparted
Version  : 3.11.7
Release  : 1
URL      : https://github.com/dcantrell/pyparted/releases/download/v3.11.7/pyparted-3.11.7.tar.gz
Source0  : https://github.com/dcantrell/pyparted/releases/download/v3.11.7/pyparted-3.11.7.tar.gz
Source1  : https://github.com/dcantrell/pyparted/releases/download/v3.11.7/pyparted-3.11.7.tar.gz.asc
Summary  : Python bindings for GNU parted
Group    : Development/Tools
License  : GPL-2.0 GPL-2.0+
Requires: pyparted-license = %{version}-%{release}
Requires: pyparted-python = %{version}-%{release}
Requires: pyparted-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : parted-dev
BuildRequires : pkgconfig(libparted)

%description
pyparted
Python bindings for libparted
-----------------------------
OVERVIEW
pyparted is a set of native Python bindings for libparted.  libparted is the
library portion of the GNU parted project.  With pyparted, you can write
applications that interact with disk partition tables and filesystems.

%package license
Summary: license components for the pyparted package.
Group: Default

%description license
license components for the pyparted package.


%package python
Summary: python components for the pyparted package.
Group: Default
Requires: pyparted-python3 = %{version}-%{release}

%description python
python components for the pyparted package.


%package python3
Summary: python3 components for the pyparted package.
Group: Default
Requires: python3-core

%description python3
python3 components for the pyparted package.


%prep
%setup -q -n pyparted-3.11.7
cd %{_builddir}/pyparted-3.11.7

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1611963824
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pyparted
cp %{_builddir}/pyparted-3.11.7/COPYING %{buildroot}/usr/share/package-licenses/pyparted/075d599585584bb0e4b526f5c40cb6b17e0da35a
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pyparted/075d599585584bb0e4b526f5c40cb6b17e0da35a

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
