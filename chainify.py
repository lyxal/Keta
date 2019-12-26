dyads = "*+-/%"
monads = list(map(chr, range(ord("A"), ord("Z") + 1)))
nilads = "1234567890"

source = input()
arities = []
for char in source:
    if char in dyads:
        arities.append((2, char))

    elif char in monads:
        arities.append((1, char))

    else:
        arities.append((0, char))

exprs = []
while len(arities):
    # Try grouping triplets

    if len(arities) - 3 >= 0:
        exprs.append(arities[-3:])
        del arities[-3:]

    # Now, try grouping pair
    elif len(arities) - 2 >= 0:
        exprs.append(arities[-2:])
        del arities[-2:]
    else:
        exprs.append(arities[-1])
        del arities[-1]

print(exprs)
        
