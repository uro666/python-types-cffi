%define module types_cffi

Name:		python-types-cffi
Version:	1.17.0.20250319
Release:	1
Source0:	https://files.pythonhosted.org/packages/source/t/types-cffi/%{module}-%{version}.tar.gz
Summary:	Typing stubs for cffi
URL:		https://pypi.org/project/types-cffi/
License:	Apache-2.0
Group:		Development/Python
BuildSystem:	python
BuildArch:	noarch

BuildRequires:	python
BuildRequires:	pkgconfig(python3)
BuildRequires:	python-setuptools
Requires:	python-types-setuptools

%description
Typing stubs for cffi

%prep
%autosetup -p1 -n %{module}-%{version}

%build
%py_build

%install
%py3_install


%files
%{py_sitedir}/_cffi_backend-stubs/*
%{py_sitedir}/cffi-stubs/*
%{py_sitedir}/%{module}-%{version}-*.*-info/*
%license LICENSE
%doc README.md