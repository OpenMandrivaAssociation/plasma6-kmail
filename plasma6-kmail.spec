%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)
%global optflags %{optflags} -fexceptions

Summary:	KDE email client
Name:		plasma6-kmail
Version:	24.01.85
Release:	1
Epoch:		3
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		http://www.kde.org
Source0:	http://download.kde.org/%{stable}/release-service/%{version}/src/kmail-%{version}.tar.xz
BuildRequires:	cmake(ECM)
BuildRequires:	boost-devel
BuildRequires:	pkgconfig(ldap)
BuildRequires:	sasl-devel
BuildRequires:	pkgconfig(Qt6DBus)
BuildRequires:	pkgconfig(Qt6Network)
BuildRequires:	pkgconfig(Qt6Test)
BuildRequires:	pkgconfig(Qt6Widgets)
BuildRequires:	pkgconfig(Qt6WebEngineCore)
BuildRequires:	pkgconfig(Qt6WebEngineWidgets)
BuildRequires:	pkgconfig(Qt6Xml)
BuildRequires:	cmake(Qt6Keychain)
BuildRequires:	cmake(KPim6WebEngineViewer)
BuildRequires:	cmake(KPim6AkonadiSearch)
BuildRequires:	cmake(Gpgmepp)
BuildRequires:	cmake(KF6Crash)
BuildRequires:	cmake(KF6Bookmarks)
BuildRequires:	cmake(KF6Codecs)
BuildRequires:	cmake(KF6Config)
BuildRequires:	cmake(KF6ConfigWidgets)
BuildRequires:	cmake(KF6DBusAddons)
BuildRequires:	cmake(KF6DocTools)
BuildRequires:	cmake(KF6GuiAddons)
BuildRequires:	cmake(KF6I18n)
BuildRequires:	cmake(KF6IconThemes)
BuildRequires:	cmake(KF6ItemViews)
BuildRequires:	cmake(KF6JobWidgets)
BuildRequires:	cmake(KF6KIO)
BuildRequires:	cmake(KF6KCMUtils)
BuildRequires:	cmake(KF6Notifications)
BuildRequires:	cmake(KF6NotifyConfig)
BuildRequires:	cmake(KF6Parts)
BuildRequires:	cmake(KF6Service)
BuildRequires:	cmake(KF6Sonnet)
BuildRequires:	cmake(KF6TextWidgets)
BuildRequires:	cmake(KF6TextUtils)
BuildRequires:	cmake(KF6WidgetsAddons)
BuildRequires:	cmake(KF6WindowSystem)
BuildRequires:	cmake(KF6XmlGui)
BuildRequires:	cmake(KPim6Akonadi)
BuildRequires:	cmake(KPim6AkonadiContactCore)
BuildRequires:	cmake(KPim6AkonadiMime)
BuildRequires:	cmake(KF6Contacts)
BuildRequires:	cmake(KF6CalendarCore)
BuildRequires:	cmake(KF6TextTemplate)
BuildRequires:	cmake(KF6StatusNotifierItem)
BuildRequires:	cmake(KPim6CalendarUtils)
BuildRequires:	cmake(KPim6IdentityManagementCore)
BuildRequires:	cmake(KPim6LdapCore)
BuildRequires:	cmake(KPim6LdapWidgets)
BuildRequires:	cmake(KPim6MailTransport)
BuildRequires:	cmake(KPim6TextEdit)
BuildRequires:	cmake(KPim6KontactInterface)
BuildRequires:	cmake(KPim6Mime)
BuildRequires:	cmake(KPim6Gravatar)
BuildRequires:	cmake(KPim6Libkleo)
BuildRequires:	cmake(KPim6KSieve)
BuildRequires:	cmake(KPim6MailCommon)
BuildRequires:	cmake(KPim6MessageCore)
BuildRequires:	cmake(KPim6MessageComposer)
BuildRequires:	cmake(KPim6MessageList)
BuildRequires:	cmake(KPim6MessageViewer)
BuildRequires:	cmake(KPim6PimCommonAkonadi)
BuildRequires:	cmake(KPim6TemplateParser)
BuildRequires:	cmake(KPim6Tnef)
BuildRequires:	cmake(KF6UserFeedback)
Requires:	kdepim-runtime
Suggests:	kdepim-addons
Suggests:	pinentry-qt6
Suggests:	ksshaskpass
Requires:	sasl-plug-plain
Requires:	sasl-plug-ntlm
Requires:	sasl-plug-login
Requires:	sasl-plug-digestmd6
Requires:	akonadi-archivemail-agent
Requires:	akonadi-followupreminder-agent
Requires:	akonadi-import-wizard
Requires:	akonadi-mailfilter-agent
Requires:	akonadi-sendlater-agent
Requires:	akonadi-unifiedmailbox-agent
Requires:	grantlee
Requires:	grantlee-editor
Requires:	ktnef
Requires:	mbox-importer
Requires:	pim-data-exporter
Requires:	pim-sieve-editor
Obsoletes:	kdepim < 3:17.04.0
Provides:	kmail2 = %{EVRD}
Obsoletes:	messageviewer
Conflicts:	kontact < 3:17.04.0
Conflicts:	kaddressbook < 3:17.04.0
Conflicts:	knotes < 3:17.04.0
Conflicts:	korganizer < 3:17.04.0

%description
KMail is the email component of Kontact, the integrated personal
information manager of KDE.

%files -f kmail.lang -f kmail-refresh-settings.lang
%{_bindir}/akonadi_mailmerge_agent
%{_datadir}/akonadi/agents/mailmergeagent.desktop
%{_datadir}/knotifications6/akonadi_mailmerge_agent.notifyrc
%{_datadir}/applications/kmail_view.desktop
%{_datadir}/applications/org.kde.kmail2.desktop
%{_datadir}/applications/org.kde.kmail-refresh-settings.desktop
%{_bindir}/kmail
%{_bindir}/kmail-refresh-settings
%{_datadir}/config.kcfg/kmail.kcfg
%dir %{_datadir}/kmail2
%{_datadir}/kmail2/*
%{_docdir}/*/*/kmail2
%{_iconsdir}/*/*/emblems/*.svg
%{_iconsdir}/*/*/apps/kmail.*
%{_datadir}/knotifications6/kmail2.notifyrc
%{_datadir}/qlogging-categories6/kmail.categories
%{_datadir}/qlogging-categories6/kmail.renamecategories
%{_datadir}/metainfo/org.kde.kmail2.appdata.xml
%{_datadir}/dbus-1/interfaces/org.kde.kmail.*.xml
%{_datadir}/dbus-1/services/org.kde.kmail.service
%{_qtdir}/plugins/kmailpart.so
%{_qtdir}/plugins/pim6/kontact/kontact_kmailplugin.so
%{_qtdir}/plugins/pim6/kontact/kontact_summaryplugin.so
%{_qtdir}/plugins/pim6/kcms/kmail/kcm_kmail_accounts.so
%{_qtdir}/plugins/pim6/kcms/kmail/kcm_kmail_appearance.so
%{_qtdir}/plugins/pim6/kcms/kmail/kcm_kmail_composer.so
%{_qtdir}/plugins/pim6/kcms/kmail/kcm_kmail_misc.so
%{_qtdir}/plugins/pim6/kcms/kmail/kcm_kmail_plugins.so
%{_qtdir}/plugins/pim6/kcms/kmail/kcm_kmail_security.so
%{_qtdir}/plugins/pim6/kcms/summary/kcmkmailsummary.so
%{_qtdir}/plugins/pim6/kcms/summary/kcmkontactsummary.so
%{_libdir}/libkmailprivate.so*
%{_libdir}/libmailfilteragentprivate.so*

#-----------------------------------------------------------------------------

%package -n akonadi-archivemail-agent
Summary:	Akonadi archivemail agent
Group:		Graphical desktop/KDE

%description -n akonadi-archivemail-agent
Akonadi archivemail agent.

%files -n akonadi-archivemail-agent -f akonadi_archivemail_agent.lang
%{_bindir}/akonadi_archivemail_agent
%{_datadir}/akonadi/agents/archivemailagent.desktop
%{_datadir}/config.kcfg/archivemailagentsettings.kcfg
%{_docdir}/*/*/akonadi_archivemail_agent
%{_datadir}/knotifications6/akonadi_archivemail_agent.notifyrc
%{_qtdir}/plugins/pim6/akonadi/config/archivemailagentconfig.so

#-----------------------------------------------------------------------------

%package -n akonadi-followupreminder-agent
Summary:	Akonadi followupreminder agent
Group:		Graphical desktop/KDE

%description -n akonadi-followupreminder-agent
Akonadi followup reminder agent allows to remind you when an email was not
answered.

%files -n akonadi-followupreminder-agent -f akonadi_followupreminder_agent.lang
%{_bindir}/akonadi_followupreminder_agent
%{_datadir}/akonadi/agents/followupreminder.desktop
%{_docdir}/*/*/akonadi_followupreminder_agent
%{_datadir}/knotifications6/akonadi_followupreminder_agent.notifyrc
%{_qtdir}/plugins/pim6/akonadi/config/followupreminderagentconfig.so

#-----------------------------------------------------------------------------

%package -n akonadi-mailfilter-agent
Summary:	Akonadi mailfilter agent
Group:		Graphical desktop/KDE

%description -n akonadi-mailfilter-agent
Akonadi mailfilter agent.

%files -n akonadi-mailfilter-agent -f akonadi_mailfilter_agent.lang -f akonadi_mailmerge_agent.lang
%{_bindir}/akonadi_mailfilter_agent
%{_datadir}/akonadi/agents/mailfilteragent.desktop
%{_datadir}/knotifications6/akonadi_mailfilter_agent.notifyrc

#-----------------------------------------------------------------------------

%package -n akonadi-sendlater-agent
Summary:	Akonadi sendlater agent
Group:		Graphical desktop/KDE

%description -n akonadi-sendlater-agent
Akonadi sendlater agent.

%files -n akonadi-sendlater-agent -f akonadi_sendlater_agent.lang
%{_bindir}/akonadi_sendlater_agent
%{_datadir}/akonadi/agents/sendlateragent.desktop
%{_docdir}/*/*/akonadi_sendlater_agent
%{_datadir}/knotifications6/akonadi_sendlater_agent.notifyrc

#-----------------------------------------------------------------------------

%package -n akonadi-unifiedmailbox-agent
Summary:	Akonadi unified mailbox agent
Group:		Graphical desktop/KDE

%description -n akonadi-unifiedmailbox-agent
Akonadi unified mailbox agent.

%files -n akonadi-unifiedmailbox-agent -f akonadi_unifiedmailbox_agent.lang
%{_bindir}/akonadi_unifiedmailbox_agent
%{_datadir}/akonadi/agents/unifiedmailboxagent.desktop

#----------------------------------------------------------------------------

%package -n ktnef
Summary:	KDE TNEF file viewer
Group:		Graphical desktop/KDE

%description -n ktnef
The TNEF file viewer allows you to handle mail attachments using the TNEF
format. These attachments are usually found in mails coming from Microsoft
mail servers and embed the mail properties as well as the actual attachments.

%files -n ktnef -f ktnef.lang
%{_datadir}/applications/org.kde.ktnef.desktop
%{_bindir}/ktnef
%{_docdir}/*/*/ktnef
%{_iconsdir}/*/*/actions/ktnef_extract_*.*
%{_iconsdir}/*/*/apps/ktnef.*

#----------------------------------------------------------------------

%prep
%autosetup -p1 -n kmail-%{version}
%cmake \
	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON \
	-G Ninja

%build
%ninja -C build

%install
%ninja_install -C build


%find_lang akonadi_archivemail_agent
%find_lang akonadi_followupreminder_agent
%find_lang akonadi_mailfilter_agent
%find_lang akonadi_mailmerge_agent
%find_lang akonadi_sendlater_agent
%find_lang akonadi_unifiedmailbox_agent
%find_lang kmail
%find_lang kmail-refresh-settings
%find_lang ktnef
