%define 	modulename pam_smb
Summary:	PAM module for auth UNIX users using an SMB server
Summary(pl.UTF-8):   Moduł PAM uwierzytelniający użytkowników przy użyciu serwera SMB
Summary(pt_BR.UTF-8):   módulo de autenticação PAM para autenticação contra servidor SMB
Name:		pam-%{modulename}
Version:	1.1.7
Release:	3
Epoch:		1
License:	GPL
Vendor:		David Airlie <airlied@samba.org>
Group:		Networking
Source0:	http://www.csn.ul.ie/~airlied/%{modulename}/%{modulename}-%{version}.tar.gz
# Source0-md5:	44b4881709e209a40239555f30ab5222
Patch0:		%{name}-ac_fixes.patch
URL:		http://www.csn.ul.ie/~airlied/pam_smb/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	pam-devel
Obsoletes:	pam_smb
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PAM module which allows authentication of UNIX users using an
Microsoft Windows NT(TM) server (or domain).

%description -l pl.UTF-8
Moduł PAM pozwalający na uwierzytelnianie użytkowników Linuksa na
serwerze (lub w domenie) Microsoft Windows NT(TM).

%description -l pt_BR.UTF-8
O pam_smb é um módulo PAM que permite autenticação de usuários contra
um servidor SMB, que por sua vez pode ser um servidor Samba ou Windows
NT. Pode ser muito útil em "redes Windows" onde todos os usuários de
workstations também são registrados como usuários NetBIOS, pois as
senhas são mantidas apenas no servidor SMB.

%prep
%setup -q -n %{modulename}
%patch0 -p1

%build
%{__aclocal}
%{__autoconf}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sysconfdir},/%{_lib}/security}

install pam_smb_auth.so $RPM_BUILD_ROOT/%{_lib}/security
install pam_smb.conf.example $RPM_BUILD_ROOT%{_sysconfdir}/pam_smb.conf

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README CHANGES TODO pam_smb.conf.example
%attr(755,root,root) /%{_lib}/security/pam_smb_auth.so
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/pam_smb.conf
