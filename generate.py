#! /usr/bin/env python3
''' Report generation script for SJSU Senior Project '''

import os
import sys
import argparse

FILES = ["report.yaml",
         "chapters/chapter1/chapter1_introduction.md",
         "chapters/chapter2/chapter2_background.md",
         "chapters/chapter3/chapter3_requirements.md",
         "chapters/chapter4/chapter4_system_design.md",
         "chapters/chapter5/chapter5_implementation.md",
         "chapters/chapter6/chapter6_tools.md",
         "chapters/chapter7/chapter7_testing.md",
         # "chapters/chapter8/chapter8_conclusion.md"
         ]


def argument_parser():
    ''' Argument parser for documentation generation script '''
    parser = argparse.ArgumentParser()
    parser.add_argument("-o", "--output", default="report.pdf")
    parser.add_argument("-v", "--verbosity", action="store_true")
    args = parser.parse_args()
    return args


def check_tools():
    '''
    Checks to see if all necessary tools are installed
    Also checks to see if additional functionality can be used.
    '''
    return 0


def update_diagrams():
    '''
    Function that runs `drawio-batch` on each of the draw.io diagrams.
    This makes sure that the most recent version of the diagram is included
    in the report.
    '''
    return 0


def get_list_of_diagrams():
    '''
    Get a list of all draw.io diagrams in the current file tree
    '''
    return 0


def clean_pdf(to_remove):
    ''' Function to delete previous pdf. Helps with Jenkins artifacting '''
    try:
        os.remove(to_remove)
    except OSError:
        pass


def create_single_markdown(file_paths):
    '''
    Join all the files together in order, adding a `\\newpage` latex command
    between each of them for formatting
    '''
    return file_paths


def main():
    ''' Entry point into the report generation script '''
    args = argument_parser()
    clean_pdf(args.output)
    template = "template.tex"
    additional_pandoc_args = ["--standalone", "--number-sections",
                              "--template", template,
                              "--pdf-engine=xelatex",
                              "--output", args.output]
    # print("pandoc " + " ".join(files + additional_pandoc_args))
    os.system("pandoc " + " ".join(FILES + additional_pandoc_args))
    if not os.path.isfile(args.output):
        sys.exit(1)


if __name__ == "__main__":
    main()
