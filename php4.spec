#
# Conditional build:
# bcond_on_oracle  - with oracle support 
# bcond_on_oci8    - with oci8 support
# bcond_on_java    - with Java support
# bcond_on_openssl - with OpenSSL support
# bcond_off_imap   - without IMAP support
# bcond_off_ldap   - without LDAP support
# bcond_off_odbc   - without ODBC support
# bcond_off_snmp   - without SNMP support
#
Summary:	The PHP HTML-embedded scripting language for use with Apache
Summary(fr):	Le langage de script embarque-HTML PHP pour Apache
Summary(pl):	J�zyk skryptowy PHP -- u�ywany wraz z serwerem Apache
Name:		php
Version:	4.0.5
Release:	0.5
Epoch:		1
Group:		Libraries
Group(de):	Libraries
Group(es):	Bibliotecas
Group(fr):	Librairies
Group(pl):	Biblioteki
License:	The PHP license (see "LICENSE" file included in distribution)
Source0:	http://www.php.net/distributions/%{name}-%{version}.tar.gz
Source1:	FAQ.php
Source2:	%{name}.ini
Source3:	zend.gif
Source4:	http://www.php.net/distributions/manual.tar.gz
Source5:	php-module-install
Patch0:		%{name}-imap.patch
Patch1:		%{name}-mysql-socket.patch
Patch2:		%{name}-mail.patch
Patch3:		%{name}-link-libs.patch
Patch4:		%{name}-DESTDIR.patch
Patch5:		%{name}-gd-shared.patch
Patch6:		%{name}-session-path.patch
Patch7:		%{name}-libtool_version_check_fix.patch
Patch8:		%{name}-pdflib.patch
Patch9:		%{name}-am_ac_lt.patch
Patch10:	%{name}-fastcgi.patch
Patch11:	%{name}-shared.patch
Icon:		php4.gif
URL:		http://www.php.net/
BuildRequires:	apache(EAPI)-devel
BuildRequires:	zip
BuildRequires:	bison
BuildRequires:	flex
BuildRequires:	db3-devel >= 3.1.17
BuildRequires:	freetype1-devel
BuildRequires:	gd-devel >= 1.8.3
BuildRequires:	gdbm-devel
%{!?bcond_off_imap:BuildRequires: imap-devel >= 4.7b-1}
# I think jdk is better for java
# BuildRequires:	jdk
%{?bcond_on_java:BuildRequires:	kaffe-devel}
BuildRequires:	libjpeg-devel
BuildRequires:	libltdl-devel >= 1.4
BuildRequires:	libpng >= 1.0.8
BuildRequires:	libtiff-devel
BuildRequires:	libtool
BuildRequires:	mm-devel >= 1.1.3
BuildRequires:	mysql-devel >= 3.23.32
%{!?bcond_off_ldap:BuildRequires: openldap-devel >= 2.0}
BuildRequires:	pam-devel
BuildRequires:	pdflib-devel >= 4.0.0
#BuildRequires:	libxml-devel >= 2.0.0
BuildRequires:	postgresql-devel
BuildRequires:	recode-devel >= 3.5d-3
BuildRequires:	t1lib-devel
%{!?bcond_off_odbc:BuildRequires: unixODBC-devel}
BuildRequires:	zlib-devel >= 1.0.9
%{!?bcond_off_snmp:BuildRequires: ucd-snmp-devel >= 4.2.1-8}
BuildRequires:	libmcrypt-devel >= 2.4.4
BuildRequires:	mhash-devel
BuildRequires:	bzip2-devel
BuildRequires:	gmp-devel
BuildRequires:	curl-devel
#BuildRequires:	fastcgi-devkit
%if %(expr %{?bcond_on_openssl:1}%{!?bcond_on_openssl:0} + %{!?bcond_off_ldap:1}%{?bcond_off_ldap:0})
BuildRequires:	openssl-devel >= 0.9.6a
%endif
Prereq:		apache(EAPI) >= 1.3.9
Prereq:		perl
Prereq:		%{_sbindir}/apxs
PreReq:		%{name}-common = %{version}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	phpfi

%define		_sysconfdir	/etc/php
# check ZEND_MODULE_API_NO in  Zend/modules.h
%define 	extensionsdir %{_libdir}/php/extensions/no-debug-non-zts-20001222

%description
PHP is an HTML-embedded scripting language. PHP attempts to make it
easy for developers to write dynamically generated web pages. PHP also
offers built-in database integration for several commercial and
non-commercial database management systems, so writing a
database-enabled web page with PHP is fairly simple. The most common
use of PHP coding is probably as a replacement for CGI scripts. The
mod_php module enables the Apache web server to understand and process
the embedded PHP language in web pages. This package contains PHP
version %{version}. If you use applications which specifically rely on
PHP/FI (PHP v2 and earlier), you should instead install the PHP/FI
module contained in the phpfi package. If you're just starting with
PHP, you should install this package. You'll also need to install the
Apache web server.

%description -l fr
PHP est un langage de script embarque dans le HTM. PHP essaye de
rendre simple aux developpeurs d'ecrire des pages web generees
dynamiquement. PHP incorpore egalement une integration avec plusieurs
systemes de gestion de bases de donnees commerciaux et
non-connerciaux, qui rent facile la creation de pages web liees avec
des bases de donnees. L'utilisation la plus commune de PHP est
probablement en remplacement de scripts CGI. Le module mod_php permet
au serveur web apache de comprendre et de traiter le langage PHP
integre dans des pages web. Ce package contient PHP version
%{version}. Si vous utilisez des applications qui utilisent
specifiquement PHP/FI, vous devrez installer le module PHP/FI inclus
dans le package mod_php. Si vous debutez avec PHP, vous devriez
installer ce package. Vous aurez egalement besoin d'installer le
serveur web Apache.

%description -l pl
PHP jest j�zykiem skryptowym, kt�rego polecenia umieszcza si� w
plikach HTML. Pakiet ten zawiera modu� przeznaczony dla serwera HTTP
(jak np. Apache), kt�ry interpretuje te polecenia. Umo�liwia to
tworzenie dynamicznie stron WWW. Spora cz�� sk�adni PHP zapo�yczona
zosta�a z j�zyk�w: C, Java i Perl.

%package cgi
Summary:	PHP as CGI program
Summary(pl):	PHP jako program CGI
Group:		Libraries
Group(de):	Libraries
Group(es):	Bibliotecas
Group(fr):	Librairies
Group(pl):	Biblioteki
PreReq:		%{name}-common = %{version}

%description cgi
PHP as CGI program.

%description cgi -l pl
PHP jako program CGI.

%package common
Summary:	Common files nneded by both apache module and CGI
Summary(pl):	Wsp�lne pliki dla modu�u apacha i programu CGI
Group:		Libraries
Group(de):	Libraries
Group(es):	Bibliotecas
Group(fr):	Librairies
Group(pl):	Biblioteki

%description common
Common files needed by both apache module and CGI.

%description common -l pl
Wsp�lne pliki dla modu�u apacha i programu CGI.

%package mysql
Summary:	MySQL database module for PHP
Summary(pl):	Modu� bazy danych MySQL dla PHP
Group:		Libraries
Group(de):	Libraries
Group(es):	Bibliotecas
Group(fr):	Librairies
Group(pl):	Biblioteki
PreReq:		%{name}-common = %{version}

%description mysql
This is a dynamic shared object (DSO) for Apache that will add MySQL
database support to PHP. If you need back-end support for MySQL, you
should install this package in addition to the main %{name} package.

%description mysql -l pl
Modu� PHP umo�liwiaj�cy dost�p do bazy danych MySQL.

%package pgsql
Summary:	PostgreSQL database module for PHP
Summary(pl):	Modu� bazy danych PostgreSQL dla PHP
Group:		Libraries
Group(de):	Libraries
Group(es):	Bibliotecas
Group(fr):	Librairies
Group(pl):	Biblioteki
PreReq:		%{name}-common = %{version}

%description pgsql
This is a dynamic shared object (DSO) for Apache that will add
PostgreSQL database support to PHP. If you need back-end support for
PostgreSQL, you should install this package in addition to the main
%{name} package.

%description pgsql -l pl
Modu� PHP umo�liwiaj�cy dost�p do bazy danych PostgreSQL.

%package oci8
Summary:	Oracle 8 database module for PHP
Summary(pl):	Modu� bazy danych Oracle 8 dla PHP
Group:		Libraries
Group(de):	Libraries
Group(es):	Bibliotecas
Group(fr):	Librairies
Group(pl):	Biblioteki
PreReq:		%{name}-common = %{version}
Autoreq:	false

%description oci8
This is a dynamic shared object (DSO) for Apache that will add Oracle
8 database support to PHP. If you need back-end support for Oracle 8,
you should install this package in addition to the main %{name}
package.

%description oci8 -l pl
Modu� PHP umo�liwiaj�cy dost�p do bazy danych Oracle 8.

%package oracle
Summary:	Oracle 7 database module for PHP
Summary(pl):	Modu� bazy danych Oracle 7 dla PHP
Group:		Libraries
Group(de):	Libraries
Group(es):	Bibliotecas
Group(fr):	Librairies
Group(pl):	Biblioteki
PreReq:		%{name}-common = %{version}
Autoreq:	false

%description oracle
This is a dynamic shared object (DSO) for Apache that will add Oracle
7 database support to PHP. If you need back-end support for Oracle 7,
you should install this package in addition to the main %{name}
package.

%description oracle -l pl
Modu� PHP umo�liwiaj�cy dost�p do bazy danych Oracle 7.

%package gd
Summary:	GD extension module for PHP
Summary:	Modu� GD dla PHP
Group:		Libraries
Group(de):	Libraries
Group(es):	Bibliotecas
Group(fr):	Librairies
Group(pl):	Biblioteki
PreReq:		%{name}-common = %{version}

%description gd
This is a dynamic shared object (DSO) for Apache that will add GD
support to PHP. You should install this package in addition to the
main %{name} package if you want to create and manipulate images with
PHP.

%description gd -l pl
Modu� PHP umo�liwiaj�cy korzystanie z biblioteki GD - do obr�bki
obrazk�w z poziomu PHP.

%package java
Summary:	Java extension module for PHP
Summary(pl):	Modu� Javy dla PHP
Group:		Libraries
Group(de):	Libraries
Group(es):	Bibliotecas
Group(fr):	Librairies
Group(pl):	Biblioteki
PreReq:		%{name}-common = %{version}

%description java
This is a dynamic shared object (DSO) for Apache that will add JAVA
support to PHP. This extension provides a simple and effective means
for creating and invoking methods on Java objects from PHP.

%description java -l pl
Modu� PHP dodaj�cy wsparcie dla Javy. Umo�liwia odwo�ywanie si� do
obiekt�w Javy z poziomu PHP.

%package xml
Summary:	XML extension module for PHP
Summary(pl):	Modu� XML dla PHP
Group:		Libraries
Group(de):	Libraries
Group(es):	Bibliotecas
Group(fr):	Librairies
Group(pl):	Biblioteki
PreReq:		%{name}-common = %{version}

%description xml
This is a dynamic shared object (DSO) for Apache that will add XML
support to PHP. This extension lets you create XML parsers and then
define handlers for different XML events. If you want to be able to
parse XML documents you should install this package in addition to the
main %{name} package.

%description xml -l pl
Modu� PHP umo�liwiaj�cy parsowanie plik�w XML i obs�ug� zdarze�
zwi�zanych z tymi plikami.

%package dba
Summary:	DBA extension module for PHP
Summary(pl):	Modu� DBA dla PHP
Group:		Libraries
Group(de):	Libraries
Group(es):	Bibliotecas
Group(fr):	Librairies
Group(pl):	Biblioteki
PreReq:		%{name}-common = %{version}

%description dba
This is a dynamic shared object (DSO) for Apache that will add
flat-file databases (DBA) support to PHP.

#%description dba -l pl

%package odbc
Summary:	ODBC extension module for PHP
Summary(pl):	Modu� ODBC dla PHP
Group:		Libraries
Group(de):	Libraries
Group(es):	Bibliotecas
Group(fr):	Librairies
Group(pl):	Biblioteki
PreReq:		%{name}-common = %{version}

%description odbc
This is a dynamic shared object (DSO) for Apache that will add ODBC
support to PHP.

%description odbc -l pl
Modu� PHP ze wsparciem dla ODBC.

%package calendar
Summary:	Calendar extension module for PHP
Summary(pl):	Modu� funkcji kalendarza dla PHP
Group:		Libraries
Group(de):	Libraries
Group(es):	Bibliotecas
Group(fr):	Librairies
Group(pl):	Biblioteki
PreReq:		%{name}-common = %{version}

%description calendar
This is a dynamic shared object (DSO) for Apache that will add
calendar support to PHP.

#%description calendar -l pl

%package dbase
Summary:	DBase extension module for PHP
Summary(pl):	Modu� DBase dla PHP
Group:		Libraries
Group(de):	Libraries
Group(es):	Bibliotecas
Group(fr):	Librairies
Group(pl):	Biblioteki
PreReq:		%{name}-common = %{version}

%description dbase
This is a dynamic shared object (DSO) for Apache that will add DBase
support to PHP.

%description dbase -l pl
Modu� PHP ze wsparciem dla DBase.

%package filepro
Summary:	FilePro extension module for PHP
Summary(pl):	Modu� FilePro dla PHP
Group:		Libraries
Group(de):	Libraries
Group(es):	Bibliotecas
Group(fr):	Librairies
Group(pl):	Biblioteki
PreReq:		%{name}-common = %{version}

%description filepro
This is a dynamic shared object (DSO) for Apache that will add FilePro
support to PHP.

#%description filepro -l pl

%package posix
Summary:	POSIX extension module for PHP
Summary(pl):	Modu� POSIX dla PHP
Group:		Libraries
Group(de):	Libraries
Group(es):	Bibliotecas
Group(fr):	Librairies
Group(pl):	Biblioteki
PreReq:		%{name}-common = %{version}

%description posix
This is a dynamic shared object (DSO) for Apache that will add POSIX
functions support to PHP.

%description posix -l pl
Modu� PHP umo�liwiaj�cy korzystanie z funkcji POSIX.

%package pcre
Summary:	PCRE extension module for PHP
Summary(pl):	Modu� PCRE dla PHP
Group:		Libraries
Group(de):	Libraries
Group(es):	Bibliotecas
Group(fr):	Librairies
Group(pl):	Biblioteki
PreReq:		%{name}-common = %{version}

%description pcre
This is a dynamic shared object (DSO) for Apache that will add Perl
Compatible Regular Expression support to PHP.

%description pcre -l pl
Modu� PHP umo�liwiaj�cy korzystanie z perlowych wyra�e� regularnych
(Perl Compatible Regular Expressions)

%package sysvsem
Summary:	SysV sem extension module for PHP
Summary(pl):	Modu� SysV sem dla PHP
Group:		Libraries
Group(de):	Libraries
Group(es):	Bibliotecas
Group(fr):	Librairies
Group(pl):	Biblioteki
PreReq:		%{name}-common = %{version}

%description sysvsem
This is a dynamic shared object (DSO) for Apache that will add SysV
semafores support to PHP.

%description sysvsem -l pl
Modu� PHP umo�liwiaj�cy korzystanie z semafor�w SysV.

%package sysvshm
Summary:	SysV shm extension module for PHP
Summary(pl):	Modu� SysV shm dla PHP
Group:		Libraries
Group(de):	Libraries
Group(es):	Bibliotecas
Group(fr):	Librairies
Group(pl):	Biblioteki
PreReq:		%{name}-common = %{version}

%description sysvshm
This is a dynamic shared object (DSO) for Apache that will add SysV
Shared Memory support to PHP.

%description sysvshm -l pl
Modu� PHP umo�liwiaj�cy korzystanie z pami�ci dzielonej SysV.

%package yp
Summary:	NIS (yp) extension module for PHP
Summary(pl):	Modu� NIS (yp) dla PHP
Group:		Libraries
Group(de):	Libraries
Group(es):	Bibliotecas
Group(fr):	Librairies
Group(pl):	Biblioteki
PreReq:		%{name}-common = %{version}

%description yp
This is a dynamic shared object (DSO) for Apache that will add NIS
(Yellow Pages) support to PHP.

#%description yp -l pl

%package bcmath
Summary:	bcmath extension module for PHP
Summary(pl):	Modu� bcmath dla PHP
Group:		Libraries
Group(de):	Libraries
Group(es):	Bibliotecas
Group(fr):	Librairies
Group(pl):	Biblioteki
PreReq:		%{name}-common = %{version}

%description bcmath
This is a dynamic shared object (DSO) for Apache that will add bc
style precision math functions support to PHP.

%description bcmath -l pl
Modu� PHP umo�liwiaj�cy korzystanie z dok�adnych funkcji
matematycznych takich jak w programie bc.

%package ftp
Summary:	FTP extension module for PHP
Summary(pl):	Modu� FTP dla PHP
Group:		Libraries
Group(de):	Libraries
Group(es):	Bibliotecas
Group(fr):	Librairies
Group(pl):	Biblioteki
PreReq:		%{name}-common = %{version}

%description ftp
This is a dynamic shared object (DSO) for Apache that will add FTP
support to PHP.

#%description ftp -l pl

%package zlib
Summary:	Zlib extension module for PHP
Summary(pl):	Modu� zlib dla PHP
Group:		Libraries
Group(de):	Libraries
Group(es):	Bibliotecas
Group(fr):	Librairies
Group(pl):	Biblioteki
PreReq:		%{name}-common = %{version}

%description zlib
This is a dynamic shared object (DSO) for Apache that will add
compression (zlib) support to PHP.

%description zlib -l pl
Modu� PHP umo�liwiaj�cy u�ywanie kompresji (poprzez bibliotek� zlib).

%package exif
Summary:	exifextension module for PHP
Summary(pl):	Modu� exif dla PHP
Group:		Libraries
Group(de):	Libraries
Group(es):	Bibliotecas
Group(fr):	Librairies
Group(pl):	Biblioteki
PreReq:		%{name}-common = %{version}

%description exif
This is a dynamic shared object (DSO) for Apache that will add exif
support to PHP.

#%description exif -l pl

%package recode
Summary:	recodeextension module for PHP
Summary(pl):	Modu� recode dla PHP
Group:		Libraries
Group(de):	Libraries
Group(es):	Bibliotecas
Group(fr):	Librairies
Group(pl):	Biblioteki
PreReq:		%{name}-common = %{version}
Requires:	recode >= 3.5d-3

%description recode
This is a dynamic shared object (DSO) for Apache that will add recode
support to PHP.

#%description recode -l pl

%package session
Summary:	sessionextension module for PHP
Summary(pl):	Modu� session dla PHP
Group:		Libraries
Group(de):	Libraries
Group(es):	Bibliotecas
Group(fr):	Librairies
Group(pl):	Biblioteki
PreReq:		%{name}-common = %{version}

%description session
This is a dynamic shared object (DSO) for Apache that will add session
support to PHP.

#%description session -l pl

%package gettext
Summary:	gettextextension module for PHP
Summary(pl):	Modu� gettext dla PHP
Group:		Libraries
Group(de):	Libraries
Group(es):	Bibliotecas
Group(fr):	Librairies
Group(pl):	Biblioteki
PreReq:		%{name}-common = %{version}

%description gettext
This is a dynamic shared object (DSO) for Apache that will add gettext
support to PHP.

#%description gettext -l pl

%package snmp
Summary:	snmpextension module for PHP
Summary(pl):	Modu� snmp dla PHP
Group:		Libraries
Group(de):	Libraries
Group(es):	Bibliotecas
Group(fr):	Librairies
Group(pl):	Biblioteki
PreReq:		%{name}-common = %{version}

%description snmp
This is a dynamic shared object (DSO) for Apache that will add snmp
support to PHP.

#%description snmp -l pl

%package imap
Summary:	imapextension module for PHP
Summary(pl):	Modu� imap dla PHP
Group:		Libraries
Group(de):	Libraries
Group(es):	Bibliotecas
Group(fr):	Librairies
Group(pl):	Biblioteki
PreReq:		%{name}-common = %{version}

%description imap
This is a dynamic shared object (DSO) for Apache that will add imap
support to PHP.

#%description imap -l pl

%package ldap
Summary:	LDAP extension module for PHP
Summary(pl):	Modu� LDAP dla PHP
Group:		Libraries
Group(de):	Libraries
Group(es):	Bibliotecas
Group(fr):	Librairies
Group(pl):	Biblioteki
PreReq:		%{name}-common = %{version}

%description ldap
This is a dynamic shared object (DSO) for Apache that will add LDAP
support to PHP.

#%description ldap -l pl

%package sockets
Summary:	sockets extension module for PHP
Summary(pl):	Modu� socket dla PHP
Group:		Libraries
Group(de):	Libraries
Group(es):	Bibliotecas
Group(fr):	Librairies
Group(pl):	Biblioteki
PreReq:		%{name}-common = %{version}

%description sockets
This is a dynamic shared object (DSO) for Apache that will add sockets
support to PHP.

#%description sockets -l pl

%package mcrypt
Summary:	mcrypt extension module for PHP
Summary(pl):	Modu� mcrypt dla PHP
Group:		Libraries
Group(de):	Libraries
Group(es):	Bibliotecas
Group(fr):	Librairies
Group(pl):	Biblioteki
PreReq:		%{name}-common = %{version}

%description mcrypt
This is a dynamic shared object (DSO) for Apache that will add mcrypt
support to PHP.

#%description mcrypt -l pl

%package mhash
Summary:	mhash extension module for PHP
Summary(pl):	Modu� mhash dla PHP
Group:		Libraries
Group(de):	Libraries
Group(es):	Bibliotecas
Group(fr):	Librairies
Group(pl):	Biblioteki
PreReq:		%{name}-common = %{version}

%description mhash
This is a dynamic shared object (DSO) for Apache that will add mhash
support to PHP.

#%description mhash -l pl

%package doc
Summary:	Online manual for PHP
Summary(pl):	Dokumentacja dla PHP
Group:		Networking/Daemons
Group(de):	Netzwerkwesen/Server
Group(pl):	Sieciowe/Serwery

%description doc
Comprehensive documentation for PHP, viewable through your web server,
too!

%description doc -l pl
Dokumentacja dla pakietu PHP. Mo�na j� r�wnie� ogl�da� poprzez serwer
WWW.

%package pear
Summary:	PEAR
Group:		Development/Languages/PHP

%description pear
PEAR.

%package devel
Summary:	Files for PHP modules development
Summary(pl):	Pliki do kompilacji modu��w PHP
Group:		Development/Languages/PHP
Requires:	%{name}-common = %{version}

%description devel
Files for PHP modules development.

%description devel -l pl
Pliki potrzebne do kompilacji modu��w PHP.

%prep
%setup  -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1 
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1
%patch11 -p1

%build
CFLAGS="%{rpmcflags} -DEAPI -I/usr/X11R6/include"; export CFLAGS
./buildconf
libtoolize --copy --force
aclocal
autoconf
#for i in cgi fastcgi apxs ; do
for i in cgi apxs ; do
%configure \
	`[ $i = cgi ] && echo --enable-discard-path` \
	`[ $i = fastcgi ] && echo --enable-discard-path --with-fastcgi=/usr` \
	`[ $i = apxs ] && echo --with-apxs=%{_sbindir}/apxs` \
	--with-config-file-path=%{_sysconfdir} \
	--with-exec-dir=%{_bindir} \
	--disable-debug \
	--enable-magic-quotes \
	--enable-shared \
	--enable-track-vars \
	--enable-safe-mode \
	--enable-trans-sid \
	--enable-sysvsem=shared \
	--enable-sysvshm=shared \
	--enable-shmop=shared \
	--enable-session \
	--enable-exif=shared \
	--with-regex=system \
	--with-gettext=shared \
	%{!?bcond_off_ldap:--with-ldap=shared} \
	--with-mysql=shared,/usr \
	--with-mysql-sock=/var/lib/mysql/mysql.sock \
	--with-gd=shared \
	--enable-gd-imgstrttf \
	--with-dbase=shared \
	--with-filepro=shared \
	--enable-ftp=shared \
	--with-hyperwave \
	--with-pdflib=shared \
	--with-cpdflib=shared \
	%{?bcond_on_java:--with-java} \
	--with-pgsql=shared,/usr \
	%{!?bcond_off_imap:--with-imap=shared} \
	--enable-bcmath=shared \
	--enable-calendar=shared \
	--with-mm \
	--with-pcre-regex=shared \
	--enable-posix=shared \
	--with-ttf \
	--with-t1lib \
	--with-recode=shared \
	--enable-ucd-snmp-hack \
	--enable-dba=shared \
	%{!?bcond_off_snmp:--with-snmp=shared} \
	--with-gdbm \
	--with-db3 \
	--enable-yp=shared \
	--with-xml=shared \
	--enable-xml=shared \
	--with-zlib=shared \
	--with-mcrypt=shared \
	--enable-sockets=shared \
	--with-bz2=shared \
	--with-ctype=shared \
	--with-mhash=shared \
	--with-curl=shared \
	--with-gmp=shared \
	%{?bcond_on_openssl:--with-openssl} \
	%{!?bcond_off_odbc:--with-unixODBC=shared} \
	%{?bcond_on_oracle:--with-oracle=shared} \
	%{?bcond_on_oci8:--with-oci8=shared} \
	--without-db2 
done

# TODO --with-pspell=/usr,shared (pspell missing)

# --with-dom need libxml >= 2.2.7 \

%{__make}
%{__make} CFLAGS="%{rpmcflags} -DDISCARD_PATH=1" -C sapi/cgi

# Kill -rpath from php binary and libphp4.so
perl -pi -e 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
perl -pi -e 's|^runpath_var=.*|runpath_var=|g' libtool
%{__make} CFLAGS="%{rpmcflags} -DDISCARD_PATH=1" php

perl -pi -e 's|^hardcode_into_libs=.*|hardcode_into_libs=no|g' libtool
rm libphp4.la ; %{__make} libphp4.la

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_libdir}/{php,apache},%{_sysconfdir}/{apache,cgi}} \
		$RPM_BUILD_ROOT/home/httpd/icons \
		$RPM_BUILD_ROOT{%{_sbindir},%{_bindir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	INSTALL_IT="install libs/libphp4.so $RPM_BUILD_ROOT%{_libdir}/apache/ ; install libs/libphp_common*.so.*.*.* $RPM_BUILD_ROOT%{_libdir}"

install .libs/php $RPM_BUILD_ROOT%{_bindir}/php

#exit 1
#install .libs/*.so	$RPM_BUILD_ROOT%{_pkglibdir}
#install modules/*.so	$RPM_BUILD_ROOT%{_pkglibdir}/php

install %{SOURCE2}		$RPM_BUILD_ROOT%{_sysconfdir}/php.ini
install %{SOURCE3} php4.gif	$RPM_BUILD_ROOT/home/httpd/icons
install %{SOURCE5} $RPM_BUILD_ROOT/%{_sbindir}

mkdir manual
tar zxf %{SOURCE4} -C manual
ln -s manual.html manual/index.html

install %{SOURCE1} .
gzip -9nf CODING_STANDARDS CREDITS FUNCTION_LIST.txt \
      EXTENSIONS NEWS TODO* LICENSE Zend/LICENSE \
      Zend/ZEND_CHANGES README.SELF-CONTAINED-EXTENSIONS README.EXT_SKEL

%post
%{_sbindir}/apxs -e -a -n php4 %{_pkglibdir}/libphp4.so 1>&2
perl -pi -e 's|^#AddType application/x-httpd-php \.php|AddType application/x-httpd-php .php|' \
	/etc/httpd/httpd.conf
if [ -f /var/lock/subsys/httpd ]; then
	/etc/rc.d/init.d/httpd restart 1>&2
fi

%preun
if [ "$1" = "0" ]; then
	%{_sbindir}/apxs -e -A -n php4 %{_pkglibdir}/libphp4.so 1>&2
	perl -pi -e \
		's|^AddType application/x-httpd-php \.php|#AddType application/x-httpd-php .php|' \
		/etc/httpd/httpd.conf
	if [ -f /var/lock/subsys/httpd ]; then
		/etc/rc.d/init.d/httpd restart 1>&2
	fi
fi

%post common -p /sbin/ldconfig
%postun common -p /sbin/ldconfig

%post bcmath
%{_sbindir}/php-module-install install bcmath %{_sysconfdir}/php.ini

%preun bcmath
if [ "$1" = "0" ]; then
        %{_sbindir}/php-module-install remove bcmath %{_sysconfdir}/php.ini
fi

%post calendar
%{_sbindir}/php-module-install install calendar %{_sysconfdir}/php.ini

%preun calendar
if [ "$1" = "0" ]; then
        %{_sbindir}/php-module-install remove calendar %{_sysconfdir}/php.ini
fi

%post dba
%{_sbindir}/php-module-install install dba %{_sysconfdir}/php.ini

%preun dba
if [ "$1" = "0" ]; then
        %{_sbindir}/php-module-install remove dba %{_sysconfdir}/php.ini
fi

%post dbase
%{_sbindir}/php-module-install install dbase %{_sysconfdir}/php.ini

%preun dbase
if [ "$1" = "0" ]; then
        %{_sbindir}/php-module-install remove dbase %{_sysconfdir}/php.ini
fi

%post exif
%{_sbindir}/php-module-install install exif %{_sysconfdir}/php.ini

%preun exif
if [ "$1" = "0" ]; then
        %{_sbindir}/php-module-install remove exif %{_sysconfdir}/php.ini
fi

%post filepro
%{_sbindir}/php-module-install install filepro %{_sysconfdir}/php.ini

%preun filepro
if [ "$1" = "0" ]; then
        %{_sbindir}/php-module-install remove filepro %{_sysconfdir}/php.ini
fi

%post ftp
%{_sbindir}/php-module-install install ftp %{_sysconfdir}/php.ini

%preun ftp
if [ "$1" = "0" ]; then
        %{_sbindir}/php-module-install remove ftp %{_sysconfdir}/php.ini
fi

%post gd
%{_sbindir}/php-module-install install gd %{_sysconfdir}/php.ini

%preun gd
if [ "$1" = "0" ]; then
        %{_sbindir}/php-module-install remove gd %{_sysconfdir}/php.ini
fi

%post gettext
%{_sbindir}/php-module-install install gettext %{_sysconfdir}/php.ini

%preun gettext
if [ "$1" = "0" ]; then
        %{_sbindir}/php-module-install remove gettext %{_sysconfdir}/php.ini
fi

%if %{?bcond_off_imap:0}%{!?bcond_off_imap:1}
%post imap
%{_sbindir}/php-module-install install imap %{_sysconfdir}/php.ini

%preun imap
if [ "$1" = "0" ]; then
        %{_sbindir}/php-module-install remove imap %{_sysconfdir}/php.ini
fi
%endif

%if %{?bond_on_java:1}%{!?bond_on_java:0}
%post java
%{_sbindir}/php-module-install install libphp_java %{_sysconfdir}/php.ini

%preun java
if [ "$1" = "0" ]; then
        %{_sbindir}/php-module-install remove libphp_java %{_sysconfdir}/php.ini
fi
%endif

%if %{?bcond_off_ldap:0}%{!?bcond_off_ldap:1}
%post ldap
%{_sbindir}/php-module-install install ldap %{_sysconfdir}/php.ini

%preun ldap
if [ "$1" = "0" ]; then
        %{_sbindir}/php-module-install remove ldap %{_sysconfdir}/php.ini
fi
%endif

%post mcrypt
%{_sbindir}/php-module-install install mcrypt %{_sysconfdir}/php.ini

%preun mcrypt
if [ "$1" = "0" ]; then
        %{_sbindir}/php-module-install remove mcrypt %{_sysconfdir}/php.ini
fi

%post mhash
%{_sbindir}/php-module-install install mhash %{_sysconfdir}/php.ini

%preun mhash
if [ "$1" = "0" ]; then
        %{_sbindir}/php-module-install remove mhash %{_sysconfdir}/php.ini
fi

%post mysql
%{_sbindir}/php-module-install install mysql %{_sysconfdir}/php.ini

%preun mysql
if [ "$1" = "0" ]; then
        %{_sbindir}/php-module-install remove mysql %{_sysconfdir}/php.ini
fi

%if %{?bcond_on_oci8:1}%{!?bcond_on_oci8:0}
%post oci8
%{_sbindir}/php-module-install install oci8 %{_sysconfdir}/php.ini

%preun oci8
if [ "$1" = "0" ]; then
        %{_sbindir}/php-module-install remove oci8 %{_sysconfdir}/php.ini
fi
%endif

%if %{?bcond_off_odbc:0}%{!?bcond_off_odbc:1}
%post odbc
%{_sbindir}/php-module-install install odbc %{_sysconfdir}/php.ini

%preun odbc
if [ "$1" = "0" ]; then
        %{_sbindir}/php-module-install remove odbc %{_sysconfdir}/php.ini
fi
%endif

%if %{?bcond_on_oracle:1}%{!?bcond_on_oracle:0}
%post oracle
%{_sbindir}/php-module-install install oracle %{_sysconfdir}/php.ini

%preun oracle
if [ "$1" = "0" ]; then
        %{_sbindir}/php-module-install remove oracle %{_sysconfdir}/php.ini
fi
%endif

%post pcre
%{_sbindir}/php-module-install install pcre %{_sysconfdir}/php.ini

%preun pcre
if [ "$1" = "0" ]; then
        %{_sbindir}/php-module-install remove pcre %{_sysconfdir}/php.ini
fi

%post pgsql
%{_sbindir}/php-module-install install pgsql %{_sysconfdir}/php.ini

%preun pgsql
if [ "$1" = "0" ]; then
        %{_sbindir}/php-module-install remove pgsql %{_sysconfdir}/php.ini
fi

%post posix
%{_sbindir}/php-module-install install posix %{_sysconfdir}/php.ini

%preun posix
if [ "$1" = "0" ]; then
        %{_sbindir}/php-module-install remove posix %{_sysconfdir}/php.ini
fi

%post recode
%{_sbindir}/php-module-install install recode %{_sysconfdir}/php.ini

%preun recode
if [ "$1" = "0" ]; then
        %{_sbindir}/php-module-install remove recode %{_sysconfdir}/php.ini
fi

%post session
%{_sbindir}/php-module-install install session %{_sysconfdir}/php.ini

%preun session
if [ "$1" = "0" ]; then
        %{_sbindir}/php-module-install remove session %{_sysconfdir}/php.ini
fi

%if %{?bcond_off_snmp:0}%{!?bcond_off_snmp:1}
%post snmp
%{_sbindir}/php-module-install install snmp %{_sysconfdir}/php.ini

%preun snmp
if [ "$1" = "0" ]; then
        %{_sbindir}/php-module-install remove snmp %{_sysconfdir}/php.ini
fi
%endif

%post sockets
%{_sbindir}/php-module-install install sockets %{_sysconfdir}/php.ini

%preun sockets
if [ "$1" = "0" ]; then
        %{_sbindir}/php-module-install remove sockets %{_sysconfdir}/php.ini
fi

%post sysvsem
%{_sbindir}/php-module-install install sysvsem %{_sysconfdir}/php.ini

%preun sysvsem
if [ "$1" = "0" ]; then
        %{_sbindir}/php-module-install remove sysvsem %{_sysconfdir}/php.ini
fi

%post sysvshm
%{_sbindir}/php-module-install install sysvshm %{_sysconfdir}/php.ini

%preun sysvshm
if [ "$1" = "0" ]; then
        %{_sbindir}/php-module-install remove sysvshm %{_sysconfdir}/php.ini
fi

%post xml
%{_sbindir}/php-module-install install xml %{_sysconfdir}/php.ini

%preun xml
if [ "$1" = "0" ]; then
        %{_sbindir}/php-module-install remove xml %{_sysconfdir}/php.ini
fi

%post yp
%{_sbindir}/php-module-install install yp %{_sysconfdir}/php.ini

%preun yp
if [ "$1" = "0" ]; then
        %{_sbindir}/php-module-install remove yp %{_sysconfdir}/php.ini
fi

%post zlib
%{_sbindir}/php-module-install install zlib %{_sysconfdir}/php.ini

%preun zlib
if [ "$1" = "0" ]; then
        %{_sbindir}/php-module-install remove zlib %{_sysconfdir}/php.ini
fi

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/apache/libphp4.so

%files cgi
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/php

%files common
%defattr(644,root,root,755)
%doc {CODING_STANDARDS,CREDITS,FUNCTION_LIST.txt,Zend/ZEND_CHANGES}.gz
%doc {LICENSE,Zend/LICENSE,EXTENSIONS,NEWS,TODO*}.gz  
%doc {README.EXT_SKEL,README.SELF-CONTAINED-EXTENSIONS}.gz
%doc manual

%dir %{_sysconfdir}
%attr(644,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/php.ini

/home/httpd/icons/*

%attr(755,root,root) %{_sbindir}/*

%attr(755,root,root) %{_libdir}/libphp_common*.so.*.*.*

%dir %{_libdir}/php
%dir %{_libdir}/php/extensions
%dir %{extensionsdir}

%files devel
%defattr(644,root,root,755)
%{_includedir}/php4
%{_libdir}/php4
%attr(755,root,root) %{_bindir}/phpextdist
%attr(755,root,root) %{_bindir}/phpize
%attr(755,root,root) %{_bindir}/php-config

%files pear
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/pear
%{_libdir}/php/Benchmark
%{_libdir}/php/Crypt
%{_libdir}/php/Date
%{_libdir}/php/DB
%{_libdir}/php/File
%{_libdir}/php/HTML
%{_libdir}/php/Mail
%{_libdir}/php/Math
%{_libdir}/php/Net
%{_libdir}/php/Payment
%{_libdir}/php/PEAR
%{_libdir}/php/XML
%{_libdir}/php/*.php

%files mysql
%defattr(644,root,root,755)
%attr(755,root,root) %{extensionsdir}/mysql.*

%files pgsql
%defattr(644,root,root,755)
%attr(755,root,root) %{extensionsdir}/pgsql.so

%if %{?bcond_on_oracle:1}%{!?bcond_on_oracle:0}
%files oracle
%defattr(644,root,root,755)
%attr(755,root,root) %{extensionsdir}/oracle.so
%endif

%if %{?bcond_on_oci8:1}%{!?bcond_on_oci8:0}
%files oci8
%defattr(644,root,root,755)
%attr(755,root,root) %{extensionsdir}/oci8.so
%endif

%files gd
%defattr(644,root,root,755)
%attr(755,root,root) %{extensionsdir}/gd.so

%files xml
%defattr(644,root,root,755)
%attr(755,root,root) %{extensionsdir}/xml.so

%files dba
%defattr(644,root,root,755)
%attr(755,root,root) %{extensionsdir}/dba.so

%files dbase
%defattr(644,root,root,755)
%attr(755,root,root) %{extensionsdir}/dbase.so

%files filepro
%defattr(644,root,root,755)
%attr(755,root,root) %{extensionsdir}/filepro.so

%files pcre
%defattr(644,root,root,755)
%attr(755,root,root) %{extensionsdir}/pcre.so

%files posix
%defattr(644,root,root,755)
%attr(755,root,root) %{extensionsdir}/posix.so

%files sysvsem
%defattr(644,root,root,755)
%attr(755,root,root) %{extensionsdir}/sysvsem.so

%files sysvshm
%defattr(644,root,root,755)
%attr(755,root,root) %{extensionsdir}/sysvshm.so

%files yp
%defattr(644,root,root,755)
%attr(755,root,root) %{extensionsdir}/yp.so

%files calendar
%defattr(644,root,root,755)
%attr(755,root,root) %{extensionsdir}/calendar.so

%files bcmath
%defattr(644,root,root,755)
%attr(755,root,root) %{extensionsdir}/bcmath.so

%files ftp
%defattr(644,root,root,755)
%attr(755,root,root) %{extensionsdir}/ftp.so

%files zlib
%defattr(644,root,root,755)
%attr(755,root,root) %{extensionsdir}/zlib.so

%files exif
%defattr(644,root,root,755)
%attr(755,root,root) %{extensionsdir}/exif.so

%files recode
%defattr(644,root,root,755)
%attr(755,root,root) %{extensionsdir}/recode.so

#%files session
#%defattr(644,root,root,755)
#%attr(755,root,root) %{extensionsdir}/session.so

%files gettext
%defattr(644,root,root,755)
%attr(755,root,root) %{extensionsdir}/gettext.so

%if %{?bcond_off_imap:0}%{!?bcond_off_imap:1}
%files imap
%defattr(644,root,root,755)
%attr(755,root,root) %{extensionsdir}/imap.so
%endif

%if %{?bcond_off_snmp:0}%{!?bcond_off_snmp:1}
%files snmp
%defattr(644,root,root,755)
%attr(755,root,root) %{extensionsdir}/snmp.so
%endif

%if %{?bcond_on_java:1}%{!?bcond_on_java:0}
%files java
%defattr(644,root,root,755)
%attr(755,root,root) %{extensionsdir}/libphp_java.so
%endif

%if %{?bcond_off_ldap:0}%{!?bcond_off_ldap:1}
%files ldap
%defattr(644,root,root,755)
%attr(755,root,root) %{extensionsdir}/ldap.*
%endif

%files sockets
%defattr(644,root,root,755)
%attr(755,root,root) %{extensionsdir}/sockets.so

%files mcrypt
%defattr(644,root,root,755)
%attr(755,root,root) %{extensionsdir}/mcrypt.so

%files mhash
%defattr(644,root,root,755)
%attr(755,root,root) %{extensionsdir}/mhash.so

%if %{?bcond_off_odbc:0}%{!?bcond_off_odbc:1}
%files odbc
%defattr(644,root,root,755)
%attr(755,root,root) %{extensionsdir}/odbc.so
%endif

%files doc
%defattr(644,root,root,755)
%doc manual/*
