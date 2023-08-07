Name:		hybrid-encoder
Version:	20230317
Release:	1
Summary:	A very complete gui for video encoding
License:	custom
BuildRequires:	curl
BuildRequires:	unzip
Requires:	framecounter
Requires:	freetype
Requires:	glib2
Requires:	openssl
Requires:	qt5-qtmultimedia
Recommends:	fdkaac
Recommends:	flac
Recommends:	gpac
Recommends: 	libvpx
Recommends:	lsdvd
Recommends:	mediainfo
Recommends:	mencoder
Recommends:	mkvtoolnix
Recommends:	mplayer
Recommends:	opus
Recommends:	sox
Recommends:	wine
Recommends:	x264
Recommends:	x265
URL:		https://www.selur.de/sites/default/files/hybrid_downloads/Hybrid_20230317_64bit_binary_qt515.zip
Source0:	Hybrid.png
Source1:	hybrid.desktop
Source2:	LICENSE

%description
A very complete gui for video encoding

%prep
curl %{url} -o hybrid.zip
unzip hybrid.zip

%install
mkdir -p %{buildroot}/usr/bin
mkdir -p %{buildroot}%{_datadir}/applications
mkdir -p %{buildroot}%{_datadir}/pixmaps
mkdir -p %{buildroot}%{_datadir}/licenses/Hybrid
install -m 755 Hybrid %{buildroot}%{_bindir}/Hybrid
install -m 644 %{SOURCE1} %{buildroot}%{_datadir}/applications/hybrid.desktop
install -m 644 %{SOURCE0} %{buildroot}%{_datadir}/pixmaps/Hybrid.png
install -m 644 %{SOURCE2} %{buildroot}%{_datadir}/licenses/Hybrid/LICENSE


%files
%{_bindir}/Hybrid
/usr/share/pixmaps/Hybrid.png
/usr/share/licenses/Hybrid/LICENSE
/usr/share/applications/hybrid.desktop

%changelog
* Mon Aug 07 2023  <> - 20230317
- Initial version
