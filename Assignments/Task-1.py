# Given labels=["  Ada "," ","Bo"], build a NEW list of trimmed 
# nonblank labels. Use a conditional expression to choose clean 
# text or None and an if statement to append only non-None values. 
# Expected ["Ada","Bo"]. Preserve input, order and duplicates.


labels = ["  Ada "," ","Bo"]

new_labels = []

for label in labels:
    clean_text = label.strip()

    value = clean_text if clean_text else None

    if value is not None:
     new_labels.append(value)

print(new_labels)