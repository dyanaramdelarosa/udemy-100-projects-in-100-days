def read_file(filename: str) -> list:
    with open(filename) as file:
        return file.readlines()


def strip_contents(data: list) -> list:
    cleaned_data = [int(item.strip()) for item in data]
    return cleaned_data


file1_contents = read_file("file1.txt")
file2_contents = read_file("file2.txt")
file1_contents = strip_contents(file1_contents)
file2_contents = strip_contents(file2_contents)


result = [item for item in file1_contents if item in file2_contents]
print(result)
