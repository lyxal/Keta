import Parse
import TokenLib
import string
from Code_Token import *
import functions

dyads: str = string.punctuation + "i"
monads: str = string.ascii_uppercase
nilads: str = "1234567890"

self = lambda x, y: y



def balance(source: str) -> str:
    

    '''

    a[bc --> a[bc]
    ab} --> {ab}
    m{ab]c -> [m{ab}]c
    
    '''

    final: str = ""
    brackets: [str] = []
    temp: str = ""
    escaped: str = False

    for char in source:

        if escaped:
            final += "\\" + char
            escaped = False

        elif char == "\\":
            escaped = True
  
        elif char in "[{":
            brackets.append(char)
            final += char

        elif char == "}":
            if brackets:
                if brackets[-1] == "{":
                    final += char

                else:
                    final = "{" + final + "]}"

                brackets.pop()

            else:
                final = "[" + final + "]"

        elif char == "]":
            if brackets:
                if brackets[-1] == "[":
                    final += char

                else:
                    final = "[" + final + "}]"

                brackets.pop()

            else:
                final = "[" + final + "]"

        else:
            final += char

    if brackets:
        for char in brackets:
            if char == "[":
                final += "]"
            else:
                final += "}"
    return final.replace("{", "[").replace("}", "]")


def arities(source: [TokenLib.Token]) -> [(int, TokenLib.Token)]:

    arity_list: [(int, TokenLib.Token)] = []
    for token in source:
        if token.get_name() == TokenLib.BLOCK:
            arity_list.append([0,
                               arities(token.get_data())])

        elif str(token.get_value()) in dyads:
            arity_list.append([2, token])

        elif str(token.get_value()) in monads:
            arity_list.append([1, token])

        else:
            arity_list.append([0, token])

    return arity_list

def code_tokenify(arity_list: [(int, TokenLib.Token)]) -> [Code_Token]:
    code_tokens = []
    exprs = []
    expr = []
    patterns = ["0", "1", "2",
        "020", "021", "022", "02", "10", "11", "12", "20", "21", "22",
                "102", "110", "111", "112", "120", "121", "122",
                "202", "210", "211", "212", "220", "221", "222"]
    pattern = ""
    while len(arity_list):
        if (pattern in patterns and
            pattern + str(arity_list[-1][0]) not in patterns):
            exprs.append([pattern, expr])
            expr = []
            pattern = ""
            
        pattern += str(arity_list[-1][0])
        expr.append(arity_list[-1][1])
        arity_list.pop()

    if expr and pattern in patterns:
        exprs.append([pattern, expr])
        expr = []
        pattern = ""


    for expr in exprs:
        arity_pattern, data = expr
        ctkn = None
        #print(arity_pattern, [m.get_data() for m in data])

        if arity_pattern == "0":
            # Nilad
            ctkn = Code_Token(self, None, data[0].get_value())

        elif arity_pattern == "1":
            # Monad
            ctkn = Code_Token(functions.search(data[0]),
                              None, Relative_Argument)

        elif arity_pattern == "2":
            # Dyad
            ctkn = Code_Token(functions.search(data[0]),
                              Relative_Argument, Relative_Argument)

        elif arity_pattern == "020":
            # Nilad-Dyad-Nilad
            ctkn = Code_Token(functions.search(data[1]),
                              data[0].get_value(), data[2].get_value())

        elif arity_pattern == "021":
            # Nilad-Dyad-Monad
            right = Code_Token(functions.search(data[2]),
                              None, Relative_Argument)
            ctkn = Code_Token(functions.search(data[1]),
                              data[0].get_value(), right)

        elif arity_pattern == "02":
            # Nilad-Dyad
            ctkn = Code_Token(functions.search(data[1]),
                              data[0].get_value(), Relative_Argument)

        elif arity_pattern == "10":
            # Monad-Nilad
            ctkn = Code_Token(functions.search(data[0]),
                              None, data[1].get_value())

        elif arity_pattern == "11":
            # Monad-Monad
            right = Code_Token(functions.search(data[1]),
                               None, Relative_Argument)

            ctkn = Code_Token(functions.search(data[0]),
                              None, right)

        elif arity_pattern == "12":
            # Monad-Dyad
            left = Code_Token(functions.search(data[0]),
                              None, Relative_Argument)

            ctkn = Code_Token(functions.search(data[1]),
                              left, Relative_Argument)

        elif arity_pattern == "20":
            # Dyad-Nilad
            ctkn = Code_Token(functions.search(data[0]),
                              Relative_Argument, data[1].get_value())
        
        elif arity_pattern == "21":
            # Dyad-Monad
            right = Code_Token(functions.search(data[1]),
                               None, Relative_Argument)

            ctkn = Code_Token(functions.search(data[0]),
                              Relative_Argument, right)

        elif arity_pattern == "22":
            # Dyad-Dyad
            left = Code_Token(functions.search(data[0]),
                              Relative_Argument, Relative_Argument)

            ctkn = Code_Token(functions.search(data[1]),
                              left, Relative_Argument)

        elif arity_pattern == "102":
            # Monad-Nilad-Dyad
            left = Code_Token(functions.search(data[0]),
                              None, data[1].get_value())

            ctkn = Code_Token(functions.search(data[2]),
                              left, Relative_Argument)

        elif arity_pattern == "110":
            # Monad-Monad-Nilad
            right = Code_Token(functions.search(data[1]),
                               None, data[2].get_value())

            ctkn = Code_Token(functions.search(data[0]),
                              None, right)

        elif arity_pattern == "111":
            # Monad-Monad-Monad
            right_1 = Code_Token(functions.search(data[2]),
                                 None, Relative_Argument)

            right = Code_Token(functions.search(data[1]),
                               None, right_1)

            ctkn = Code_Token(functions.search(data[0]),
                              None, right)

        elif arity_pattern == "120":
            # Monad-Dyad-Nilad
            left = Code_Token(functions.search(data[0]),
                               None, Relative_Argument)

            ctkn = Code_Token(functions.search(data[1]),
                              left, data[2].get_value())

        elif arity_pattern == "121":
            # Monad-Dyad-Monad
            left = Code_Token(functions.search(data[0]),
                              None, Relative_Argument)

            right = Code_Token(functions.search(data[2]),
                               None, Relative_Argument)

            ctkn = Code_Token(functions.search(data[1]),
                              left, right)

        elif arity_pattern == "122":
            # Monad-Dyad-Dyad
            left = Code_Token(functions.search(data[0]),
                              None, Relative_Argument)

            right = Code_Token(functions.search(data[2]),
                               Relative_Argument, Relative_Argument)

            ctkn = Code_Token(functions.search(data[1]),
                              left, right)

        elif arity_pattern == "202":
            # Dyad-Nilad-Dyad
            left = Code_Token(functions.search(data[0]),
                              Relative_Argument, data[1].get_value())

            ctkn = Code_Token(functions.search(data[2]),
                              left, Relative_Argument)

        elif arity_pattern == "210":
            # Dyad-Monad-Nilad
            right = Code_Token(functions.search(data[1]),
                               None, data[2].get_value())

            ctkn = Code_Token(functions.search(data[0]),
                              Relative_Argument, right)

        elif arity_pattern == "211":
            # Dyad-Monad-Monad
            right_1 = Code_Token(functions.search(data[2]),
                                 None, Relative_Argument)

            right = Code_Token(functions.search(data[1]),
                              None, right_1)

            ctkn = Code_Token(functions.search(data[0]),
                              Relative_Argument, right)

        elif arity_pattern == "212":
            # Dyad-Monad-Dyad
            right_1 = Code_Token(functions.search(data[1]),
                                 None, Relative_Argument)
            
            left = Code_Token(functions.search(data[0]),
                              Relative_Argument, right_1)

            ctkn = Code_Token(functions.search(data[2]),
                              left, Relative_Argument)

        elif arity_pattern == "220":
            # Dyad-Dyad-Nilad
            left = Code_Token(functions.search(data[0]),
                              Relative_Argument, Relative_Argument)

            ctkn = Code_Token(functions.search(data[1]),
                              left, data[2].get_value())

        elif arity_pattern == "221":
            # Dyad-Dyad-Monad
            left = Code_Token(functions.search(data[0]),
                              Relative_Argument, Relative_Argument)

            right = Code_Token(functions.search(data[2]),
                               None, Relative_Argument)

            ctkn = Code_Token(functions.search(data[1]),
                              left, right)

        elif arity_pattern == "222":
            # Triple Dyad

            left_1 = Code_Token(functions.search(data[0]),
                              Relative_Argument, Relative_Argument)

            left = Code_Token(functions.search(data[1]),
                              left_1, Relative_Argument)

            ctkn = Code_Token(functions.search(data[2]),
                              left, Relative_Argument)
            
            
        code_tokens.append(ctkn)

    return code_tokens

source: str = input()
parser: Parse.Parser = Parse.Parser(source)
x = code_tokenify(arities(parser.parse()[::-1]))
print(x[0].execute())
