# %%
def read_text(filename: str) -> str:
    with open(filename, "rt", 
        encoding = "utf-8", errors = "ignore") as f:
            return f.read()
def stat_char(text: str) -> list:
    print(id(text))
    print("2", len(text))
    for c in "abcdefghijklmnopqrstuvwxyz" \
        "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789" \
        " ~!@#$%^&*()_+=-`[]\{}|:\";',./<>?，。、　" \
        "《》？；’：”“【】、｛｝§=-+——）（*&……%￥#@！～·\n":
            text = text.replace(c, "")
    print("3", len(text))
    print(id(text))
    chars = {}
    for c in text:
        chars[c] = chars.get(c, 0) + 1
    result = list(chars.items())	
    result.sort(key = lambda x: x[1], reverse = True)
    return result

# filename = "c:/Users/1/Desktop/cxj.txt"
filename = "./test.txt"
text = read_text(filename)
print(id(text))
print("1", len(text))
conclusion = stat_char(text)
print("4", len(text))
print("总字数：", len(text))
print("用字数：", len(conclusion))
print("最常用百字频率如下：")
for i in range(100):
    print("{}：{:>5d}".format(*conclusion[i]))

# %%
