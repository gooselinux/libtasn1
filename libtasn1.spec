%{!?release_func:%global release_func() %1%{?dist}}

Summary:	The ASN.1 library used in GNUTLS
Name:		libtasn1
Version:	2.3
Release: 	%release_func 3

# The libtasn1 library is LGPLv2+, utilities are GPLv3+
License: 	GPLv3+ and LGPLv2+
Group:		System Environment/Libraries
URL:		http://www.gnu.org/software/libtasn1/
Source0:	http://ftp.gnu.org/gnu/libtasn1/%name-%version.tar.gz
Source1:	http://ftp.gnu.org/gnu/libtasn1/%name-%version.tar.gz.sig
Patch1:		libtasn1-2.4-rpath.patch
BuildRoot:	%_tmppath/%name-%version-%release-buildroot
BuildRequires:	bison, pkgconfig
%ifarch %ix86 x86_64 ppc ppc64
BuildRequires:	valgrind
%endif


%package devel
Summary:	Files for development of applications which will use libtasn1
Group:		Development/Libraries
Requires:	%name = %version-%release
Requires:	pkgconfig
Requires(post):		/sbin/install-info
Requires(postun):	/sbin/install-info


%package tools
Summary:	Some ASN.1 tools
Group:		Applications/Text
License:	GPLv3+
Requires:	%name = %version-%release


%description
This is the ASN.1 library used in GNUTLS.  More up to date information can
be found at http://www.gnu.org/software/gnutls and http://www.gnutls.org

%description devel
This is the ASN.1 library used in GNUTLS.  More up to date information can
be found at http://www.gnu.org/software/gnutls and http://www.gnutls.org

This package contains files for development of applications which will
use libtasn1.


%description tools
This is the ASN.1 library used in GNUTLS.  More up to date information can
be found at http://www.gnu.org/software/gnutls and http://www.gnutls.org

This package contains tools using the libtasn library.


%prep
%setup -q

%patch1 -p1 -b .rpath

%build
%configure --disable-static

make %{?_smp_mflags}


%install
rm -rf "$RPM_BUILD_ROOT"

make DESTDIR="$RPM_BUILD_ROOT" install

rm -f $RPM_BUILD_ROOT{%_libdir/*.la,%_infodir/dir}


%check
make check


%clean
rm -rf "$RPM_BUILD_ROOT"


%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig


%post devel
test -f %_infodir/%name.info.gz && \
	/sbin/install-info --info-dir=%_infodir %_infodir/%name.info || :

%preun devel
test "$1" = 0 -a -f %_infodir/%name.info.gz && \
	/sbin/install-info --info-dir=%_infodir --delete %_infodir/%name.info || :

%files
%defattr(-,root,root,-)
%doc doc/TODO doc/*.pdf
%doc AUTHORS COPYING* ChangeLog NEWS README THANKS
%_libdir/*.so.*

%files tools
%defattr(-,root,root,-)
%_bindir/asn1*
%_mandir/man1/asn1*

%files devel
%defattr(-,root,root,-)
%_libdir/*.so
%_libdir/pkgconfig/*.pc
%_includedir/*
%_infodir/*.info.*
%_mandir/man3/*asn1*


%changelog
* Thu Jan 28 2010 Tomas Mraz <tmraz@redhat.com> - 2.3-3
- drop superfluous rpath

* Mon Jan 11 2010 Tomas Mraz <tmraz@redhat.com> - 2.3-2
- no longer ignore make check result on ppc64

* Mon Nov 30 2009 Dennis Gregorovic <dgregor@redhat.com> - 2.3-1.1
- Rebuilt for RHEL 6

* Tue Aug 11 2009 Tomas Mraz <tmraz@redhat.com> - 2.3-1
- updated to new upstream version
- fix warnings when installed with --excludedocs (#515950)

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri May 29 2009 Tomas Mraz <tmraz@redhat.com> - 2.2-1
- updated to new upstream version
- SMP build should work now
- drop fix for spurious rpath - no longer necessary

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Jan 27 2009 Enrico Scholz <enrico.scholz@informatik.tu-chemnitz.de> - 1.8-1
- updated to 1.8
- updated URLs
- disabled SMP builds for now

* Fri Dec 12 2008 Caolán McNamara <caolanm@redhat.com> - 1.7-2
- rebuild to get provides pkgconfig(libtasn1)

* Fri Nov 21 2008 Tomas Mraz <tmraz@redhat.com> - 1.7-1
- updated to new upstream version

* Tue Sep 30 2008 Tomas Mraz <tmraz@redhat.com> - 1.5-1
- updated to new upstream version
- fix license tag
- fix spurious rpath in the tool binaries

* Thu Aug  7 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.4-2
- fix license tag

* Thu Jun  5 2008 Tomas Mraz <tmraz@redhat.com> - 1.4-1
- updated to new upstream version

* Wed Feb 13 2008 Enrico Scholz <enrico.scholz@informatik.tu-chemnitz.de> - 1.3-1
- updated to 1.3 (#426488, #431334)
- use wrapper around libtasn1-config which should make it multilib
  safe (#342411); this implies an untagged 'Requires: pkgconfig' for
  -devel now
- conditionalized BR of valgrind (#401041)

* Mon Sep  3 2007 Enrico Scholz <enrico.scholz@informatik.tu-chemnitz.de> - 1.1-1
- updated to 1.1
- workaround 'make check' errors on ppc64

* Thu Jun 14 2007 Enrico Scholz <enrico.scholz@informatik.tu-chemnitz.de> - 0.3.10-1
- updated to 0.3.10

* Fri Mar  2 2007 Enrico Scholz <enrico.scholz@informatik.tu-chemnitz.de> - 0.3.9-1
- updated to 0.3.9

* Sat Feb  3 2007 Enrico Scholz <enrico.scholz@informatik.tu-chemnitz.de> - 0.3.8-1
- updated to 0.3.8

* Sun Nov  5 2006 Enrico Scholz <enrico.scholz@informatik.tu-chemnitz.de> - 0.3.6-1
- updated to 0.3.6
- BR valgrind

* Fri Sep 15 2006 Enrico Scholz <enrico.scholz@informatik.tu-chemnitz.de> - 0.3.5-1
- updated to 0.3.5

* Sat Jun  3 2006 Enrico Scholz <enrico.scholz@informatik.tu-chemnitz.de> - 0.3.4-1
- updated to 0.3.4

* Sun Mar 26 2006 Enrico Scholz <enrico.scholz@informatik.tu-chemnitz.de> - 0.3.2-1
- updated to 0.3.2
- added -tools subpackage

* Wed Mar  8 2006 Enrico Scholz <enrico.scholz@informatik.tu-chemnitz.de> - 0.3.1-1
- updated to 0.3.1

* Mon Mar  6 2006 Enrico Scholz <enrico.scholz@informatik.tu-chemnitz.de> - 0.3.0-1
- updated to 0.3.0
- removed unneeded curlies
- created -devel subpackage

* Sun May 22 2005 Jeremy Katz <katzj@redhat.com> - 0.2.6-3
- rebuild on all arches

* Fri Apr  7 2005 Michael Schwendt <mschwendt[AT]users.sf.net>
- rebuilt

* Tue Nov 18 2003 Enrico Scholz <enrico.scholz@informatik.tu-chemnitz.de> - 0:0.2.6-0.fdr.1
- updated to 0.2.6

* Mon Aug  4 2003 Enrico Scholz <enrico.scholz@informatik.tu-chemnitz.de> 0:0.2.5-0.fdr.1
- updated to 0.2.5
- changed license to LGPL
- rearranged %%check to reflect execution order
- minor cosmetical changes

* Tue Jun 10 2003 Enrico Scholz <enrico.scholz@informatik.tu-chemnitz.de> 0:0.2.4-0.fdr.1
- Initial build.
