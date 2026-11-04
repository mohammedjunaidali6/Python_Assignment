# Using a loop, sum positive values in [-2,5,0,3]. 
# Expected total: 8. State whether zero and negatives contribute, and do not mutate the input.

numbers = [-2,5,0,3]

total = 0

for num in numbers:
    if num > 0:
        total += num


print("total", total)