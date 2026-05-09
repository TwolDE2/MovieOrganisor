# -*- coding: utf-8 -*-
from Components.Language import language
from Tools.Directories import resolveFilename, SCOPE_PLUGINS
from os import environ as os_environ
import gettext

__version__ = "3.99"


def localeInit():
	lang = language.getLanguage()[:2]  # getLanguage returns e.g. "fi_FI" for "language_country"
	os_environ["LANGUAGE"] = lang  # Enigma doesn't set this (or LC_ALL, LC_MESSAGES, LANG). gettext needs it!
	gettext.bindtextdomain("MovieOrganisor", resolveFilename(SCOPE_PLUGINS, "Extensions/MovieOrganisor/locale"))


def _(txt):
	t = gettext.dgettext("MovieOrganisor", txt)
	if t == txt:
#		print "[MovieOrganisor] fallback to default translation for", txt
		t = gettext.gettext(txt)
	return t


def ngettext(singular, plural, n):
	t = gettext.dngettext('MovieOrganisor', singular, plural, n)
	if t in (singular, plural):
		t = gettext.ngettext(singular, plural, n)
	return t


localeInit()
language.addCallback(localeInit)
