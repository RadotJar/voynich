class Word:
  def __init__(self, word):
    self.word = word
    self.characters = [l for l in word]
    self.characters.sort()
    self.anagrams = []
    self.anagram_count = 0
  def add_anagram(self, anagram):
    self.anagrams.append(anagram)
    self.anagram_count += 1
  def __str__(self):
    return self.word

def main():
  import numpy as np
  import sys
  from itertools import permutations

  inputText = sys.argv[1]
  word_array = []
  outputLines = []

  # First go through text and add each word to an array
  with open(inputText, 'r') as f:
      lines = f.readlines()

  for line in lines:
    words = line.split()

    for word in words:
      word_array.append(Word(word))

  # For each word, check which other word contains the same characters (is an anagram)
  for word in word_array:
        for other_word in word_array:
          if (other_word.word != word.word) and (np.array_equal(word.characters, other_word.characters)) and (other_word.word not in word.anagrams):
            word.add_anagram(other_word.word)

  # Sort word array by number of anagrams
  word_array.sort(key=lambda x: x.anagram_count, reverse=True)

  # Create output
  for word in word_array:
    output_line = word.word + ': ' + str(word.anagram_count) + ' anagrams: '
    for anagram in word.anagrams:
      output_line += anagram + ' '
    output_line += '\n'
    outputLines.append(output_line)

  with open(inputText + '_anagrams', 'w') as f:
      f.writelines(outputLines)

if __name__ == "__main__":
    main()
