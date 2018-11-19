'''
Spell Check script using aspell and python unit tests
'''
import os
import argparse
import subprocess
from junit_xml import TestSuite, TestCase

def argument_parser():
    ''' Argument parser for documentation generation script '''
    parser = argparse.ArgumentParser()
    parser.add_argument("-o", "--output", default="results.xml")
    parser.add_argument("-v", "--verbosity", action="store_true")
    parser.add_argument("-d", "--dictionary", default="dictionary.txt",
                        help="Dictionary of corrections used by aspell")
    parser.add_argument("-e", "--extra-dictionary",
                        default="extra_dictionary.txt",
                        help="Spelling mistakes that can't be overwritten \
                             using aspell dictionary")
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
    ''' Run the file through aspell and capture the spelling mistakes'''
    print_file = "cat ./" + file
    check_file = "aspell -a --extra-dicts ./" + dictionary

    pipe_1 = subprocess.Popen(print_file, stdout=subprocess.PIPE,
                              shell=True)
    pipe_2 = subprocess.Popen(check_file, stdin=pipe_1.stdout,
                              stdout=subprocess.PIPE, shell=True)
    pipe_1.stdout.close()
    output = pipe_2.communicate()[0]
    return_list = []
    for line in output.decode("utf-8").split("\n"):
        if line.startswith("&"):
            return_list.append(line.split()[1:])
    if return_list.__len__():
        return return_list
    return None


def parse_spelling_mistakes(spelling_mistakes, extra_dictionary):
    '''
    Parse the output of the spelling aspell mistakes for common issuses with
    aspell. aspell doesn't support apostrophes or numbers in the word. That
    is why we need two dictionaries.
    '''
    words = []
    with open(extra_dictionary) as file:
        words = [line.strip() for line in file]
    mistakes_to_return = []
    for mistake in spelling_mistakes:
        if mistake[0] not in words:
            mistakes_to_return.append(mistake)
        else:
            print(mistake)
    return mistakes_to_return


def generate_test_case(spelling_mistakes, file):
    ''' Create a test case for all of the mistakes in a file '''
    test_case = TestCase(name=file)
    if spelling_mistakes is not None:
        error_message = "Mispelled words:\n"
        words = []
        for mistake in spelling_mistakes:
            if mistake[0] not in words:
                words.append(mistake[0])
        error_message = error_message + ", ".join(words)
        test_case.add_error_info(message=error_message)
    return test_case


def generate_test_output(test_cases, test_output):
    ''' Compile all of the test cases and output a junit test report '''
    test_suite = TestSuite("Spell Check", test_cases)
    with open(test_output, 'w') as file:
        TestSuite.to_file(file, [test_suite], prettyprint=False)


def main():
    ''' Main function of spell_check.py'''
    args = argument_parser()
    files = get_list_of_markdown_files()
    test_cases = []
    for file in files:
        spelling_mistakes = check_spelling_in_file(file, args.dictionary)
        if spelling_mistakes is not None:
            spelling_mistakes = parse_spelling_mistakes(spelling_mistakes,
                                                        args.extra_dictionary)
        test_cases.append(generate_test_case(spelling_mistakes, file))
    generate_test_output(test_cases, args.output)

if __name__ == "__main__":
    main()
