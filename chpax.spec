Summary:	Manage PaX flags for ELF and a.out binaries
Summary(pl):	Zarz±dca znaczników PaX dla binarek ELF oraz a.out
Name:		chpax
Version:	0.20020901
Release:	3
License:	Public Domain
Group:		Applications/System
Source0:	http://pageexec.virtualave.net/%{name}.c
# Source0-md5:	c2d99ffcecb5cb61f4dd9a50d8d5c41a
Source1:	http://www.openwall.com/linux/linux-2.2.21-ow2.tar.gz
# Source1-md5:	f84249514f5ae1f7c445955725738174
URL:		http://pageexec.virtualave.net/
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
%setup -q -T -c -a 1
install %{SOURCE0} .
cp `find -name chstk.c` .

%build
%{__cc} %{rpmcflags} %{rpmldflags} -o chpax chpax.c
%{__cc} %{rpmcflags} %{rpmldflags} -o chstk chstk.c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sbindir}

install chpax chstk $RPM_BUILD_ROOT%{_sbindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_sbindir}/*
