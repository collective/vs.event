################################################################
# vs.event - published under the GPL 2
# Authors: Andreas Jung, Veit Schiele, Anne Walther
################################################################
from AccessControl import getSecurityManager
from DateTime.DateTime import DateTime
from vs.event.content import event_util
from vs.event.testing import IntegrationTestCase


class VSEventTest(IntegrationTestCase):

    def testCalendarToolCheck(self):
        pc = self.portal.portal_calendar
        self.assertEqual(pc.meta_type, 'Chronos Calendar Tool')

    def testProperties(self):
        pc = self.portal.portal_calendar
        self.assertEqual(pc.vs_event_supplementary_events, True)
        self.assertEqual('VSEvent' in pc.getCalendarTypes(), True)
        self.assertEqual('VSSubEvent' in pc.getCalendarTypes(), True)

    def testCreateEvent(self):
        user = getSecurityManager().getUser()
        self.assertEqual('Manager' in user.getRoles(), True)
        self.portal.invokeFactory('VSEvent', id='foo')
        event = self.portal['foo']
        self.assertEqual(event.portal_type, 'VSEvent')

    def testOneDayEvent(self):
        self.portal.invokeFactory('VSEvent', id='foo')
        event = self.portal['foo']
        event.setStartDate(DateTime(2009, 01, 01))
        event.setEndDate(DateTime(2009, 01, 01))
        event.setWholeDay(True)
        d = event_util.date_for_display(event)
        self.assertEqual(d['from_str'], 'Jan 01, 2009')
        self.assertEqual(d['to_str'], None)
        self.assertEqual(d['same_day'], True)

    def testSeveralDaysEvent(self):
        self.portal.invokeFactory('VSEvent', id='foo')
        event = self.portal['foo']
        event.setStartDate(DateTime(2009, 01, 01))
        event.setEndDate(DateTime(2009, 12, 31))
        event.setWholeDay(True)
        d = event_util.date_for_display(event)
        self.assertEqual(d['from_str'], 'Jan 01, 2009')
        self.assertEqual(d['to_str'], 'Dec 31, 2009')
        self.assertEqual(d['same_day'], False)

    def testiCalVSEvent(self):
        self.portal.invokeFactory('VSEvent', id='foo')
        event = self.portal['foo']
        event.getICal()

    def testiCalVSSubEvent(self):
        self.portal.invokeFactory('VSSubEvent', id='foo')
        event = self.portal['foo']
        event.getICal()

    def testVCal(self):
        self.portal.invokeFactory('VSEvent', id='foo')
        event = self.portal['foo']
        event.getVCal()
