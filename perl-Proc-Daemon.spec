%include	/usr/lib/rpm/macros.perl
%define	pdir	Proc
%define	pnam	Daemon
Summary:	Proc::Daemon perl module
Summary(pl):	Modu³ perla Proc::Daemon
Name:		perl-Proc-Daemon
Version:	0.02
Release:	9
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	aed8014890240b1fb8b6a8bb18e3decf
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-devel >= 5.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Proc::Daemon - Run Perl program as a daemon process.

%description -l pl
Proc::Daemon - umo¿liwia uruchamianie programów perla w trybie demona.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor 
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Proc/Daemon.pm
%{_mandir}/man3/*
