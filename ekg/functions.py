functions = {
    "+" : lambda x, y: x + y,
    "-" : lambda x, y: x - y,
    "*" : lambda x, y: x * y,
    "/" : lambda x, y: x / y,
    "%" : lambda x, y: x % y,
    "<" : lambda x, y: x < y,
    ">" : lambda x, y: x > y,
    "=" : lambda x, y: x == y,
    "a" : lambda x, y: all(y),
    "b" : lambda x, y: int(bin(y)[2:]),
    "c" : lambda x, y: y in x,
    "d" : lambda x, y: list(divmod(x, y)),
    "e" : None,
    "f" : None,
    "g" : lambda x, y: range(y),
    "h" : lambda x, y: x[y[0]:y[1]],
    "i" : lambda x, y: "".join([i[0] + i[1] for i in zip(x, y)]),
    "j" : None,
    "k" : None,
    "l" : lambda x, y: -1 if x.count(y) == 0 else x.index(y),
    "H" : lambda x, y: y / 2
}

def search(what):
    char = what.get_value()
    if char in functions and functions[char]:
        return functions[char]
    return lambda x, y: y
