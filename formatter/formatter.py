import sys
import argparse

def main():
    # Get input from command line
    input = get_input()
    
    # Open file
    file_path = "./texts/" + input["file_name"] + ".txt"
    with open(file_path, "r") as file:
        input_lines = file.readlines()

    # Format lines
    output_lines = format(input_lines, input)

    # Write output
    output_path = "./texts/" + input["file_name"] + "_formatted.txt"
    with open(output_path, "w") as file:
        for line in output_lines:
            file.write(line)

# Takes input lines and input options, formats the lines accordingly and returns them.
def format(input_lines, input):
    intermediate_lines = []
    output_lines = []

    intermediate_lines = format_start_of_line(input_lines, input)
    output_lines = format_in_text(intermediate_lines, input)

    return output_lines

# Performs all formatting tasks not occuring on start of line elements.
def format_in_text(intermediate_lines, input):
    return intermediate_lines

# Performs all formatting tasks occuring on start of line elements.
def format_start_of_line(input_lines, input):
    intermediate_lines = []

    for line in input_lines:
        # Comments
        if(line[0] == "#"):
            if(input["keepcomments"]):
                intermediate_lines.append(line)
            else:
                continue
        # Locus data
        elif(line[0] == "<" and line[1] == "f"):
            if(input["locusraw"]):
                intermediate_lines.append(line)
            elif(input["locusproc"]):
                locus = ""
                i = 1
                while(line[i] != ">"):
                    locus += line[i]
                    i += 1
                locus = process_locus(locus)
                rest_of_line = line[i+1:]
                formatted_line = locus + rest_of_line
                intermediate_lines.append(formatted_line)
            else:
                i = 0
                while(line[i] != ">"):
                    i += 1
                rest_of_line = line[i+1:].strip(' ')
                intermediate_lines.append(rest_of_line)
        # Paragraph data
        elif(line[0] == "<" and line[1] == "%"):
            if(input["pararaw"]):
                intermediate_lines.append(line)
            elif(input["paraproc"]):
                paragraph_start = "<New Paragraph>"
                rest_of_line = line[3:]
                formatted_line = paragraph_start + rest_of_line
                intermediate_lines.append(formatted_line)
            else:
                i = 0
                while(line[i] != ">"):
                    i += 1
                rest_of_line = line[i+1:].strip(' ')
                intermediate_lines.append(rest_of_line)
        else:
            intermediate_lines.append(line)
        
    return intermediate_lines

# Processes locus indicators into readable form.
def process_locus(locus):
    print(locus)
    return ""

def get_input():
    parser = argparse.ArgumentParser(description="Voynich Manuscript Formatter", formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("file_name", help="The name of the file to be formatted. The file must be a .txt file stored in ./texts/, containing a transcription of the Voynich Manuscript written in EVA and formatted in IVTFF.")
    parser.add_argument("--keepcomments", action="store_true", help="Keep comments.")
    locus_group = parser.add_mutually_exclusive_group()
    locus_group.add_argument("--locusraw", action="store_true", help="Keep raw locus data.")
    locus_group.add_argument("--locusproc", action="store_true", help="Keep processed locus data.")
    parser.add_argument("--nospace", action="store_true", help="Keep '.' characters.")
    parser.add_argument("--nouncertainspace", action="store_true", help="Remove ',' characters.")
    parser.add_argument("--keepuncertain", action="store_true", help="Keep uncertain characters in their list format '[x:y:z]'.")
    parser.add_argument("--nocapitallig", action="store_true", help="Do not convert ligatures in brace form to capital form.")
    parser.add_argument("--nodrawingspaces", action="store_true", help="Remove '-' characters instead of converting to whitespace.")
    paragraph_group = parser.add_mutually_exclusive_group()
    paragraph_group.add_argument("--pararaw", action="store_true", help="Keep paragraph beggining (%) and end ($) characters in raw form.")
    paragraph_group.add_argument("--paraproc", action="store_true", help="Process paragraph beggining (%) and end ($) into readable form.")
    parser.add_argument("--noillegible", action="store_true", help="Words containing illegible characters (? | ???) are removed.")
    args = parser.parse_args()
    input = vars(args)
    return input

if __name__ == "__main__":
    main()