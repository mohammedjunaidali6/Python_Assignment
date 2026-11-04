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
