"""An example Python script showing IAI Style Guide format and argparse usage.

This Python script implements a dummy function that takes input and output file
paths. The main purpose of this script is to show how a Python file should look
in order to be presentable and conform to the IAI Python Style Guide. As a
bonus, the usage of the argparse library is demonstrated for use with command-
line interface (CLI).

    Typical usage example in shell CLI:

    python example_script.py -in ../foo/input.txt -out ../bar/output.txt

:Author: Trond Linjordet
"""

import argparse

def dummy_line_modification(line, i):
    """Defines the modification to be perfomed for a single input line.

    Args:
        line: A string.
        i: An integer.
    Returns:
        Modified form of the input line.
    """
    return line.rstrip('\n')+'Added dummy modification '+str(i)+'.\n'


def dummy_function(input_path, output_path):
    """Takes input from a file, modifies each line, and writes output
    accordingly, line by line.

    Args:
        input_path: A file path to an existing file.
        output_path: A file path to a non-existent file.
    """
    with open(input_path, 'r', encoding='utf8') as f_in, \
            open(output_path, 'w', encoding='utf8') as f_out:
        for i, line in enumerate(f_in):
            f_out.write(dummy_line_modification(line, i))

if __name__ == '__main__':
    # Parse required (or expected) arguments passed from command-line call.
    parser = argparse.ArgumentParser()
    requiredNamed = parser.add_argument_group('Required named arguments')
    requiredNamed.add_argument('-in', '--input_path', dest='input_path',
                               help='short explanation, input',
                               default='../foo/input.txt',
                               required=True)
    requiredNamed.add_argument('-out', '--output_path', dest='output_path',
                               help='short explanation, output',
                               required=True)
    args = parser.parse_args()
    input_path = args.input_path
    output_path = args.output_path

    # Execute script given parsed arguments.
    dummy_function(input_path, output_path)
