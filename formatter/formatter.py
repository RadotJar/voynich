import sys

inputText = sys.argv[1]
outputLines = []

with open(inputText, 'r') as f:
    lines = f.readlines()

for lineNum, line in enumerate(lines):
    words = line.split('.')
    
    # Remove words with uncertain characters
    words[:] = [word for word in words if '*' not in word and '!' not in word]

    # Reformat lines of words
    for index, word in enumerate(words):
        if '-' in word:
            word = word.replace('-', '')
        if '\n' in word:
            word = word.replace('\n', '')
        if '=' in word:
            word = word.replace('=', '\n\n')
        if index == len(words) - 1 and '\n' not in word:
            word = word + '\n'
        words[index] = word

    # Add all non-empty lines to output lines
    if len(words) > 0:
        outputLine = ' '.join(words)
    else:
        outputLine = ''
    
    outputLines.append(outputLine)

with open(inputText + '_formatted', 'w') as f:
    f.writelines(outputLines)
