import char_ocurrence as cO

def find_anagrams(sentence):
    result_anagrams = []

    sentence_list = list(sentence)

    sentence_frequencies = cO.CharOcurrence(sentence_list)

    return result_anagrams
