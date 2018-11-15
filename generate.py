#! /usr/bin/env python3
''' Report generation script for SJSU Senior Project '''

import os
import sys
import argparse
from multiprocessing.dummy import Pool as ThreadPool

FILES = ["report.yaml",
         "chapters/chapter1/chapter1_introduction.md",
         "chapters/chapter2/chapter2_background.md",
         "chapters/chapter3/chapter3_requirements.md",
         "chapters/chapter4/chapter4_system_design.md",
         "chapters/chapter5/chapter5_implementation.md",
         "chapters/chapter6/chapter6_tools.md",
         "chapters/chapter7/chapter7_testing.md",
         "chapters/chapter8/chapter8_conclusion.md"]


def argument_parser():
    ''' Argument parser for documentation generation script '''
    parser = argparse.ArgumentParser()
    parser.add_argument("-o", "--output", default="report.pdf")
    parser.add_argument("-v", "--verbosity", action="store_true")
    parser.add_argument("-u", "--update_diagrams", action="store_true")
    args = parser.parse_args()
    return args


def update_diagrams():
    '''
    Function that runs `drawio-batch` on each of the draw.io diagrams.
    This makes sure that the most recent version of the diagram is included
    in the report.
    '''
    diagrams = get_list_of_diagrams()
    pool = ThreadPool(4)
    pool.map(generate_diagram, diagrams)
    pool.close()
    pool.join()


def generate_diagram(diagram):
    ''' Generate a png diagram from a draw.io xml file '''
    drawio_batch_args = ["--format", "png",
                         "--quality", "100",
                         "--scale", "4",
                         diagram, diagram.replace(".xml", ".png")]
    os.system("drawio-batch " + " ".join(drawio_batch_args))
    print("Updated " + diagram)


def get_list_of_diagrams():
    '''
    Get a list of all draw.io diagrams in the current file tree
    '''
    diagrams = []
    for root, dirs, files in os.walk("."):
        for file in files:
            if file.endswith(".xml"):
                if check_for_draw_io(os.path.join(root, file)):
                    diagrams.append(os.path.join(root, file).lstrip("./"))
    return diagrams


def check_for_draw_io(filepath):
    ''' Check if a file is a draw.io file '''
    with open(filepath, 'r') as file:
        line = file.readline()
    return 'draw.io' in line


def clean_pdf(to_remove):
    ''' Function to delete previous pdf. Helps with Jenkins artifacting '''
    try:
        os.remove(to_remove)
    except OSError:
        pass


def create_single_body_markdown(file_paths, output_file):
    '''
    Join all the files together in order, adding a `\\newpage` latex command
    between each of them for formatting
    '''
    with open(output_file, "w+") as outputfile:
        for file_path in file_paths:
            with open(file_path) as inputfile:
                for line in inputfile:
                    outputfile.write(line)
            outputfile.write("\n\\newpage\n")


def create_appendix_markdown(root_directory, output_file):
    ''' Create appendicies for modules and software architecture '''
    resources = []
    detail_files = []
    trim_amount = root_directory.split("/").__len__()
    with open(output_file, "w+") as outputfile:
        for root, dirs, files in os.walk(root_directory):
            for file in files:
                if file.endswith(".md"):
                    resource_path = os.path.join(root, file).split("/")
                    resource_path = "/".join(resource_path[trim_amount: \
                                             resource_path.__len__()-1])
                    resources.append(resource_path)
                    if root == root_directory:
                        with open(os.path.join(root, file)) as input_file:
                            for line in input_file:
                                outputfile.write(line)
                        outputfile.write("\n\n")
                    else:
                        detail_files.append(os.path.join(root, file))
        for file in sorted(detail_files, key=lambda s: s.lower()):
            with open(file) as input_file:
                for line in input_file:
                    outputfile.write(line)
            outputfile.write("\n\n")
        outputfile.write("\\newpage\n")
    return resources


def create_appendix_markdown_file():
    with open("appendix.md", "w+") as appendix_file:
        appendix_file.write("\\appendix\n")


def main():
    ''' Entry point into the report generation script '''
    args = argument_parser()
    if args.update_diagrams:
        update_diagrams()
    clean_pdf(args.output)
    template = "template.tex"
    markdown_files = []
    resource_paths = ["chapters/chapter1", "chapters/chapter2",
                      "chapters/chapter3", "chapters/chapter4",
                      "chapters/chapter5", "chapters/chapter6",
                      "chapters/chapter7", "chapters/chapter8"]
    body_markdown = "body.md"
    markdown_files.append(body_markdown)
    create_single_body_markdown(FILES, body_markdown)

    # Appendix Generation #
    create_appendix_markdown_file()
    markdown_files.append("appendix.md")

    fpga_modules_root = "documentation/fpga/modules"
    fpga_modules_appendix = "fpga_modules.md"
    markdown_files.append(fpga_modules_appendix)
    appendix_resources = create_appendix_markdown(fpga_modules_root,
                                                  fpga_modules_appendix)
    for resource in appendix_resources:
        resource_paths.append(fpga_modules_root + "/" + resource)

    fpga_diagrams_root = "documentation/fpga/diagrams"
    fpga_diagrams_appendix = "fpga_diagrams.md"
    markdown_files.append(fpga_diagrams_appendix)
    appendix_resources = create_appendix_markdown(fpga_diagrams_root,
                                                  fpga_diagrams_appendix)
    for resource in appendix_resources:
        resource_paths.append(fpga_diagrams_root + "/" + resource)

    additional_pandoc_args = ["--standalone", "--number-sections",
                              "--template", template,
                              "--resource-path=" + ":".join(resource_paths),
                              "--pdf-engine=xelatex",
                              "--output", args.output]

    print("pandoc " + " ".join(markdown_files + additional_pandoc_args))
    os.system("pandoc " + " ".join(markdown_files + additional_pandoc_args))
    if not os.path.isfile(args.output):
        sys.exit(1)
    
    for file in markdown_files:
        os.remove(file)


if __name__ == "__main__":
    main()
