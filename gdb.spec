Summary:	Symbolic debugger for C and other languages
Summary(de):	Symbolischer Debugger für C und andere Sprachen 
Summary(fr):	Débugger symbolique pour C et d'autres langages
Summary(pl):	Symboliczny debugger dla C i innych jêzyków
Summary(tr):	C ve diðer diller için sembolik hata ayýklayýcý
Name:		gdb
Version:	4.18
Release:	4
Copyright:	GPL
Group:		Development/Debuggers
Group(pl):	Programowanie/Odpluskwiacze
Source:		ftp://sourceware.cygnus.com/pub/gdb/%{name}-%{version}.tar.bz2
Patch0:		gdb-info.patch
Prereq:		/usr/sbin/fix-info-dir
Buildroot:	/tmp/%{name}-%{version}-root

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
/usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%preun
/usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*

%{_mandir}/man1/*
%{_infodir}/gd*.info*
%{_infodir}/stabs*.info*
