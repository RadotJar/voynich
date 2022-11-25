# Note: Some aspects of this script are extremely inefficienct simply due to time constraints


Script is written to run on one script at a time (an inefficiency), which calculates the entropy of the individual characters in a text and then the
entropy of each string (normalised and non-normalised). Then, finding the average entropy for numbers and words in that text. Only unique characters
are considered for the average calculation.

set "VM" variable to 'True' the script will use the specified entropy thresholds (threshold refers to raw vaue and thresold_norm refers to noamalised)
to extract strings that are lower than this threshold.

Ensure "VM" is 'false' when analysing a text

Outputs are sent to the 'entropy' folder