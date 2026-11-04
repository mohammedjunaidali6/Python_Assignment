# Count occurrences in ['sql','python','sql'] with a dictionary. 
# Expected: {'sql':2,'python':1}. Explain how you handle a word seen for the first time.

words = ['sql', 'python', 'sql']

count = {}

for word in words:
    if word in count:
        count[word] += 1
    else: 
        count[word] = 1

print(count)