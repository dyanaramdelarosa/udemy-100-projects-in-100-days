"""
Day 24 Project (Files, Directories, and Paths): Mail Merge

This project automates the generation of letter for a set of
recipients given a template
"""


STARTING_LETTER_FILE = "Input/Letters/starting_letter.txt"
INVITED_NAMES_FILE = "Input/Names/invited_names.txt"
PLACEHOLDER = "[name]"

def read_file(file_name):
    with open(file_name) as file:
        return file.readlines()


def replace_placeholder(name, letter_contents):
    new_contents = []
    for line in letter_contents:
        new_contents.append((line.replace(PLACEHOLDER, name)))
    return new_contents

def write_letter(name, letter_contents):
    letter_contents = replace_placeholder(name, letter_contents)
    file_name = f"Output/ReadyToSend/{name}.txt"
    with open(file_name, mode="w") as file:
        for line in letter_contents:
            file.write(line)


def generate_letters(names, letter_contents):
    for name in names:
        write_letter(name.strip(), letter_contents)


if __name__ == "__main__":
    names = read_file(INVITED_NAMES_FILE)
    letter_contents = read_file(STARTING_LETTER_FILE)

    generate_letters(names, letter_contents)

