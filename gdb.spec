Summary:	A GNU source-level debugger for C, C++ and Fortran
Summary(de.UTF-8):   Symbolischer Debugger für C und andere Sprachen
Summary(es.UTF-8):   Depurador de programas C y otras lenguajes
Summary(fr.UTF-8):   Débugger symbolique pour C et d'autres langages
Summary(pl.UTF-8):   Symboliczny odpluskwiacz dla C i innych języków
Summary(pt_BR.UTF-8):   Depurador de programas C e outras linguagens
Summary(tr.UTF-8):   C ve diğer diller için sembolik hata ayıklayıcı
Name:		gdb
Version:	5.1.1
Release:	2
License:	GPL
Group:		Development/Debuggers
Source0:	ftp://ftp.gnu.org/pub/gnu/gdb/%{name}-%{version}.tar.gz
Source1:	http://www.mif.pg.gda.pl/homepages/ankry/man-PLD/%{name}-non-english-man-pages.tar.bz2
Patch0:		%{name}-gettext.patch
Patch1:		%{name}-ncurses.patch
Patch2:		%{name}-readline.patch
Patch3:		%{name}-info.patch
Patch4:		%{name}-procfs.patch
Patch5:		%{name}-ppc-include.patch
Patch6:		%{name}-passflags.patch
BuildRequires:	ncurses-devel >= 5.2
BuildRequires:	readline-devel >= 4.2
BuildRequires:	XFree86-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Gdb is a full featured, command driven debugger. Gdb allows you to
trace the execution of programs and examine their internal state at
any time. Gdb works for C and C++ compiled with the GNU C compiler
gcc.

%description -l de.UTF-8
dem Sie die Ausführung von Programmen verfolgen und jederzeit den
inneren Zustand überprüfen können. Er funktioniert für C und mit GNU C
kompiliertes C++.

%description -l es.UTF-8
Este es un debugger orientado a comandos repleto de características.
Te permite rastrear la ejecución de programas y examinar su estado
interno a cualquier momento. Funciona para C y C++ compilado con el
compilador GNU C.

%description -l fr.UTF-8
Débugger complet, piloté par commandes. Permet de tracer l'exécution
des programmes et d'examiner à tout moment leur état interne.
Fonctionne avec les binaires C et C++ compilés avec le compilateur C
de GNU, gcc.

%description -l pl.UTF-8
Gdb jest rozbudowanym odpluskwiaczem (debuggerem), pozwalającym
śledzić wykonywanie programu i badać jego stan wewnętrzny. Gdb
umożliwia odpluskwianie programów napisanych w C/C++ i skompilowanych
przy pomocy kompilatora GNU (gcc).

%description -l pt_BR.UTF-8
Este é um debugger orientado a comandos repleto de características.
Ele permite à você rastrear a execução de programas e examinar o seu
estado interno a qualquer momento. Ele funciona para para C e C++
compilado com o compilador GNU C.

%description -l tr.UTF-8
Bir komut arayüzü üzerinden programcıya programını adım adım izleme
(trace) ve herhangi bir anda programın durumunu inceleme olanağı
verir.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1

%build
(cd gdb; autoconf)
(cd gdb/doc; autoconf)
(cd gdb/testsuite; autoconf)
(cd gdb/testsuite/gdb.asm; autoconf)
(cd gdb/testsuite/gdb.base; autoconf)
(cd gdb/testsuite/gdb.c++; autoconf)
(cd gdb/testsuite/gdb.chill; autoconf)
(cd gdb/testsuite/gdb.disasm; autoconf)
(cd gdb/testsuite/gdb.fortran; autoconf)
(cd gdb/testsuite/gdb.java; autoconf)
(cd gdb/testsuite/gdb.mi; autoconf)
(cd gdb/testsuite/gdb.stabs; autoconf)
(cd gdb/testsuite/gdb.threads; autoconf)
(cd gdb/testsuite/gdb.trace; autoconf)
(cd gdb/gdbserver; autoconf)
# !! Don't enable shared here !!
# This will cause serious problems --misiek
%configure2_13 \
	--disable-shared \
	--enable-nls \
	--without-included-gettext \
	--enable-multi-ice \
	--enable-gdbmi \
	--enable-gdcli \
	--enable-netrom \
	--with-cpu=%{_target_cpu} \
	--with-x \
	--enable-tui \
%ifnarch alpha
	--with-mmalloc \
%endif
	--with-mmap

# something is wrong after above - e.g. $exeext=="no" - fix it:
(cd gdb
%configure
)

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
