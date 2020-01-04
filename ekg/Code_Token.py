class Code_Token():
    def __init__(self, function, left, right):
        '''

        function: a callable function object
        left: the left argument (if applicable)
        right: the right argument

        '''
        self.fn = function
        self.left_arg = left
        self.right_arg = right

    def execute(self, surrounds=None):
        if self.left_arg == Relative_Argument:
            if surrounds:
                self.left_arg = surrounds[0]
            else:
                self.left_arg = eval(input())            

        if self.right_arg == Relative_Argument:
            if surrounds:
                self.right_arg = surrounds[-1]
            else:
                self.right_arg = eval(input())

        if type(self.left_arg) == Code_Token:
            self.left_arg = self.left_arg.execute()

        if type(self.right_arg) == Code_Token:
            self.right_arg = self.right_arg.execute()
        return self.fn(self.left_arg, self.right_arg)

class Relative_Argument:
    pass
