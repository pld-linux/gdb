Summary:	A GNU source-level debugger for C, C++ and Fortran
Summary(de):	Symbolischer Debugger für C und andere Sprachen
Summary(es):	Depurador de programas C y otras lenguajes
Summary(fr):	Débugger symbolique pour C et d'autres langages
Summary(pl):	Symboliczny odpluskwiacz dla C i innych jêzyków
Summary(pt_BR):	Depurador de programas C e outras linguagens
Summary(ru):	óÉÍ×ÏÌÉÞÅÓËÉÊ ÏÔÌÁÄÞÉË ÄÌÑ C É ÄÒÕÇÉÈ ÑÚÙËÏ×
Summary(tr):	C ve diðer diller için sembolik hata ayýklayýcý
Summary(uk):	óÉÍ×ÏÌØÎÉÊ ×¦ÄÌÁÄÞÉË ÄÌÑ ó ÔÁ ¦ÎÛÉÈ ÍÏ×
Summary(zh_CN):	[¿ª·¢]CºÍÆäËûÓïÑÔµÄµ÷ÊÔÆ÷
Summary(zh_TW):	[.-A¶}µo]C©M.$)B¨ä.-A¥L»y.$)B¨¥ªº½Õ¸Õ¾¹
Name:		gdb
Version:	6.0
Release:	0.2
License:	GPL
Group:		Development/Debuggers
Source0:	ftp://ftp.gnu.org/pub/gnu/gdb/%{name}-%{version}.tar.gz
# Source0-md5:	e2314b7c9c7670b5384deb90701446f4
Source1:	http://www.mif.pg.gda.pl/homepages/ankry/man-PLD/%{name}-non-english-man-pages.tar.bz2
# Source1-md5:	2e8a48939ae282c12bbacdd54e398247
Patch0:		%{name}-ncurses.patch
Patch1:		%{name}-readline.patch
Patch2:		%{name}-info.patch
Patch3:		%{name}-procfs.patch
Patch4:		%{name}-passflags.patch
Patch5:		%{name}-sparc-workaround.patch
BuildRequires:	XFree86-devel
BuildRequires:	autoconf >= 2.53
BuildRequires:	libtool
BuildRequires:	ncurses-devel >= 5.2
BuildRequires:	readline-devel >= 4.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Gdb is a full featured, command driven debugger. Gdb allows you to
trace the execution of programs and examine their internal state at
any time. Gdb works for C and C++ compiled with the GNU C compiler
gcc.

%description -l de
dem Sie die Ausführung von Programmen verfolgen und jederzeit den
inneren Zustand überprüfen können. Er funktioniert für C und mit GNU C
kompiliertes C++.

%description -l es
Este es un debugger orientado a comandos repleto de características.
Te permite rastrear la ejecución de programas y examinar su estado
interno a cualquier momento. Funciona para C y C++ compilado con el
compilador GNU C.

%description -l fr
Débugger complet, piloté par commandes. Permet de tracer l'exécution
des programmes et d'examiner à tout moment leur état interne.
Fonctionne avec les binaires C et C++ compilés avec le compilateur C
de GNU, gcc.

%description -l pl
Gdb jest rozbudowanym odpluskwiaczem (debuggerem), pozwalaj±cym
¶ledziæ wykonywanie programu i badaæ jego stan wewnêtrzny. Gdb
umo¿liwia odpluskwianie programów napisanych w C/C++ i skompilowanych
przy pomocy kompilatora GNU (gcc).

%description -l pt_BR
Este é um debugger orientado a comandos repleto de características.
Ele permite à você rastrear a execução de programas e examinar o seu
estado interno a qualquer momento. Ele funciona para para C e C++
compilado com o compilador GNU C.

%description -l ru
üÔÏ ÐÏÌÎÏÃÅÎÎÙÊ ÏÔÌÁÄÞÉË, ÕÐÒÁ×ÌÑÅÍÙÊ ËÏÍÁÎÄÁÍÉ. ïÎ ÐÏÚ×ÏÌÑÅÔ
ÔÒÁÓÓÉÒÏ×ÁÔØ ÉÓÐÏÌÎÅÎÉÅ ÐÒÏÇÒÁÍÍ É ÉÚÕÞÁÔØ ÉÈ ×ÎÕÔÒÅÎÎÅÅ ÓÏÓÔÏÑÎÉÅ ×
ÌÀÂÏÊ ÍÏÍÅÎÔ ×ÒÅÍÅÎÉ. òÁÂÏÔÁÅÔ Ó ÐÒÏÇÒÁÍÍÁÍÉ ÎÁ C É C++,
ÓËÏÍÐÉÌÉÒÏ×ÁÎÎÙÍÉ GNU ËÏÍÐÉÌÑÔÏÒÏÍ C (gcc, egcs, pgcc).

%description -l tr
Bir komut arayüzü üzerinden programcýya programýný adým adým izleme
(trace) ve herhangi bir anda programýn durumunu inceleme olanaðý
verir.

%description -l uk
ãÅ ÐÏ×ÎÏÃ¦ÎÎÉÊ ×¦ÄÌÁÄÞÉË, ÝÏ ËÅÒÕ¤ÔØÓÑ ËÏÍÁÎÄÁÍÉ. ÷¦Î ÄÏÚ×ÏÌÑ¤
ÔÒÁÓÕ×ÁÔÉ ×ÉËÏÎÁÎÎÑ ÐÒÏÇÒÁÍ ÔÁ ×É×ÞÁÔÉ §È ×ÎÕÔÒ¦ÛÎ¦Ê ÓÔÁÎ × ÄÏ×¦ÌØÎÉÊ
ÍÏÍÅÎÔ ÞÁÓÕ. ðÒÁÃÀ¤ Ú ÐÒÏÇÒÁÍÁÍÉ ÎÁ C ÔÁ C++, ÚËÏÍÐ¦ÌØÏ×ÁÎÉÍÉ
ËÏÍÐ¦ÌÑÔÏÒÁÍÉ GNU C (gcc, egcs, pgcc).

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1

%build
for dir in `find gdb/ -name 'configure.in'`; do
	dir=$(dirname "$dir")
	olddir=$(pwd)
	cd $dir
	rm -f aclocal.m4
	%{__aclocal}
	%{__autoconf}
	cd $olddir
done
# !! Don't enable shared here !!
# This will cause serious problems --misiek
%configure2_13 \
	--disable-shared \
	--enable-nls \
	--without-included-gettext \
	--without-included-regex \
	--enable-gdcli \
	--enable-gdbmi \
	--enable-multi-ice \
	--enable-netrom \
	--with-cpu=%{_target_cpu} \
	--enable-tui \
%ifnarch alpha
	--with-mmalloc
%endif

# something is wrong after above - e.g. $exeext=="no" - fix it:
cd gdb
%configure
cd ..

%{__make}
%{__make} info

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_infodir}

%{__make} install install-info \
	prefix=$RPM_BUILD_ROOT%{_prefix} \
	bindir=$RPM_BUILD_ROOT%{_bindir} \
	sbindir=$RPM_BUILD_ROOT%{_sbindir} \
	infodir=$RPM_BUILD_ROOT%{_infodir} \
	includedir=$RPM_BUILD_ROOT%{_includedir} \
	libdir=$RPM_BUILD_ROOT%{_libdir} \
	mandir=$RPM_BUILD_ROOT%{_mandir}

bzip2 -dc %{SOURCE1} | tar xf - -C $RPM_BUILD_ROOT%{_mandir}

%clean
rm -rf $RPM_BUILD_ROOT

%post
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%postun
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*

%{_mandir}/man1/*
%lang(es) %{_mandir}/es/man1/*
%lang(fr) %{_mandir}/fr/man1/*
%lang(hu) %{_mandir}/hu/man1/*
%lang(ja) %{_mandir}/ja/man1/*
%lang(pl) %{_mandir}/pl/man1/*
%{_infodir}/gdb*.info*
%{_infodir}/stabs*.info*
