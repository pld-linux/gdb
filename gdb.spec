%define		snap	20010313
Summary:	A GNU source-level debugger for C, C++ and Fortran
Summary(de):	Symbolischer Debugger für C und andere Sprachen 
Summary(fr):	Débugger symbolique pour C et d'autres langages
Summary(pl):	Symboliczny odpluskwiacz dla C i innych jêzyków
Summary(tr):	C ve diðer diller için sembolik hata ayýklayýcý
Name:		gdb
Version:	5.1
Release:	0.%{snap}
License:	GPL
Group:		Development/Debuggers
Group(pl):	Programowanie/Odpluskwiacze
Group(de):	Entwicklung/Debugger
Source0:	ftp://ftp.gnu.org/pub/gnu/gdb/%{name}-%{snap}.tar.gz
BuildRequires:	ncurses-devel >= 5.0
BuildRequires:	readline-devel >= 4.1
BuildRequires:	XFree86-devel
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
%setup -q -n %{name}-%{snap}

%build
# !! Don't enable shared here !! 
# This will cause serious problems --misiek
rm -rf obj-%{_target_platform} && install -d obj-%{_target_platform} && cd obj-%{_target_platform}  

../configure \
	--prefix=%{_prefix} \
	--libdir=%{_libdir} \
	--datadir=%{_datadir} \
	--infodir=%{_infodir} \
	--mandir=%{_mandir} \
	--disable-shared \
	--disable-tui \
	--enable-nls \
	--without-included-gettext \
	--enable-gdbcli \
	--enable-gdbmi \
	--enable-multi-ice \
	--enable-netrom \
	--enable-tui \
	--with-cpu=%{_target_cpu} \
	--with-x \
%ifnarch alpha
	--with-mmalloc \
%endif
%ifarch alpha sparc64
	--enable-64-bit-bfd \
%endif
	--with-mmap

			
%{__make}
%{__make} info

%install
rm -rf $RPM_BUILD_ROOT
cd obj-%{_target_platform}  
install -d $RPM_BUILD_ROOT%{_infodir}

%{__make} install install-info \
	prefix=$RPM_BUILD_ROOT%{_prefix} \
	bindir=$RPM_BUILD_ROOT%{_bindir} \
	sbindir=$RPM_BUILD_ROOT%{_sbindir} \
	infodir=$RPM_BUILD_ROOT%{_infodir} \
	includedir=$RPM_BUILD_ROOT%{_includedir} \
	libdir=$RPM_BUILD_ROOT%{_libdir} \
	mandir=$RPM_BUILD_ROOT%{_mandir}

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
