%define module	dulwich
%define name	python-%{module}
%define version	0.8.5
%define release 1

Summary:	Python implementation of the Git file formats and protocols
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source0:	http://samba.org/~jelmer/dulwich/%{module}-%{version}.tar.gz
License:	GPLv2
Group:		Development/Python
Url:		https://launchpad.net/dulwich/
BuildRequires:	python-sphinx
BuildRequires:	python-nose, git-core
%py_requires -d

%description
Dulwich is a pure-Python implementation of the Git file formats and protocols.

%prep
%setup -q -n %{module}-%{version}

%install
%__rm -rf %{buildroot}
PYTHONDONTWRITEBYTECODE= %__python setup.py install --root=%{buildroot}

pushd docs
%__make html
popd

# Tests require unittest2 to run:
#%check
#make check

%files
%doc AUTHORS COPYING HACKING NEWS README docs/build/html
%_bindir/dul*
%py_platsitedir/%{module}*
