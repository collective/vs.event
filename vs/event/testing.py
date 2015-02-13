# -*- coding: utf-8 -*-
"""Base module for unittesting."""

from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import login
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import PloneSandboxLayer
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from plone.app.testing import TEST_USER_NAME
from plone.testing import z2

import unittest2 as unittest


class VsEventLayer(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        """Set up Zope."""
        # Load ZCML
        import dateable.chronos
        self.loadZCML(package=dateable.chronos)
        import vs.event
        self.loadZCML(package=vs.event)
        z2.installProduct(app, 'vs.event')
        z2.installProduct(app, 'dateable.chronos')

    def setUpPloneSite(self, portal):
        """Set up Plone."""
        # Install into Plone site using portal_setup
        applyProfile(portal, 'vs.event:default')

        # Login and create some test content
        setRoles(portal, TEST_USER_ID, ['Manager'])
        login(portal, TEST_USER_NAME)
        portal.invokeFactory('Folder', 'folder')

        # Commit so that the test browser sees these objects
        portal.portal_catalog.clearFindAndRebuild()
        import transaction
        transaction.commit()

    def tearDownZope(self, app):
        """Tear down Zope."""
        z2.uninstallProduct(app, 'rg.infocard')


FIXTURE = VsEventLayer()
INTEGRATION_TESTING = IntegrationTesting(
    bases=(FIXTURE,),
    name="VsEventLayer:Integration"
)
FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(FIXTURE,),
    name="VsEventLayer:Functional"
)


class IntegrationTestCase(unittest.TestCase):

    """Base class for integration tests."""

    layer = INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']


class FunctionalTestCase(unittest.TestCase):

    """Base class for functional tests."""

    layer = FUNCTIONAL_TESTING
