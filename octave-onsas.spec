%global octpkg onsas

Summary:	An open nonlinear structural analysis solver for GNU-Octave
Name:		octave-onsas
Version:	0.2.7
Release:	2
License:	GPLv3+
Group:		Sciences/Mathematics
#Url:		https://packages.octave.org/onsas/
Url:		https://github.com/ONSAS/ONSAS.m/
Source0:	https://github.com/ONSAS/ONSAS.m/archive/v%{version}/ONSAS.m-%{version}.tar.gz

BuildRequires:  octave-devel >= 4.0.0

Requires:	octave(api) = %{octave_api}

Requires(post): octave
Requires(postun): octave

BuildArch:	noarch

%description
ONSAS is a GNU-Octave code for static/dynamic and linear/non-linear analysis
of structures. The first version was developed for educational purposes and
was published in a handbook of the course Análisis no lineal de Estructuras
taught at Facultad de Ingeniería, Universidad de la República.

The current version allows to perform dynamic/static nonlinear analyses of
beam/truss/solid 3D structures. A reduced list of features is listed at next:

  *  Elements 2-node truss, 2-node Bernoulli frame, 4-node tetrahedron.
  *  Static analysis methods Newton-Raphson Method and Cylindrical Arc-Length
     Method.
  *  Dynamic analysis methods Newmark Method and α-HHT method.
  *  Loads nodal loads, time-history user-defined loading program.


%files
%license COPYING
#doc NEWS
%dir %{octpkgdir}
%{octpkgdir}/*

#---------------------------------------------------------------------------

%prep
%autosetup -p1 -n ONSAS.m-%{version}

# fix version in DESCRIPTION
sed -i -e "s|Version: 0.2.4|Version: %{version}|" DESCRIPTION

%build
%octave_pkg_build

%install
%octave_pkg_install

%check
%octave_pkg_check

%post
%octave_cmd pkg rebuild

%preun
%octave_pkg_preun

%postun
%octave_cmd pkg rebuild

