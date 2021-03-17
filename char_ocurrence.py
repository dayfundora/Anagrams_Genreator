import collections

class CharOcurrence(object):

    def __init__(self, sentence):
        self.frequencies = collections.Counter(sentence)
        if ' ' in self.frequencies:
            del self.frequencies[' ']

    def __sub__(self, other):
        result = CharOcurrence('')

        result.frequencies = self.frequencies - other.frequencies

        return result

    def is_subset(self, other):
        self_keys = set(self.frequencies)
        other_keys = set(other.frequencies)

        if self_keys <= other_keys:
            for key in self_keys:
                if self.frequencies[key] > other.frequencies[key]:
                    return False
            return True

        return False

  