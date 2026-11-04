# Write a function reading all text from a supplied path using UTF-8 and 
# closing the handle even if reading fails. State behavior for an empty file versus a missing file.

def read_file(path):
    with open(path, "r", encoding="utf-8") as file:
        text = file.read()

    return text

result = read_file("Assignments/notes.txt")
print(result)