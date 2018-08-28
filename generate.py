#! /usr/bin/env python3

import os
import argparse


def argument_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("-o", "output")
    parser.add_argument("-v", "verbosity", action="store_true")
    args = parser.parse_args()
    return args


def main():
    # args = argument_parser()
    os.system("pandoc README.md -o report.pdf")


if __name__ == "__main__":
    main()