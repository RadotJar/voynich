# Voynich Manuscript Analysis Code
## Contributing
Clone the repo and get going. No build steps or anything needed, just a python install.

## General Folder Structure
The voynich root folder is divided into sub-folders, each containing code, plaintext files etc that fulfill a specific purpose in the VM's analysis. Each sub-folder contains a relevant analysis script, aswell as a `/texts/` and `/figures/` sub-folder. All scripts take input text files from `/texts/`, output text files to `/texts/` and output figures to `/figures/`. Any new scripts should satisfy these conventions.

## Formatter

The formatter is written in [Python](https://www.python.org/). It can be found at voynich/formatter/formatter.py.

The purpose of this formatter is to take transliterated ASCII text of the Voynich Manuscript and convert it into a form that is needed for particular analyses.

### Inputs

The formatter takes a **single required argument** and **many optional arguments**.

#### Required Argument
The name of the plaintext file containing text from the Voynich Manuscript, written in EVA (Extensible Voynich Alphabet and formatted in [IVTFF](http://www.voynich.nu/transcr.html).

#### Optional Arguments
A number of optional arguments can be passed through the command line to toggle certain text features from being formatted.
- `--keepcomments` :     Comments made by the transcriber in the text file are retained.
- `--locusraw`:          Locus indicators are retained in raw form. i.e. `<f...>`. Further details about locus indicators can be found below.
- `--locusproc`:         Locus indicators are retained but processed into meaningful English. i.e. `<f17r>` would become "Beginning of folio 17, right side" in the output text.
- `--nospace` :          `.` characters are not converted into whitespace in the output text.
- `--nouncertainspace`:  `,` characters are not converted into whitespace in the output text.
- `--keepuncertain`  :   Uncertain characters are retained in their "list" form. I.e. `[x:y:z]`.
- `--nocapitallig`:      Ligatures are not converted from brace form to capitalised form. I.e. `{ao}` remains `{ao}`.
- `--nodrawingspaces`:   No drawing spaces. `-` characters are removed instead of being converted to whitespace.
- `--pararaw` :          Paragraph identifiers (`%` at the start and `$` at the end) are kept in raw form.
- `--paraproc` :         Paragraph identifiers are processed into meaningful English. "New Paragraph" or "End Paragraph" respectively.
- `--noillegible` :      No illegible words. Not only are `?` and `???` character sequences removed, if they occur within a word (delimited by `.` characters), the entire word is removed aswell.


### Outputs
The output of the formatter is a single text file of formatted ASCII. The file will be located in `/texts/` and will be named the same as the input file with any command line arguments passed to it appended after a `_`. I.e. if the formatter was passed `voynich -c -lr`, the output file would be named `voynich_c_lr`.

If passed no command line arguments, the formatter will produce an output file in the following default format.
- Comments removed.
- Locus indicators removed.
- `.` characters converted to whitespace.
- Uncertain spaces (`,` characters) are converted to whitespace.
- Uncertain character readings, found in the transcription in form `[x:y:z]` are replaced with the first character in the option sequence. This character is the one that the transcriber deemed most likely.
- Ligatures are converted to their capitalised form. For example `{ao}` becomes `Ao`, where the capitalisation of A indicates it connects to the character to its right (o). Note that there are a number of **special cases**.
 - c and q already connect to the right, so they are never capitalised.
 - h connects to the left, H connects to the right and left.
 - E connects its bottom.
- ASCII codes are retained for rare characters. I.e. `@185` represents a rare character in the manuscript and will remain as such.
- `-` characters are converted to whitespace.
- Paragraph identifiers are removed and replaced with double newlines to format text into actual paragraphs.
- Locus continuation characters `/` are removed.
- Illegible character identifiers `?` and `???` are removed.

### Locus Indicators
Locus indicators provide a lot of meta information about the manuscript's text. There are three forms of locus indicators.
- `<f17r>`: Indicates the beginning of a new page, in this case, folio 17, right side. Following will be meta comments about the contents of page.
- `<f17r.N@Ab>`: `N` is the current count of this locus as an identified unique section of text on the current page. `@Ab` is a code which gives some more insight into the grouping of text section types that this locus is a part of (See below).
- `<f17r.N@Ab;T>`: `T` idenfities the transcriber of this particular locus.

#### Locus Types
![Locus Types](https://user-images.githubusercontent.com/70213167/182542486-13eaa4ba-607c-4a0c-ae92-29568dfa44d7.png)

### Current Questions
The formatter is not perfect, and some further testing is required to refine it. Namely:
- The uncertain space character `,` needs to be analysed for whether it is more likely to be a correct or incorrect space and handled as such by default.
- The "drawing intruding onto text" character `-` needs to be analysed in a similar manner to determine whether it should be handled as whitespace or not by default.

## Anagrammer

## Frequency Analyser

## HMM Analyser
