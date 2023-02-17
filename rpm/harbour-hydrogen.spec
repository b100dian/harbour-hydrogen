#
# Do NOT Edit the Auto-generated Part!
# Generated by: spectacle version 0.32
#

Name:       harbour-hydrogen

# >> macros
# << macros

Summary:    hydrogen, a matrix client
Version:    0.3.7.1
Release:    1
Group:      Qt/Qt
License:    LICENSE
BuildArch:  noarch
URL:        https://github.com/thigg/sfos-hydrogen
Source0:    %{name}-%{version}.tar.bz2
Requires:   sailfishsilica-qt5 >= 0.10.9
Requires:   sailfish-components-webview-qt5
BuildRequires:  pkgconfig(sailfishapp) >= 1.0.3
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Qml)
BuildRequires:  pkgconfig(Qt5Quick)
BuildRequires:  pkgconfig(qt5embedwidget)
BuildRequires:  pkgconfig(sailfishwebengine)
BuildRequires:  desktop-file-utils
BuildRequires:  nodejs
BuildRequires:  nodejs-common
BuildRequires:  npm
BuildRequires:  yarn

%description
Short description of my Sailfish OS Application


%prep
%setup -q -n %{name}-%{version}
# >> setup
# << setup

%build
# >> build pre
# << build pre
cd hydrogen
yarn
yarn build
cd -
%qmake5

make %{?_smp_mflags}

# >> build post
# << build post

%install
rm -rf %{buildroot}
# >> install pre
# << install pre
%qmake5_install

# >> install post
# << install post

desktop-file-install --delete-original       \
  --dir %{buildroot}%{_datadir}/applications             \
   %{buildroot}%{_datadir}/applications/*.desktop

%files
%defattr(-,root,root,-)
%defattr(0644,root,root,-)
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png
# >> files
# << files

%changelog
