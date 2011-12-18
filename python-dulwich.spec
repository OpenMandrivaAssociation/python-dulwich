%define module	dulwich
%define name	python-%{module}
%define version	0.8.2
%define release %mkrel 1

Summary:	Python implementation of the Git file formats and protocols
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source0:	%{module}-%{version}.tar.gz
License:	GPLv2
Group:		Development/Python
Url:		https://launchpad.net/dulwich/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	python-sphinx
BuildRequires:	python-nose, git-core
%py_requires -d

%description
Dulwich is a pure-Python implementation of the Git file formats and protocols.

%prep
%setup -q -n %{module}-%{version}

%install
%__rm -rf %{buildroot}
PYTHONDONTWRITEBYTECODE= %__python setup.py install --root=%{buildroot} --record=FILE_LIST

pushd docs
%__make html
popd

# Tests require unittest2 to run:
#%check
#make check

%clean
%__rm -rf %{buildroot}

%files -f FILE_LIST
%defattr(-,root,root)
%doc AUTHORS COPYING HACKING NEWS README docs/build/html
