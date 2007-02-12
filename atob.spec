Summary:	Ain't Tape Oriented Backup
Summary(pl.UTF-8):   Ain't Tape Oriented Backup - system kopii zapasowych
Name:		atob
Version:	0.14.108
Release:	1
License:	GPL
Group:		Networking/Utilities
Source0:	http://ep09.pld-linux.org/~djrzulf/%{name}-%{version}.tar.bz2
# Source0-md5:	835ddc8f017d1ec66ad357f231ee16ca
#Source0:	cvs://cvs.pld.org.pl/cvsroot/%{name}-%{version}.tar.bz2
Vendor:		wrobell <wrobell@pld-linux.org>
BuildRequires:	afio
BuildRequires:	docbook-dtd42-xml
BuildRequires:	docbook-style-xsl
BuildRequires:	grep
BuildRequires:	libxslt-progs
BuildRequires:	sh-utils
BuildRequires:	textutils
Requires:	afio
Requires:	findutils
Requires:	grep
Requires:	sh-utils
Requires:	textutils
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_localstatedir	%{_var}/lib/atob

%description
Atob is based on tob (Tape Oriented Backup). The main difference
between tob and atob is that only afio is supported to create backups.

The atob package presents a shell-script to create and maintain full
or differential or incremental backups. Backups are defined by a
`volume', listings of backups are kept. The archive contains extensive
documentation.

%description -l pl.UTF-8
Atob bazuje na tob (Tape Oriented Backup - system kopii zapasowych
zorientowany na taśmy). Główną różnicą pomiędzy tob i atob jest to, że
atob potrafi używać afio do tworzenia kopii zapasowych.

Pakiet atob to skrypt shella do tworzenia pełnych, różnicowych lub
przyrostowych kopii zapasowych. Kopie, zdefiniowane są za pomocą
`wolumenów'. Informacja o tym, co zostało zarchiwizowane jest
przechowywana w systemie. Archiwum zawiera dokładną dokumentację.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

cd doc && xsltproc --xinclude html-chunk.xsl atob.docb

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/*.{html,css} AUTHORS README TODO examples/[a-z]*
%attr(755,root,root) %{_sbindir}/*
%dir %{_sysconfdir}/atob
%dir %{_sysconfdir}/atob/volumes
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/atob/atobrc
%attr(750,root,root) %dir %{_localstatedir}/atob
