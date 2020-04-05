from pymongo.command_cursor import CommandCursor
import warnings
import json


def one_line_warning(message, category, filename, lineno, file=None, line=None):
    return f'{filename}:{lineno}: {category.__name__}: {message}\n'


class ToObject(object):
    def __init__(self, d):
        if type(d) is CommandCursor:
            ref = d.next()
            if d.alive:
                warnings.formatwarning = one_line_warning
                warnings.warn(f"Object Generator Is Still Alive => {d}", RuntimeWarning)
            d = ref
        self.__dict__ = d


def to_dicts(d):
    return json.loads(d.to_json())
