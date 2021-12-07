# 打开文件
f = open("sample.txt", "r")
content = f.read()
f.close()

output_lines = []
line_num = 1
for line in content.split('\n'):
    # 用于检查每两段之间的空行
    if line.strip() == "":
        output_lines.append(line.strip() + "\n")
        continue
    cursor = 0
    # 在每个长行中间进行断句
    while True:
        if cursor >= len(line):
            break
        if cursor + 60 < len(line): # 分句
            if not line[cursor+59].isalpha() or not line[cursor+60].isalpha():
                output_lines.append(str(line_num) + " "*(5-len(str(line_num))) + line[cursor:cursor+60].strip() + "\n")
                line_num += 1
                cursor += 60
            else:
                cursor2 = cursor + 59
                while line[cursor2].isalpha():
                    cursor2 -= 1
                output_lines.append(str(line_num) + " "*(5-len(str(line_num))) + line[cursor:cursor2+1].strip() + "\n")
                line_num += 1
                cursor = cursor2 + 1
                continue
        else:   # 处理最后一句
            output_lines.append(str(line_num) + " "*(5-len(str(line_num))) + line[cursor:].strip() + "\n")
            line_num += 1
            break

# 写入文件
f = open("sample_out.txt", "w")
for line in output_lines:
    f.write(line)
f.close()
