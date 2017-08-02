#
# Conditional build:
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

Summary:	A library to handle automated deprecations
Name:		python-deprecation
Version:	1.0.1
Release:	1
License:	Apache
Group:		Libraries/Python
Source0:	https://pypi.python.org/packages/8c/e3/e5c66eba8fa2fd567065fa70ada98b990f449f74fb812b408fa7aafe82c9/deprecation-%{version}.tar.gz
# Source0-md5:	d8a318c66d442dc4b900e070267ed9aa
URL:		https://pypi.python.org/pypi/deprecation
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with python2}
BuildRequires:	python-setuptools
%endif
%if %{with python3}
BuildRequires:	python3-setuptools
%endif
Requires:	python-modules
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The deprecation library provides a deprecated decorator and a
fail_if_not_removed decorator for your tests. Together, the two enable
the automation of several things:

- The docstring of a deprecated method gets the deprecation details
  appended to the end of it. If you generate your API docs direct from
  your source, you don't need to worry about writing your own
  notification. You also don't need to worry about forgetting to write
  it. It's done for you.
- Rather than having code live on forever because you only deprecated
  it but never actually moved on from it, you can have your tests tell
  you when it's time to remove the code. The @deprecated decorator can
  be told when it's time to entirely remove the code, which causes
  @fail_if_not_removed to raise an AssertionError, causing either your
  unittest or py.test tests to fail.

%package -n python3-deprecation
Summary:	A library to handle automated deprecations
Group:		Libraries/Python
Requires:	python3-modules

%description -n python3-deprecation
The deprecation library provides a deprecated decorator and a
fail_if_not_removed decorator for your tests. Together, the two enable
the automation of several things:

- The docstring of a deprecated method gets the deprecation details
  appended to the end of it. If you generate your API docs direct from
  your source, you don't need to worry about writing your own
  notification. You also don't need to worry about forgetting to write
  it. It's done for you.
- Rather than having code live on forever because you only deprecated
  it but never actually moved on from it, you can have your tests tell
  you when it's time to remove the code. The @deprecated decorator can
  be told when it's time to entirely remove the code, which causes
  @fail_if_not_removed to raise an AssertionError, causing either your
  unittest or py.test tests to fail.

%prep
%setup -q -n deprecation-%{version}

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
%doc README.rst
%{py_sitescriptdir}/deprecation.py[co]
%{py_sitescriptdir}/deprecation-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-deprecation
%defattr(644,root,root,755)
%doc README.rst
%{py3_sitescriptdir}/deprecation.py
%{py3_sitescriptdir}/__pycache__/*
%{py3_sitescriptdir}/deprecation-%{version}-py*.egg-info
%endif
