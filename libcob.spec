Name:           libcob
Version:        2.2
Release:        4%{?dist}
Summary:        GnuCOBOL - COBOL runtime library

# Packager:     Whoever

Group:          Development/Languages/Other
License:        GPLv3+/LGPLv3+

URL:            https://www.gnu.org/software/gnucobol/
Source:         https://ftp.gnu.org/gnu/gnucobol/gnucobol-%{version}.tar.gz

BuildRoot:      %{_tmppath}/gnucobol-%{version}-%{release}-root-%(%{__id_u} -n)

Provides:       libcob = 2.2
Obsoletes:      libcob < 2.2

BuildRequires:  gcc
BuildRequires:  glibc-devel
BuildRequires:  glibc
BuildRequires:  gmp-devel >= 4.1.4
BuildRequires:  gmp >= 4.1.4
BuildRequires:  libdb-devel >= 4.1.24
BuildRequires:  libdb >= 4.1.24
BuildRequires:  ncurses-devel >= 5.4
BuildRequires:  ncurses-libs >= 5.4
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  gettext
BuildRequires:  m4
BuildRequires:  texinfo
BuildRequires:  bison
BuildRequires:  flex
BuildRequires:  help2man

Requires:       glibc
Requires:       gmp >= 4.1.4
Requires:       libdb >= 4.1.24
Requires:       ncurses-libs >= 5.4

%description
GnuCOBOL is a free, modern COBOL compiler. GnuCOBOL implements a substantial part of the COBOL 85,
COBOL 2002 and COBOL 2014 standards, as well as many extensions included in other COBOL compilers.

GnuCOBOL translates COBOL into C and compiles the translated code using a native C compiler.

%prep
%setup -q -n gnucobol-%{version}

%build
./configure --enable-debug \
        --disable-rpath \
        --host=%{_host} --build=%{_build} \
        --program-prefix=%{?_program_prefix} \
        --disable-dependency-tracking \
        --prefix=%{_prefix} \
        --exec-prefix=%{_exec_prefix} \
        --bindir=%{_bindir} \
        --sbindir=%{_sbindir} \
        --sysconfdir=%{_sysconfdir} \
        --datadir=%{_datadir} \
        --includedir=%{_includedir} \
        --libdir=%{_libdir} \
        --libexecdir=%{_libexecdir} \
        --localstatedir=%{_localstatedir} \
        --sharedstatedir=%{_sharedstatedir} \
        --mandir=%{_mandir} \
        --infodir=%{_infodir}
make

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
rm -rf $RPM_BUILD_ROOT/%{_infodir}/dir
rm -rf $RPM_BUILD_ROOT/%{_bindir}
rm -rf $RPM_BUILD_ROOT/%{_datadir}
rm -rf $RPM_BUILD_ROOT/%{_includedir}

%check
make check

%files
#-f gnucobol.lang
%defattr (-,root,root,-)
%doc AUTHORS COPYING COPYING.LESSER COPYING.DOC ChangeLog
%doc NEWS README THANKS
%{_libdir}/libcob.so*
%{_libdir}/libcob.a
%{_libdir}/libcob.la
%{_libdir}/gnucobol/CBL_OC_DUMP.so

%clean
rm -rf $RPM_BUILD_ROOT
rm -rf $RPM_BUILD_DIR/%{name}-%{version}

%post
/sbin/ldconfig

%postun
/sbin/ldconfig

%changelog
* Wed Jan 10 2018 Christoph Jahn
- Created SPEC
