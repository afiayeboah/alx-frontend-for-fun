#!/usr/bin/python3
"""
markdown2html.py

A script that converts Markdown files to HTML.

Usage:
    ./markdown2html.py <input_file> <output_file>

Arguments:
    <input_file>  The Markdown file to be converted.
    <output_file> The file where the HTML output will be saved.
"""

import sys
import os
import re


def convert_markdown_to_html(input_file, output_file):
    """
    Converts a Markdown file to HTML and writes the output to a file.

    Args:
        input_file (str): The path to the input Markdown file.
        output_file (str): The path to the output HTML file.

    Raises:
        FileNotFoundError: If the input file does not exist or is not a file.
    """
    if not (os.path.exists(input_file) and os.path.isfile(input_file)):
        raise FileNotFoundError(f"Missing {input_file}")

    html_lines = []
    with open(input_file, encoding="utf-8") as f:
        for line in f:
            match = re.match(r"^(#+) (.*)$", line)
            if match:
                heading_level = len(match.group(1))
                heading_text = match.group(2)
                html_lines.append(f"<h{heading_level}>{heading_text}
                                  </h{heading_level}>")
            else:
                html_lines.append(line.rstrip())

    with open(output_file, "w", encoding="utf-8") as f:
        f.write("\n".join(html_lines))


def main():
    """
    Main function to handle the command-line arguments
    """
    if len(sys.argv) != 3:
        print("Usage: ./markdown2html.py <input_file> <output_file>",
             file=sys.stderr)
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    try:
        convert_markdown_to_html(input_file, output_file)
    except FileNotFoundError as e:
        print(e, file=sys.stderr)
        sys.exit(1)

    sys.exit(0)


if __name__ == "__main__":
    main()
