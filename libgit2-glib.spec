#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : libgit2-glib
Version  : 0.99.0.1
Release  : 9
URL      : https://github.com/GNOME/libgit2-glib/archive/v0.99.0.1/libgit2-glib-0.99.0.1.tar.gz
Source0  : https://github.com/GNOME/libgit2-glib/archive/v0.99.0.1/libgit2-glib-0.99.0.1.tar.gz
Summary  : GLib wrapper for libgit2
Group    : Development/Tools
License  : LGPL-2.1
Requires: libgit2-glib-data = %{version}-%{release}
Requires: libgit2-glib-lib = %{version}-%{release}
Requires: libgit2-glib-license = %{version}-%{release}
Requires: libgit2-glib-python = %{version}-%{release}
Requires: libgit2-glib-python3 = %{version}-%{release}
BuildRequires : buildreq-gnome
BuildRequires : buildreq-meson
BuildRequires : libgit2-dev
BuildRequires : libssh2-dev
BuildRequires : pkgconfig(libgit2)
BuildRequires : pygobject
BuildRequires : pygobject-dev
BuildRequires : vala

%description
General Information
===================
libgit2-glib is a glib wrapper library around the libgit2 git access library.

%package data
Summary: data components for the libgit2-glib package.
Group: Data

%description data
data components for the libgit2-glib package.


%package dev
Summary: dev components for the libgit2-glib package.
Group: Development
Requires: libgit2-glib-lib = %{version}-%{release}
Requires: libgit2-glib-data = %{version}-%{release}
Provides: libgit2-glib-devel = %{version}-%{release}
Requires: libgit2-glib = %{version}-%{release}
Requires: libgit2-glib = %{version}-%{release}

%description dev
dev components for the libgit2-glib package.


%package lib
Summary: lib components for the libgit2-glib package.
Group: Libraries
Requires: libgit2-glib-data = %{version}-%{release}
Requires: libgit2-glib-license = %{version}-%{release}

%description lib
lib components for the libgit2-glib package.


%package license
Summary: license components for the libgit2-glib package.
Group: Default

%description license
license components for the libgit2-glib package.


%package python
Summary: python components for the libgit2-glib package.
Group: Default
Requires: libgit2-glib-python3 = %{version}-%{release}

%description python
python components for the libgit2-glib package.


%package python3
Summary: python3 components for the libgit2-glib package.
Group: Default
Requires: python3-core

%description python3
python3 components for the libgit2-glib package.


%prep
%setup -q -n libgit2-glib-0.99.0.1
cd %{_builddir}/libgit2-glib-0.99.0.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1582736798
# -Werror is for werrorists
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$CFLAGS -fno-lto "
export FFLAGS="$CFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
CFLAGS="$CFLAGS" CXXFLAGS="$CXXFLAGS" LDFLAGS="$LDFLAGS" meson --libdir=lib64 --prefix=/usr --buildtype=plain   builddir
ninja -v -C builddir

%install
mkdir -p %{buildroot}/usr/share/package-licenses/libgit2-glib
cp %{_builddir}/libgit2-glib-0.99.0.1/COPYING %{buildroot}/usr/share/package-licenses/libgit2-glib/3704f4680301a60004b20f94e0b5b8c7ff1484a9
DESTDIR=%{buildroot} ninja -C builddir install

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/lib64/girepository-1.0/Ggit-1.0.typelib
/usr/share/gir-1.0/*.gir
/usr/share/vala/vapi/libgit2-glib-1.0.deps
/usr/share/vala/vapi/libgit2-glib-1.0.vapi

%files dev
%defattr(-,root,root,-)
/usr/include/libgit2-glib-1.0/libgit2-glib/ggit-annotated-commit.h
/usr/include/libgit2-glib-1.0/libgit2-glib/ggit-blame-options.h
/usr/include/libgit2-glib-1.0/libgit2-glib/ggit-blame.h
/usr/include/libgit2-glib-1.0/libgit2-glib/ggit-blob-output-stream.h
/usr/include/libgit2-glib-1.0/libgit2-glib/ggit-blob.h
/usr/include/libgit2-glib-1.0/libgit2-glib/ggit-branch-enumerator.h
/usr/include/libgit2-glib-1.0/libgit2-glib/ggit-branch.h
/usr/include/libgit2-glib-1.0/libgit2-glib/ggit-checkout-options.h
/usr/include/libgit2-glib-1.0/libgit2-glib/ggit-cherry-pick-options.h
/usr/include/libgit2-glib-1.0/libgit2-glib/ggit-clone-options.h
/usr/include/libgit2-glib-1.0/libgit2-glib/ggit-commit-parents.h
/usr/include/libgit2-glib-1.0/libgit2-glib/ggit-commit.h
/usr/include/libgit2-glib-1.0/libgit2-glib/ggit-config-entry.h
/usr/include/libgit2-glib-1.0/libgit2-glib/ggit-config.h
/usr/include/libgit2-glib-1.0/libgit2-glib/ggit-cred-plaintext.h
/usr/include/libgit2-glib-1.0/libgit2-glib/ggit-cred-ssh-interactive.h
/usr/include/libgit2-glib-1.0/libgit2-glib/ggit-cred-ssh-key-from-agent.h
/usr/include/libgit2-glib-1.0/libgit2-glib/ggit-cred.h
/usr/include/libgit2-glib-1.0/libgit2-glib/ggit-diff-binary-file.h
/usr/include/libgit2-glib-1.0/libgit2-glib/ggit-diff-binary.h
/usr/include/libgit2-glib-1.0/libgit2-glib/ggit-diff-delta.h
/usr/include/libgit2-glib-1.0/libgit2-glib/ggit-diff-file.h
/usr/include/libgit2-glib-1.0/libgit2-glib/ggit-diff-find-options.h
/usr/include/libgit2-glib-1.0/libgit2-glib/ggit-diff-format-email-options.h
/usr/include/libgit2-glib-1.0/libgit2-glib/ggit-diff-hunk.h
/usr/include/libgit2-glib-1.0/libgit2-glib/ggit-diff-line.h
/usr/include/libgit2-glib-1.0/libgit2-glib/ggit-diff-options.h
/usr/include/libgit2-glib-1.0/libgit2-glib/ggit-diff-similarity-metric.h
/usr/include/libgit2-glib-1.0/libgit2-glib/ggit-diff.h
/usr/include/libgit2-glib-1.0/libgit2-glib/ggit-enum-types.h
/usr/include/libgit2-glib-1.0/libgit2-glib/ggit-error.h
/usr/include/libgit2-glib-1.0/libgit2-glib/ggit-fetch-options.h
/usr/include/libgit2-glib-1.0/libgit2-glib/ggit-index-entry-resolve-undo.h
/usr/include/libgit2-glib-1.0/libgit2-glib/ggit-index-entry.h
/usr/include/libgit2-glib-1.0/libgit2-glib/ggit-index.h
/usr/include/libgit2-glib-1.0/libgit2-glib/ggit-main.h
/usr/include/libgit2-glib-1.0/libgit2-glib/ggit-merge-options.h
/usr/include/libgit2-glib-1.0/libgit2-glib/ggit-message.h
/usr/include/libgit2-glib-1.0/libgit2-glib/ggit-native.h
/usr/include/libgit2-glib-1.0/libgit2-glib/ggit-note.h
/usr/include/libgit2-glib-1.0/libgit2-glib/ggit-object-factory-base.h
/usr/include/libgit2-glib-1.0/libgit2-glib/ggit-object-factory.h
/usr/include/libgit2-glib-1.0/libgit2-glib/ggit-object.h
/usr/include/libgit2-glib-1.0/libgit2-glib/ggit-oid.h
/usr/include/libgit2-glib-1.0/libgit2-glib/ggit-patch.h
/usr/include/libgit2-glib-1.0/libgit2-glib/ggit-proxy-options.h
/usr/include/libgit2-glib-1.0/libgit2-glib/ggit-push-options.h
/usr/include/libgit2-glib-1.0/libgit2-glib/ggit-rebase-operation.h
/usr/include/libgit2-glib-1.0/libgit2-glib/ggit-rebase-options.h
/usr/include/libgit2-glib-1.0/libgit2-glib/ggit-rebase.h
/usr/include/libgit2-glib-1.0/libgit2-glib/ggit-ref-spec.h
/usr/include/libgit2-glib-1.0/libgit2-glib/ggit-ref.h
/usr/include/libgit2-glib-1.0/libgit2-glib/ggit-reflog-entry.h
/usr/include/libgit2-glib-1.0/libgit2-glib/ggit-reflog.h
/usr/include/libgit2-glib-1.0/libgit2-glib/ggit-remote-callbacks.h
/usr/include/libgit2-glib-1.0/libgit2-glib/ggit-remote.h
/usr/include/libgit2-glib-1.0/libgit2-glib/ggit-repository.h
/usr/include/libgit2-glib-1.0/libgit2-glib/ggit-revert-options.h
/usr/include/libgit2-glib-1.0/libgit2-glib/ggit-revision-walker.h
/usr/include/libgit2-glib-1.0/libgit2-glib/ggit-signature.h
/usr/include/libgit2-glib-1.0/libgit2-glib/ggit-status-options.h
/usr/include/libgit2-glib-1.0/libgit2-glib/ggit-submodule-update-options.h
/usr/include/libgit2-glib-1.0/libgit2-glib/ggit-submodule.h
/usr/include/libgit2-glib-1.0/libgit2-glib/ggit-tag.h
/usr/include/libgit2-glib-1.0/libgit2-glib/ggit-transfer-progress.h
/usr/include/libgit2-glib-1.0/libgit2-glib/ggit-tree-builder.h
/usr/include/libgit2-glib-1.0/libgit2-glib/ggit-tree-entry.h
/usr/include/libgit2-glib-1.0/libgit2-glib/ggit-tree.h
/usr/include/libgit2-glib-1.0/libgit2-glib/ggit-types.h
/usr/include/libgit2-glib-1.0/libgit2-glib/ggit.h
/usr/lib64/libgit2-glib-1.0.so
/usr/lib64/pkgconfig/libgit2-glib-1.0.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/libgit2-glib-1.0.so.0
/usr/lib64/libgit2-glib-1.0.so.0.9900.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/libgit2-glib/3704f4680301a60004b20f94e0b5b8c7ff1484a9

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
