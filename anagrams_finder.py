from __future__ import print_function

import sys
import collections
import char_ocurrence as cO

def contains_vowel(string):
    """Return True iff string contains a vowel"""
    vowels = set('aeiou')
    string_set = set(string)

    return bool(vowels & string_set)

def get_words_dict(file_):
    """Read a file with words.  Prune out anything with punctuation."""
    result_dict = collections.defaultdict(set)

    for candidate_line in file_:
        candidate_word = candidate_line.lower().rstrip()
        if candidate_word.isalpha() and contains_vowel(candidate_word):
            length = len(candidate_word)
            result_dict[length].add(candidate_word)

    return result_dict

def is_word_of_alphabet(alphabet, word):
    """Check if a word conforms to our alphabet."""
    words_alphabet = cO.CharOcurrence(word)
    return bool(words_alphabet.is_subset(alphabet))


def prune_words_dict_for_alphabet(words_dict, alphabet):
    """Eliminate words that aren't over the appropriate alphabet from our words_dict."""
    result_dict = collections.defaultdict(set)
    for length, words_of_length in words_dict.items():
        for word in words_of_length:
            if is_word_of_alphabet(alphabet, word):
                result_dict[length].add(word)
    return result_dict

def del_blanks(input_string):
    """Delete blanks from input_string, returning the result."""
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


def find_anagrams_recursive(
        result_anagrams,
        sentence,
        sentence_frequencies,
        prune_dict,
        candidate_sentence,
):
    """Find anagrams for sentence."""
    usable_letter_counts = cO.CharOcurrence(sentence) - cO.CharOcurrence(candidate_sentence)

    current_words_dict = prune_words_dict_for_alphabet(prune_dict, usable_letter_counts)

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


def find_anagrams(sentence, dict_file='english.txt'):
    """Find anagrams for a sentence."""
    
    result_anagrams = []

    sentence_list = list(sentence)

    sentence_frequencies = cO.CharOcurrence(sentence_list)
    
    with open(dict_file, 'r') as dictionary_file:
        original_dict = get_words_dict(dictionary_file)

    prune_dict = prune_words_dict_for_alphabet(original_dict, sentence_frequencies)

    candidate_sentence = []

    find_anagrams_recursive(
        result_anagrams,
        sentence_list,
        sentence_frequencies,
        prune_dict,
        candidate_sentence,
        )

    return result_anagrams
