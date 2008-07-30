Name: 		treecc
Version: 	0.3.8
Release: 	%mkrel 3
Summary: 	A tool for helping in compiler development
Group: 		Development/C
License: 	GPL
Source: 	%name-%version.tar.bz2
BuildRequires:	flex byacc
URL: 		http://www.southern-storm.com.au/treecc.html
Buildroot: 	%_tmppath/%name-%version-buildroot


%description
The treecc program is designed to assist in the development of 
compilers and other language-based tools. It manages the 
generation of code to handle abstract syntax trees and operations 
upon the trees.
Treecc was originally written to assist with the development of 
the C# compiler for the Portable.NET project. However, it is much 
more general than that and can be used in any system that makes 
heavy use of abstract syntax trees and the operations upon them.

%prep
%setup -q

%build
%configure
%make
make -C tests check-TESTS

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall

%clean
rm -rf $RPM_BUILD_ROOT

%post
%_install_info %name

%preun
%_remove_install_info %name

%files
%defattr(-,root,root)
%doc AUTHORS ChangeLog COPYING NEWS README doc/essay.html
%_bindir/%name
%_infodir/* 
%_mandir/man1/%name.*
%_libdir/*

