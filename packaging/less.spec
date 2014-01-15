Name:           less
Version:        458
Release:        0
License:        GPL-3.0+
Summary:        A text file browser similar to more, but better
Url:            http://www.greenwoodsoftware.com/less/
Group:          System/Utilities
Source0:        http://www.greenwoodsoftware.com/less/%{name}-%{version}.tar.gz
Source1001:     %{name}.manifest
BuildRequires:  pkgconfig(ncurses)

%description
The less utility is a text file browser that resembles more, but has
more capabilities.  Less allows you to move backwards in the file as
well as forwards.  Since less doesn't have to read the entire input file
before it starts, less starts up more quickly than text editors (for
example, vi).

You should install less because it is a basic utility for viewing text
files, and you'll use it frequently.

%prep
%setup -q
cp %{SOURCE1001} .

%build

%configure
make %{?_smp_mflags}

%install
%make_install

%docs_package

%files
%manifest %{name}.manifest
%license LICENSE
%{_bindir}/*
