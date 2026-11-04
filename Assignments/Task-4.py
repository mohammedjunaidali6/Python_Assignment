# Define Note(text) with an instance text attribute and load_note(path) 
# that reads UTF-8 text inside a with block then returns a Note. A file contains hello. 
# Verify returned text and independent notes for two files.


class Note:
    def __init__(self, text):
        self.text = text


def load_note(path):    
    with open(path, "r", encoding="utf-8") as file:
        text = file.read()

    return Note(text)

    
note1 = load_note("Assignments/note1.txt")
note2 = load_note("Assignments/note2.txt")

assert note1.text.strip() == "hello"
assert note2.text.strip() == "Python learning"

assert note1 is not note2

print("First Note", note1.text)
print("Second Note", note2.text) 
