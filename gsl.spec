Summary: The GNU Scientific Library for numerical analysis.
Name: gsl
Version: 0.3f
Release: 2
URL: http://www.gnu.org
Source: ftp://nis-ftp.lanl.gov/pub/users/rosalia/gsl-%{version}.tar.gz
Patch: gsl-0.3b-errlib.patch
Patch1: gsl-glibc21.patch
Patch2: gsl-foo.patch
Copyright: GPL 
Group: System Environment/Libraries
BuildRoot: /var/tmp/gsl-root

%description
The gsl package includes the GNU Scientific Library (GSL).  The GSL is a
collection of routines for numerical analysis, written in C.  The GSL is
in alpha development.  It now includes a random number suite, an FFT
package, simulated annealing and root finding.  In the future, it will
include numerical and Monte Carlo integration and special functions.
Linking against the GSL allows programs to access functions which can
handle many of the problems encountered in scientific computing.

Install the gsl package if you need a library for high-level scientific
numerical analysis.

%prep
%setup
#%patch -p1
%patch1 -p1 -b .glibc21
%patch2 -p1 -b .foo

%build
./configure --prefix=${RPM_BUILD_ROOT}/usr
touch doc/gsl-ref.info
make CFLAGS="${RPM_OPT_FLAGS}"

%install
mkdir -p ${RPM_BUILD_ROOT}/usr/lib ${RPM_BUILD_ROOT}/usr/info \
         ${RPM_BUILD_ROOT}/usr/include

make CFLAGS="${RPM_OPT_FLAGS}" install
#cd ${RPM_BUILD_ROOT}/usr/lib
#strip *

%post
/sbin/ldconfig

# change back when shared libs working
#%post devel
/sbin/install-info /usr/info/gsl-ref.info.gz /usr/info/dir > /dev/null 2>&1
exit 0

%postun
/sbin/ldconfig

# change back to devel when shared libs working
#%preun devel
%preun 
if [ "$1" = 0 ]; then
    /sbin/install-info --delete /usr/info/gsl-ref.info.gz /usr/info/dir
fi

%clean
rm -rf $RPM_BUILD_ROOT

%files
#/usr/lib/lib*.so

#%files devel
%doc AUTHORS COPYING ChangeLog INSTALL NEWS README
#/usr/lib/libgmp.so
/usr/lib/lib*.a
/usr/include/*
/usr/info/gsl-ref.info*
