# A Simple Parser For Ekg

import TokenLib
from TokenLib import Token


class Parser():
    def __init__(self, source: str):
        self.source = source

    def parse(self, optional_source: str = "") -> [TokenLib.Token]:

        # Assumes that the source is already balanced

        # Variables used for determining if a block is being parsed/
        # if an escape sequence is present

        escaped = False
        block_level = 0
        temp_block = ""
        token_list = []
        string_mode = False
        temp_string = ""
        integer_mode = False
        temp_integer = ""

        if optional_source:
            code = optional_source
        else:
            code = self.source

        for char in code:
            #print(char, temp_integer, [str(x) for x in token_list])
            if integer_mode:
                if char not in "0123456789" and char != ".":
                    integer_mode = False
                    if block_level:
                        temp_block += temp_integer
                    else:
                        token_list.append(Token(TokenLib.NUMBER,
                                                eval(temp_integer)))


                    temp_integer = ""

                elif char == ".":
                    if "." in temp_integer:
                        raise SyntaxError("Misplaced '.'")
                    temp_integer += "."

                else:
                    temp_integer += char
                    continue
                        
            elif string_mode:
                if escaped:
                    escaped = False
                    temp_string += char
                else:
                    if char == '"':
                        string_mode = False
                        if block_level:
                            temp_block += '"' + temp_string + '"'
                        else:
                            token_list.append(Token(TokenLib.STRING,
                                                    temp_string))

                        temp_string = ""

                    elif char == "\\":
                        escaped = True
                        temp_string += char

                    else:
                        temp_string += char
                continue
                        
            elif escaped:
                self.token_list.append(Token(TokenLib.ESCAPE, char))
                escaped = False
                continue

            elif char == "\\":
                escaped = True
                continue

            elif char in "0123456789":
                temp_integer += char
                integer_mode = True
                continue

            elif char == '"':
                string_mode = True
                continue

            if char == "[":
                if block_level >= 1:
                    block_level += 1
                    temp_block += char

                else:
                    block_level = 1

            elif block_level:
                if char == "]":
                    if block_level == 1:
                        token_list.append(Token(TokenLib.BLOCK,
                                                self.parse(temp_block)))
                        block_level = 0
                        temp_block = ""

                    else:
                        temp_block += char
                        block_level -= 1

                else:
                    temp_block += char

            else:
                if char == " ":
                    continue
                token_list.append(Token(TokenLib.INSTRUCTION,
                                             char))

        if temp_block:
            token_list.append(Token(TokenLib.BLOCK,
                                         temp_block))

        elif temp_integer:
            token_list.append(Token(TokenLib.NUMBER,
                                    eval(temp_integer)))

        elif temp_string:
            token_list.append(Token(TokenLib.STRING,
                                    temp_string))
            

        return token_list

if __name__ == "__main__":
    source: str = "384+89"
    parser: Parser = Parser(source)
    tokens: [Token] = parser.parse()

    for token in tokens:
        print(token.get_data())
