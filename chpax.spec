Summary:	Manage PaX flags for ELF and a.out binaries
Summary(pl):	Zarz±dca znaczników PaX dla binarek ELF oraz a.out
Name:		chpax
Version:	0.6
Release:	1
License:	Public Domain
Group:		Applications/System
Source0:	http://pax.grsecurity.net/%{name}-%{version}.tar.gz
# Source0-md5:	376ee0327bb6060a03052cdc71bb371f
Patch0:		%{name}-elf.patch
URL:		http://pax.grsecurity.net/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sbindir	/sbin

%description
This program manages various PaX related flags for ELF and a.out
binaries. The flags only have effect when running the patched Linux
kernel.

%description -l pl
Program zarz±dzaj±cy flagami zwi±zanymi z PaX w binarkach ELF oraz
a.out. Znaczniki te s± brane pod uwagê tylko w momencie u¿ywania
odpowiednio za³atanego j±dra systemu.

%prep
%setup -q
%patch0 -p2

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
