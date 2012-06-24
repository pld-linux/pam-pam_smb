%define 	modulename pam_smb
Summary:	PAM module for auth UNIX users using an NT
Summary(pl):	Modu� PAM autentyfikuj�cy u�ytkownik�w Linuksa na NT
Summary(pt_BR):	m�dulo de autentica��o PAM para autentica��o contra servidor SMB
Name:		pam-%{modulename}
Version:	1.1.7
Release:	1
Epoch:		1
License:	GPL
Vendor:		David Airlie <airlied@samba.org>
Group:		Networking
Source0:	http://www.csn.ul.ie/~airlied/%{modulename}/%{modulename}-%{version}.tar.gz
# Source0-md5:	44b4881709e209a40239555f30ab5222
Patch0:		%{name}-ac_fixes.patch
URL:		http://www.csn.ul.ie/~airlied/%{modulename}/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	pam-devel
Obsoletes:	%{modulename}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PAM module which allows authentication of UNIX users using an
Microsoft Windows NT(TM) server (or domain).

%description -l pl
Modu� PAM pozwalaj�cy na autentyfikacj� u�ytkownik�w Linuksa na
serwerze (lub w domenie) Microsoft Windows NT(TM).

%description -l pt_BR
O pam_smb � um m�dulo PAM que permite autentica��o de usu�rios contra
um servidor SMB, que por sua vez pode ser um servidor Samba ou Windows
NT. Pode ser muito �til em "redes Windows" onde todos os usu�rios de
workstations tamb�m s�o registrados como usu�rios NetBIOS, pois as
senhas s�o mantidas apenas no servidor SMB.

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
install -d $RPM_BUILD_ROOT/{etc,lib/security}

install pam_smb_auth.so $RPM_BUILD_ROOT/lib/security
install pam_smb.conf.example $RPM_BUILD_ROOT%{_sysconfdir}/pam_smb.conf

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README CHANGES TODO pam_smb.conf.example
%attr(755,root,root) /lib/security/pam_smb_auth.so
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/pam_smb.conf
