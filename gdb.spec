Summary:	A GNU source-level debugger for C, C++ and Fortran
Summary(de):	Symbolischer Debugger für C und andere Sprachen 
Summary(fr):	Débugger symbolique pour C et d'autres langages
Summary(pl):	Symboliczny odpluskwiacz dla C i innych jêzyków
Summary(tr):	C ve diðer diller için sembolik hata ayýklayýcý
Name:		gdb
Version:	5.0
Release:	1
License:	GPL
Group:		Development/Debuggers
Group(pl):	Programowanie/Odpluskwiacze
Source0:	ftp://ftp.gnu.org/pub/gnu/gdb/%{name}-%{version}.tar.bz2
#Patch0:	gdb-shared-readline.patch
BuildRequires:	ncurses-devel >= 5.0
BuildRequires:	readline-devel >= 4.1
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

%description -l tr
Bir komut arayüzü üzerinden programcýya programýný adým adým izleme
(trace) ve herhangi bir anda programýn durumunu inceleme olanaðý
verir.

%prep
%setup -q
#%patch0 -p1

%build
CFLAGS="$RPM_OPT_FLAGS" LDFLAGS="-s" \
./configure %{_target_platform} \
	--prefix=%{_prefix} \
	--infodir=%{_infodir} \
	--mandir=%{_mandir} \
	--enable-shared

%{__make}
%{__make} info

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_infodir}

%{__make} install \
	prefix=$RPM_BUILD_ROOT%{_prefix} \
	infodir=$RPM_BUILD_ROOT%{_infodir} \
	mandir=$RPM_BUILD_ROOT%{_mandir}

# install by hand
install gdb/doc/*.info* $RPM_BUILD_ROOT%{_infodir}

strip $RPM_BUILD_ROOT%{_bindir}/*

gzip -9nf $RPM_BUILD_ROOT{%{_infodir}/*info*,%{_mandir}/man?/*}

%post
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%postun
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*

%{_mandir}/man1/*
%{_infodir}/gdb*.info*
%{_infodir}/stabs*.info*
