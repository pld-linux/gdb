#
# NOTE:	Do not remove -lib package, it is required by FPC
#
Summary:	A GNU source-level debugger for C, C++ and Fortran
Summary(de.UTF-8):	Symbolischer Debugger für C und andere Sprachen
Summary(es.UTF-8):	Depurador de programas C y otras lenguajes
Summary(fr.UTF-8):	Débugger symbolique pour C et d'autres langages
Summary(pl.UTF-8):	Symboliczny odpluskwiacz dla C i innych języków
Summary(pt_BR.UTF-8):	Depurador de programas C e outras linguagens
Summary(ru.UTF-8):	Символический отладчик для C и других языков
Summary(tr.UTF-8):	C ve diğer diller için sembolik hata ayıklayıcı
Summary(uk.UTF-8):	Символьний відладчик для С та інших мов
Summary(zh_CN.UTF-8):	[开发]C和其他语言的调试器
Summary(zh_TW.UTF-8):	[.-A開發]C和.$)B其.-A他語.$)B言的調試器
%define	snap	20081014
Name:		gdb
Version:	6.8.50
Release:	0.%{snap}.1
License:	GPL v3+
Group:		Development/Debuggers
# Source0:	http://ftp.gnu.org/gnu/gdb/%{name}-%{version}.tar.bz2
Source0:	ftp://sourceware.org/pub/gdb/snapshots/current/gdb-%{version}.%{snap}.tar.bz2
# Source0-md5:	7317a7da78f28058e45c1f0dec24cbdb
Source1:	http://www.mif.pg.gda.pl/homepages/ankry/man-PLD/%{name}-non-english-man-pages.tar.bz2
# Source1-md5:	2e8a48939ae282c12bbacdd54e398247
Patch0:		%{name}-readline.patch
Patch1:		%{name}-info.patch
Patch2:		%{name}-passflags.patch
Patch4:		%{name}-gdbinit-stat.patch
Patch5:		%{name}-pretty-print-by-default.patch
Patch6:		%{name}-absolute-gnu_debuglink-path.patch
URL:		http://www.gnu.org/software/gdb/
BuildRequires:	autoconf >= 2.53
BuildRequires:	automake
BuildRequires:	bison
BuildRequires:	flex
BuildRequires:	libtool
BuildRequires:	ncurses-devel >= 5.2
BuildRequires:	readline-devel >= 4.3
BuildRequires:	texinfo >= 4.4
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

%description -l ru.UTF-8
Это полноценный отладчик, управляемый командами. Он позволяет
трассировать исполнение программ и изучать их внутреннее состояние в
любой момент времени. Работает с программами на C и C++,
скомпилированными GNU компилятором C (gcc, egcs, pgcc).

%description -l tr.UTF-8
Bir komut arayüzü üzerinden programcıya programını adım adım izleme
(trace) ve herhangi bir anda programın durumunu inceleme olanağı
verir.

%description -l uk.UTF-8
Це повноцінний відладчик, що керується командами. Він дозволяє
трасувати виконання програм та вивчати їх внутрішній стан в довільний
момент часу. Працює з програмами на C та C++, зкомпільованими
компіляторами GNU C (gcc, egcs, pgcc).

%package lib
Summary:	GDB in the form of a static library
Summary(pl.UTF-8):	GDB w postaci biblioteki statycznej
Group:		Development/Debuggers
#Requires:	binutils-devel >= 2.17.50

%description lib
GDB in the form of a static library.

%description lib -l pl.UTF-8
GDB w postaci biblioteki statycznej.

%prep
%setup -q -n %{name}-%{version}.%{snap}
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch4 -p0
%patch5 -p1
%patch6 -p1

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
cp -f /usr/share/automake/config.* .
# don't --enable-shared here, there would be libs version mismatch with binutils
%configure \
	--disable-gdbtk \
	--disable-shared \
	--enable-gdbcli \
	--enable-gdbmi \
	--enable-multi-ice \
	--enable-netrom \
	--enable-nls \
	--enable-tui \
	--with-cpu=%{_target_cpu} \
%ifnarch alpha
	--with-mmalloc \
%endif
	--without-included-gettext \
	--without-included-regex \
	--without-x

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

install gdb/libgdb.a $RPM_BUILD_ROOT%{_libdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p	/sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%postun	-p	/sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%files
%defattr(644,root,root,755)
%doc gdb/{ChangeLog,NEWS,PROBLEMS,README}
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
%lang(es) %{_mandir}/es/man1/*
%lang(fr) %{_mandir}/fr/man1/*
%lang(hu) %{_mandir}/hu/man1/*
%lang(ja) %{_mandir}/ja/man1/*
%lang(pl) %{_mandir}/pl/man1/*
%{_infodir}/gdb*.info*
%{_infodir}/stabs*.info*

%files lib
%defattr(644,root,root,755)
%{_libdir}/libgdb.a
