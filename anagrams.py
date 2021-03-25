import sys
import anagrams_finder


def main():
    sentence, include_words = [], []

    for word in sys.argv[1:]:
        
        if(word.startswith('+')):
            include_words.append(word[1:].lower())
        else:
            sentence.append(word.lower())

    original_sentence = ' '.join(word.strip() for word in sys.argv[1:]).lower()
    
    anagrams_finder.find_anagrams(original_sentence, include=include_words)


main()
