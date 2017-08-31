# GNUCobol 2.2 RPM Spec for RHEL 7

## What?
RPM Spec for GNUCOBOL on RedHat Enterprise Server 7

I had some problems with the default spec delivered with the tar.gz.
So I modified it to run on RHEL 7

## Version

This is tested with RHEL 7.4 and
GNUCobol 2.2 rc (https://sourceforge.net/p/open-cobol/)

## QuickUsage

### Created rpmbuild structure in /root

```
/root/rpmbuild/
/root/rpmbuild/BUILD
/root/rpmbuild/BUILDROOT
/root/rpmbuild/RPMS
/root/rpmbuild/SOURCES
/root/rpmbuild/SPECS
/root/rpmbuild/SRPMS
```

### Put files in folders

```
/root/rpmbuild/SOURCES/gnucobol-2.2-rc.tar.gz
/root/rpmbuild/SPECS/gnucobol.spec
```

### Build

```
cd /root/
rpmbuild -ba rpmbuild/SPECS/gnucobol.spec
```
