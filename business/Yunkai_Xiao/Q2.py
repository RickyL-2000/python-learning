# %%
# -*- encoding:utf-8 -*-
# 习题二
def compare(op1, op2):
    return op1 in ["*", "/"] and op2 in ["+", "-"]

def getvalue(num1, num2, operator):
    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    else:
        return num1 / num2

def process(data, opt):
    operator = opt.pop()
    num2 = data.pop()
    num1 = data.pop()
    data.append(getvalue(num1, num2, operator))

def calculate(s):
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
            while opt and not compare(s[i], opt[-1]):
                process(data, opt)
            opt.append(s[i])
        i += 1 
    while opt:
        process(data, opt)
    print(data.pop())

if __name__ == '__main__':
    exp = input('请输入四则运算表达式（不要包含空格与括号）：\n')
    calculate(exp)

# %%
