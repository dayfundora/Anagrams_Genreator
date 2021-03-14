from __future__ import print_function

import sys
import collections
import char_ocurrence as cO

def get_words_dict(file_):
    result_dict = collections.defaultdict(set)

    for candidate_line in file_:
        candidate_word = candidate_line.lower().rstrip()
        if candidate_word.isalpha() and contains_vowel(candidate_word):
            length = len(candidate_word)
            result_dict[length].add(candidate_word)

    return result_dict

def del_blanks(input_string):
    """
    Delete blanks from input_string, returning the result.

    If the input was a list, return a list.
    If the input was anything else, return a str.
    """
    output_list = []
    for character in input_string:
        if character == ' ':
            pass
        else:
            output_list.append(character)

    if isinstance(input_string, list):
        return output_list

    output_string = ''.join(output_list)
    return output_string

def is_word_of_alphabet(alphabet, word):
    words_alphabet = cO.CharOcurrence(word)

    return bool(words_alphabet.is_subset(alphabet))

def prune_words_dict_for_alphabet(words_dict, alphabet):
    result_dict = collections.defaultdict(set)
    for length, words_of_length in words_dict.items():
        for word in words_of_length:
            if is_word_of_alphabet(alphabet, word):
                result_dict[length].add(word)
    return result_dict


def find_anagrams_recursive(
        result_anagrams,
        sentence,
        sentence_frequencies,
        current_words_dict,
        candidate_sentence,
):
    max_word_len = len(del_blanks(sentence)) - len(del_blanks(candidate_sentence))

    if max_word_len == 0:
        print(''.join(candidate_sentence))
        result_anagrams.append(''.join(candidate_sentence))
        return

    for current_word_len in range(1, max_word_len + 1):
        if current_word_len in current_words_dict:
            for current_word in current_words_dict[current_word_len]:
                current_candidate_sentence = candidate_sentence[:]
                if current_candidate_sentence:
                    current_candidate_sentence.append(' ')

                current_candidate_sentence.extend(current_word)

                find_anagrams_recursive(
                    result_anagrams,
                    sentence,
                    sentence_frequencies,
                    current_words_dict,
                    current_candidate_sentence,
                    )

def find_anagrams(sentence):
    result_anagrams = []

    sentence_list = list(sentence)

    sentence_frequencies = cO.CharOcurrence(sentence_list)
    
    with open('english.txt', 'r') as dictionary_file:
        original_dict = get_words_dict(dictionary_file)

    candidate_sentence = []

    find_anagrams_recursive(
        result_anagrams,
        sentence_list,
        sentence_frequencies,
        original_dict,
        candidate_sentence,
        )

    return result_anagrams
