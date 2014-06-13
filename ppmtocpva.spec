Summary:	Converts PPM files to the format used by the Citizen Printiva series printers
Name:		ppmtocpva
Version:	1.0
Release:	18
License:	GPLv2
Group:		System/Printing
Url:		http://www.stevens-bradfield.com/ppmtomd/
Source0:	http://www.dcs.ed.ac.uk/home/jcb/ppmtocpva-%{version}.tar.bz2
Patch0:		ppmtocpva-1.0-includes.patch
Patch1:		ppmtocpva-1.0-netpbm.patch
Patch2:		ppmtocpva-1.0-LDFLAGS.diff
BuildRequires:	netpbm-devel

%description
This program converts PPM files to the format used by the Citizen Printiva
series printers and some printers of the Alps MD series.

%prep
%setup -q
%apply_patches

# fix attribs
chmod 644 *

%build
%make CFLAGS="%{optflags}" LDFLAGS="%{ldflags}"

%install
install -d %{buildroot}%{_bindir}
install -m0755 ppmtocpva %{buildroot}%{_bindir}/
install -m0755 cpva-colour %{buildroot}%{_bindir}/

%files
%doc README
%attr(0755,root,root) %{_bindir}/*

