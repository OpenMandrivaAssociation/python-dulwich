%define srcname dulwich

Name:           python-%{srcname}
Version:	0.20.2
Release:	1
Summary:        Pure-Python Git implementation
Group:		Development/Python
License:        BSD
URL:            https://github.com/dulwich/dulwich
Source0:        https://github.com/dulwich/dulwich/archive/dulwich-%{version}.tar.gz

BuildRequires:  pkgconfig(python2)
BuildRequires:  pythonegg(setuptools)
BuildRequires:  python2-pkg-resources
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3egg(setuptools)
BuildRequires:  python-pkg-resources

%description
This is the Dulwich project.

It aims to provide an interface to git repos (both local and remote) that
doesn't call out to git directly but instead uses pure Python.

%package -n python2-%{srcname}
Summary:        Pure-Python Git implementation
Group:		Development/Python

%description -n python2-%{srcname}
This is the Dulwich project.

It aims to provide an interface to git repos (both local and remote) that
doesn't call out to git directly but instead uses pure Python.

%prep
%setup -q -n %{srcname}-%{srcname}-%{version}
cp -a . %{py2dir}


%build
%__python setup.py build

pushd %{py2dir}
%{__python2} setup.py build
popd

%install
pushd %{py2dir}
%{__python2} setup.py install --skip-build --root %{buildroot}
for i in %{buildroot}%{_bindir}/*; do
	mv $i ${i}2
done
popd

%__python setup.py install --skip-build --root %{buildroot}

%files
%{_bindir}/dul-receive-pack
%{_bindir}/dul-upload-pack
%{_bindir}/dulwich
%{py_platsitedir}/%{srcname}
%{py_platsitedir}/%{srcname}-%{version}-py%{py_ver}.egg-info
%doc %{py_platsitedir}/docs/tutorial

%files -n python2-%{srcname}
%{_bindir}/dul-receive-pack2
%{_bindir}/dul-upload-pack2
%{_bindir}/dulwich2
%{py2_platsitedir}/%{srcname}
%{py2_platsitedir}/%{srcname}-%{version}-py%{py2_ver}.egg-info
%doc %{py2_platsitedir}/docs/tutorial
