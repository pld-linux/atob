Summary:	Ain't Tape Oriented Backup
Summary(pl):	Ain't Tape Oriented Backup - system kopii zapasowych
Name:		atob
Version:	0.14.108
Release:	1
License:	GPL
Group:		Networking/Utilities
# Source0-md5:	835ddc8f017d1ec66ad357f231ee16ca
Source0:	http://ep09.kernel.pl/~djrzulf/atob-0.14.108.tar.bz2
#Source0:	cvs://cvs.pld.org.pl/cvsroot/%{name}-%{version}.tar.bz2
Vendor:		wrobell <wrobell@pld-linux.org>
Requires:	afio
Requires:	findutils
Requires:	grep
Requires:	sh-utils
Requires:	textutils
BuildRequires:	afio
BuildRequires:	findutils
BuildRequires:	grep
BuildRequires:	sh-utils
BuildRequires:	textutils
BuildRequires:	libxslt-progs
BuildRequires:	docbook-style-xsl
BuildRequires:	docbook-dtd42-xml
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

%description -l pl
Atob bazuje na tob (Tape Oriented Backup - system kopii zapasowych
zorientowany na ta¶my).  G³ówn± ró¿nic± pomiêdzy tob i atob jest to, ¿e
atob potrafi u¿ywaæ afio do tworzenia kopii zapasowych.

Pakiet atob to skrypt shella do tworzenia pe³nych, ró¿nicowych lub
przyrostowych kopii zapasowych. Kopie, zdefiniowane s± za pomoc±
`wolumenów'. Informacja o tym, co zosta³o zarchiwizowane jest
przechowywana w systemie. Archiwum zawiera dok³adn± dokumentacjê.

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
%config(noreplace) %verify(not md5 size mtime) %{_sysconfdir}/atob/atobrc
%attr(750,root,root) %dir %{_localstatedir}/atob
