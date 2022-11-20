# Voynich Manuscript Analysis Code
## Contributing
Clone the repo and get going. No build steps or anything needed, just a python install.

## General Folder Structure
The voynich root folder contains the various scripts for analysis. It also containes two sub-folders: `/texts/` and `/figures/`. All text outputs are saved in `/texts/`, all figure outputs are saved to `/figures/`. It is reccomended that input txt files are also stored in `/texts/`.

## Formatter
The purpose of this formatter is to take transliterated text of the Voynich Manuscript and convert it into a form that is needed for particular analyses.

### Inputs

The formatter takes a **single required argument** and **many optional arguments**.

#### Required Argument
The path to the plaintext file containing the transliterated Voynich Manuscript, written in EVA (Extensible Voynich Alphabet and formatted in [IVTFF](http://www.voynich.nu/transcr.html).

#### Optional Arguments
A number of optional arguments can be passed through the command line to toggle certain text features from being formatted.
- `--keepcomments` :     Comments made by the transcriber in the text file are retained.
- `--locusraw`:          Locus indicators are retained in raw form. i.e. `<f...>`. Further details about locus indicators can be found below.
- `--locusproc`:         Locus indicators are retained but processed into meaningful English. i.e. `<f17r>` would become "Beginning of folio 17, right side" in the output text.
- `--nospace` :          `.` characters are not converted into whitespace in the output text.
- `--nouncertainspace`:  `,` characters are not converted into whitespace in the output text.
- `--keepuncertain`  :   Uncertain characters are retained in their "list" form. I.e. `[x:y:z]`.
- `--pararaw` :          Paragraph identifiers (`%` at the start and `$` at the end) are kept in raw form.
- `--paraproc` :         Paragraph identifiers are processed into meaningful English. "New Paragraph" or "End Paragraph" respectively.
- `--noillegible` :      No illegible words. Not only are `?` and `???` character sequences removed, if they occur within a word (delimited by `.` characters), the entire word is removed aswell.
- `--keepillegible` :    Illegible characters and their containing words are retained in the output text.


### Outputs
The output of the formatter is a single text file of formatted ASCII. The file will be located in `/texts/` and will be named the same as the input file with `_formatted.txt` appended.

If passed no command line arguments, the formatter will produce an output file in the following default format.
- Comments removed.
- Locus indicators removed.
- `.` characters converted to whitespace.
- Uncertain spaces (`,` characters) converted to whitespace.
- Uncertain character readings, found in the transcription in form `[x:y:z]` replaced with the first character in the option sequence. This character is the one that the transliteration producer deemed most likely.
- ASCII codes are retained for rare characters. 3.g. `@185`.
- `-` characters are removed
- Paragraph identifiers are removed and replaced with double newlines to format text into actual paragraphs.
- Illegible character identifiers `?` and `???` are removed.

### Locus Indicators
Locus indicators provide a lot of meta information about the manuscript's text. There are three forms of locus indicators.
- `<f17r>`: Indicates the beginning of a new page, in this case, folio 17, right side. Following will be meta comments about the contents of page.
- `<f17r.N@Ab>`: `N` is the current count of this locus as an identified unique section of text on the current page. `@Ab` is a code which gives some more insight into the grouping of text section types that this locus is a part of (See below).
- `<f17r.N@Ab;T>`: `T` identifies the transcriber of this particular locus.

#### Locus Types
![Locus Types](https://user-images.githubusercontent.com/70213167/182542486-13eaa4ba-607c-4a0c-ae92-29568dfa44d7.png)

## Frequency Analyser
The frequency anaysler takes a text, producing a frequency analysis and providing other key details such as the longest word in the text, the word count, etc.

### Inputs
The frequency analyser takes a single required argument: the path to the text file to be analysed. The `--voynich` option can be passed as an optional argument, and is required when a frequency analysis of the Voynich Manuscript is to be performed. This will ensure that ligatures and special characters are treated as single characters rather than the string of ASCII characters they appear as in the transliteration.

### Outputs
The frequency analyser produces a text output, aswell as a figure.

#### Text Output
The text output will be saved to `/texts/` and will be named the same as the input file with `_frequency_analysis.txt` appended. Within this file can be found a summary of the interesting characteristics of the text:
- Number of words
- Number of unique characters
- Longest word and its length
- Average word length

In addition, the text output contains the frequency counts for each unique character appearing in the text.

#### Figure Output
The figure output will be saved to `/figures/` and will be named the same as the input file with `_freq_analysis.png` appended. This figure is a bar chart of the frequency of each unique character in the text.

In the case of texts with a large number of unique characters, or the Voynich Manscript where ligatures are long strings of ASCII characters, it may occur that the figure does not fit all unique characters on the x-axis. It is likely possible to tweak the figure size to fix this issue, but it has not been confirmed.
## Anagram Analyser


## HMM Analyser

## Corpus
This codebase contains a corpus of texts in a number of different languages covering various topics. These texts are stored in plaintext files and are used in conjunction with the various analysis scripts to help draw patterns with the VM. Below is a list of the texts included and their important features.
- UN Declaration of Human Rights [Chosen for its availability in many languages; Human Rights]
  - English
  - Spanish
  - French
  - German
  - Italian
- Species Plantarum Sections I-III [Latin; Botanical]
- Nova Analysis Aquarum Medeviensium [Latin; Chemistry]
- Ephemerides Barometricae Mutinenses (anni M.DC.XCIV) [Latin; Weather Patterns]
- De Canibus Britannicis[Latin; Animals/Agriculture]
- Of English Dogges [English; Animals/Agriculture; Translated from Canibus Britannicis] 
- The Medicinal Plants of the Philippines [English; Botanical]
- The Works of Edgar Allen Poe (Volume II) [English; Narrative Fiction]
- A Preliminary Dissertation on the Mechanisms of the Heavens [English; Astronomy]
- The New England Cook book or Young Housekeeper's Guide [English; Recipes]
- Henley's Twentieth Century Formulas, Recipes and Processes [English; Chemistry]
- Die Epiphytische Vegetation Amerikas [German; Botanical]
- Sonne und Sterne [German; Astronomy]
- Neuestes Suddeutsches Kochbuch fur alle Stande [German; Recipes]
- Le Systeme Solaire se Mouvant [French; Astronomy]
- La Navigation Aerienne L'aviation Et La Direction Des Aerostats Dans Les Temps [French; Aeronautics, History]
