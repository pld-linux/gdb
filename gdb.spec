Summary:     Symbolic debugger for C and other languages
Summary(de): Symbolischer Debugger für C und andere Sprachen 
Summary(fr): Débugger symbolique pour C et d'autres langages
Summary(pl): Symboliczny debugger dla C i innych jêzyków
Summary(tr): C ve diðer diller için sembolik hata ayýklayýcý
Name:        gdb
Version:     4.17.0.4
Release:     3
Copyright:   GPL
Group:       Development/Debuggers
Source:      ftp://ftp.cygnus.com/pub/gdb/%{name}-4.17.tar.gz
Patch0:      gdb-19980528-jbj.patch
Patch1:      ftp://ftp.yggdrasil.com/private/hjl/gdb-4.17-4.17.0.4.diff.gz
Patch2:      gdb-4.17-debug-threads.patch.gz
Prereq:      /sbin/install-info
Buildroot:   /tmp/%{name}-%{version}-root

%description
This is a full featured, command driven debugger. It allows you to
trace the exectuion of programs and examine their internal state
at any time. It works for C and C++ compiled with the GNU C compiler
gcc.

%description -l de
dem Sie die Ausführung von Programmen verfolgen und jederzeit den 
inneren Zustand überprüfen können. Er funktioniert für C und mit 
GNU C kompiliertes C++. 

%description -l fr
Débugger complet, piloté par commandes. Permet de tracer l'exécution
des programmes et d'examiner à tout moment leur état interne. Fonctionne
avec les binaires C et C++ compilés avec le compilateur C de GNU, gcc.

%description -l pl
Gdb jest rozbudowanym debugerem, pozwalaj±cym ¶ledziæ wykonanie
programu i badaæ jego stan wewnêtrzny. gdb umo¿liwia debugowanie
programów napisanych w C i C++ i skompilowanych przy pomocy kompilatora
C GNU (egcs).

%description -l tr
Bir komut arayüzü üzerinden programcýya programýný adým adým izleme (trace)
ve herhangi bir anda programýn durumunu inceleme olanaðý verir.

%prep
%setup -q -n gdb-4.17
%ifarch sparc
%patch0 -p1 -b .jbj
%endif

%patch1 -p2 -b .hjl

# XXX can't debug threads on sparc yet
%ifarch i386 alpha
%patch2 -p1 -b .debug_threads
%endif

%build
CC=gcc CFLAGS=$RPM_OPT_FLAGS ./configure --prefix=/usr 
make
make info

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/usr

make install install-info prefix=$RPM_BUILD_ROOT/usr 

strip $RPM_BUILD_ROOT/usr/bin/*

rm -f $RPM_BUILD_ROOT/usr/info/{bfd*,history*,readline*,standard*,texinfo*}
gzip -fn9 $RPM_BUILD_ROOT/usr/info/*info*

%post
install-info /usr/info/gdb.info.gz /usr/info/dir
install-info /usr/info/stabs.info.gz /usr/info/dir
install-info /usr/info/gdbint.info.gz /usr/info/dir

%preun
install-info --delete /usr/info/gdb.info.gz /usr/info/dir
install-info --delete /usr/info/stabs.info.gz /usr/info/dir
install-info --delete /usr/info/gdbint.info.gz /usr/info/dir

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644, root, root, 755)
%attr(755, root, root) /usr/bin/*
%attr(644, root,  man) /usr/man/man1/*
/usr/info/*info*

%changelog
* Sun Sep 27 1998 Marcin Korzonek <mkorz@shadow.eu.org>
- added pl translation.

* Thu May 07 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Thu Apr 30 1998 Cristian Gafton <gafton@redhat.com>
- upgraded to 4.17

* Wed Oct 08 1997 Erik Troan <ewt@redhat.com>
- updated to use a buildroot
- uses install-info

* Tue Aug 19 1997 Erik Troan <ewt@redhat.com>
- turned off mmalloc() support, which seems to annoy glibc (resulting in
  a quick core dump inside of getcwd())

* Thu Jul 17 1997 Erik Troan <ewt@redhat.com>
- built against glibc
