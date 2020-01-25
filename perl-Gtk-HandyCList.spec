#
# Conditional build:
%bcond_without	tests	# do not perform "make test"

%define		pdir	Gtk
%define		pnam	HandyCList
Summary:	Gtk::HandyCList - a more Perl-friendly columned list
Summary(pl.UTF-8):	Gtk::HandyCList - bardziej przyjazny Perlowi widget listy kolumnowej
Name:		perl-Gtk-HandyCList
Version:	0.03
Release:	1
License:	unknown
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	d61e94a7bfede08010b75948123c0e7b
URL:		http://search.cpan.org/dist/Gtk-HandyCList/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-gnome
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a version of Gtk::CList which takes care of some common things
for the programmer. For instance, it keeps track of what's stored in
the list, so you don't need to keep a separate array; when the column
titles are clicked, the list will be re-sorted according to
user-supplied functions or some default rules. It allows you to
reference columns by name, instead of by number.

%description -l pl.UTF-8
To jest wersja Gtk::Clist dbająca za programistę o parę powszechnych
zachowań. Na przykład śledzi co jest zapisane w liście, więc nie
trzeba przechowywać oddzielnej tablicy; po kliknięciu na tytuły lista
zostanie przesortowana zgodnie z podanymi funkcjami lub jakimiś
domyślnymi regułami. Widget pozwala na odwoływanie się do kolumn po
nazwie zamiast po numerze.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%dir %{perl_vendorlib}/Gtk
%{perl_vendorlib}/Gtk/HandyCList.pm
%{_mandir}/man3/*
