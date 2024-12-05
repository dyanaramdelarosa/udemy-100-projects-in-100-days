"""
Day 26 Project (List Comprehension): Nato Phonetic Alphabet

This project provides the nato phonetic alphabet for a given word.
It uses list comprehension in order to achieve this
"""

NATO = "nato_phonetic_alphabet.csv"


def read_file(filename: str) -> list:
    with open(filename) as file:
        return file.readlines()


def strip_contents(data: list) -> list:
    cleaned_data = [item.strip() for item in data[1:]]
    return cleaned_data


def setup_nato_alphabet(cleaned_nato: list) -> dict:
    nato_alphabet = {nato.split(",")[0]: nato.split(",")[1] for nato in cleaned_nato}
    return nato_alphabet


if __name__ == "__main__":
    nato = read_file(NATO)
    nato = strip_contents(nato)
    nato_alphabet = setup_nato_alphabet(nato)

    word = input("Enter a word: ")
    nato_equivalent = [nato_alphabet[letter.capitalize()] for letter in word]
    print(nato_equivalent)
