# %%
# 打开文件
f = open("sample.txt", "r", encoding="utf-8")
content = f.read()
f.close()

lines = []
cursor = 0
line_num = 1
while cursor < len(content):
    # if content[cursor] == "\n" and cursor != len(content) - 1:
    #     end = cursor + 1
    #     while not content[end].isalpha() and end < len(content):
    #         end += 1
    #     lines.append(content[cursor: end])
    #     cursor = end
    #     continue
    # end = cursor + 1
    end = content[cursor+1: cursor+60].find("\n")
    if end != -1:
        # if cursor == end:
        #     end += 1
        end = cursor + 1 + end
        lines.append(str(line_num) + " "*(5-len(str(line_num))) + content[cursor: end + 1])
        cursor = end + 1
        line_num += 1
    else:
        # end = cursor + 1 + end
        # 分句
        if cursor + 60 >= len(content):
            # 处理最后一句的情况
            lines.append(str(line_num) + " "*(5-len(str(line_num))) + content[cursor: ])
            break
        elif content[cursor+59].isalpha() and content[cursor+60].isalpha():
            end = cursor + 59
            while content[end].isalpha():
                end -= 1
            lines.append(str(line_num) + " "*(5-len(str(line_num))) + content[cursor: end+1] + "\n")
            line_num += 1
            cursor = end + 1
            continue
        else:
            lines.append(str(line_num) + " "*(5-len(str(line_num))) + content[cursor: cursor+60] + "\n")
            line_num += 1
            cursor += 60

# 写入文件
f = open("sample_out.txt", "w", encoding="utf-8")
for line in lines:
    f.write(line)
f.close()