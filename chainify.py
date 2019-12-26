dyads = "*+-/%"
monads = list(map(chr, range(ord("A"), ord("Z") + 1)))
nilads = "1234567890"

source = input()[::-1]
arities = []
for char in source:
    if char in dyads:
        arities.append((2, char))

    elif char in monads:
        arities.append((1, char))

    else:
        arities.append((0, char))

exprs = []
expr = []
patterns = ["02", "10", "11", "12", "20", "21", "22"]
pattern = ""
while len(arities):
    if pattern in patterns:
        exprs += [pattern, expr]
        expr = []
        pattern = ""
        
    pattern += str(arities[-1][0])
    expr.append(arities[-1][1])
    arities.pop()

if not exprs and pattern in patterns:
        exprs += [pattern, expr]
        expr = []
        pattern = ""

print(exprs)
