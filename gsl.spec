Summary:	The GNU Scientific Library for numerical analysis
Name:		gsl
Version:	0.7
Release:	3
License:	GPL
Group:		Libraries
Group(de):	Libraries
Group(fr):	Librairies
Group(pl):	Biblioteki
Source0:	ftp://sourceware.cygnus.com/pub/gsl/%{name}-%{version}.tar.gz
Patch0:		%{name}-info.patch
URL:		http://www.gnu.org/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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

%description -l pl
Pakiet gsl zawiera bibliotekê funkcji przydatnych w pracy naukowej
dostêpnych na licencji (GNU). GSL jest zbiorem funkcji napisanych
wjezyku C, przeznaczonych do analizy numerycznej. Biblioteka jest
jeszcze w bardzo wczesnym stadium tworzenia. W tej chwili zawiera
generatory liczb losowych, FFT, znajdowanie miejsc zerowych. W
przysz³o¶ci, bêdzie zawieraæ ca³kowanie metod± Monte Carlo oraz
funkcje specjalne. Linkowanie z GSL pozwala Twoim programom na dostep
do funkcji, które moga byæ u¿yteczne w wielu problemach pojawiajacych
sie w obliczeniach naukowych. Zainstaluj gsl jesli potrzebujesz
biblioteki do obliczeñ numerycznych.

%package devel
Summary:	Header files for developing programs using gsl
Summary(pl):	Pliki nag³ówkowe i dokumentacja do bibliotek gsl
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Requires:	%{name} = %{version}

%description devel
Header files for developing programs using gsl.

%description -l pl devel
Pliki nag³ówkowe i dokumentacja do bibliotek gsl.

%package static
Summary:	Static gsl librariries
Summary(pl):	Biblioteki statyczne gsl
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Requires:	%{name}-devel = %{version}

%description static
Static gsl librariries.

%description static -l pl
Biblioteki statyczne gsl.

%package progs
Summary:	gsl utility programs
Summary(pl):	Narzêdzia dla gsl
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Requires:	%{name} = %{version}

%description progs
gsl utility programs.

%description -l pl progs
Narzêdzia dla gsl.

%prep
%setup -q
%patch -p1

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	m4datadir=%{_aclocaldir}

gzip -9nf AUTHORS ChangeLog NEWS README KNOWN-PROBLEMS THANKS TODO

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%post devel
%fix_info_dir

%postun devel
%fix_info_dir

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/gsl-config
%attr(755,root,root) %{_libdir}/lib*.so
%attr(755,root,root) %{_libdir}/lib*.la
%{_aclocaldir}/gsl.m4
%{_includedir}/gsl
%{_infodir}/gsl*

%files progs
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/gsl-histogram
%attr(755,root,root) %{_bindir}/gsl-randist

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
