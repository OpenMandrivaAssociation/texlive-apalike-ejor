Name:		texlive-apalike-ejor
Version:	59667
Release:	2
Summary:	A BibTeX style file for the European Journal of Operational Research
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/apalike-ejor
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/apalike-ejor.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/apalike-ejor.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package contains a BibTeX style file, apalike-ejor.bst,
made to follow the European Journal of Operational Research
reference style guidelines. It is a fork of apalike version
0.99a, by Oren Patashnik, and consists of minor modifications
of standard APA style. Among other changes it adds support for
hyperlinked URL and DOI fields (which requires hyperref).

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/bibtex/bst/apalike-ejor
%doc %{_texmfdistdir}/doc/bibtex/apalike-ejor

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
