# Voynich Character Categorisation
## Contributing

## Formatter

The formatter is written in [Python](https://www.python.org/). It can be found at voynich/formatter/formatter.py.

The purpose of this formatter is to take transcripted text from the Voynich manuscript and convert it into a form that is ideal for categorising characters. To these ends, the formatter aims to remove as much uncertainty as possible.

 ### Inputs

The formatter takes a **single required argument**, the path to the plaintext file containing text from the **Takahashi** transcription of the Voynich manuscript.

The text file is assumed to have been generated from the [Interlinear transcription archive extractor](http://voynich.freie-literatur.de/index.php?show=extractor), with the following settings:

**Transcriber:**
- [x] Takeshi Takahashi
**Output Formatting:**
- [x] Remove locators
- [x] Remove comments
- [x] Remove inline comments
- [x] Remove parsable information
- [x] Remove suspicious spaces
- [ ] Convert weirdos to characters
**Transcription:** Basic EVA 

Other settings may be selected by the user without restriction.

    Justifications:
    - Takeshi Takahashi: His transcription has been shown by previous honours students to be the most complete.
    - Remove locators: Line locations are not relevant to the categorisation of characters.
    - Remove comments: Comments are not relevant to the categorisation of characters.
    - Remove inline comments: The only inline comments that are close to being relevant are those that indicate weirdo characters. As below, however, weirdo characters are not to be included in analysis.
    - Remove parsable information: This information is not actual manuscript text and hence not relevant to the categorisation of characters.
    - Remove suspicious spaces: The goal of the formatter is to remove as much uncertainty as possible, so any "suspicious" elements should be removed.
    - Convert weirdos to characters: Weirdo characters are rare and hence add to uncertainty of outcomes, they should not be included in the text as characters.

The formatter takes **a number of optional arguments**, which are described below.
- WIP

### Outputs
The formatter produces a plaintext file containing the formatted text. This will resemble the input file, but with the following changes:
- All "." characters are replaced with spaces.
- All "-" characters are replaced with newlines.
- All "=" characters are replaced with double newlines.
- All words separated by "," characters are removed.
- All words containing "*" are removed.
- All words containing "!" are removed.

    Justifications: 
    Referring to the following definition of the EVA:
    ![EVA Definition](http://www.voynich.nu/img/extra/eva01.gif)
    - ".", "-" and "=" represent spaces, new lines and new paragraphs respectively.
    - "," represents an uncertain space, best to remove affected words to reduce uncertainty.
    - "*" represents an unreadable character, best to remove affected words to reduce uncertainty.
    - "!" represents a spacing character used to align different transcriptions of the manuscript. There is an element of uncertainty inherent in any word on which different transcribers couldn't agree to a representation of, and hence should be removed.