Summary:	Ain't Tape Oriented Backup
Summary(pl):	System Kopii Zapasowych Niezorientowany na Ta¶my
Name:		atob
Version:	0.14.100
Release:	1
License:	GPL
Group:		Networking/Utilities
Source0:	cvs://cvs.pld.org.pl/cvsroot/%{name}-%{version}.tar.gz
Vendor:		wrobell <wrobell@ite.pl>
BuildArch:	noarch
Requires:	atob
Requires:	findutils
Requires:	grep
Requires:	sh-utils
Requires:	textutils
Requires:	tar
BuildRequires:	libxslt-progs
BuildRequires:	docbook-style-xsl
BuildRequires:	docbook-dtd42-xml
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
atob is based on tob (Tape Oriented Backup). The main difference
between tob and atob is that only afio is supported to create backups.

The atob package presents a shell-script to create and maintain full
or differential or incremental backups. Backups are defined by a
`volume', listings of backups are kept. The archive contains extensive
documentation.

%description -l pl
atob bazuje na tob (System Kopii Zapasowych zorientowany na Ta¶my).
G³ówn± ró¿nic± pomiêdzy tob i atob jest to, ¿e atob potrafi u¿ywaæ
afio do tworzenia kopii zapasowych.

Pakiet atob to skrypt shella do tworzenia pe³nych, ró¿nicowych lub
inkrementalnych kopii zapasowych. Kopie zdefiniowane s± poprzez
`volumeny', listy kopii s± utrzymywane. Archiwum zawiera dok³adn±
dokumentacjê.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

cd doc && xsltproc -o atob.html html.xsl atob.docb

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/*.html AUTHORS README TODO
%attr(755,root,root) %{_sbindir}/*
%{_mandir}/man?/*
%dir %{_sysconfdir}/atob
%dir %{_sysconfdir}/atob/volumes
%config(noreplace) %verify(not md5 size mtime) %{_sysconfdir}/atob/atobrc
%attr(750,root,root) %dir %{_var}/lib/atob
