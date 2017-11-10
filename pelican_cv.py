'''
#################################################
Pelican plugin to generate a cv from a JSONResume
#################################################
'''
import os
import json

from datetime import datetime
from pelican import signals
from pelican.utils import get_date


def fix_dates(entries):
    """Convert string star / end dates to datetime objects.
    """
    for entry in entries:
        if 'startDate' in entry:
            entry['startDate'] = get_date(entry['startDate'])
        if 'endDate' in entry:
            entry['endDate'] = get_date(entry['endDate'])


def sort_entries(entries):
    """Sort entries by startDate and endDate.
    """
    entries.sort(key=lambda e: (e['startDate'], e['endDate'])if 'endDate' in e else (e['startDate'], datetime.now()),
                 reverse=True)


def load_cvs(generator):
    """Adds ``cvs`` list to the context. It is a dictionary of source filenames
    containing the loaded JSON.
    """
    if 'CVS_SRC' in generator.settings:
        cvs = {}
        for source in generator.settings['CVS_SRC']:
            with open(source) as in_f:
                cv = json.load(in_f)
                for value in cv.values():
                    if isinstance(value, list):
                        fix_dates(value)
                        sort_entries(value)
                cvs[source.replace(os.path.sep, '/').split('/')[-1]] = cv
        generator.context['cvs'] = cvs


def register():
    """Registers the processing callbacks."""
    signals.generator_init.connect(load_cvs)
