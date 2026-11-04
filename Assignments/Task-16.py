# Write total_positive(values) returning the sum of positive numbers. 
# For [-1,2,3], return 5. For [], return 0. Do not print instead of returning or mutate values.

def total_positive(values):
    total = 0

    for number in values:
        if number > 0:
            total += number

    return total

result = total_positive([-1,2,3])
print(result)