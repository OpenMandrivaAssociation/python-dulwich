%undefine _debugsource_template
%define module dulwich

Name:		python-dulwich
Version:	1.1.0
Release:	1
Summary:	Pure-Python Git implementation
Group:		Development/Python
License:	Apache-2.0 OR GPL-2.0-or-later
URL:		https://github.com/dulwich/dulwich
Source0:	https://files.pythonhosted.org/packages/source/d/%{module}/%{module}-%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildSystem:	python
BuildRequires:	pkgconfig(python3)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(setuptools-rust)
BuildRequires:	python%{pyver}dist(wheel)

%description
This is the Dulwich project.

It aims to provide an interface to git repos (both local and remote) that
doesn't call out to git directly but instead uses pure Python.

%files
%{_bindir}/dul-receive-pack
%{_bindir}/dul-upload-pack
%{_bindir}/dulwich
%{py_platsitedir}/%{module}
%{py_platsitedir}/%{module}-%{version}.dist-info
