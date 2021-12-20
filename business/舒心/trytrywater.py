# %%
# with open("sample.txt", "r", encoding="utf-8") as f:
#     content = f.read()

content = "The Python Tutorial\n      \nPython is an easy to learn, powerful programming language. It has efficient high-level data structures and a simple but effective approach to object-oriented programming. Python’s elegant syntax and dynamic typing, together with its interpreted nature, make it an ideal language for scripting and rapid application development in many areas on most platforms.\n   \t \nThe Python interpreter and the extensive standard library are freely available in source or binary form for all major platforms from the Python web site, https://www.python.org/, and may be freely distributed. The same site also contains distributions of and pointers to many free third party Python modules, programs and tools, and additional documentation.\n\nThe Python interpreter is easily extended with new functions and data types implemented in C or C++ (or other languages callable from C). Python is also suitable as an extension language for customizable applications.\n\nThis tutorial introduces the reader informally to the basic concepts and features of the Python language and system. It helps to have a Python interpreter handy for hands-on experience, but all examples are self-contained, so the tutorial can be read off-line as well.\n\nFor a description of standard objects and modules, see The Python Standard Library. The Python Language Reference gives a more formal definition of the language. To write extensions in C or C++, read Extending and Embedding the Python Interpreter and Python/C API Reference Manual. There are also several books covering Python in depth.\n\nThis tutorial does not attempt to be comprehensive and cover every single feature, or even every commonly used feature. Instead, it introduces many of Python’s most noteworthy features, and will give you a good idea of the language’s flavor and style. After reading it, you will be able to read and write Python modules and programs, and you will be ready to learn more about the various Python library modules described in The Python Standard Library."

# %%
origin_lines = content.split('\n')

# %%
lines = []
cnt = 1
for origin_line in origin_lines:
    if origin_line.strip() == "":
        lines.append(origin_line)
        continue
    idx = 0
    while idx < len(origin_line):
        if idx + 60 >= len(origin_line):
            lines.append(str(cnt).ljust(5) + origin_line[idx:])
            cnt += 1
        else:
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
        print(idx)
        idx += 60

# %%
for line in lines:
    print(line)