%define oname flup

%define name python-%oname
%define version 1.0
%define release 1

Summary:  Python module related to FastCGI and WSGI
Name: %{name}
Version: %{version}
Release: %mkrel %{release}

Source0: http://www.saddi.com/software/%oname/dist/%oname-%version.tar.gz 
License: BSD
Group: Development/Python
BuildArch: noarch
Url: http://trac.saddi.com/flup
BuildRequires: python-devel
BuildRequires: python-setuptools

%description
This Python package is a random collection of WSGI and FCGI modules.

%prep
%setup -q -n %oname-%version 
perl -pi -e 's/^(use_setuptools)/#$1/' setup.py

%build
python setup.py build

%install
rm -rf %buildroot
python setup.py install --root=$RPM_BUILD_ROOT 

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc ChangeLog
%py_sitedir/%{oname}
%py_sitedir/*.egg-info/

