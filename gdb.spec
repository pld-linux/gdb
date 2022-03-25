# NOTE: -lib package is used by fpc.spec

# TODO
# - rpm5 librpm support (gdb/configure.ac checks for 4.x or so)
# - change install msg to poldek in buildid-locate-rpm-pld.patch when poldek allows it. LP#493922
# - reenable guile after https://sourceware.org/bugzilla/show_bug.cgi?id=21104 is fixed
#
# Conditional build:
%bcond_with	guile		# Guile embedded scripting
%bcond_without	python		# build without python support

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
Name:		gdb
Version:	11.2
Release:	2
License:	GPL v3+
Group:		Development/Debuggers
Source0:	https://ftp.gnu.org/gnu/gdb/%{name}-%{version}.tar.xz
# Source0-md5:	433bd0904caa31c247b1b1867f2f911d
Source1:	http://www.mif.pg.gda.pl/homepages/ankry/man-PLD/%{name}-non-english-man-pages.tar.bz2
# Source1-md5:	2e8a48939ae282c12bbacdd54e398247
Source3:	%{name}-gstack.man
Patch1:		x32.patch
Patch100:	gdb-6.6-buildid-locate.patch
Patch101:	gdb-6.6-buildid-locate-solib-missing-ids.patch
Patch102:	gdb-6.6-buildid-locate-rpm.patch
Patch104:	gdb-6.6-buildid-locate-rpm-librpm-workaround.patch
Patch105:	gdb-6.6-buildid-locate-misleading-warning-missing-debuginfo-rhbz981154.patch
Patch106:	gdb-6.6-buildid-locate-rpm-scl.patch
Patch110:	gdb-6.3-gstack-20050411.patch

Patch114:	gdb-vla-intel-stringbt-fix.patch
Patch115:	gdb-vla-intel-tests.patch
Patch1000:	%{name}-readline.patch
Patch1001:	%{name}-info.patch
Patch1002:	%{name}-passflags.patch
Patch1005:	%{name}-pretty-print-by-default.patch
Patch1006:	buildid-locate-rpm-pld.patch
URL:		http://www.gnu.org/software/gdb/
BuildRequires:	autoconf >= 2.69
BuildRequires:	automake
BuildRequires:	bison
BuildRequires:	babeltrace-devel >= 1.1.0
BuildRequires:	expat-devel
BuildRequires:	flex >= 2.6.4
BuildRequires:	gettext-tools >= 0.12.1
BuildRequires:	gmp-devel
%if %{with guile}
BuildRequires:	guile-devel >= 2.0
BuildRequires:	guile-devel < 3.2
%endif
%ifarch %{ix86} %{x8664}
BuildRequires:	libipt-devel
%endif
BuildRequires:	libmpc-devel
BuildRequires:	libselinux-devel
BuildRequires:	libstdc++-devel >= 6:4.8
BuildRequires:	libtool
BuildRequires:	make >= 3.81
BuildRequires:	mpfr-devel
BuildRequires:	ncurses-devel >= 5.2
BuildRequires:	pkgconfig
BuildRequires:	readline-devel
BuildRequires:	rpmbuild(macros) >= 1.219
BuildRequires:	source-highlight-devel >= 3.0
BuildRequires:	tar >= 1:1.22
BuildRequires:	texinfo >= 4.4
BuildRequires:	xxHash-devel
BuildRequires:	xz
BuildRequires:	xz-devel
BuildRequires:	zlib-devel
%if %{with python}
BuildRequires:	python3-devel
BuildRequires:	rpm-pythonprov
Obsoletes:	python-gdb < 7.3
# for traceback module
Requires:	python3-modules
%endif
%{?with_guile:Requires:	guile >= 2.0.12}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		autoconf_ver	%(rpm -q --qf='%%{VERSION}' autoconf)

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

%package gdbserver
Summary:	A standalone server for GDB (the GNU source-level debugger)
Summary(pl.UTF-8):	Samodzielny serwer GDB (debuggera GNU)
Group:		Development/Debuggers

%description gdbserver
GDB, the GNU debugger, allows you to debug programs written in C, C++,
Java, and other languages, by executing them in a controlled fashion
and printing their data.

This package provides a program that allows you to run GDB on a
different machine than the one which is running the program being
debugged.

%description gdbserver -l pl.UTF-8
GDB (GNU debugger) pozwala śledzić programy napisane w C, C++, Javie i
innych językach programowania poprzez wykonywanie ich w sposób
kontrolowany oraz wypisywanie ich danych.

Ten pakiet zawiera program pozwalający uruchamiać GDB na innej
maszynie niż ta, na której działa śledzony program.

%package lib
Summary:	GDB in the form of a static library
Summary(pl.UTF-8):	GDB w postaci biblioteki statycznej
Group:		Development/Debuggers
# libraries that needs to be linked to fulfill libgdb.a symbol requirements
Requires:	binutils-devel >= 2.17.50
Requires:	expat-devel
Requires:	libselinux-devel
Requires:	libsepol-devel
Requires:	ncurses-devel
Requires:	python3-devel
Requires:	readline-devel
Requires:	xz-devel
Requires:	zlib-devel

%description lib
GDB in the form of a static library.

%description lib -l pl.UTF-8
GDB w postaci biblioteki statycznej.

%prep
%setup -q

# Files have `# <number> <file>' statements breaking VPATH / find-debuginfo.sh .
%{__rm} gdb/ada-exp.c gdb/ada-lex.c gdb/c-exp.c gdb/cp-name-parser.c gdb/f-exp.c
%{__rm} gdb/m2-exp.c gdb/p-exp.c

%patch1 -p1
%patch100 -p1
%patch101 -p1
%patch102 -p1
%patch104 -p1
%patch105 -p1
%patch106 -p1
%patch110 -p1

%patch114 -p1
%patch115 -p1

%patch1000 -p1
%patch1001 -p1
%patch1002 -p1
%patch1005 -p1
%patch1006 -p1

# Change the version that gets printed at GDB startup, so it is PLD Linux specific.
cat > gdb/version.in << EOF
%{version}-%{release} (PLD Linux)
EOF

sed -E -i -e '1s,#!\s*/usr/bin/env\s+python2(\s|$),#!%{__python}\1,' -e '1s,#!\s*/usr/bin/env\s+python(\s|$),#!%{__python3}\1,' -e '1s,#!\s*/usr/bin/python(\s|$),#!%{__python3}\1,' \
      contrib/dg-extract-results.py \
      gdb/contrib/test_pubnames_and_indexes.py \
      gdb/testsuite/analyze-racy-logs.py \
      gdb/testsuite/print-ts.py

sed -E -i -e '1s,#!\s*/usr/bin/env\s+python3(\s|$),#!%{__python3}\1,' \
      gdb/copyright.py

sed -E -i -e '1s,#!\s*/usr/bin/env\s+(.*),#!%{__bindir}\1,' \
      gdb/contrib/cc-with-tweaks.sh \
      gdb/gcore \
      gdb/gcore.in \
      src-release.sh

sed -i -e 's/\[2\.69\]/[%{autoconf_ver}]/' config/override.m4

%build
# omit hand-written gdb/testsuite aclocal.m4
for dir in gdb gdbserver ; do
	olddir=$(pwd)
	cd $dir
	%{__rm} aclocal.m4
	%{__aclocal} $(grep '^ACLOCAL_AMFLAGS' Makefile.in | sed -e 's/.*=//')
	cd $olddir
done
for dir in $(find gdb -name 'configure.in' -o -name 'configure.ac'); do
	dir=$(dirname "$dir")
	olddir=$(pwd)
	cd $dir
	%{__autoconf}
	grep -q AC_CONFIG_HEADER configure.* && %{__autoheader}
	cd $olddir
done
cp -f /usr/share/automake/config.* .
install -d build && cd build
# don't --enable-shared here, there would be libs version mismatch with binutils
../%configure \
	--disable-gdbtk \
	--disable-shared \
	--disable-silent-rules \
	--enable-gdbcli \
	--enable-gdbmi \
	--enable-multi-ice \
	--enable-netrom \
	--enable-nls \
	--enable-tui \
	--with-cpu=%{_target_cpu} \
	--with-gdb-datadir=%{_datadir}/gdb \
	--with-guile%{!?with_guile:=no} \
%ifnarch alpha
	--with-mmalloc \
%endif
%if %{with python}
	--with-python="%{__python3}" \
	--with-pythondir=%{py3_sitescriptdir} \
%else
	--without-python \
%endif
	--with-separate-debug-dir=/usr/lib/debug \
	--with-system-readline \
	--without-included-gettext \
	--without-included-regex \
	--without-x

# V=1 because only some subdirs honour --enable-silent-rules
%{__make} \
	V=1

%{__make} -j1 info

# gdb/ChangeLog: Build gdb directly from *.o files not using libgdb.a.
%{__make} -C gdb libgdb.a \
	V=1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_infodir}

%{__make} -C build -j1 install install-info \
	DESTDIR=$RPM_BUILD_ROOT

cp -a build/gdb/libgdb.a $RPM_BUILD_ROOT%{_libdir}

# gdbtui seems all identical to gdb except when invoked as gdbtui, ncurses
# window is created too.
echo ".so gdb.1" > $RPM_BUILD_ROOT%{_mandir}/man1/gdbtui.1
ln -f $RPM_BUILD_ROOT%{_bindir}/{gdb,gdbtui}

bzip2 -dc %{SOURCE1} | tar xf - -C $RPM_BUILD_ROOT%{_mandir}
%{__rm} $RPM_BUILD_ROOT%{_mandir}/README.gdb-non-english-man-pages

rm -f $RPM_BUILD_ROOT%{_infodir}/dir

%if %{with python}
# Temporarily now:
for LIB in lib lib64 libx32; do
	LIBPATH="$RPM_BUILD_ROOT%{_datadir}/gdb/auto-load%{_prefix}/$LIB"
	install -d $LIBPATH
done

%py3_ocomp $RPM_BUILD_ROOT%{py3_sitescriptdir}
%py3_comp $RPM_BUILD_ROOT%{py3_sitescriptdir}
%endif

cp -a %{SOURCE3} $RPM_BUILD_ROOT%{_mandir}/man1/gstack.1

cp -p build/libdecnumber/libdecnumber.a $RPM_BUILD_ROOT%{_libdir}

# Remove the files that are part of a gdb build but that are owned and provided by other packages.
# These are part of binutils:
%{__rm} $RPM_BUILD_ROOT%{_localedir}/*/LC_MESSAGES/{bfd,opcodes}.mo
%{__rm} $RPM_BUILD_ROOT%{_infodir}/bfd.info*
%{__rm} $RPM_BUILD_ROOT%{_includedir}/{ansidecl,bfd,bfdlink,ctf,ctf-api,diagnostics,dis-asm,symcat,plugin-api}.h
%{__rm} $RPM_BUILD_ROOT%{_libdir}/lib{bfd,ctf,ctf-nobfd,opcodes}.la
%{__rm} $RPM_BUILD_ROOT%{_libdir}/lib{bfd,ctf,ctf-nobfd,opcodes}.a

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%postun	-p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%files
%defattr(644,root,root,755)
%doc gdb/{ChangeLog,NEWS,PROBLEMS,README}
%attr(755,root,root) %{_bindir}/gdb
%attr(755,root,root) %{_bindir}/gdbtui
%attr(755,root,root) %{_bindir}/gdb-add-index
%attr(755,root,root) %{_bindir}/gstack
%attr(755,root,root) %{_bindir}/gcore
%dir %{_datadir}/gdb
%dir %{_datadir}/gdb/auto-load
%dir %{_datadir}/gdb/auto-load%{_prefix}
%dir %{_datadir}/gdb/auto-load%{_prefix}/lib
%ifarch %{x8664} x32
%dir %{_datadir}/gdb/auto-load%{_prefix}/lib64
%dir %{_datadir}/gdb/auto-load%{_prefix}/libx32
%endif
%ifarch aarch64
%dir %{_datadir}/gdb/auto-load%{_prefix}/lib64
%endif
%{?with_guile:%{_datadir}/gdb/guile}
%{_datadir}/gdb/syscalls
%{_datadir}/gdb/system-gdbinit
%{_datadir}/gdb/python
%{_mandir}/man1/gdb.1*
%{_mandir}/man1/gdbtui.1*
%{_mandir}/man1/gdb-add-index.1*
%{_mandir}/man1/gstack.1*
%{_mandir}/man1/gcore.1*
%{_mandir}/man5/gdbinit.5*
%lang(es) %{_mandir}/es/man1/*
%lang(fr) %{_mandir}/fr/man1/*
%lang(hu) %{_mandir}/hu/man1/*
%lang(ja) %{_mandir}/ja/man1/*
%lang(pl) %{_mandir}/pl/man1/*
%{_infodir}/annotate.info*
%{_infodir}/gdb.info*
%{_infodir}/stabs.info*

%files gdbserver
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/gdbserver
%{_mandir}/man1/gdbserver.1*
%ifnarch %{arm}
%attr(755,root,root) %{_libdir}/libinproctrace.so
%endif

%files lib
%defattr(644,root,root,755)
%{_libdir}/libdecnumber.a
%{_libdir}/libgdb.a
%{_includedir}/gdb
# -devel?
%{_includedir}/sim
