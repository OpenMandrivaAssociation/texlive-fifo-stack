%global tl_name fifo-stack
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.0
Release:	%{tl_revision}.1
Summary:	FIFO and stack implementation for package writers
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/fifo-stack
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/fifo-stack.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/fifo-stack.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/fifo-stack.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
A LaTeX implementation of a combined FIFO Stack modified from the
existing stack package by Benjamin Bayart. The package renames the
original's \Push and \Pop commands \FSPush and \FSPop, and which work on
the top/end of the FIFO/Stack), and adds the ability to \FSUnshift and
\FSShift from the bottom (front) of the FIFO/Stack.

