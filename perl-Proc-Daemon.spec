%include	/usr/lib/rpm/macros.perl
Summary:	Proc-Daemon perl module
Summary(pl):	Modu³ perla Proc-Daemon
Name:		perl-Proc-Daemon
Version:	0.02
Release:	3
Copyright:	GPL
Group:		Development/Languages/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/Proc/Proc-Daemon-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.005_03-14
%requires_eq	perl
Requires:	%{perl_sitearch}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Proc-Daemon - Run Perl program as a daemon process. 

%description -l pl
Proc-Daemon - umo¿liwia uruchamianie programów perla w trybie demona.

%prep
%setup -q -n Proc-Daemon-%{version}

%build
perl Makefile.PL
make

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

(
  cd $RPM_BUILD_ROOT%{perl_sitearch}/auto/Proc/Daemon
  sed -e "s#$RPM_BUILD_ROOT##" .packlist >.packlist.new
  mv .packlist.new .packlist
)

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man3/* \
        Changes README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {Changes,README}.gz

%{perl_sitelib}/Proc/Daemon.pm
%{perl_sitearch}/auto/Proc/Daemon

%{_mandir}/man3/*
