# -*- coding: utf-8 -*-
################################################################
# vs.event - published under the GPL 2
# Authors: Andreas Jung, Veit Schiele, Anne Walther
################################################################
from config import PROJECTNAME

try:
    from Products.LinguaPlone import public as atapi
except ImportError:
    from Products.Archetypes import atapi

from Products.CMFCore import utils

from AccessControl import ModuleSecurityInfo
from zope.i18nmessageid import MessageFactory
MessageFactory = MessageFactory(PROJECTNAME)
ModuleSecurityInfo('vs.event').declarePublic('MessageFactory')

from logging import getLogger
logger = getLogger(PROJECTNAME)

def initialize(context):
    """Initializer called when used as a Zope 2 product."""

    content_types, constructors, ftis = atapi.process_types(
        atapi.listTypes(PROJECTNAME),
        PROJECTNAME)

    ADD_PERMISSIONS={}
    for type in content_types:
        ADD_PERMISSIONS[type.portal_type] = """Add %s""" %type.portal_type

    allTypes = zip(content_types, constructors)
    for atype, constructor in allTypes:
        utils.ContentInit(
            "%s: %s" % (PROJECTNAME, atype.portal_type),
            content_types      = (atype,),
            permission         = ADD_PERMISSIONS[atype.portal_type],
            extra_constructors = (constructor,),
            ).initialize(context)


#from Products.CMFCore.permissions import setDefaultRoles
#setDefaultRoles('Add VSEvent', ('Manager', ))
