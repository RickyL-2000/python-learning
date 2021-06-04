class Calculator:
    def __init__(self, exp=None, verbose=True):
        self.exp = exp
        self.res = None
        if self.exp is not None and len(self.exp) > 0:
            self.res = self.calculate(self.exp)
        if verbose and self.res is not None:
            print(self.res)
    
    @staticmethod
    def _compare(op1, op2):
        return op1 in ["*", "/"] and op2 in ["+", "-"]

    @staticmethod
    def _getvalue(num1, num2, operator):
        if operator == "+":
            return num1 + num2
        elif operator == "-":
            return num1 - num2
        elif operator == "*":
            return num1 * num2
        else:
            return num1 / num2

    def _process(self, data, opt):
        operator = opt.pop()
        num2 = data.pop()
        num1 = data.pop()
        data.append(self._getvalue(num1, num2, operator))

    def calculate(self, s):
        data = []  
        opt = [] 
        i = 0 
        while i < len(s):
            if s[i].isdigit(): 
                start = i 
                while i + 1 < len(s) and s[i + 1].isdigit():
                    i += 1
                data.append(int(s[start: i + 1]))  
            else: 
                while opt and not self._compare(s[i], opt[-1]):
                    self._process(data, opt)
                opt.append(s[i])
            i += 1 
        while opt:
            self._process(data, opt)
        return data.pop()

if __name__ == '__main__':
    exp = input('请输入四则运算表达式（不要包含空格与括号）：\n')
    res = Calculator(exp)
