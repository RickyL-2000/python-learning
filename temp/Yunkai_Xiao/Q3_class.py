import random
import time
import operator

class Calc24:
    __array_op = ('+', '-', '*', '/')

    @staticmethod
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

    @classmethod
    def Cal_abcd1(cls, num1,num2,num3,num4,op1,op2,op3):
        r1=cls.Cal_pri(num1,num2,op1)
        r2=cls.Cal_pri(r1,num3,op2)
        return cls.Cal_pri(r2,num4,op3)

    @classmethod
    def Cal_abcd2(cls, num1,num2,num3,num4,op1,op2,op3):
        r1 = cls.Cal_pri(num1, num2, op1)
        r2 = cls.Cal_pri(num3, num4, op3)
        return cls.Cal_pri(r1, r2, op2)

    @classmethod
    def Cal_abcd3(cls, num1,num2,num3,num4,op1,op2,op3):
        r1 = cls.Cal_pri(num2, num3, op2)
        r2 = cls.Cal_pri(r1, num4, op3)
        return cls.Cal_pri(num1, r2, op1)

    @classmethod
    def Cal_abcd4(cls, num1,num2,num3,num4,op1,op2,op3):
        r1 = cls.Cal_pri(num2, num3, op2)
        r2 = cls.Cal_pri(num1, r1, op1)
        return cls.Cal_pri(r2,num4,op3)

    @classmethod
    def Cal_abcd5(cls, num1,num2,num3,num4,op1,op2,op3):
        r1 = cls.Cal_pri(num3, num4, op3)
        r2 = cls.Cal_pri(num2, r1, op2)
        return cls.Cal_pri(num1, r2, op1)

    @classmethod
    def get_24(cls, i,j,k,t):
        str1="N0_Answer"
        for op1 in cls.__array_op:
            for op2 in cls.__array_op:
                for op3 in cls.__array_op:
                    if cls.Cal_abcd1(i,j,k,t,op1,op2,op3)==24:
                        return (i,j,k,t,op1,op2,op3,"1")
                    elif cls.Cal_abcd2(i,j,k,t,op1,op2,op3)==24:
                        return (i,j,k,t,op1,op2,op3,"2")
                    elif cls.Cal_abcd3(i,j,k,t,op1,op2,op3)==24:
                        return (i,j,k,t,op1,op2,op3,"3")
                    elif cls.Cal_abcd4(i,j,k,t,op1,op2,op3)==24:
                        return (i,j,k,t,op1,op2,op3,"4")
                    elif cls.Cal_abcd5(i,j,k,t,op1,op2,op3)==24:
                        return (i,j,k,t,op1,op2,op3,"5")
        return str1

    @classmethod
    def calculate(cls, list24):
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
                        list25=cls.get_24(list24[i],list24[j],list24[k],list24[t])
                        if operator.eq(list25,"N0_Answer") is False:
                            return list25
        return list25

    def begin(self):
        while 1:
            list24 = []
            for i in range(0,4):
                list24.append(float(random.randint(1, 10)))
            print("####################")
            print("计算：")
            print(list24)
            print("查看参考答案，答案不唯一：(按下2并回车)")
            print("退出：（按下1并回车）")
            list25 = self.calculate(list24)
            result = input()
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

if __name__ == '__main__':
    calc24 = Calc24()
    calc24.begin()
