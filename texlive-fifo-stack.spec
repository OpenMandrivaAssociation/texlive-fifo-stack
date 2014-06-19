# revision 33288
# category Package
# catalog-ctan /macros/latex/contrib/fifo-stack
# catalog-date 2014-04-08 11:20:21 +0200
# catalog-license lppl
# catalog-version 1.0
Name:		texlive-fifo-stack
Version:	1.0
Release:	1
Summary:	FIFO and stack implementation for package writers
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/fifo-stack
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fifo-stack.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fifo-stack.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fifo-stack.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
A LaTeX implementation of a combined FIFO Stack modified from
the existing stack package by Benjamin Bayart. The package
renames the original's \Push and \Pop commands \FSPush and
\FSPop, and which work on the top/end of the FIFO/Stack), and
adds the ability to \FSUnshift and \FSShift from the the
bottom(front) of the FIFO/Stack.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/fifo-stack/fifo-stack.sty
%doc %{_texmfdistdir}/doc/latex/fifo-stack/README
%doc %{_texmfdistdir}/doc/latex/fifo-stack/fifo-stack-test.tex
%doc %{_texmfdistdir}/doc/latex/fifo-stack/fifo-stack.cwl
%doc %{_texmfdistdir}/doc/latex/fifo-stack/fifo-stack.pdf
#- source
%doc %{_texmfdistdir}/source/latex/fifo-stack/fifo-stack.dtx
%doc %{_texmfdistdir}/source/latex/fifo-stack/fifo-stack.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
