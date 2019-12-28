# A Simple Token Class For Ekg


class Token():
    def __init__(self, name: str, value: str) -> None:
        self.tkn_name: str = name
        self.tkn_value: str = value

    def get_name(self) -> str:
        return self.tkn_name

    def get_value(self) -> str:
        return self.tkn_value

    def get_data(self) -> (str, str):
        return (self.tkn_name, self.tkn_value)

    def set_name(self, name: str):
        self.tkn_name = name

    def set_value(self, value: str):
        self.tkn_value = name

# Token names

INSTRUCTION = "instruction"
BLOCK = "block"
STRING = "string"
INTEGER = "integer"
ESCAPE = "escape"
