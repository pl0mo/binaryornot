# -*- coding: utf-8 -*-

"""
binaryornot.check
-----------------

Main code for checking if a file is binary or text.
"""
import argparse
import logging
from pathlib import Path

from binaryornot.helpers import get_starting_chunk, is_binary_string

logger = logging.getLogger(__name__)


def is_binary(file_path: Path):
    """
    :param file_path: File to check.
    :returns: True if it's a binary file, otherwise False.
    """
    if file_path.is_file():
        debug_msg = f'is_binary: {file_path}'
        logger.debug(debug_msg)

        # Check if the file extension is in a list of known binary types
        #     binary_extensions = ['.pyc', ]
        #     for ext in binary_extensions:
        #         if filename.endswith(ext):
        #             return True

        # Check if the starting chunk is a binary string
        chunk = get_starting_chunk(file_path)
        return is_binary_string(chunk)

    return False


def main():
    """Starting point."""
    desc = 'Check if a supplied file path is binary or not.'
    parser = argparse.ArgumentParser(description=desc)
    parser.add_argument('path', nargs='+', help='File path to check for.')

    args = parser.parse_args()

    for fp_path in map(Path, args.path):
        print(is_binary(fp_path))


if __name__ == "__main__":
    main()
