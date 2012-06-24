Summary:	The GNU Scientific Library for numerical analysis
Summary(es):	Biblioteca cient�fica del GNU
Summary(pl):	GNU Scientific Library do analizy numerycznej
Summary(pt_BR):	Biblioteca cient�fica GNU
Summary(ru):	������� ���������� GNU ��� ��������� �������
Summary(uk):	������� ¦�̦����� GNU ��� ��������� ���̦��
Name:		gsl
Version:	1.5
Release:	1
Epoch:		1
License:	GPL
Group:		Libraries
Source0:	ftp://sources.redhat.com/pub/gsl/%{name}-%{version}.tar.gz
# Source0-md5:	de5ae1cce71645b40461a59ba8c9cf43
Patch0:		%{name}-info.patch
Patch1:		%{name}-link.patch
URL:		http://www.gnu.org/software/gsl/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	libtool >= 1:1.4.2-9
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

%description -l es
Esta es la biblioteca cient�fica del GNU. Ofrece acceso a funciones
para manejar muchos problemas que aparecen en computaci�n cient�fica.

%description -l pl
Pakiet gsl zawiera bibliotek� funkcji przydatnych w pracy naukowej
dost�pnych na licencji (GNU). GSL jest zbiorem funkcji napisanych
w j�zyku C, przeznaczonych do analizy numerycznej. Biblioteka jest
jeszcze w bardzo wczesnym stadium tworzenia. W tej chwili zawiera
generatory liczb losowych, FFT, znajdowanie miejsc zerowych. W
przysz�o�ci, b�dzie zawiera� ca�kowanie metod� Monte Carlo oraz
funkcje specjalne. Konsolidacja z GSL pozwala programom na dost�p do
funkcji, kt�re mog� by� przydatne w rozwi�zywaniu wielu problem�w
pojawiaj�cych si� w obliczeniach naukowych.

%description -l pt_BR
Esta � a biblioteca cient�fica do projeto GNU. Fornece acesso a
fun��es para tratar muitos problemas que surgem em computa��o
cient�fica.

%description -l ru
��� ������� ���������� GNU. ������ � ��� ���� ������ � ��������,
�������� ������ ������, �������� ��� ������� ��������.

%description -l uk
�� ������� ¦�̦����� GNU. ������ � ��� ��� ������ �� ����æ�, ��
���������� ����'����� ������ �����, ������� ��� �������� ��������˦�.

%package devel
Summary:	Header files for developing programs using gsl
Summary(pl):	Pliki nag��wkowe i dokumentacja do bibliotek gsl
Summary(pt_BR):	Ferramentas de desenvolvimento para a gsl
Summary(ru):	����� ��� ���������� � ������� ����������� GNU (GSL)
Summary(uk):	����� ��� �������� � �������� ¦�̦������ GNU (GSL)
Group:		Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	libgsl0-devel

%description devel
Header files for developing programs using gsl.

%description devel -l pl
Pliki nag��wkowe i dokumentacja do bibliotek gsl.

%description devel -l pt_BR
Arquivos de inclus�o, bibliotecas e documenta��o necess�rio para
desenvolver aplicativos que utilizam a biblioteca gsl.

%description devel -l ru
��� ����������, ������ � ������������ �� ������������� �������
���������� GNU � ����� ����������.

%description devel -l uk
�� ¦�̦�����, ������ �� ���������æ� �� ������������ ������ϧ
¦�̦����� GNU � ����� ���������.

%package static
Summary:	Static gsl librariries
Summary(pl):	Biblioteki statyczne gsl
Summary(pt_BR):	Bibliotecas est�ticas para desenvolvimento com gsl
Summary(ru):	����������� ���������� ��� ���������� � ������� ����������� GNU (GSL)
Summary(uk):	������Φ ¦�̦����� ��� �������� � �������� ¦�̦������ GNU (GSL)
Group:		Development/Libraries
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}

%description static
Static gsl librariries.

%description static -l pl
Biblioteki statyczne gsl.

%description static -l pt_BR
Bibliotecas est�ticas para desenvolvimento com gsl.

%description static -l ru
��� ����������� ���������� ��� ������������� ������� ���������� GNU �
����� ����������.

%description static -l uk
�� �������� ¦�̦����� ��� ������������ ������ϧ ¦�̦����� GNU �
����� ���������.

%package progs
Summary:	gsl utility programs
Summary(pl):	Narz�dzia dla gsl
Group:		Applications/Science
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description progs
gsl utility programs.

%description progs -l pl
Narz�dzia dla gsl.

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
%{_pkgconfigdir}/*
%{_infodir}/gsl*
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
