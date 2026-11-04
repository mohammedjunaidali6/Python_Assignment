# Create point=(3,4), unpack it into x,y, 
# and construct a new point with x increased by 1. Show the original and 
# new tuples and a one-element tuple containing x.

point = (3,4)

x,y = point

new_point = (x+1,y)

single = (x,)

print("Orginal tuple", point)
print("new tuple", new_point)
print("one-element tuple", single)