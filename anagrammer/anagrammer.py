class Character:
  def __init__(self, character):
    self.character = character
    self.anagram_count = 0
    self.occurence_count = 0
  def add_anagram(self):
    self.anagram_count += 1
  def add_occurence(self):
    self.occurence_count += 1
  def percentage(self):
    if self.anagram_count == 0:
      return 0
    else:
      return self.anagram_count / self.occurence_count * 100
class Word:
  def __init__(self, word):
    self.word = word
    self.characters = [l for l in word]
    self.characters.sort()
    self.anagrams = {}
    self.anagram_count = 0
  def add_anagram(self, anagram):
    if anagram in self.anagrams:
      self.anagrams[anagram] = self.anagrams[anagram] + 1
    else:
      self.anagrams[anagram] = 1
      self.anagram_count += 1
  def __str__(self):
    return self.word

def main():
  import numpy as np
  import sys
  from itertools import permutations

  inputText = sys.argv[1]
  word_array = []
  character_array = []
  outputLines = []

  # First go through text and add each word and character occurrence array
  with open(inputText, 'r') as f:
      lines = f.readlines()

  for line in lines:
    words = line.split()
    for word in words:
      word_object = Word(word)
      word_array.append(word_object)
      for character in word_object.characters:
        character_object = Character(character)
        for existing_character in character_array:
          if existing_character.character == character_object.character:
            existing_character.add_occurence()
            break
        else:
          character_object.add_occurence()
          character_array.append(character_object)

  # For each word, check which other word contains the same characters (is an anagram)
  for word in word_array:
    for other_word in word_array:
      if (other_word.word != word.word) and (np.array_equal(word.characters, other_word.characters)):
        word.add_anagram(other_word.word)

  # Sort word array by number of anagrams
  word_array.sort(key=lambda x: x.anagram_count, reverse=True)

  # Remove duplicate words from word_array
  output_word_array = []
  for word in word_array:
    for output_word in output_word_array:
      if word.word == output_word.word:
        break
    else:
      output_word_array.append(word)

  # For each unique word with anagrams, add to its character's anagram count
  for word in output_word_array:
    for character in word.characters:
      for existing_character in character_array:
        if existing_character.character == character:
          for anagram in word.anagrams:
            for i in range(word.anagrams[anagram]):
              existing_character.add_anagram()

  # Sort character array by number of anagrams
  character_array.sort(key=lambda x: x.percentage(), reverse=True)

  # Create output
  outputLines.append("Word Profiles:\n")
  for word in output_word_array:
    if(word.anagram_count > 0):
      output_line = word.word + ': ' + str(word.anagram_count) + ' anagrams: '
      for anagram in word.anagrams:
        output_line += anagram + ' (' + str(word.anagrams[anagram]) + ') '
      output_line += '\n'
      outputLines.append(output_line)
  
  outputLines.append("\nCharacter Profiles (# times in anagrammable word / # total occurences):\n")
  for character in character_array:
    if(character.anagram_count > 0):
      output_line = character.character + ': ' + str(character.anagram_count) + '/' + str(character.occurence_count) + ' = ' + str(character.percentage()) + '%\n'
      outputLines.append(output_line)

  with open(inputText + '_anagrams', 'w') as f:
      f.writelines(outputLines)

if __name__ == "__main__":
    main()
