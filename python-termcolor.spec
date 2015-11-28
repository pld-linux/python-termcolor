%define		module	termcolor
Summary:	ANSII Color formatting for output in terminal
Name:		python-%{module}
Version:	1.1.0
Release:	1
License:	GPL v3
Group:		Development/Languages/Python
Source0:	http://pypi.python.org/packages/source/t/termcolor/termcolor-%{version}.tar.gz
# Source0-md5:	043e89644f8909d462fbbfa511c768df
URL:		http://pypi.python.org/pypi/termcolor
BuildRequires:	python-distribute
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
Requires:	python-modules
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ANSII Color formatting for output in terminal.

%prep
%setup -q -n %{module}-%{version}

%build
%py_build

%install
rm -rf $RPM_BUILD_ROOT
%py_install

%py_ocomp $RPM_BUILD_ROOT%{py_sitescriptdir}
%py_comp $RPM_BUILD_ROOT%{py_sitescriptdir}
%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES.rst README.rst
%{py_sitescriptdir}/*.py[co]
%if "%{py_ver}" > "2.4"
%{py_sitescriptdir}/termcolor-*.egg-info
%endif
