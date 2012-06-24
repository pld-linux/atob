Summary:	Ain't Tape Oriented Backup
Summary(pl):	Ain't Tape Oriented Backup - system kopii zapasowych
Name:		atob
Version:	0.14.101
Release:	1
License:	GPL
Group:		Networking/Utilities
Source0:	cvs://cvs.pld.org.pl/cvsroot/%{name}-%{version}.tar.gz
Vendor:		wrobell <wrobell@pld.org.pl>
BuildArch:	noarch
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
zorientowany na ta�my).  G��wn� r�nic� pomi�dzy tob i atob jest to, �e
atob potrafi u�ywa� afio do tworzenia kopii zapasowych.

Pakiet atob to skrypt shella do tworzenia pe�nych, r�nicowych lub
przyrostowych kopii zapasowych. Kopie, zdefiniowane s� za pomoc�
`wolumen�w'. Informacja o tym, co zosta�o zarchiwizowane jest
przechowywana w systemie. Archiwum zawiera dok�adn� dokumentacj�.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

cd doc && xsltproc --xinclude -o atob.html html.xsl atob.docb

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/*.html AUTHORS README TODO examples/*.*
%attr(755,root,root) %{_sbindir}/*
%{_mandir}/man?/*
%dir %{_sysconfdir}/atob
%dir %{_sysconfdir}/atob/volumes
%config(noreplace) %verify(not md5 size mtime) %{_sysconfdir}/atob/atobrc
%attr(750,root,root) %dir %{_localstatedir}/atob
