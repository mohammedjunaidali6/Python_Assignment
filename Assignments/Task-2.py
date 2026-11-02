# Read an integer quantity as text. Preserve raw and parsed quantity, 
# then calculate doubled without changing either earlier binding. 
# For input 7, test all three values. Explain why class is not a 
# valid variable name and why rebinding doubled does not change quantity.

raw_quantity = input("Enter quantity: ")

quantity = int(raw_quantity)

doubled = quantity * 2

print("Raw quantity:", raw_quantity, type(raw_quantity))
print("Parsed quantity:", quantity, type(quantity))
print("Doubled quantity:", doubled, type(doubled))

# class is a Python keyword, so it cannot be a variable name.

# Rebinding doubled does not change quantity
# because they are separate variable bindings.

                     
                     