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

        if optional_source:
            code = optional_source
        else:
            code = self.source

        for char in code:
            if escaped:
                self.token_list.append(Token(TokenLib.ESCAPE, char))
                escaped = False

            elif char == "\\":
                escaped = True

            elif char == "[":
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
                token_list.append(Token(TokenLib.INSTRUCTION,
                                             char))

        if temp_block:
            token_list.append(Token(TokenLib.BLOCK,
                                         temp_block))

        return token_list

if __name__ == "__main__":
    source: str = "[P[DD+s]]S3"
    parser: Parser = Parser(source)
    tokens: [Token] = parser.parse()

    for token in tokens:
        print(token.get_data())
