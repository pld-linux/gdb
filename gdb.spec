Summary:	A GNU source-level debugger for C, C++ and Fortran
Summary(de):	Symbolischer Debugger f�r C und andere Sprachen
Summary(es):	Depurador de programas C y otras lenguajes
Summary(fr):	D�bugger symbolique pour C et d'autres langages
Summary(pl):	Symboliczny odpluskwiacz dla C i innych j�zyk�w
Summary(pt_BR):	Depurador de programas C e outras linguagens
Summary(ru):	������������� �������� ��� C � ������ ������
Summary(tr):	C ve di�er diller i�in sembolik hata ay�klay�c�
Summary(uk):	���������� צ������� ��� � �� ����� ���
Summary(zh_CN):	[����]C���������Եĵ�����
Summary(zh_TW):	[.-A�}�o]C�M.$)B��.-A�L�y.$)B�����ով�
Name:		gdb
Version:	5.3
Release:	1
License:	GPL
Group:		Development/Debuggers
Source0:	ftp://ftp.gnu.org/pub/gnu/gdb/%{name}-%{version}.tar.gz
Source1:	http://www.mif.pg.gda.pl/homepages/ankry/man-PLD/%{name}-non-english-man-pages.tar.bz2
Patch0:		%{name}-gettext.patch
Patch1:		%{name}-ncurses.patch
Patch2:		%{name}-readline.patch
Patch3:		%{name}-info.patch
Patch4:		%{name}-procfs.patch
Patch5:		%{name}-passflags.patch
BuildRequires:	XFree86-devel
BuildRequires:	autoconf >= 2.53
BuildRequires:	libtool
BuildRequires:	ncurses-devel >= 5.2
BuildRequires:	readline-devel >= 4.2
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

%description -l es
Este es un debugger orientado a comandos repleto de caracter�sticas.
Te permite rastrear la ejecuci�n de programas y examinar su estado
interno a cualquier momento. Funciona para C y C++ compilado con el
compilador GNU C.

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

%description -l pt_BR
Este � um debugger orientado a comandos repleto de caracter�sticas.
Ele permite � voc� rastrear a execu��o de programas e examinar o seu
estado interno a qualquer momento. Ele funciona para para C e C++
compilado com o compilador GNU C.

%description -l ru
��� ����������� ��������, ����������� ���������. �� ���������
������������ ���������� �������� � ������� �� ���������� ��������� �
����� ������ �������. �������� � ����������� �� C � C++,
����������������� GNU ������������ C (gcc, egcs, pgcc).

%description -l tr
Bir komut aray�z� �zerinden programc�ya program�n� ad�m ad�m izleme
(trace) ve herhangi bir anda program�n durumunu inceleme olana��
verir.

%description -l uk
�� �����æ���� צ�������, �� ���դ���� ���������. ��� ������Ѥ
��������� ��������� ������� �� ������� �� ����Ҧ�Φ� ���� � ��צ�����
������ ����. ������ � ���������� �� C �� C++, ����Ц���������
���Ц�������� GNU C (gcc, egcs, pgcc).

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1

%build
cd gdb
%{__autoconf}
cd doc
%{__autoconf}
cd ../testsuite
%{__autoconf}
cd gdb.arch
%{__autoconf}
cd ../gdb.asm
%{__autoconf}
cd ../gdb.base
%{__autoconf}
cd ../gdb.c++
%{__autoconf}
cd ../gdb.chill
%{__autoconf}
cd ../gdb.disasm
%{__autoconf}
#cd ../gdb.fortran
#%{__autoconf}
cd ../gdb.java
%{__autoconf}
cd ../gdb.mi
%{__autoconf}
cd ../gdb.stabs
%{__autoconf}
cd ../gdb.threads
%{__autoconf}
cd ../gdb.trace
%{__autoconf}
cd ../../gdbserver
%{__autoconf}
cd ../..
# !! Don't enable shared here !!
# This will cause serious problems --misiek
%configure2_13 \
	--disable-shared \
	--enable-nls \
	--without-included-gettext \
	--without-included-regex \
	--enable-gdcli \
	--enable-gdbmi \
	--enable-multi-ice \
	--enable-netrom \
	--with-cpu=%{_target_cpu} \
	--enable-tui \
%ifnarch alpha
	--with-mmalloc
%endif

# something is wrong after above - e.g. $exeext=="no" - fix it:
cd gdb
%configure
cd ..

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
