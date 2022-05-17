"""
HW13_1. 修改第七章课件P23的例子, 在源程序文件(可能是.cpp/.py文件, 如: goldbach.cpp  下载 goldbach.cpp /property.py  下载 property.py )的每一行代码行首加上行号，保存为一个新的同类型文件(如: test.cpp保存为test_n.cpp). 要求: 空白行和单行注释不加行号(.py文件的单行注释以'#'开始, .cpp文件的单行注释以'//'开始).
Tip .cpp/.py文件都是文本文件, 可以用记事本打开.
"""

def comment(fname):
    with open(fname, 'r', encoding='UTF-8') as f:
        idx = 1
        lines = []
        for line in f.readlines():
            if len(line.strip()) == 0:
                lines.append(line)
                continue
            if fname[-2:] == "py" and line.strip()[0] == "#":
                lines.append(line)
                continue
            if len(line.strip()) >= 2 and fname[-3:] == "cpp" and line.strip()[:2] == "//":
                lines.append(line)
                continue
            line = str(idx) + ") " + line
            lines.append(line)
            idx += 1

    with open(fname[: -3] + ('_n.py' if fname[-2:] == "py" else '_n.cpp'), 'w', encoding='UTF-8') as f:
        f.writelines(lines)

if __name__ == '__main__':
    comment('emm.cpp')

