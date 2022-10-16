#!/bin/bash

# This is a script that will run a suite of tests on the voynich scripts.
# The script iterates through an array of test files and runs each test on ./tester.sh, once for each script.
# The script requires no inputs
# The script echoes the outputs of each individual test run.
# More tests and scripts to test can be added to the suite by adding test filenames and script names to the array below.

TESTS=(empty.txt multi_line.txt one_character.txt single_number.txt single_word.txt multi_paragraph.txt single_repeated_character.txt all_anagrams.txt)
SCRIPTS=(frequency anagram)


for test in "${TESTS[@]}"
do
    for script in "${SCRIPTS[@]}"
    do
        bash "./tester.sh" $script $test
    done
done
exit 0