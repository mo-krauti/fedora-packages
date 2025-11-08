# mo's fedora packages

## Using

Enable my [copr repo](https://copr.fedorainfracloud.org/coprs/mo-k12/personal/)
```bash
sudo dnf copr enable mo-k12/personal
```

## Developing

Adapt rpmbuild path by adding `~/.rpmmacros`:
```
%_topdir   %{getenv:HOME}/path/to/your/rpmbuild
```

Build package:
```
spectool -g -R package.spec
rpmbuild -ba package.spec
```
