################################################################
# vs.event - published under the GPL 2
# Authors: Andreas Jung, Veit Schiele, Anne Walther
################################################################
from DateTime.DateTime import DateTime
from dateable import kalends
from datetime import date
from dateutil import rrule
from vs.event.testing import IntegrationTestCase
from zope.interface import alsoProvides


class RecurrenceTest(IntegrationTestCase):

    def testRecurranceBasic(self):
        # Basic recurrence, daily for one year:
        self.portal.invokeFactory('VSEvent', 'event')
        event = getattr(self.portal, 'event')
        event.update(
            startDate=DateTime('2001/02/01 10:00'),
            endDate=DateTime('2001/02/01 14:00')
        )

        # Mark as recurring
        alsoProvides(event, kalends.IRecurringEvent)
        recurrence = kalends.IRecurrence(event)

        # Set the recurrence info
        event.frequency = rrule.DAILY
        event.until = DateTime('2002/02/01')
        event.interval = 1
        event.count = None

        # Test
        dates = recurrence.getOccurrenceDays()
        self.failUnlessEqual(dates[0], date(2001, 2, 2).toordinal())
        self.failUnlessEqual(dates[-1], date(2002, 2, 1).toordinal())
        self.failUnlessEqual(len(dates), 365)

        # Try with an interval
        event.interval = 3
        dates = recurrence.getOccurrenceDays()
        self.failUnlessEqual(dates[0], date(2001, 2, 4).toordinal())
        self.failUnlessEqual(dates[-1], date(2002, 1, 30).toordinal())
        self.failUnlessEqual(len(dates), 121)

        # Have a max count:
        event.count = 25
        dates = recurrence.getOccurrenceDays()
        self.failUnlessEqual(len(dates), 24)

    def testRecurranceMidnight(self):
        # Check that the recurrence works correctly with events starting
        # at midnight
        self.portal.invokeFactory('VSEvent', 'event')
        event = getattr(self.portal, 'event')

        event.update(startDate=DateTime('2001/02/01 00:00'),
                     endDate=DateTime('2001/02/01 04:00'))

        # Mark as recurring
        alsoProvides(event, kalends.IRecurringEvent)
        recurrence = kalends.IRecurrence(event)

        # Set the recurrence info
        event.frequency = rrule.DAILY
        event.until = DateTime('2001/02/04')
        event.interval = 1
        event.count = None

        # Test
        dates = recurrence.getOccurrenceDays()
        self.failUnlessEqual(dates[0], date(2001, 2, 2).toordinal())
        self.failUnlessEqual(dates[-1], date(2001, 2, 4).toordinal())
        self.failUnlessEqual(len(dates), 3)

    def testRecurranceWeek(self):
        self.portal.invokeFactory('VSEvent', 'event')
        event = getattr(self.portal, 'event')

        event.update(startDate=DateTime('2007/02/01 00:00'),
                     endDate=DateTime('2007/02/01 04:00'))

        # Mark as recurring
        alsoProvides(event, kalends.IRecurringEvent)
        recurrence = kalends.IRecurrence(event)

        # Set the recurrence info
        event.frequency = rrule.WEEKLY
        event.until = DateTime('2008/02/04')
        event.interval = 1
        event.count = None

        # Test
        dates = recurrence.getOccurrenceDays()
        self.failUnlessEqual(dates[0], date(2007, 2, 8).toordinal())
        self.failUnlessEqual(dates[1], date(2007, 2, 15).toordinal())
        self.failUnlessEqual(dates[2], date(2007, 2, 22).toordinal())
        self.failUnlessEqual(dates[-1], date(2008, 1, 31).toordinal())
        self.failUnlessEqual(len(dates), 52)
