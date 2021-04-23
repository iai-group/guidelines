"""An example Python script showing IAI Style Guide format and argparse usage.

This Python script implements a dummy function that takes input and output file
paths. The main purpose of this script is to show how a Python file should look
in order to be presentable and conform to the IAI Python Style Guide. As a
bonus, the usage of the argparse library is demonstrated for use with command-
line interface (CLI).

    Typical usage example in shell CLI:

    python example_script.py -i input.txt -o output.txt -m buzzfizz.json

    Or simply:

    python example_script.py -i input.txt -o output.txt

"""

import argparse
import json
import typing


def dummy_line_modification(line: str, i: int, mods: typing.Dict[str, dict]) -> str:
    """Defines the modification to be perfomed for a single input line.

    Args:
        line: The line from the input file to be modified.
        i: The line number where the line argument was read.
        mods: Substitution mapping to modify line based on line number.

    Returns:
        Modified form of the input line.
    """
    output_line = line.rstrip("\n") + " \t | "
    if not mods == dict():
        if i % 3 == 0 and i % 5 == 0:
            output_line += str(mods["fizz"][str(i % 5)]) + str(mods["buzz"][str(i % 3)])
        elif i % 3 == 0:
            output_line += str(mods["fizz"][str(i % 5)])
        elif i % 5 == 0:
            output_line += str(mods["buzz"][str(i % 3)])
    else:
        output_line += "Added standard modification " + str(i) + "."
    return output_line + "\n"


def dummy_function(input_path: str, output_path: str, mod_path: str = None):
    """Takes input from a file, modifies each line, and writes output
    accordingly, line by line.

    Args:
        input_path: A file path to an existing file.
        output_path: A file path to a non-existent file.
        mod_path: A file path to a JSON file with a dictionary to modify lines.
    """
    if mod_path is not None:
        assert isinstance(mod_path, str)
        assert mod_path[-5:] == ".json"
        with open(mod_path) as json_file:
            mods = json.load(json_file)
    else:
        mods = dict()

    with open(input_path, "r", encoding="utf8") as f_in, open(
        output_path, "w", encoding="utf8"
    ) as f_out:
        for i, line in enumerate(f_in):
            f_out.write(dummy_line_modification(line, i, mods))


if __name__ == "__main__":
    # Parse required (or expected) arguments passed from command-line call.
    parser = argparse.ArgumentParser()
    named = parser.add_argument_group("Named arguments")
    named.add_argument(
        "-i",
        "--input_path",
        dest="input_path",
        help="short explanation, input",
        default="input.txt",
        required=True,
    )
    named.add_argument(
        "-o",
        "--output_path",
        dest="output_path",
        help="short explanation, output",
        default="output.txt",
        required=True,
    )
    named.add_argument(
        "-m",
        "--modification_path",
        dest="mod_path",
        help="short explanation, modifiying file",
        default=None,
        required=False,
    )
    args = parser.parse_args()

    # Execute script given parsed arguments.
    dummy_function(args.input_path, args.output_path, args.mod_path)
