s = input("请输入字符串: ")
while True:
    start = s.find("<")
    end = s.find(">")
    if start == -1:
        break
    s = s[:start] + s[end+1:]
print("输出:", s)
