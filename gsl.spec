Summary:	The GNU Scientific Library for numerical analysis
Name:		gsl
Version:	0.5
Release:	1
License:	GPL
Group:		Libraries
Group(pl):	Biblioteki
Source0:	ftp://nis-ftp.lanl.gov/pub/users/rosalia/%{name}-%{version}.tar.gz
Source0:	ftp://sourceware.cygnus.com/pub/gsl/%{name}-%{version}.tar.gz
Source2:	ftp://sourceware.cygnus.com/pub/gsl/%{name}-ref.ps.gz
Patch0:		gsl-0.3b-errlib.patch
#Patch1:	gsl-glibc21.patch
#Patch2:	gsl-foo.patch
URL:		http://www.gnu.org/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define	_prefix	/usr

%description
The gsl package includes the GNU Scientific Library (GSL). The GSL is
a collection of routines for numerical analysis, written in C. The GSL
is in alpha development. It now includes a random number suite, an FFT
package, simulated annealing and root finding. In the future, it will
include numerical and Monte Carlo integration and special functions.
Linking against the GSL allows programs to access functions which can
handle many of the problems encountered in scientific computing.
Install the gsl package if you need a library for high-level
scientific numerical analysis.

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

install -d ${RPM_BUILD_ROOT}{%{_libdir},%{_infodir},%{_includedir}} \
	$RPM_BUILD_ROOT%{_docdir}/%name-%version

make install \
	DESTDIR=$RPM_BUILD_ROOT \
	infodir=%{_infodir}

strip $RPM_BUILD_ROOT%{_bindir}/{gsl-h*,gsl-r*}

install %{SOURCE2} $RPM_BUILD_DIR/%name-%version

gzip -9nf {AUTHORS,ChangeLog,NEWS,README,KNOWN-PROBLEMS,THANKS,TODO} \
	$RPM_BUILD_ROOT%{_infodir}/*.inf*

%post
/sbin/ldconfig
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%postun
/sbin/ldconfig
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {AUTHORS,ChangeLog,KNOWN-PROBLEMS,README,NEWS,THANKS,gsl-ref.ps}.gz 
%attr(755,root,root) %{_bindir}/gsl-*
%{_includedir}/gsl/*.h
%{_libdir}/gsl/libgsl*.a
%{_libdir}/gsl/libutils.a
%{_infodir}/gsl*.gz
