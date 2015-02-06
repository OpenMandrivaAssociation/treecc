%define debug_package %nil

Name: 		treecc
Version: 	0.3.10
Release: 	8
Summary: 	A tool for helping in compiler development
Group: 		Development/C
License: 	GPLv2
Source0: 	http://download.savannah.gnu.org/releases/dotgnu-pnet/%{name}-%{version}.tar.gz
BuildRequires:	flex byacc
URL: 		http://www.southern-storm.com.au/treecc.html


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
%makeinstall



%files
%doc AUTHORS ChangeLog COPYING NEWS README doc/essay.html
%_bindir/%name
%_infodir/* 
%_mandir/man1/%name.*
%_libdir/*
