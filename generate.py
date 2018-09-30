#! /usr/bin/env python3

import os
import argparse

files = ["report.yaml",
         "documents/chapter1_introduction.md",
         "documents/chapter2_background.md",
         "documents/chapter3_requirements.md",
         "documents/chapter4_system_design.md",
         "documents/chapter5_implementation.md",
         "documents/chapter6_tools.md",
         "documents/chapter7_testing.md",
         "documents/chapter8_conclusion.md"
         ]


def argument_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("-o", "output")
    parser.add_argument("-v", "verbosity", action="store_true")
    args = parser.parse_args()
    return args


def main():
    # args = argument_parser()
    os.system("pandoc " + " ".join(files) + " -s --template report.tex -N -o report.pdf")


if __name__ == "__main__":
    main()
