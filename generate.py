#! /usr/bin/env python3
''' Report generation script for SJSU Senior Project '''

import os
import sys
import argparse

files = ["report.yaml",
         "documents/chapter1_introduction.md",
         "documents/chapter2_background.md",
         "documents/chapter3_requirements.md",
         "documents/chapter4_system_design.md",
         "documents/chapter5_implementation.md",
         "documents/chapter6_tools.md",
         "documents/chapter7_testing.md",
         # "documents/chapter8_conclusion.md"
         ]


def argument_parser():
    ''' Argument parser for documentation generation script '''
    parser = argparse.ArgumentParser()
    parser.add_argument("-o", "--output", default="report.pdf")
    parser.add_argument("-v", "--verbosity", action="store_true")
    args = parser.parse_args()
    return args


def clean_pdf(to_remove):
    ''' Function to delete previous pdf. Helps with Jenkins artifacting '''
    try:
        os.remove(to_remove)
    except OSError:
        pass


def main():
    ''' Entry point into the report generation script '''
    args = argument_parser()
    clean_pdf(args.output)
    template = "template.tex"
    additional_pandoc_args = ["-s", "--template", template,
                              "--pdf-engine=xelatex", "-N", "-o",
                              args.output]
    # print("pandoc " + " ".join(files + additional_pandoc_args))
    os.system("pandoc " + " ".join(files + additional_pandoc_args))
    if not os.path.isfile(args.output):
        sys.exit(1)


if __name__ == "__main__":
    main()
