Summary:	The GNU Scientific Library for numerical analysis.
Name:		gsl
Version:	0.5
Release:	1
URL:		http://www.gnu.org
#Source:	ftp://nis-ftp.lanl.gov/pub/users/rosalia/%{name}-%{version}.tar.gz
Source:		ftp://sourceware.cygnus.com/pub/gsl/%{name}-%{version}.tar.gz
Source2:	ftp://sourceware.cygnus.com/pub/gsl/%{name}-ref.ps.gz
#Patch:		gsl-0.3b-errlib.patch
#Patch1:		gsl-glibc21.patch
#Patch2:		gsl-foo.patch
License:	GPL
Group:		System Environment/Libraries
Group(pl):	Biblioteki
Prereq:		/usr/sbin/fix-info-dir
BuildRoot:	/tmp/%{name}-%{version}-root

%define	_prefix	/usr

%description
The gsl package includes the GNU Scientific Library (GSL).  The GSL is a 
collection of routines for numerical analysis, written in C.  The GSL is in 
alpha development.  It now includes a random number suite, an FFT package, 
simulated annealing and root finding.  In the future, it will include 
numerical and Monte Carlo integration and special functions. Linking 
against the GSL allows programs to access functions which can handle many 
of the problems encountered in scientific computing.  Install the gsl 
package if you need a library for high-level scientific numerical analysis. 
  

%prep
%setup -q
#%patch -p1
#%patch1 -p1 -b .glibc21
#%patch2 -p1 -b .foo

%build
./configure --prefix=%{_prefix}
touch doc/gsl-ref.info
make CFLAGS="${RPM_OPT_FLAGS}"

%install
rm -rf $RPM_BUILD_ROOT

install -d ${RPM_BUILD_ROOT}{%{_libdir},%{_infodir},%{_includedir}}
install -d $RPM_BUILD_ROOT%{_docdir}/%name-%version

make DESTDIR=$RPM_BUILD_ROOT CFLAGS="${RPM_OPT_FLAGS}"	\
    infodir=%{_datadir}/info install

strip $RPM_BUILD_ROOT%{_bindir}/{gsl-h*,gsl-r*}

install %{SOURCE2} $RPM_BUILD_DIR/%name-%version

gzip -9 {AUTHORS,ChangeLog,NEWS,README,KNOWN-PROBLEMS,THANKS,TODO}
gzip -9 $RPM_BUILD_ROOT%{_infodir}/*.inf*


%post
/sbin/ldconfig

/usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%postun
/sbin/ldconfig

/usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {AUTHORS,ChangeLog,KNOWN-PROBLEMS,README,NEWS,THANKS,gsl-ref.ps}.gz 
%attr(755,root,root) %{_bindir}/gsl-*
%attr(644,root,root) %{_includedir}/gsl/*.h
%attr(644,root,root) %{_libdir}/gsl/libgsl*.a
%attr(644,root,root) %{_libdir}/gsl/libutils.a
%attr(644,root,root) %{_infodir}/gsl*.gz
