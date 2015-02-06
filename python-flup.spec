%define oname flup

%define name python-%oname
%define version 1.0.2
%define release 3

Summary:  Python module related to FastCGI and WSGI
Name: %{name}
Version: %{version}
Release: %mkrel %{release}

Source0: http://www.saddi.com/software/%oname/dist/%oname-%version.tar.gz 
License: BSD
Group: Development/Python
BuildRoot: %{_tmppath}/%{name}-buildroot
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



%changelog
* Thu Nov 11 2010 Eugeni Dodonov <eugeni@mandriva.com> 1.0.2-2mdv2011.0
+ Revision: 596286
- Rebuild for new python.

* Tue Jun 09 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.0.2-1mdv2010.0
+ Revision: 384249
- update to new version 1.0.2

* Sat Jan 03 2009 Funda Wang <fwang@mandriva.org> 1.0-2mdv2009.1
+ Revision: 323712
- rebuild

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 1.0-1mdv2009.0
+ Revision: 136447
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sat Dec 01 2007 Michael Scherer <misc@mandriva.org> 1.0-1mdv2008.1
+ Revision: 114349
- import python-flup


