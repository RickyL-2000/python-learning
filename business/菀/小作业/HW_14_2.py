"""
14_2. 如果一个数能够被组成它的各个非0数字整除, 则称它是魔法数. 例如: 1-9都是魔法数, 10, 11, 12, 101都是魔法数, 但17就不是魔法数(因为17不能被数字7整除). 现在给定正整数x,y, 求闭区间[x,y]内的魔法数个数. 要求:
1) 有效的区间输入: 必须是由一个分隔符从中连接的两个正整数, 且分隔符只能是空格、 "-"或者","号, 其它输入均无效; 第二个正整数必须大于等于第一个正整数, 若小于则用raise主动抛出异常.
2) 用try...except结构处理各种非法输入.
3) 计算魔法数个数, 并输出计算结果.
4) 最后, 提示用户是否继续运行: 若是, 则重复输入和计算; 否则, 退出程序运行.
"""
# %%
import re

def check_magic(num):
    str_num = str(num)
    for c in str_num:
        if c != "0":
            if num % int(c) == 0:
                continue
            else:
                return False
    return True
            

if __name__ == '__main__':
    while True:
        try:
            rng = input("Please enter range[a,b] (0<a<=b):").strip()
            if not re.match(r"\w+([\s]|[-,])\w+", rng):
                raise Exception("wrong separator!")
            rng = re.sub(r"([\s]|[-,])", " ", rng)
            left, right = rng.split()
            left, right = int(left), int(right)
            if left > right:
                raise Exception("wrong range!")
        except ValueError:
            print("wrong type!")
            continue
        except Exception as err:
            print(err)
            continue
        cnt = 0
        for num in range(left, right+1):
            if check_magic(num):
                cnt += 1
        print(f"[{left},{right}] has {cnt} magic numbers!")
        while True:
            ans = input("Continue? (Y/N)").strip()
            if ans.lower() in "yn":
                break
        if ans.lower() == "y":
            continue
        else:
            print("Bye....")
            break
