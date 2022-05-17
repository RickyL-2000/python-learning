"""
HW14_3. 统计电影信息: 读取文件movie.txt, 输出字典. 要求实现以下两个函数：
1) 函数extract_data_list(filename)
读取文件filename, 返回一个列表. 列表的每个元素为(年份，电影名，票房，导演)构成的元组. 处理时, 去除空行以及行首包含'#'的行; 去除行首和行尾的空白符. 例如: 对于文件movie.txt, 生成的列表如下:
[('2013', 'Rush', '2.44', 'Ron Howard'), ('2001', 'A Beautiful Mind', '3.11', 'Ron Howard'), ('2008', 'Hunger', '1.54', 'Steve McQueen'), ('2009', 'Avatar', '28.47', 'James Cameron'), ('2019', 'Avengers: Endgame', '27.97', 'Anthony Russo'), ('1997', 'Titanic', '22.01', 'James Cameron')]
2) 函数construct_movies_by_director(data_list)
参数data_list为调用函数extract_data_list得到的列表. 经处理之后, 返回一个字典: 键是导演, 值为电影信息列表, 列表元素为(年份, 电影名, 票房)元组, 且该电影信息列表按票房从多到少顺序排列.
 HW14_3_1.png
在处理过程中, 如果同样的电影信息出现多于一次, 则抛出异常"重复数据:电影名". 例如: 在movie.txt中,影片信息"2009,Avatar,US,28.47,James Cameron"出现2次,则程序输出:
HW14_3_2.png
"""

def extract_data_list(filename):
    data_list = []
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f.readlines():
            if len(line.strip()) == 0:
                continue
            if line.strip()[0] == "#":
                continue
            data = line.strip().split(",")
            data_list.append(tuple([data[0].strip(), data[1].strip(), data[3].strip(), data[4].strip()]))

    return data_list

def construct_movies_by_director(data_list):
    movie_dict = {}
    for line in data_list:
        data = tuple([int(line[0]), line[1], float(line[2])])
        if line[3] in movie_dict:
            if data in movie_dict[line[3]]:
                raise Exception(f"重复数据:{line[1]}")
            movie_dict[line[3]].append(data)
        else:
            movie_dict[line[3]] = [data]
    for dir in movie_dict:
        movie_dict[dir] = sorted(movie_dict[dir], key=lambda x: x[2], reverse=True)
    return movie_dict

if __name__ == '__main__':
    data_list = extract_data_list("movie.txt")
    print(construct_movies_by_director(data_list))
