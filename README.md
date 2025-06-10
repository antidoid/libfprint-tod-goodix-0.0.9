# Building

- mkdir ~/rpmbuild
- git clone https://github.com/antidoid/libfprint-tod-goodix-0.0.9
- cd libfprint-tod-goodix-0.0.9
- cp -rf * ~/rpmbuild
- distrobox ephemeral --image fedora:$(( $(rpm -E %fedora) + 1 ))
- sudo dnf install -y rpmdevtools rpmlint
- rpmbuild -bs ~/rpmbuild/SPECS/libfprint-tod-goodix.spec
