%global forgeurl https://github.com/hunkyburrito/xdg-desktop-portal-termfilechooser
%global tag v1.2.1
%forgemeta

Name:           xdg-desktop-portal-termfilechooser
Version:        %{tag}
Release:        %{autorelease}
Summary:        xdg-desktop-portal backend for terminal file choosers (hunkyburrito fork)

License:        MIT
URL:            %{forgeurl}
Source0:        %{forgesource}
Provides:       xdg-desktop-portal-impl

BuildRequires:  gcc
BuildRequires:  meson
BuildRequires:  systemd-rpm-macros

BuildRequires:  pkgconfig(inih)
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(scdoc)
BuildRequires:  pkgconfig(systemd)

Requires:       xdg-desktop-portal
Requires:       inih

Recommends:     fzf
Recommends:     ranger

%description
xdg-desktop-portal backend that lets you choose files or folders using a terminal file chooser.

%prep
%forgeautosetup

%build
%meson -Dsd-bus-provider=libsystemd
%meson_build

%install
%meson_install
install -Dm0644 LICENSE %{buildroot}%{_licensedir}/%{name}/LICENSE

%post
%systemd_user_post %{name}.service

%preun
%systemd_user_preun %{name}.service

%files
%license LICENSE
%doc README.md
%{_userunitdir}/%{name}.service
%{_libexecdir}/%{name}
%{_datadir}/dbus-1/services/org.freedesktop.impl.portal.desktop.termfilechooser.service
%{_datadir}/xdg-desktop-portal/portals/termfilechooser.portal
%{_datadir}/%{name}/*
%{_mandir}/man5/%{name}.5*

%changelog
%autochangelog
