# -*- encoding:utf-8 -*-
# 习题三
import random
import time
import operator
def Cal_pri(first_x,second_y,op):
    if op=='+':
        return first_x+second_y
    elif op=='-':
        return first_x-second_y
    elif op=='*':
        return first_x*second_y
    elif op=='/':
        if second_y!=0:
            return first_x/second_y
        else:
            return 0.0001

def Cal_abcd1(num1,num2,num3,num4,op1,op2,op3):
    r1=Cal_pri(num1,num2,op1)
    r2=Cal_pri(r1,num3,op2)
    return Cal_pri(r2,num4,op3)

def Cal_abcd2(num1,num2,num3,num4,op1,op2,op3):
    r1 = Cal_pri(num1, num2, op1)
    r2 = Cal_pri(num3, num4, op3)
    return Cal_pri(r1, r2, op2)

def Cal_abcd3(num1,num2,num3,num4,op1,op2,op3):
    r1 = Cal_pri(num2, num3, op2)
    r2 = Cal_pri(r1, num4, op3)
    return Cal_pri(num1, r2, op1)

def Cal_abcd4(num1,num2,num3,num4,op1,op2,op3):
    r1 = Cal_pri(num2, num3, op2)
    r2 = Cal_pri(num1, r1, op1)
    return Cal_pri(r2,num4,op3)

def Cal_abcd5(num1,num2,num3,num4,op1,op2,op3):
    r1 = Cal_pri(num3, num4, op3)
    r2 = Cal_pri(num2, r1, op2)
    return Cal_pri(num1, r2, op1)

def get_24(i,j,k,t,array_op):
    str1="N0_Answer"
    for op1 in array_op:
        for op2 in array_op:
            for op3 in array_op:
                if Cal_abcd1(i,j,k,t,op1,op2,op3)==24:
                    return (i,j,k,t,op1,op2,op3,"1")
                elif Cal_abcd2(i,j,k,t,op1,op2,op3)==24:
                    return (i,j,k,t,op1,op2,op3,"2")
                elif Cal_abcd3(i,j,k,t,op1,op2,op3)==24:
                    return (i,j,k,t,op1,op2,op3,"3")
                elif Cal_abcd4(i,j,k,t,op1,op2,op3)==24:
                    return (i,j,k,t,op1,op2,op3,"4")
                elif Cal_abcd5(i,j,k,t,op1,op2,op3)==24:
                    return (i,j,k,t,op1,op2,op3,"5")
    return str1

def new_arry(list24,array_op):
    list25=[]
    p=0
    for i in range(4):
        for j in range(4):
            if i==j:
                continue
            for k in range(4):
                if i==k or j==k:
                    continue
                for t in range(4):
                    if i==t or j==t or k==t:
                        continue
                    list25=get_24(list24[i],list24[j],list24[k],list24[t],array_op)
                    if operator.eq(list25,"N0_Answer") is False:
                        return list25
    return list25

if __name__ == "__main__":
    array_op = ['+', '-', '*', '/']
    while 1:
        list24 = []
        for i in range(0,4):
            list24.append(float(random.randint(1, 10)))
        print("####################")
        print("计算：")
        print(list24)
        print("查看参考答案，答案不唯一：(按下2并回车)")
        print("退出：（按下1并回车）")
        list25=new_arry(list24,array_op)
        result=input()
        if result == '2':
            if list25[len(list25)-1]=="1":
                print('(','(',list25[0],list25[4],list25[1],')',list25[5],list25[2],')',list25[6],list25[3]," = 24");
                print("####################")
            elif list25[len(list25)-1]=="2":
                print('(',list25[0], list25[4], list25[1],')', list25[5], '(',list25[2], list25[6], list25[3],')', " = 24");
                print("####################")
            elif list25[len(list25)-1]=="3":
                print(list25[0],list25[4],'(', '(',list25[1], list25[5],list25[2],')', list25[6], list25[3],')', " = 24");
                print("####################")
            elif list25[len(list25)-1]=="4":
                print('(',list25[0], list25[4],'(', list25[1], list25[5], list25[2],')',')', list25[6], list25[3], " = 24");
                print("####################")
            elif list25[len(list25)-1]=="5":
                print(list25[0], list25[4],  '(',list25[1], list25[5], '(',list25[2], list25[6], list25[3],')', ')'," = 24");
                print("####################")
        elif result == '1':
            break