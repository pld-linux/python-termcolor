#
# Conditional build:
%bcond_without	python2	# CPython 2.x module
%bcond_without	python3	# CPython 3.x module

Summary:	ANSI Color formatting for output in terminal
Summary(pl.UTF-8):	Kolorowe formatowanie wyjścia na terminalu przy użyciu sekwencji ANSI
Name:		python-termcolor
Version:	1.1.0
Release:	6
License:	MIT
Group:		Development/Languages/Python
Source0:	https://files.pythonhosted.org/packages/source/t/termcolor/termcolor-%{version}.tar.gz
# Source0-md5:	043e89644f8909d462fbbfa511c768df
URL:		https://pypi.org/project/termcolor/
%{?with_python2:BuildRequires:	python-modules >= 1:2.6}
%{?with_python3:BuildRequires:	python3-modules >= 1:3.2}
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python-modules >= 1:2.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ANSI Color formatting for output in terminal.

%description -l pl.UTF-8
Kolorowe formatowanie wyjścia na terminalu przy użyciu sekwencji ANSI.

%package -n python3-termcolor
Summary:	ANSI Color formatting for output in terminal
Summary(pl.UTF-8):	Kolorowe formatowanie wyjścia na terminalu przy użyciu sekwencji ANSI
Group:		Development/Languages/Python
Requires:	python3-modules >= 1:3.2

%description -n python3-termcolor
ANSI Color formatting for output in terminal.

%description -n python3-termcolor -l pl.UTF-8
Kolorowe formatowanie wyjścia na terminalu przy użyciu sekwencji ANSI.

%prep
%setup -q -n termcolor-%{version}

%build
%if %{with python2}
%py_build
%endif

%if %{with python3}
%py3_build
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc CHANGES.rst COPYING.txt README.rst
%{py_sitescriptdir}/termcolor.py[co]
%{py_sitescriptdir}/termcolor-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-termcolor
%defattr(644,root,root,755)
%doc CHANGES.rst COPYING.txt README.rst
%{py3_sitescriptdir}/termcolor.py
%{py3_sitescriptdir}/__pycache__/termcolor.cpython-*.py[co]
%{py3_sitescriptdir}/termcolor-%{version}-py*.egg-info
%endif
