Summary:	The GNU Scientific Library for numerical analysis
Summary(es):	Biblioteca científica del GNU
Summary(pl):	GNU Scientific Library do analizy numerycznej
Summary(pt_BR):	Biblioteca científica GNU
Name:		gsl
Version:	1.1.1
Release:	2
Epoch:		1
License:	GPL
Group:		Libraries
Source0:	ftp://sources.redhat.com/pub/gsl/%{name}-%{version}.tar.gz
Patch0:		%{name}-info.patch
URL:		http://sourceware.cygnus.com/gsl/
BuildRequires:	libtool
BuildRequires:	autoconf
BuildRequires:	automake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	libgsl0

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

%description -l es
Esta es la biblioteca científica del GNU. Ofrece acceso a funciones
para manejar muchos problemas que aparecen en computación científica.

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

%description -l pt_BR
Esta é a biblioteca científica do projeto GNU. Fornece acesso a
funções para tratar muitos problemas que surgem em computação
científica.

%package devel
Summary:	Header files for developing programs using gsl
Summary(pl):	Pliki nag³ówkowe i dokumentacja do bibliotek gsl
Summary(pt_BR):	Ferramentas de desenvolvimento para a gsl
Group:		Development/Libraries
Requires:	%{name} = %{version}
Obsoletes:	libgsl0-devel

%description devel
Header files for developing programs using gsl.

%description devel -l pl
Pliki nag³ówkowe i dokumentacja do bibliotek gsl.

%description devel -l pt_BR
Arquivos de inclusão, bibliotecas e documentação necessário para
desenvolver aplicativos que utilizam a biblioteca gsl.

%package static
Summary:	Static gsl librariries
Summary(pl):	Biblioteki statyczne gsl
Summary(pt_BR):	Bibliotecas estáticas para desenvolvimento com gsl
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
Static gsl librariries.

%description static -l pl
Biblioteki statyczne gsl.

%description static -l pt_BR
Bibliotecas estáticas para desenvolvimento com gsl.

%package progs
Summary:	gsl utility programs
Summary(pl):	Narzêdzia dla gsl
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description progs
gsl utility programs.

%description progs -l pl
Narzêdzia dla gsl.

%prep
%setup -q 
%patch0 -p1

%build
rm -f missing
%{__libtoolize}
aclocal
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	m4datadir=%{_aclocaldir}

gzip -9nf AUTHORS ChangeLog NEWS README KNOWN-PROBLEMS THANKS TODO

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%post devel
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%postun devel
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

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
%{_libdir}/pkgconfig/*
%{_includedir}/gsl
%{_infodir}/gsl*
%{_mandir}/man1/gsl-config.1*
%{_mandir}/man3/*

%files progs
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/gsl-histogram
%attr(755,root,root) %{_bindir}/gsl-randist

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
