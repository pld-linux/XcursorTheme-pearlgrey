%define		_name pearlgrey
Summary:	A simple, small and crispy grey cursor theme
Summary(pl):	Prosty, ma³y i szary motyw kursorów
Name:		XcursorTheme-%{_name}
Version:	1.0
Release:	1
License:	GPL
Group:		Themes
Source0:	http://www.kde-look.org/content/files/11313-%{_name}-%{version}.tar.gz
# Source0-md5:	c9aee12d90d33efa08b9d724fcb0cec8
URL:		http://www.kde-look.org/content/show.php?content=11313
BuildRequires:	XFree86 >= 4.3
Requires:	XFree86 >= 4.3
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This theme contains simple, clear, grey and very usable cursors.

%description -l pl
Ten motyw zawiera proste, wyra¼ne, szare i bardzo funkcjonalne
kursory.

%prep
%setup -q -n %{_name}-%{version}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_iconsdir}/%{_name}/cursors
cp -df pearlgrey/cursors/*  $RPM_BUILD_ROOT%{_iconsdir}/%{_name}/cursors
echo "[Icon Theme]" > $RPM_BUILD_ROOT%{_iconsdir}/%{_name}/index.theme
echo "Name = pearlgrey" >> $RPM_BUILD_ROOT%{_iconsdir}/%{_name}/index.theme
echo "Comment = A simple, small and crispy grey cursor theme" >> $RPM_BUILD_ROOT%{_iconsdir}/%{_name}/index.theme

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_iconsdir}/%{_name}
