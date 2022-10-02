import argparse
import os
import numpy as np
import sys
from itertools import permutations
import matplotlib.pyplot as plt


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

class VWord:
  def __init__(self, word):
    self.word = word
    self.characters = constructVMCharacters(word)
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

# Constructs characters according to special VM rules
def constructVMCharacters(word):
    i = 0
    characters = []
    while i < len(word):
        character = ""
        if(word[i] == "{"):
            j = i
            while word[j] != "}":
                character += word[j]
                j += 1
            else:
                character += word[j]
            i = j
        elif(word[i] == "@"):
            j = i
            while word[j] != ";":
                character += word[j]
                j += 1
            else:
                character += word[j]
            i = j
        else:
            character = word[i]
        
        characters.append(character)
        i += 1
    return characters

def main():

  # Get input from command line
  input = get_input()

  filePath = input["file_path"]
  fileName = os.path.basename(filePath)
  word_array = []
  character_array = []
  outputLines = []
  plot_x_axis = []
  plot_y_axis = []

  with open(filePath, 'r') as f:
      lines = f.readlines()

  word_array = []
  character_array = []
  # First go through text and add each word and character occurrence array
  for line in lines:
    words = line.split()
    for word in words:
      if(input["voynich"]):
        word_object = VWord(word)
      else:
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
        # Ignore single character words
        if len(word.characters) > 1:
          word.add_anagram(other_word.word)
    # For each word that has anagrams, add to its character's anagram count
    for character in word.characters:
      for existing_character in character_array:
        if existing_character.character == character:
          if word.anagram_count > 0:
            existing_character.add_anagram()
  
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
      plot_x_axis.append(character.character)
      plot_y_axis.append(character.percentage())

  with open("./texts/" + fileName + "_anagrams.txt", "w") as f:
      f.writelines(outputLines)

  ax = plt.figure()
  ax.suptitle("Anagram Analysis of " + fileName)
  ax.supxlabel("Character", va='bottom')
  ax.supylabel("Percentage of Occurences in Valid Anagrams")

  ax1 = plt.subplot(111)
  ax1.bar(plot_x_axis, plot_y_axis)
  ax1.set_ylim([0,100])
  plt.savefig("./figures/" + fileName + "_anagram_plot.png")

def get_input():
    parser = argparse.ArgumentParser(description="Voynich Manuscript Anagram Analyser", formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("file_path", help="The path to the file to be analysed. Must be a .txt file.")
    parser.add_argument("--voynich", action="store_true", help="Apply Voynich specific analysis rules.")
    args = parser.parse_args()
    input = vars(args)
    return input


if __name__ == "__main__":
    main()
