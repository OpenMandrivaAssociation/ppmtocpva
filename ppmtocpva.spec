Summary:	Converts PPM files to the format used by the Citizen Printiva series printers
Name:		ppmtocpva
Version:	1.0
Release:	%mkrel 11
License:	GPL
Group:		System/Printing
URL:		http://www.stevens-bradfield.com/ppmtomd/
Source0:	http://www.dcs.ed.ac.uk/home/jcb/ppmtocpva-%{version}.tar.bz2
Patch0:		ppmtocpva-1.0-includes.patch
Patch1:		ppmtocpva-1.0-netpbm.patch
Patch2:		ppmtocpva-1.0-LDFLAGS.diff
BuildRequires:	netpbm-devel
Conflicts:	printer-utils = 2007
Conflicts:	printer-filters = 2007
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
This program converts PPM files to the format used by the Citizen Printiva
series printers and some printers of the Alps MD series.

%prep

%setup -q
%patch0 -p1 -b .includes
%patch1 -p1
%patch2 -p0

# fix attribs
chmod 644 *

%build

%make CFLAGS="%{optflags}" LDFLAGS="%{ldflags}"

%install
rm -rf %{buildroot}

install -d %{buildroot}%{_bindir}

install -m0755 ppmtocpva %{buildroot}%{_bindir}/
install -m0755 cpva-colour %{buildroot}%{_bindir}/

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README
%attr(0755,root,root) %{_bindir}/*
