import collections

class CharOcurrence(object):

    def __init__(self, sentence):
        self.frequencies = collections.Counter(sentence)
        if ' ' in self.frequencies:
            del self.frequencies[' ']
   