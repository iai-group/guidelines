"""An example Python script showing IAI Style Guide format and argparse usage.

This Python script implements a dummy function that takes input and output file
paths. The main purpose of this script is to show how a Python file should look
in order to be presentable and conform to the IAI Python Style Guide. As a
bonus, the usage of the argparse library is demonstrated for use with command-
line interface (CLI).

    Typical usage example in shell CLI:

    python example_script.py -i input.txt -o output.txt -m buzzfizz.json \
                             -x happy

    Or simply:

    python example_script.py -i input.txt -o output.txt -x happy

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


def dummy_function(input_path: str, output_path: str, mod_path: str = None) -> None:
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


class DummyThing:
    def __init__(self, mood: str, weight: float, color: str = "green") -> None:
        """The class docstring goes under the __init__ method.
        
        Args:
            mode: What mode the class should instantiate: happy or sad.
            weight (float): How heavy this thing is in Earth gravity. 
            color (str): The optical color label of the imaginary object.            
        """
        self._mood = mood
        self._color = color
        self._weight = weight

    def weight(self) -> float:
        """Methods can be defined that reveal private variables.

        Returns:
            float: The value of the weight of the object. 
        """
        return self._weight

    def act(self, command: str) -> str:
        """The object returns a string based on the command and mode.

        Args:
            command: Tell the object whether to sing or dance.

        Returns:
            A description of the resulting behavior.
        """
        if command == "sing":
            if self._mood == "happy":
                return "This DummyThing sings 'What a Wonderful World'"
            if self._mood == "sad":
                return "This DummyThing sings 'Everybody Hurts'"
        if command == "dance":
            if self._mood == "happy":
                return "This DummyThing bobs and weaves to the beat"
            if self._mood == "sad":
                return "Oh no, this DummyThing fell down."


if __name__ == "__main__":
    # Parse required (or expected) arguments passed from command-line call.
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-i",
        "--input_path",
        dest="input_path",
        help="short explanation, input",
        default="input.txt",
        required=True,
    )
    parser.add_argument(
        "-o",
        "--output_path",
        dest="output_path",
        help="short explanation, output",
        default="output.txt",
        required=True,
    )
    parser.add_argument(
        "-m",
        "--modification_path",
        dest="mod_path",
        help="short explanation, modifiying file",
        default=None,
        required=False,
    )
    parser.add_argument(
        "-x",
        "--mood",
        dest="mood",
        help="The mode argument for the DummyClass object",
        default=None,
        required=True,
    )
    args = parser.parse_args()

    # Execute script given parsed arguments.
    dummy_function(args.input_path, args.output_path, args.mod_path)
    my_dummything = DummyThing(args.mood, 456.9)
    print(my_dummything.act("sing"))
    print(my_dummything.act("dance"))
