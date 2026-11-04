# Write a lambda returning the square of its argument. 
# Apply it to 3 and -2 and assert results 9 and 4. 
# Compare its return with a lambda that only prints the input.

square = lambda number: number * number

result1= square(3)
result2 =square(-2)

assert result1 == 9
assert result2 == 4

print("Square of 3:", result1)
print("Square of -2:", result2)

show = lambda number:print(number)

result3 = show(3)

print("print lambda return:", result3)