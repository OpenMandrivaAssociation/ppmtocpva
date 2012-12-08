Summary:	Converts PPM files to the format used by the Citizen Printiva series printers
Name:		ppmtocpva
Version:	1.0
Release:	%mkrel 13
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


%changelog
* Thu May 05 2011 Oden Eriksson <oeriksson@mandriva.com> 1.0-13mdv2011.0
+ Revision: 667817
- mass rebuild

* Fri Dec 03 2010 Oden Eriksson <oeriksson@mandriva.com> 1.0-12mdv2011.0
+ Revision: 607201
- rebuild

* Sat Jan 16 2010 Jérôme Brenier <incubusss@mandriva.org> 1.0-11mdv2010.1
+ Revision: 491945
- fix netpbm includes

* Thu Sep 03 2009 Christophe Fergeau <cfergeau@mandriva.com> 1.0-10mdv2010.0
+ Revision: 426776
- rebuild

* Thu Dec 25 2008 Oden Eriksson <oeriksson@mandriva.com> 1.0-9mdv2009.1
+ Revision: 319082
- use %%ldflags (P2)

* Sat Jul 12 2008 Oden Eriksson <oeriksson@mandriva.com> 1.0-8mdv2009.0
+ Revision: 234062
- rebuild
- rebuild

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

* Tue Mar 04 2008 Oden Eriksson <oeriksson@mandriva.com> 1.0-5mdv2008.1
+ Revision: 179257
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Thu Aug 30 2007 Oden Eriksson <oeriksson@mandriva.com> 1.0-4mdv2008.0
+ Revision: 75356
- fix deps (pixel)

* Thu Aug 16 2007 Oden Eriksson <oeriksson@mandriva.com> 1.0-3mdv2008.0
+ Revision: 64175
- use the new System/Printing RPM GROUP

* Tue Aug 14 2007 Thierry Vignaud <tv@mandriva.org> 1.0-2mdv2008.0
+ Revision: 63107
- fix description

* Tue Aug 14 2007 Oden Eriksson <oeriksson@mandriva.com> 1.0-1mdv2008.0
+ Revision: 63076
- Import ppmtocpva



* Tue Aug 14 2007 Oden Eriksson <oeriksson@mandriva.com> 1.0-1mdv2008.0
- initial Mandriva package
