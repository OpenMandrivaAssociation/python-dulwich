%define module	dulwich

Summary:	Python implementation of the Git file formats and protocols

Name:		python-%{module}
Version:	0.9.6
Release:	2
Source0:	https://pypi.python.org/packages/source/d/dulwich/dulwich-%{version}.tar.gz
License:	GPLv2
Group:		Development/Python
Url:		https://launchpad.net/dulwich/
BuildRequires:	python-sphinx
BuildRequires:	python-nose, git-core
BuildRequires:  python-devel

%description
Dulwich is a pure-Python implementation of the Git file formats and protocols.

%prep
%setup -q -n %{module}-%{version}

%install
PYTHONDONTWRITEBYTECODE= %__python setup.py install --root=%{buildroot}

pushd docs
%__make html
popd

# Tests require unittest2 to run:
#%check
#make check

%files
%doc  COPYING  NEWS  docs/build/html
%{_bindir}/dul*
%{py_platsitedir}/%{module}*



