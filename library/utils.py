# coding: utf-8
# This file is a part of VK4XMPP transport
# © simpleApps, 2014.

import xmpp, urllib
from hashlib import sha1

##needed: requred fields
## needed: form title

def buildDataForm(form=None, type="submit", fields=[], title=None):
	form = form or xmpp.DataForm(type, title=title)
	for key in fields:
		field = form.setField(key["var"], key.get("value"), key.get("type"), key.get("options"))
		if key.get("payload"):
			field.setPayload(key["payload"])
		if key.get("label"):
			field.setLabel(key["label"])
		if key.get("requred"):
			field.setRequired()

	return form

def buildIQError(stanza, error=None, text=None):
	if not error:
		error = xmpp.ERR_FEATURE_NOT_IMPLEMENTED
	error = xmpp.Error(stanza, error, True)
	if text:
		eTag = error.getTag("error")
		eTag.setTagData("text", text)
	return error

def getLinkData(url, encode=True):
	try:
		opener = urllib.urlopen(url)
	except Exception:
		return ""
	data = opener.read()
	if data and encode:
		data = data.encode("base64")
	return data