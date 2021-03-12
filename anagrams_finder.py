from __future__ import print_function

import sys
import collections
import char_ocurrence as cO

def get_words_dict(file_):
    result_dict = collections.defaultdict(set)

    for candidate_line in file_:
        candidate_word = candidate_line.lower().rstrip()
        length = len(candidate_word)
        result_dict[length].add(candidate_word)

    return result_dict

def find_anagrams(sentence):
    result_anagrams = []

    sentence_list = list(sentence)

    sentence_frequencies = cO.CharOcurrence(sentence_list)
    
    with open('english.txt', 'r') as dictionary_file:
        original_dict = get_words_dict(dictionary_file)

    return result_anagrams
