# -*- coding: utf-8 -*-
from dateable import kalends
from plone.indexer.decorator import indexer
from zope.component import ComponentLookupError


@indexer()
def recurrence_days(context, **kwargs):
    """Return the dates of recurrences as ordinals
    """
    try:
        recurrence = kalends.IRecurrence(context)
        return recurrence.getOccurrenceDays()
    except (ComponentLookupError, TypeError, ValueError):
        # The catalog expects AttributeErrors when a value can't be found
        raise AttributeError
