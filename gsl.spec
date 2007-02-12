Summary:	The GNU Scientific Library for numerical analysis
Summary(es.UTF-8):   Biblioteca científica del GNU
Summary(pl.UTF-8):   GNU Scientific Library do analizy numerycznej
Summary(pt_BR.UTF-8):   Biblioteca científica GNU
Summary(ru.UTF-8):   Научная библиотека GNU для числового анализа
Summary(uk.UTF-8):   Наукова бібліотека GNU для числового аналізу
Name:		gsl
Version:	1.8
Release:	1
Epoch:		1
License:	GPL
Group:		Libraries
Source0:	ftp://sources.redhat.com/pub/gsl/%{name}-%{version}.tar.gz
# Source0-md5:	c60a5d193cc6b472496ff191744fc306
Patch0:		%{name}-info.patch
Patch1:		%{name}-link.patch
URL:		http://www.gnu.org/software/gsl/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	libtool >= 1:1.4.2-9
BuildRequires:	texinfo
Obsoletes:	libgsl0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The gsl package includes the GNU Scientific Library (GSL). The GSL is
a collection of routines for numerical analysis, written in C. The GSL
is in alpha development. It now includes a random number suite, an FFT
package, simulated annealing and root finding. In the future, it will
include numerical and Monte Carlo integration and special functions.
Linking against the GSL allows programs to access functions which can
handle many of the problems encountered in scientific computing.

%description -l es.UTF-8
Esta es la biblioteca científica del GNU. Ofrece acceso a funciones
para manejar muchos problemas que aparecen en computación científica.

%description -l pl.UTF-8
Pakiet gsl zawiera bibliotekę funkcji przydatnych w pracy naukowej
dostępnych na licencji (GNU). GSL jest zbiorem funkcji napisanych
w języku C, przeznaczonych do analizy numerycznej. Biblioteka jest
jeszcze w bardzo wczesnym stadium tworzenia. W tej chwili zawiera
generatory liczb losowych, FFT, znajdowanie miejsc zerowych. W
przyszłości, będzie zawierać całkowanie metodą Monte Carlo oraz
funkcje specjalne. Konsolidacja z GSL pozwala programom na dostęp do
funkcji, które mogą być przydatne w rozwiązywaniu wielu problemów
pojawiających się w obliczeniach naukowych.

%description -l pt_BR.UTF-8
Esta é a biblioteca científica do projeto GNU. Fornece acesso a
funções para tratar muitos problemas que surgem em computação
científica.

%description -l ru.UTF-8
Это научная библиотека GNU. Сборка с ней дает доступ к функциям,
решающим многие задачи, типичные для научных расчетов.

%description -l uk.UTF-8
Це наукова бібліотека GNU. Зборка з нею дає доступ до функцій, що
дозволяють розв'язати багато задач, типових для наукових розрахунків.

%package devel
Summary:	Header files for developing programs using gsl
Summary(pl.UTF-8):   Pliki nagłówkowe i dokumentacja do bibliotek gsl
Summary(pt_BR.UTF-8):   Ferramentas de desenvolvimento para a gsl
Summary(ru.UTF-8):   Файлы для разработки с научной библиотекой GNU (GSL)
Summary(uk.UTF-8):   Файли для розробки з науковою бібліотекою GNU (GSL)
Group:		Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	libgsl0-devel

%description devel
Header files for developing programs using gsl.

%description devel -l pl.UTF-8
Pliki nagłówkowe i dokumentacja do bibliotek gsl.

%description devel -l pt_BR.UTF-8
Arquivos de inclusão, bibliotecas e documentação necessário para
desenvolver aplicativos que utilizam a biblioteca gsl.

%description devel -l ru.UTF-8
Это библиотеки, хедеры и документация по использованию научной
библиотеки GNU в ваших программах.

%description devel -l uk.UTF-8
Це бібліотеки, хедери та документація по використанню наукової
бібліотеки GNU у ваших програмах.

%package static
Summary:	Static gsl librariries
Summary(pl.UTF-8):   Biblioteki statyczne gsl
Summary(pt_BR.UTF-8):   Bibliotecas estáticas para desenvolvimento com gsl
Summary(ru.UTF-8):   Статические библиотеки для разработки с научной библиотекой GNU (GSL)
Summary(uk.UTF-8):   Статичні бібліотеки для розробки з науковою бібліотекою GNU (GSL)
Group:		Development/Libraries
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}

%description static
Static gsl librariries.

%description static -l pl.UTF-8
Biblioteki statyczne gsl.

%description static -l pt_BR.UTF-8
Bibliotecas estáticas para desenvolvimento com gsl.

%description static -l ru.UTF-8
Это статическая библиотека для использования научной библиотеки GNU в
ваших программах.

%description static -l uk.UTF-8
Це статична бібліотека для використання наукової бібліотеки GNU у
ваших програмах.

%package progs
Summary:	gsl utility programs
Summary(pl.UTF-8):   Narzędzia dla gsl
Group:		Applications/Science
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description progs
gsl utility programs.

%description progs -l pl.UTF-8
Narzędzia dla gsl.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	m4datadir=%{_aclocaldir}

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
%doc AUTHORS ChangeLog NEWS README THANKS TODO
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/gsl-config
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/gsl
%{_aclocaldir}/gsl.m4
%{_pkgconfigdir}/*.pc
%{_infodir}/gsl*.info*
%{_mandir}/man1/gsl-config.1*
%{_mandir}/man3/*

%files progs
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/gsl-histogram
%attr(755,root,root) %{_bindir}/gsl-randist
%{_mandir}/man1/gsl-histogram.1*
%{_mandir}/man1/gsl-randist.1*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
