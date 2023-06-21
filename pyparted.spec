#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: distutils3
#
# Source0 file verified with key 0x62977BB9C841B965 (dcantrel@redhat.com)
#
Name     : pyparted
Version  : 3.13.0
Release  : 7
URL      : https://github.com/dcantrell/pyparted/releases/download/v3.13.0/pyparted-3.13.0.tar.gz
Source0  : https://github.com/dcantrell/pyparted/releases/download/v3.13.0/pyparted-3.13.0.tar.gz
Source1  : https://github.com/dcantrell/pyparted/releases/download/v3.13.0/pyparted-3.13.0.tar.gz.asc
Summary  : Python bindings for GNU parted
Group    : Development/Tools
License  : GPL-2.0 GPL-2.0+
Requires: pyparted-license = %{version}-%{release}
Requires: pyparted-python = %{version}-%{release}
Requires: pyparted-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pkg-config
BuildRequires : pkgconfig(libparted)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
# pyparted
## Python bindings for libparted
---
### Overview
pyparted is a set of native Python bindings for libparted.  libparted
is the library portion of the GNU parted project.  With pyparted, you
can write applications that interact with disk partition tables and
filesystems.

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
Provides: pypi(pyparted)

%description python3
python3 components for the pyparted package.


%prep
%setup -q -n pyparted-3.13.0
cd %{_builddir}/pyparted-3.13.0
pushd ..
cp -a pyparted-3.13.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1687382932
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 setup.py build

popd
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pyparted
cp %{_builddir}/pyparted-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/pyparted/075d599585584bb0e4b526f5c40cb6b17e0da35a || :
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -tt setup.py build install --root=%{buildroot}-v3
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pyparted/075d599585584bb0e4b526f5c40cb6b17e0da35a

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/V3/usr/lib/python3*/*
/usr/lib/python3*/*
