Summary:	A GNU source-level debugger for C, C++ and Fortran
Summary(de):	Symbolischer Debugger f�r C und andere Sprachen 
Summary(fr):	D�bugger symbolique pour C et d'autres langages
Summary(pl):	Symboliczny odpluskwiacz dla C i innych j�zyk�w
Summary(tr):	C ve di�er diller i�in sembolik hata ay�klay�c�
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
dem Sie die Ausf�hrung von Programmen verfolgen und jederzeit den
inneren Zustand �berpr�fen k�nnen. Er funktioniert f�r C und mit GNU C
kompiliertes C++.

%description -l fr
D�bugger complet, pilot� par commandes. Permet de tracer l'ex�cution
des programmes et d'examiner � tout moment leur �tat interne.
Fonctionne avec les binaires C et C++ compil�s avec le compilateur C
de GNU, gcc.

%description -l pl
Gdb jest rozbudowanym odpluskwiaczem (debuggerem), pozwalaj�cym
�ledzi� wykonywanie programu i bada� jego stan wewn�trzny. Gdb
umo�liwia odpluskwianie program�w napisanych w C/C++ i skompilowanych
przy pomocy kompilatora GNU (gcc).

%description -l tr
Bir komut aray�z� �zerinden programc�ya program�n� ad�m ad�m izleme
(trace) ve herhangi bir anda program�n durumunu inceleme olana��
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
