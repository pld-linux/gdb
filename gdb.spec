# NOTE
# - Do not remove -lib package, it is required by FPC

# TODO
# - change install msg to poldek in buildid-locate-rpm-pld.patch when poldek allows it. LP#493922
#
# Conditional build:
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
Version:	7.0
Release:	6
License:	GPL v3+
Group:		Development/Debuggers
Source0:	http://ftp.gnu.org/gnu/gdb/%{name}-%{version}.tar.bz2
# Source0-md5:	3386a7b69c010785c920ffc1e9cb890a
Source1:	http://www.mif.pg.gda.pl/homepages/ankry/man-PLD/%{name}-non-english-man-pages.tar.bz2
# Source1-md5:	2e8a48939ae282c12bbacdd54e398247
Source3:	%{name}-gstack.man
Source4:	libstdc++-v3-python-r151798.tar.bz2
# Source4-md5:	7507540c50a1edeb2fc22a37bc4a08b8

# FEDORA -- use the same numbering that they do
# don't ever modify these patches, apply secondary patch to alter it pld way
# use:'<,'>!grep -vE '^(\#|$)' in vim to filterout comments, spaces

Patch1:		%{name}-6.3-rh-dummykfail-20041202.patch
Patch2:		%{name}-6.3-rh-testversion-20041202.patch
Patch3:		%{name}-6.3-rh-testlibunwind-20041202.patch
Patch104:	%{name}-6.3-ppcdotsolib-20041022.patch
Patch105:	%{name}-6.3-ppc64syscall-20040622.patch
Patch106:	%{name}-6.3-framepczero-20040927.patch
Patch111:	%{name}-6.3-ppc64displaysymbol-20041124.patch
Patch112:	%{name}-6.6-scheduler_locking-step-sw-watchpoints2.patch
Patch260:	%{name}-6.6-scheduler_locking-step-is-default.patch
Patch118:	%{name}-6.3-gstack-20050411.patch
Patch122:	%{name}-6.3-test-pie-20050107.patch
Patch124:	%{name}-archer-pie.patch
Patch389:	%{name}-archer-pie-addons.patch
Patch125:	%{name}-6.3-test-self-20050110.patch
Patch133:	%{name}-6.3-test-dtorfix-20050121.patch
Patch136:	%{name}-6.3-test-movedir-20050125.patch
Patch140:	%{name}-6.3-gcore-thread-20050204.patch
Patch141:	%{name}-6.6-step-thread-exit.patch
Patch259:	%{name}-6.3-step-thread-exit-20050211-test.patch
Patch142:	%{name}-6.3-terminal-fix-20050214.patch
Patch145:	%{name}-6.3-threaded-watchpoints2-20050225.patch
Patch148:	%{name}-6.3-inheritance-20050324.patch
Patch153:	%{name}-6.3-ia64-gcore-page0-20050421.patch
Patch157:	%{name}-6.3-security-errata-20050610.patch
Patch158:	%{name}-6.3-ia64-sigtramp-frame-20050708.patch
Patch160:	%{name}-6.3-ia64-gcore-speedup-20050714.patch
Patch161:	%{name}-6.3-inferior-notification-20050721.patch
Patch162:	%{name}-6.3-ia64-info-frame-fix-20050725.patch
Patch163:	%{name}-6.3-inheritancetest-20050726.patch
Patch164:	%{name}-6.3-readnever-20050907.patch
Patch169:	%{name}-6.3-ia64-sigill-20051115.patch
Patch170:	%{name}-6.3-bt-past-zero-20051201.patch
Patch176:	%{name}-6.3-large-core-20051206.patch
Patch177:	%{name}-6.3-gstack-without-path-20060414.patch
Patch188:	%{name}-6.5-bz203661-emit-relocs.patch
Patch190:	%{name}-6.5-dwarf-stack-overflow.patch
Patch194:	%{name}-6.5-bz185337-resolve-tls-without-debuginfo-v2.patch
Patch195:	%{name}-6.5-tls-of-separate-debuginfo.patch
Patch196:	%{name}-6.5-sharedlibrary-path.patch
Patch199:	%{name}-6.5-bz190810-gdbserver-arch-advice.patch
Patch201:	%{name}-6.5-gcore-i386-on-amd64.patch
Patch211:	%{name}-6.5-last-address-space-byte-test.patch
Patch208:	%{name}-6.5-BEA-testsuite.patch
Patch209:	%{name}-6.5-readline-long-line-crash.patch
Patch213:	%{name}-6.5-readline-long-line-crash-test.patch
Patch214:	%{name}-6.5-bz216711-clone-is-outermost.patch
Patch215:	%{name}-6.5-bz218379-ppc-solib-trampoline-fix.patch
Patch216:	%{name}-6.5-bz218379-ppc-solib-trampoline-test.patch
Patch217:	%{name}-6.5-bz218379-solib-trampoline-lookup-lock-fix.patch
Patch225:	%{name}-6.5-bz109921-DW_AT_decl_file-test.patch
Patch229:	%{name}-6.3-bz140532-ppc-unwinding-test.patch
Patch231:	%{name}-6.3-bz202689-exec-from-pthread-test.patch
Patch232:	%{name}-7.0-upstream.patch
Patch234:	%{name}-6.6-bz230000-power6-disassembly-test.patch
Patch235:	%{name}-6.3-bz231832-obstack-2gb.patch
Patch240:	%{name}-6.6-bz225783-prelink-path.patch
Patch241:	%{name}-6.6-bz225783-gdb-debuginfo-paths.patch
Patch245:	%{name}-6.6-bz229517-gcore-without-terminal.patch
Patch247:	%{name}-6.6-bz235197-fork-detach-info.patch
Patch249:	%{name}-6.6-gcore32-test.patch
Patch254:	%{name}-6.6-testsuite-timeouts.patch
Patch258:	%{name}-6.6-bz237572-ppc-atomic-sequence-test.patch
Patch261:	%{name}-6.6-readline-system.patch
Patch263:	%{name}-6.3-attach-see-vdso-test.patch
Patch265:	%{name}-6.6-bz247354-leader-exit-fix.patch
Patch266:	%{name}-6.6-bz247354-leader-exit-test.patch
Patch271:	%{name}-6.5-bz243845-stale-testing-zombie-test.patch
Patch274:	%{name}-6.6-buildid-locate.patch
Patch353:	%{name}-6.6-buildid-locate-rpm.patch
Patch282:	%{name}-6.7-charsign-test.patch
Patch284:	%{name}-6.7-ppc-clobbered-registers-O2-test.patch
Patch287:	%{name}-6.7-testsuite-stable-results.patch
Patch289:	%{name}-6.5-ia64-libunwind-leak-test.patch
Patch290:	%{name}-6.5-missed-trap-on-step-test.patch
Patch293:	%{name}-6.7-bz426600-DW_TAG_interface_type-fix.patch
Patch294:	%{name}-6.7-bz426600-DW_TAG_interface_type-test.patch
Patch296:	%{name}-6.5-gcore-buffer-limit-test.patch
Patch298:	%{name}-6.6-threads-static-test.patch
Patch304:	%{name}-6.7-kernel-headers-compat.patch
Patch309:	%{name}-6.3-mapping-zero-inode-test.patch
Patch311:	%{name}-6.3-focus-cmd-prev-test.patch
Patch314:	%{name}-6.3-watchpoint-cond-gone-test.patch
Patch315:	%{name}-6.8-bz442765-threaded-exec-test.patch
Patch317:	%{name}-6.8-sparc64-silence-memcpy-check.patch
Patch318:	%{name}-6.8-gcc35998-ada-memory-trash.patch
Patch320:	%{name}-6.5-section-num-fixup-test.patch
Patch322:	%{name}-6.8-constant-watchpoints.patch
Patch324:	%{name}-6.8-glibc-headers-compat.patch
Patch326:	%{name}-6.8-tui-singlebinary.patch
Patch350:	%{name}-6.8-inlining-addon.patch
Patch328:	%{name}-6.8-inlining-by-name.patch
Patch329:	%{name}-6.8-bz254229-gcore-prpsinfo.patch
Patch330:	%{name}-6.8-bz436037-reg-no-longer-active.patch
Patch331:	%{name}-6.8-quit-never-aborts.patch
Patch332:	%{name}-6.8-fortran-tag-constant.patch
Patch337:	%{name}-6.8-attach-signalled-detach-stopped.patch
Patch343:	%{name}-6.8-watchpoint-conditionals-test.patch
Patch348:	%{name}-6.8-bz466901-backtrace-full-prelinked.patch
Patch349:	%{name}-archer.patch
Patch352:	%{name}-6.8-bz457187-largefile.patch
Patch360:	%{name}-6.8-bz457187-largefile-test.patch
Patch375:	%{name}-readline-6.0.patch
Patch376:	libstdc++-v3-python-common-prefix.patch
Patch381:	%{name}-simultaneous-step-resume-breakpoint-test.patch
Patch382:	%{name}-core-open-vdso-warning.patch
Patch383:	%{name}-bz528668-symfile-sepcrc.patch
Patch384:	%{name}-bz528668-symfile-cleanup.patch
Patch385:	%{name}-bz528668-symfile-multi.patch
Patch387:	%{name}-bz539590-gnu-ifunc.patch
Patch388:	%{name}-bz538626-bp_location-accel-bp-cond.patch
Patch390:	%{name}-readline-6.0-signal.patch
Patch391:	%{name}-x86_64-i386-syscall-restart.patch

# PLD patches
Patch1000:	%{name}-readline.patch
Patch1001:	%{name}-info.patch
Patch1002:	%{name}-passflags.patch
Patch1005:	%{name}-pretty-print-by-default.patch
Patch1006:	buildid-locate-rpm-pld.patch
Patch1007:	%{name}-python.patch
URL:		http://www.gnu.org/software/gdb/
BuildRequires:	autoconf >= 2.53
BuildRequires:	automake
BuildRequires:	bison
BuildRequires:	expat-devel
BuildRequires:	flex
BuildRequires:	libtool
BuildRequires:	ncurses-devel >= 5.2
BuildRequires:	pkgconfig
BuildRequires:	readline-devel
BuildRequires:	rpmbuild(macros) >= 1.219
BuildRequires:	texinfo >= 4.4
BuildRequires:	zlib-devel
%if %{with python}
BuildRequires:	python-devel
BuildRequires:	rpm-pythonprov
%endif
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

%package gdbserver
Summary:	A standalone server for GDB (the GNU source-level debugger)
Group:		Development/Debuggers

%description gdbserver
GDB, the GNU debugger, allows you to debug programs written in C, C++,
Java, and other languages, by executing them in a controlled fashion
and printing their data.

This package provides a program that allows you to run GDB on a
different machine than the one which is running the program being
debugged.

%package -n python-%{name}
Summary:	GDB Python bindings
Summary(pl.UTF-8):	Wiązania PackageKit dla Pythona
Group:		Development/Languages/Python
Requires:	python-libs

%description -n python-%{name}
GDB Python bindings.

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
%setup -q

# libstdc++ pretty printers.
bzip2 -dc %{SOURCE4} | tar xf -

# Files have `# <number> <file>' statements breaking VPATH / find-debuginfo.sh .
rm -f gdb/ada-exp.c gdb/ada-lex.c gdb/c-exp.c gdb/cp-name-parser.c gdb/f-exp.c
rm -f gdb/jv-exp.c gdb/m2-exp.c gdb/objc-exp.c gdb/p-exp.c

# FEDORA PATCHES -- keep them in same order they do
%patch2 -p1
%patch232 -p1
%patch349 -p1
%patch383 -p1
%patch384 -p1
%patch385 -p1
%patch124 -p1
%patch1 -p1
%patch3 -p1
%patch104 -p1
%patch105 -p1
%patch106 -p1
%patch111 -p1
%patch112 -p1
%patch118 -p1
%patch122 -p1
%patch125 -p1
%patch133 -p1
%patch136 -p1
%patch140 -p1
%patch141 -p1
%patch259 -p1
%patch142 -p1
%patch145 -p1
%patch148 -p1
%patch153 -p1
%patch157 -p1
%patch158 -p1
%patch160 -p1
%patch161 -p1
%patch162 -p1
%patch163 -p1
%patch164 -p1
%patch169 -p1
%patch170 -p1
%patch176 -p1
%patch177 -p1
%patch188 -p1
%patch190 -p1
%patch194 -p1
%patch195 -p1
%patch196 -p1
%patch199 -p1
%patch201 -p1
%patch208 -p1
%patch209 -p1
%patch211 -p1
%patch213 -p1
%patch214 -p1
%patch215 -p1
%patch216 -p1
%patch217 -p1
%patch225 -p1
%patch229 -p1
%patch231 -p1
%patch234 -p1
%patch235 -p1
%patch240 -p1
%patch241 -p1
%patch245 -p1
%patch247 -p1
%patch249 -p1
%patch254 -p1
%patch258 -p1
%patch260 -p1
%patch261 -p1
%patch263 -p1
%patch265 -p1
%patch266 -p1
%patch271 -p1
%patch274 -p1
%patch353 -p1
%patch282 -p1
%patch284 -p1
%patch287 -p1
%patch289 -p1
%patch290 -p1
%patch293 -p1
%patch294 -p1
%patch296 -p1
%patch298 -p1
%patch304 -p1
%patch309 -p1
%patch311 -p1
%patch314 -p1
%patch315 -p1
%patch317 -p1
%patch318 -p1
%patch320 -p1
%patch322 -p1
%patch324 -p1
%patch326 -p1
%patch350 -p1
%patch328 -p1
%patch329 -p1
%patch330 -p1
%patch331 -p1
%patch332 -p1
%patch337 -p1
%patch343 -p1
%patch348 -p1
%patch352 -p1
%patch360 -p1
%patch375 -p1
%patch376 -p1
%patch381 -p1
%patch382 -p1
%patch387 -p1
%patch388 -p1
%patch389 -p1
%patch390 -p1
%patch391 -p1

# PLD patches
%patch1000 -p1
%patch1001 -p1
%patch1002 -p1
%patch1005 -p1
%patch1006 -p1
%patch1007 -p1

mv $(basename %{SOURCE4} .tar.bz2) libstdcxxpython

# Change the version that gets printed at GDB startup, so it is PLD Linux specific.
cat > gdb/version.in << EOF
PLD Linux (%{version}-%{release})
EOF

sed -i -e 's#_GCC_AUTOCONF_VERSION\], \[2\.64\]#_GCC_AUTOCONF_VERSION], [2.65]#g' config/override.m4

%build
for dir in $(find gdb -name 'configure.in' -o -name 'configure.ac'); do
	dir=$(dirname "$dir")
	olddir=$(pwd)
	cd $dir
	rm -f aclocal.m4
	%{__aclocal}
	%{__autoconf}
	grep -q AC_CONFIG_HEADER configure.* && %{__autoheader}
	cd $olddir
done
cp -f /usr/share/automake/config.* .
# don't --enable-shared here, there would be libs version mismatch with binutils
%configure \
	--with-gdb-datadir=%{_datadir}/gdb \
	--with-separate-debug-dir=/usr/lib/debug \
%if %{with python}
	--with-python \
	--with-pythondir=%{py_sitescriptdir} \
%else
	--without-python \
%endif
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

%{__make} -j1
%{__make} -j1 info

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_infodir}

%{__make} -j1 install install-info \
	DESTDIR=$RPM_BUILD_ROOT

# gdbtui seems all identical to gdb except when invoked as gdbtio, ncurses
# window is created too.
echo ".so gdb.1" > $RPM_BUILD_ROOT%{_mandir}/man1/gdbtui.1
ln -f $RPM_BUILD_ROOT%{_bindir}/{gdb,gdbtui}

bzip2 -dc %{SOURCE1} | tar xf - -C $RPM_BUILD_ROOT%{_mandir}
cp -a gdb/libgdb.a $RPM_BUILD_ROOT%{_libdir}

rm -f $RPM_BUILD_ROOT%{_infodir}/dir
rm -f $RPM_BUILD_ROOT%{_mandir}/README.gdb-non-english-man-pages

%if %{with python}
# Temporarily now:
for LIB in lib lib64; do
	LIBPATH="$RPM_BUILD_ROOT%{_datadir}/gdb/auto-load%{_prefix}/$LIB"
	install -d $LIBPATH
	# basename is being run only for the native (non-biarch) file.
	sed -e 's,@pythondir@,%{_datadir}/gdb/python,' \
	  -e 's,@toolexeclibdir@,%{_prefix}/'"$LIB," \
	  < libstdcxxpython/hook.in	\
	  > $LIBPATH/$(basename %{_prefix}/%{_lib}/libstdc++.so.6.*)-gdb.py
done
cp -a libstdcxxpython/libstdcxx	$RPM_BUILD_ROOT%{py_sitescriptdir}

%py_ocomp $RPM_BUILD_ROOT%{py_sitescriptdir}
%py_comp $RPM_BUILD_ROOT%{py_sitescriptdir}
%py_postclean
%endif

cp -a %{SOURCE3} $RPM_BUILD_ROOT%{_mandir}/man1/gstack.1

# Remove the files that are part of a gdb build but that are owned and provided by other packages.
# These are part of binutils
rm -rf $RPM_BUILD_ROOT%{_datadir}/locale
rm -f $RPM_BUILD_ROOT%{_infodir}/bfd*
rm -f $RPM_BUILD_ROOT%{_infodir}/standard*
rm -f $RPM_BUILD_ROOT%{_infodir}/mmalloc*
rm -f $RPM_BUILD_ROOT%{_infodir}/configure*
rm -rf $RPM_BUILD_ROOT%{_includedir}
rm -rf $RPM_BUILD_ROOT%{_libdir}/lib{bfd*,opcodes*,iberty*,mmalloc*}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p	/sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%postun	-p	/sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%files
%defattr(644,root,root,755)
%doc gdb/{ChangeLog,NEWS,PROBLEMS,README}
%attr(755,root,root) %{_bindir}/gdb
%attr(755,root,root) %{_bindir}/gdbtui
%attr(755,root,root) %{_bindir}/gstack
%dir %{_datadir}/gdb
%{_datadir}/gdb/syscalls
%{_mandir}/man1/gdb.1*
%{_mandir}/man1/gdbtui.1*
%{_mandir}/man1/gstack.1*
%lang(es) %{_mandir}/es/man1/*
%lang(fr) %{_mandir}/fr/man1/*
%lang(hu) %{_mandir}/hu/man1/*
%lang(ja) %{_mandir}/ja/man1/*
%lang(pl) %{_mandir}/pl/man1/*
%{_infodir}/annotate.info*
%{_infodir}/gdb.info*
%{_infodir}/gdbint.info*
%{_infodir}/stabs.info*

%if %{with python}
%files -n python-%{name}
%defattr(644,root,root,755)
%dir %{py_sitescriptdir}/gdb
%{py_sitescriptdir}/gdb/*.py[co]
%dir %{py_sitescriptdir}/gdb/command
%{py_sitescriptdir}/gdb/command/*.py[co]
%dir %{py_sitescriptdir}/gdb/function
%{py_sitescriptdir}/gdb/function/*.py[co]

# likely oneday gcc.spec will provide this
%dir %{py_sitescriptdir}/libstdcxx
%{py_sitescriptdir}/libstdcxx/*.py[co]
%dir %{py_sitescriptdir}/libstdcxx/v6
%{py_sitescriptdir}/libstdcxx/v6/*.py[co]

# or should we include it in base package?
%{_datadir}/gdb/auto-load
%endif

%files gdbserver
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/gdbserver
%{_mandir}/man1/gdbserver.1*

%files lib
%defattr(644,root,root,755)
%{_libdir}/libgdb.a
