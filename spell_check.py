import os
import sys
import argparse


def argument_parser():
    ''' Argument parser for documentation generation script '''
    parser = argparse.ArgumentParser()
    parser.add_argument("-o", "--output", default="results.xml")
    parser.add_argument("-v", "--verbosity", action="store_true")
    parser.add_argument("-d", "--dictionary", help="Dictionary of corrections")
    args = parser.parse_args()
    return args


def get_list_of_markdown_files():
    ''' Get a list of all markdown files used in the report '''
    diagrams = []
    for root, dirs, files in os.walk("."):
        for file in files:
            if file.endswith(".md"):
                diagrams.append(os.path.join(root, file).lstrip("./"))
    return diagrams

def main():
    ''' Main function of spell_check.py'''
    args = argument_parser()
    files = get_list_of_markdown_files()
    for file in files:
        print("\n\n" + file + ":")
        os.system("cat " + file + " | aspell -a --extra-dicts ./" +
            args.dictionary + " | grep '&'")
    return 0

if __name__ == "__main__":
    main()
