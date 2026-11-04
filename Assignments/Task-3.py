def transform_pair(pair,fn):
    return (fn(pair[0]), fn(pair[1]))

pair = (2,5)

result = transform_pair(pair, lambda x: x+1)

assert result ==(3,6)

assert pair == (2,5)

print ("Original tuple:", pair)
print ("New tuple:", result)








    