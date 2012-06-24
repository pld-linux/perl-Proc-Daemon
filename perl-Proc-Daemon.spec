%include	/usr/lib/rpm/macros.perl
Summary:	Proc-Daemon perl module
Summary(pl):	Modu� perla Proc-Daemon
Name:		perl-Proc-Daemon
Version:	0.02
Release:	4
License:	GPL
Group:		Development/Languages/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(pl):	Programowanie/J�zyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Proc/Proc-Daemon-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Proc-Daemon - Run Perl program as a daemon process.

%description -l pl
Proc-Daemon - umo�liwia uruchamianie program�w perla w trybie demona.

%prep
%setup -q -n Proc-Daemon-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf Changes README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%{perl_sitelib}/Proc/Daemon.pm
%{_mandir}/man3/*
