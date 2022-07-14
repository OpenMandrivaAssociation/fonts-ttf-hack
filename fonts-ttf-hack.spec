Name:		fonts-ttf-hack
Version:	3.003
Release:	1
Summary:	Hack ttf fonts
License:	MIT License Bitstream Vera License
Group:		System/Fonts/True type
Url:		https://sourcefoundry.org/hack/
Source0:	https://github.com/source-foundry/Hack/releases/download/v%{version}/Hack-v%{version}-ttf.tar.xz
BuildArch:	noarch

%description
A typeface designed for source code.

%prep
%autosetup -p1 -c %{name}

%install
mkdir -p %{buildroot}%{_datadir}/fonts/TTF/hack
install -Dm 644 *.ttf  %{buildroot}%{_datadir}/fonts/TTF/hack/

%files
%{_datadir}/fonts/TTF/hack
