import sys
import argparse

def main():
    # Get input from command line
    input = get_input()
    
    # Open file
    file_path = "./texts/" + input["file_name"] + ".txt"
    with open(file_path, "r") as file:
        input_lines = file.readlines()
    output_lines = []

    # Formatting
    for line in input_lines:
        # Start of line formatting
            print(line[0])
            # Comments
            if(line[0] == "#"):
                if(input["keepcomments"]):
                    output_lines.append(line)
                else:
                    continue
            # Locus data
            elif(line[0] == "<" and line[1] == "f"):
                if(input["locusraw"]):
                    output_lines.append(line)
                elif(input["locusproc"]):
                    locus = ""
                    i = 1
                    while(line[i] != ">"):
                        locus += line[i]
                        i += 1
                    output_lines.append(process_locus(locus))
                else:
                    continue
            # Paragraph data

def process_locus(locus):
    print(locus)
    return locus

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