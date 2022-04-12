#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-jeepney
Version  : 0.8.0
Release  : 34
URL      : https://files.pythonhosted.org/packages/d6/f4/154cf374c2daf2020e05c3c6a03c91348d59b23c5366e968feb198306fdf/jeepney-0.8.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/d6/f4/154cf374c2daf2020e05c3c6a03c91348d59b23c5366e968feb198306fdf/jeepney-0.8.0.tar.gz
Summary  : Low-level, pure Python DBus protocol wrapper.
Group    : Development/Tools
License  : MIT
Requires: pypi-jeepney-license = %{version}-%{release}
Requires: pypi-jeepney-python = %{version}-%{release}
Requires: pypi-jeepney-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(flit_core)

%description
Jeepney is a pure Python implementation of D-Bus messaging. It has an `I/O-free
<https://sans-io.readthedocs.io/>`__ core, and integration modules for different
event loops.

%package license
Summary: license components for the pypi-jeepney package.
Group: Default

%description license
license components for the pypi-jeepney package.


%package python
Summary: python components for the pypi-jeepney package.
Group: Default
Requires: pypi-jeepney-python3 = %{version}-%{release}

%description python
python components for the pypi-jeepney package.


%package python3
Summary: python3 components for the pypi-jeepney package.
Group: Default
Requires: python3-core
Provides: pypi(jeepney)

%description python3
python3 components for the pypi-jeepney package.


%prep
%setup -q -n jeepney-0.8.0
cd %{_builddir}/jeepney-0.8.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1649768905
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-jeepney
cp %{_builddir}/jeepney-0.8.0/LICENSE %{buildroot}/usr/share/package-licenses/pypi-jeepney/b2f7e71b77f14f21cd693e1c6fbe7236a8deac5f
pip install --root=%{buildroot} --no-deps --ignore-installed dist/*.whl
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-jeepney/b2f7e71b77f14f21cd693e1c6fbe7236a8deac5f

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
