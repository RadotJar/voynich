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

  # For each word, check all of its anagrams against all other words in the array
  for word in word_array:
    for anagram in permutations(word.word):
      anagram = ''.join(anagram)
      print(anagram)
      if anagram != word.word:
        for other_word in word_array:
          if (other_word.word == anagram) and (anagram not in word.anagrams):
            word.add_anagram(anagram)

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
