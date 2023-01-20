# Copyright 2022 Wong Hoi Sing Edison <hswong3i@pantarei-design.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

%global debug_package %{nil}

Name: git
Epoch: 100
Version: 2.35.6
Release: 1%{?dist}
Summary: Fast, scalable, distributed revision control system
License: GPL-2.0-only
URL: https://github.com/git/git/tags
Source0: %{name}_%{version}.orig.tar.gz
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: curl-devel
BuildRequires: expat-devel
BuildRequires: gcc
BuildRequires: gettext-devel
BuildRequires: glibc-static
BuildRequires: libtool
BuildRequires: openssl-devel
BuildRequires: pcre2-devel
BuildRequires: perl-devel
BuildRequires: pkgconfig
BuildRequires: zlib-devel
Requires: expat
Requires: libcurl
Requires: openssl
Requires: pcre2
Requires: perl
Requires: zlib
Provides: git-all
Provides: git-core
Provides: git-core-doc
Provides: git-credential-libsecret
Provides: git-cvs
Provides: git-daemon
Provides: git-email
Provides: git-gui
Provides: git-instaweb
Provides: git-subtree
Provides: git-svn
Provides: gitk
Provides: gitweb
Provides: perl-Git
Provides: perl-Git-SVN

%description
Git is a fast, scalable, distributed revision control system with an
unusually rich command set that provides both high-level operations and
full access to internals.

%prep
%autosetup -T -c -n %{name}_%{version}-%{release}
tar -zx -f %{S:0} --strip-components=1 -C .

%build
make configure
%configure
%make_build \
    DEVELOPER_CFLAGS="-std=gnu99" \
    DEFAULT_EDITOR=editor \
    DEFAULT_PAGER=pager \
    DESTDIR=%{buildroot} \
    NO_PERL_CPAN_FALLBACKS=1 \
    PYTHON_PATH=%{_bindir}/python3 \
    SHELL_PATH=/bin/sh

%install
%make_install \
    DEVELOPER_CFLAGS="-std=gnu99" \
    NO_CROSS_DIRECTORY_HARDLINKS=1 \
    NO_INSTALL_HARDLINKS=1 \
    PYTHON_PATH=%{_bindir}/python3 \
    SHELL_PATH=/bin/sh \
    gitexecdir=%{_libexecdir}/git-core \
    libexecdir=%{_libexecdir}/git-core \
    prefix=%{_prefix}
install -Dpm755 -d %{buildroot}%{_datadir}/bash-completion/completions
install -Dpm644 contrib/completion/git-completion.bash %{buildroot}%{_datadir}/bash-completion/completions/git
rm -rf %{buildroot}%{_libdir}/git-core/git-p4

%files
%license COPYING
%dir %{_datadir}/git-core
%dir %{_datadir}/git-gui
%dir %{_datadir}/gitk
%dir %{_datadir}/gitweb
%dir %{_datadir}/perl5
%dir %{_datadir}/perl5/FromCPAN
%dir %{_datadir}/perl5/FromCPAN/Mail
%dir %{_datadir}/perl5/Git
%{_bindir}/*
%{_libexecdir}/git-core
%{_datadir}/bash-completion/completions/git
%{_datadir}/git-core/*
%{_datadir}/git-gui/*
%{_datadir}/gitk/*
%{_datadir}/gitweb/*
%{_datadir}/locale/*/LC_MESSAGES/git.*
%{_datadir}/perl5/FromCPAN/Error.pm
%{_datadir}/perl5/FromCPAN/Mail/Address.pm
%{_datadir}/perl5/Git.pm
%{_datadir}/perl5/Git/*

%changelog
