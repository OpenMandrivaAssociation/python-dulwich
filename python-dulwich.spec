%define module	dulwich

Summary:	Python implementation of the Git file formats and protocols
Name:		python-%{module}
Version:	0.9.0
Release:	2
Source0:	http://www.samba.org/~jelmer/dulwich/dulwich-%{version}.tar.gz
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
%doc AUTHORS COPYING HACKING NEWS README docs/build/html
%_bindir/dul*
%py_platsitedir/%{module}*


%changelog
* Wed May 09 2012 Alexander Khrukin <akhrukin@mandriva.org> 0.8.5-1
+ Revision: 797632
- version update 0.8.5

* Wed Mar 28 2012 Lev Givon <lev@mandriva.org> 0.8.4-1
+ Revision: 788026
- Update to 0.8.4.

* Sun Jan 22 2012 Lev Givon <lev@mandriva.org> 0.8.3-1
+ Revision: 765013
- Update to 0.8.3.

* Mon Dec 19 2011 Lev Givon <lev@mandriva.org> 0.8.2-1
+ Revision: 743637
- Update to 0.8.2.

* Tue Nov 01 2011 Lev Givon <lev@mandriva.org> 0.8.1-1
+ Revision: 709401
- Update to 0.8.1.

* Sun Aug 07 2011 Lev Givon <lev@mandriva.org> 0.8.0-1
+ Revision: 693600
- Update to 0.8.0.
- Update to 0.7.1.

* Sun Jan 23 2011 Lev Givon <lev@mandriva.org> 0.7.0-1
+ Revision: 632400
- Update to 0.7.0.

* Tue Nov 02 2010 Michael Scherer <misc@mandriva.org> 0.6.2-2mdv2011.0
+ Revision: 592364
- rebuild for python 2.7

* Sun Oct 17 2010 Lev Givon <lev@mandriva.org> 0.6.2-1mdv2011.0
+ Revision: 586448
- Update to 0.6.2.

* Thu Jul 22 2010 Lev Givon <lev@mandriva.org> 0.6.1-1mdv2011.0
+ Revision: 556977
- Update to 0.6.1.

* Sun May 23 2010 Lev Givon <lev@mandriva.org> 0.6.0-1mdv2011.0
+ Revision: 545734
- Update to 0.6.0.

* Wed Apr 14 2010 Lev Givon <lev@mandriva.org> 0.5.0-1mdv2010.1
+ Revision: 534932
- import python-dulwich


