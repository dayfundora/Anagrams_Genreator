import collections

class CharOcurrence(object):
    """Collection of char ocurrence in a sentence"""

    def __init__(self, sentence):
        """Initialize a CharOcurrence."""
        self.frequencies = collections.Counter(sentence)
        if ' ' in self.frequencies:
            del self.frequencies[' ']

    def __sub__(self, other):
        """Subtract two CharOcurrence"""
        result = CharOcurrence('')

        result.frequencies = self.frequencies - other.frequencies

        return result

    def is_subset(self, other):
        """Return True iff self is a subset of other."""
        self_keys = set(self.frequencies)
        other_keys = set(other.frequencies)

        if self_keys <= other_keys:
            for key in self_keys:
                if self.frequencies[key] > other.frequencies[key]:
                    return False
            return True

        return False

  