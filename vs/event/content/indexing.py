from dateable import kalends
from zope.component import ComponentLookupError
from plone.indexer.decorator import indexer
from vs.event.interfaces import IVSEvent, IVSSubEvent


@indexer(IVSEvent)
@indexer(IVSSubEvent)
def recurrence_days(object, **kwargs):
    """Return the dates of recurrences as ordinals
    """
    try:
        recurrence = kalends.IRecurrence(object)
        return recurrence.getOccurrenceDays()
    except (ComponentLookupError, TypeError, ValueError):
        # The catalog expects AttributeErrors when a value can't be found
        raise AttributeError
