%define srcname dulwich
%define debug_package %nil

Name:           python-%{srcname}
Version:	0.22.8
Release:	1
Summary:        Pure-Python Git implementation
Group:		Development/Python
License:        BSD
URL:            https://github.com/dulwich/dulwich
Source0:        https://github.com/dulwich/dulwich/archive/dulwich-%{version}.tar.gz

BuildRequires:  python%{pyver}dist(setuptools-rust)
BuildSystem:	python

%description
This is the Dulwich project.

It aims to provide an interface to git repos (both local and remote) that
doesn't call out to git directly but instead uses pure Python.

%files
%{_bindir}/dul-receive-pack
%{_bindir}/dul-upload-pack
%{_bindir}/dulwich
%{py_platsitedir}/%{srcname}
%{py_platsitedir}/%{srcname}*.*-info
