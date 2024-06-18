#!/usr/bin/python3
"""
A script that converts Markdown to HTML.
"""

import sys
import os
import re


def convert_markdown_to_html(input_file, output_file):
    """
    Converts a Markdown file to HTML and writes the result to the specified output file.
    """
    # Verify that the input Markdown file exists and is a regular file
    if not (os.path.exists(input_file) and os.path.isfile(input_file)):
        print(f"Error: {input_file} not found", file=sys.stderr)
        sys.exit(1)

    # Read the Markdown file and perform the conversion to HTML
    with open(input_file, encoding="utf-8") as f:
        html_lines = []
        for line in f:
            # Detect Markdown headings and convert them to HTML headings
            match = re.match(r"^(#+) (.*)$", line)
            if match:
                heading_level = len(match.group(1))
                heading_text = match.group(2)
                html_lines.append(f"<h{heading_level}>{heading_text}</h{heading_level}>")
            else:
                html_lines.append(line.rstrip())

    # Write the generated HTML content to the output file
    with open(output_file, "w", encoding="utf-8") as f:
        f.write("\n".join(html_lines))


if __name__ == "__main__":
    # Ensure the script is provided with the correct number of command-line arguments
    if len(sys.argv) != 3:
        print("Usage: ./markdown2html.py <input_file> <output_file>", file=sys.stderr)
        sys.exit(1)

    # Extract the input and output file paths from the command-line arguments
    input_file = sys.argv[1]
    output_file = sys.argv[2]

    # Perform the Markdown to HTML conversion
    convert_markdown_to_html(input_file, output_file)

    # Exit successfully
    sys.exit(0)
