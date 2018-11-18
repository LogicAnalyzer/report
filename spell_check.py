'''
Spell Check script using aspell and python unit tests
'''
import os
import sys
import argparse
import unittest
import subprocess

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


def check_spelling_in_file(file, dictionary):
    print_file = "cat ./" + file
    check_file = "aspell -a --extra-dicts ./" + dictionary + " | grep -v '\*'"

    p1 = subprocess.Popen(print_file, stdout=subprocess.PIPE, shell=True)
    p2 = subprocess.Popen(check_file, stdin=p1.stdout, stdout=subprocess.PIPE, shell=True)
    p1.stdout.close()  # Allow p1 to receive a SIGPIPE if p2 exits.
    output = p2.communicate()[0]
    return_list = []
    for line in output.decode("utf-8").split("\n"):
        if line.startswith("&"):
            return_list.append(line.split()[1:4])
    if return_list.__len__():
        return return_list


def main():
    ''' Main function of spell_check.py'''
    args = argument_parser()
    files = get_list_of_markdown_files()
    all_mistakes = {}
    for file in files:
        spelling_mistakes = check_spelling_in_file(file, args.dictionary)
        if spelling_mistakes is not None:
            all_mistakes[file] = spelling_mistakes
    print(all_mistakes)

if __name__ == "__main__":
    main()
    #import xmlrunner
    #unittest.main(testRunner=xmlrunner.XMLTestRunner(output='test-reports'))
