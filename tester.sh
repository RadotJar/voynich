#!/bin/bash

# This is a script that runs a single test and prints the result.
# The script is called with the type of test as the first argument and the input test file as the second.
# - Type of test is one of: "frequency", "anagram"
# The script will print "running test: <testType> <testFile>..."
# The script will look for a file named <testFile> in ./texts.
# The script will run this test and print the resultant outputs to ./texts as <testFile>_frequency_analysis.txt or <testFile>_anagrams.txt
# The script will then compare the outputs with the expected output at ./texts/<testFile>_frequency_analysis_eo.txt or ./texts/<testFile>_anagrams_eo.txt.
# The script will then print "PASS" to the command line if the outputs match the expected outputs or "FAIL" if they do not match.

testType=$1
testname=$2

TESTTYPES=(frequency anagram)
# Check that inputs are provided and correct
if [ -z "$testType" ] || [ -z "$testname" ]; then
    echo "Error: testType and testname must be provided as arguments"
    exit 1
fi
if [[ ! " ${TESTTYPES[@]} " =~ " ${testType} " ]]; then
    echo "Error: testType must be one of: ${TESTTYPES[@]}"
    exit 1
fi
if [ ! -f "./texts/$testname" ]; then
    echo "No input file found for test $testname."
    exit 1
fi

# Use python venv
source /home/radotjar/dev/github/voynich/venv/bin/activate

# Run the test
if [ "$testType" == "frequency" ]; then
    echo "running test: $testType $testname..."
    python frequencyAnalyser.py ./texts/"$testname"
    diff ./texts/"$testname"_frequency_analysis.txt ./texts/"$testname"_frequency_analysis_eo.txt
    if [ $? -eq 0 ]; then
        echo "PASS"
    else
        echo "FAIL"
    fi
elif [ "$testType" == "anagram" ]; then
    echo "running test: $testType $testname..."
    python anagrammer.py ./texts/"$testname"
    diff ./texts/"$testname"_anagrams.txt ./texts/"$testname"_anagrams_eo.txt
    if [ $? -eq 0 ]; then
        echo "PASS"
    else
        echo "FAIL"
    fi
else
    echo "Invalid test type: $testType"
    echo "Valid test types are: ${TESTTYPES[@]}"
fi

exit 0