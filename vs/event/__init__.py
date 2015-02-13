# -*- coding: utf-8 -*-
################################################################
# vs.event - published under the GPL 2
# Authors: Andreas Jung, Veit Schiele, Anne Walther
################################################################
from .config import PROJECTNAME
from Products.Archetypes import atapi
from Products.CMFCore import utils
from logging import getLogger
from zope.i18nmessageid import MessageFactory

MessageFactory = MessageFactory(PROJECTNAME)
log = getLogger(">>>>>>>>")


def initialize(context):
    """Initializer called when used as a Zope 2 product."""

    content_types, constructors, ftis = atapi.process_types(
        atapi.listTypes(PROJECTNAME),
        PROJECTNAME
    )

    ADD_PERMISSIONS = {}
    for t in content_types:
        ADD_PERMISSIONS[t.portal_type] = """Add %s""" % t.portal_type

    for atype, constructor in zip(content_types, constructors):
        utils.ContentInit(
            "%s: %s" % (PROJECTNAME, atype.portal_type),
            content_types=(atype,),
            permission = ADD_PERMISSIONS[atype.portal_type],
            extra_constructors = (constructor,),
        ).initialize(context)

