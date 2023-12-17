Name:           libfprint-tod-goodix
Version:        0.0.9
Release:        1%{?dist}
Summary:        Goodix driver module for fingerprint reader to support 27c6:550a.

License:        GPL-3.0
Source0:        libfprint-tod-goodix-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:       libfprint-tod

%global debug_package %{nil}

%description
Goodix driver module for fingerprint reader to support 27c6:550a.


%prep
%setup -q -n libfprint-tod-goodix-%{version}

%build
# empty


%install
install -p -d -m 0755 %{buildroot}/%{_libdir}/libfprint-2/tod-1/
install -m 0644 usr/lib/x86_64-linux-gnu/libfprint-2/tod-1/libfprint-tod-goodix-550a-%{version}.so %{buildroot}/%{_libdir}/libfprint-2/tod-1/


%files
%defattr(-,root,root,-)
%{_libdir}/libfprint-2/tod-1/libfprint-tod-goodix-550a-%{version}.so

%changelog
* Sun Dec  17 2023 Piyush Singh <singhpiyush998@gmail.com>
- Goodix driver version 0.0.9
