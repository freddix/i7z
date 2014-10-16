Summary:	i3, i5 and i7 reporting tool for Linux
Name:		i7z
Version:	0.27.2
Release:	2
License:	GPL v2
Group:		Applications/System
#Source0Download: http://code.google.com/p/i7z/downloads/list
Source0:	http://i7z.googlecode.com/files/%{name}-%{version}.tar.gz
# Source0-md5:	7f2c4928146b722d67ecdd0d905a4353
URL:		http://code.google.com/p/i7z/
BuildRequires:	ncurses-devel
#BuildRequires:	qt4-build
#BuildRequires:	qt4-qmake
#BuildRequires:	QtGui-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A better i7 (and now i3, i5) reporting tool for Linux.

%package gui
Summary:	Qt-based graphical i3/i5/i7 CPU reporting tool
Group:		X11/Applications
Requires:	%{name} = %{version}-%{release}

%description gui
Qt-based graphical i3/i5/i7 CPU reporting tool.

%prep
%setup -q

%build
export CFLAGS="%{rpmcflags} -I/usr/include/ncurses"
export LDFLAGS="%{rpmldflags}"
%{__make} clean
%{__make} \
	CC="%{__cc}"

#cd GUI
#qmake-qt4 \
#	QMAKE_CXX="%{__cxx}" \
#	QMAKE_CXXFLAGS_RELEASE="%{rpmcxxflags}" \
#	QMAKE_LFLAGS_RELEASE="%{rpmldflags}"
#%{__make} clean
#%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sbindir}

install %{name} $RPM_BUILD_ROOT%{_sbindir}
#install GUI/i7z_GUI $RPM_BUILD_ROOT%{_sbindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.txt
%attr(755,root,root) %{_sbindir}/i7z

#%files gui
#%defattr(644,root,root,755)
#%attr(755,root,root) %{_sbindir}/i7z_GUI

