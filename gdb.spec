Summary:	Symbolic debugger for C and other languages
Summary(de):	Symbolischer Debugger f�r C und andere Sprachen 
Summary(fr):	D�bugger symbolique pour C et d'autres langages
Summary(pl):	Symboliczny debugger dla C i innych j�zyk�w
Summary(tr):	C ve di�er diller i�in sembolik hata ay�klay�c�
Name:		gdb
Version:	4.18
Release:	4
Copyright:	GPL
Group:		Development/Debuggers
Group(pl):	Programowanie/Odpluskwiacze
Source:		ftp://sourceware.cygnus.com/pub/gdb/%{name}-%{version}.tar.bz2
Patch0:		gdb-info.patch
Prereq:		/sbin/install-info
Buildroot:	/tmp/%{name}-%{version}-root

%description
This is a full featured, command driven debugger. It allows you to
trace the exectuion of programs and examine their internal state
at any time. It works for C and C++ compiled with the GNU C compiler
gcc.

%description -l de
dem Sie die Ausf�hrung von Programmen verfolgen und jederzeit den 
inneren Zustand �berpr�fen k�nnen. Er funktioniert f�r C und mit 
GNU C kompiliertes C++. 

%description -l fr
D�bugger complet, pilot� par commandes. Permet de tracer l'ex�cution
des programmes et d'examiner � tout moment leur �tat interne. Fonctionne
avec les binaires C et C++ compil�s avec le compilateur C de GNU, gcc.

%description -l pl
Gdb jest rozbudowanym debugerem, pozwalaj�cym �ledzi� wykonanie
programu i bada� jego stan wewn�trzny. gdb umo�liwia debugowanie
program�w napisanych w C i C++ i skompilowanych przy pomocy kompilatora
C GNU (egcs).

%description -l tr
Bir komut aray�z� �zerinden programc�ya program�n� ad�m ad�m izleme (trace)
ve herhangi bir anda program�n durumunu inceleme olana�� verir.

%prep
%setup -q
%patch -p1

%build
CFLAGS="$RPM_OPT_FLAGS" LDFLAGS="-s" \
./configure \
	--prefix=%{_prefix} \
	--infodir=%{_infodir} \
	--mandir=%{_mandir} \
	%{_target_platform} 

make
make info

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_prefix}

make \
	prefix=$RPM_BUILD_ROOT%{_prefix} \
	infodir=$RPM_BUILD_ROOT%{_infodir} \
	mandir=$RPM_BUILD_ROOT%{_mandir} \
	install

# install by hand
install gdb/doc/*.info* $RPM_BUILD_ROOT%{_infodir}

strip $RPM_BUILD_ROOT%{_bindir}/*

rm -f $RPM_BUILD_ROOT%{_infodir}{bfd*,history*,readline*,standard*,texinfo*}

gzip -fn9 $RPM_BUILD_ROOT{%{_infodir}/*info*,%{_mandir}/man?/*}

%post
/sbin/install-info %{_infodir}/gdb.info.gz	/etc/info-dir
/sbin/install-info %{_infodir}/stabs.info.gz	/etc/info-dir
/sbin/install-info %{_infodir}/gdbint.info.gz	/etc/info-dir

%preun
if [ "$1" = 0 ]; then
	/sbin/install-info --delete %{_infodir}/gdb.info.gz	/etc/info-dir
	/sbin/install-info --delete %{_infodir}/stabs.info.gz	/etc/info-dir
	/sbin/install-info --delete %{_infodir}/gdbint.info.gz	/etc/info-dir
fi

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*

%{_mandir}/man1/*
%{_infodir}/gd*.info*
%{_infodir}/stabs*.info*

%changelog
* Sun May 16 1999 Artur Frysiak <wiget@pld.org.pl>
  [4.18-3]
- configure with --host=%{_host_alias} instead --host=%{_host} to prevent build
  crosscompiler prefix (eg i586-pc-linux-gdb)
- using more rpm macros

* Fri May 14 1999 Tomasz K�oczko <kloczek@rudy.mif.pg.gda.pl>
  [4.18-2]
- now package is FHS 2.0 compliant.

* Tue Apr 13 1999 Tomasz K�oczko <kloczek@rudy.mif.pg.gda.pl>
  [4.18-1]
- standarized {un}registering info pages (added gdb-info.patch).
- removed man group from man pages.

* Mon Apr 12 1999 Marcin Dalecki <dalecki@cs.net.pl>
  [4.18]
- updated to this fresh new release.

* Sat Oct 17 1998 Tomasz K�oczko <kloczek@rudy.mif.pg.gda.pl>
  [4.17.0.4-3]
- added gdb-readline_ncurses.patch for compiling gdb agains shared
  libredline and libncurses.

* Sun Sep 27 1998 Marcin Korzonek <mkorz@shadow.eu.org>
- added pl translation,
- major changes for PLD Linux
