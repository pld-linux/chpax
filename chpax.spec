Summary:	Manage PaX flags for ELF and a.out binaries
Summary(pl.UTF-8):   Zarządca znaczników PaX dla binarek ELF oraz a.out
Name:		chpax
Version:	0.7
Release:	1
Epoch:		1
License:	Public Domain
Group:		Applications/System
Source0:	http://pax.grsecurity.net/%{name}-%{version}.tar.gz
# Source0-md5:	6a0aac11abf1a40c50704c7f93bc8953
URL:		http://pax.grsecurity.net/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sbindir	/sbin

%description
This program manages various PaX related flags for ELF and a.out
binaries. The flags only have effect when running the patched Linux
kernel.

%description -l pl.UTF-8
Program zarządzający flagami związanymi z PaX w binarkach ELF oraz
a.out. Znaczniki te są brane pod uwagę tylko w momencie używania
odpowiednio załatanego jądra systemu.

%prep
%setup -q

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sbindir}

install chpax $RPM_BUILD_ROOT%{_sbindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_sbindir}/*
