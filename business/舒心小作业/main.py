# open file
with open("sample.txt", "r", encoding="utf-8") as f:
    content = f.read()

origin_lines = content.split('\n')

lines = []
cnt = 1
for origin_line in origin_lines:
    if origin_line.strip() == "":
        lines.append(origin_line)
        continue
    idx = 0
    while idx < len(origin_line):
        print(idx)
        if origin_line[idx].strip() == "":  # no spaces in beginning
            idx += 1
            continue
        if idx + 60 >= len(origin_line):    # at the end
            lines.append(str(cnt).ljust(5) + origin_line[idx:])
            cnt += 1
        else:   # split
            if origin_line[idx+59].isalpha() and origin_line[idx+60].isalpha():
                end = idx + 59
                while origin_line[end].isalpha():
                    end -= 1
                lines.append(str(cnt).ljust(5) + origin_line[idx:end+1])
                cnt += 1
                idx = end + 1
                continue
            else:
                lines.append(str(cnt).ljust(5) + origin_line[idx:idx+60])
                cnt += 1
        idx += 60

# write file
with open("sample_out.txt", "w", encoding="utf-8") as f:
    for line in lines:
        f.write(line + "\n")
