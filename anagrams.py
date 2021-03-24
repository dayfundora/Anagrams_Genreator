import sys
import anagrams_finder


def main():
    original_sentence = ' '.join(word.strip() for word in sys.argv[1:]).lower()
    
    anagrams_finder.find_anagrams(original_sentence)


main()
