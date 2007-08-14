Summary:	Converts PPM files to the format used by the Citizen Printiva series printers
Name:		ppmtocpva
Version:	1.0
Release:	%mkrel 1
License:	GPL
Group:		System/Kernel and hardware
URL:		http://www.stevens-bradfield.com/ppmtomd/
Source0:	http://www.dcs.ed.ac.uk/home/jcb/ppmtocpva-%{version}.tar.bz2
Patch0:		ppmtocpva-1.0-includes.patch
Patch1:		ppmtocpva-1.0-netpbm.patch
BuildRequires:	netpbm-devel
Conflicts:	printer-utils-2006 printer-utils-2007
Conflicts:	printer-filters-2006 printer-filters-2007
BuildRoot:	%{_tmppath}/%{name}-%{version}-root

%description
This program converts PPM files to the format used by the Citizen Printiva
series printers -- and therefore also, I presume, the Alps MD series, at least
in the earlier versions.

I don't have an Alps printer, so I can make no guarantees about what works. The
Printiva 600C corresponds to a very early Alps model; there may be changes in
later models that break things. In particular, I would be interested to know
whether the output from this program works with the Alps MD-5000 (sold in Europe
as the Oki DP-5000). (It appears that Alps have now (2001) sold their printer
business to OKI.)

This program is NOT written for robust end-user use! It is merely the result of
many weeks' experimentation; it includes numerous experimental features that
turned out to be useless, and the options are designed to give maximum control,
not maximum ease of use.

I would like to acknowledge with gratitude the help of Citizen, who provided me
with the programmers' guide for the Printer Control Language (which they call
RGL, for Raster Graphics Language).

%prep

%setup -q
%patch0 -p1
%patch1 -p1

# fix attribs
chmod 644 *

%build

%make CFLAGS="%{optflags}"

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
