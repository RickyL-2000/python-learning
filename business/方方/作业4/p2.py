s = input("请输入: ")
for i in range(len(s)-1, 0, -1):
    out = s[:i] + " " + s[i:]
    print(out)
print("-----")
for i in range(1, len(s)):
    out = s[:i] + " " + s[i:]
    print(out)
