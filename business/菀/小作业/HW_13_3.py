"""
HW13_3. 已知一个文件hosts.txt, 它保存了若干IP地址与主机名之间的映射. hosts的每行保存一条映射, 一个IP地址可能对应多个主机名(多个主机名之间以空白符分隔). IP地址的格式为点十进制描述法，即包含4个整数，每个整数为1到3个数字，4个整数之间以小数点隔开. 主机名由小写英文字母组成, 可能包括小数点. #后面的内容为注释部分, 忽略.
程序对hosts保存的所有纪录进行分析，分析结果保存在字典hosts_dict中. 该字典的key为IP地址, 值为该IP地址对应的一个或者多个主机名. 注意: 可能有多条纪录对应同一个IP地址, 此时要求将这些纪录合并. 
"""
# %%
import re

if __name__ == '__main__':
    hosts_dict = {}
    with open("hosts.txt", 'r') as f:
        for line in f.readlines():
            line = line.strip()
            if len(line) == 0:
                continue
            if line[0] == "#":
                continue
            line_lst = line.split()
            if re.match(r"(([1-9]\d\d|[1-9]?\d)\.){3}([1-9]\d\d|[1-9]?\d)", line_lst[0]):
                for domain in line_lst[1:]:
                    if domain[0] == "#":
                        break
                    if line_lst[0] in hosts_dict and domain not in hosts_dict[line_lst[0]]:
                        hosts_dict[line_lst[0]].append(domain)
                    else:
                        hosts_dict[line_lst[0]] = [domain]
    for key in hosts_dict:
        print(f"{key}: {hosts_dict[key]}")
    