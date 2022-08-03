import sys

fileName = sys.argv[1]
inputFile = "./texts/" + fileName + ".txt"
outputLines = []

with open(inputFile, 'r') as f:
    lines = f.readlines()

for lineNum, line in enumerate(lines):
    words = line.split('.')
    
    # Remove words with uncertain characters
    # words[:] = [word for word in words if '*' not in word and '!' not in word]

    # Reformat lines of words
    for index, word in enumerate(words):
        if '-' in word:
            word = word.replace('-', '')
        if '\n' in word:
            word = word.replace('\n', '')
        if '=' in word:
            word = word.replace('=', '')
        if '!' in word:
            word = word.replace('!', '')
        if '%' in word:
            word = word.replace('%', '')
        if '*' in word:
            word = word.replace('*', '')
        if index == len(words) - 1:
            word = word + '\n'
        words[index] = word

    # Add all non-empty lines to output lines
    if len(words) > 0:
        outputLine = ' '.join(words)
    else:
        outputLine = ''
    
    outputLines.append(outputLine)

with open("./texts/" + fileName + "_formatted.txt", 'w') as f:
    f.writelines(outputLines)
