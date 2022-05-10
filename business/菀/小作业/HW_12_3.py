"""
HW12_3. Sofia在公司刚刚经历了异常忙碌的一个月, 她决定休假一周. 为了能在假期好好休息而又不错过重要的工作邮件, 她打算把需要紧急处理的邮件转发给假期代理她工作的Stephen.
编写程序, 根据邮件主题(长度<=100字符)判断该邮件是否需要紧急处理. 满足如下规则中至少一条的邮件主题将被判断为紧急:
1) 包含所有字母均为大写的单词;
2) 以至少3个感叹号结束;
3) 包含下列单词: help, asap, urgent. 这些单词可能用不同方式拼写, 如: "HELP", "help", "HeLp", "H!E!L!P!", "H-E-L-P", 甚至是"HHHEEEEEEEEELLP".

Enter an email subject: Hi
Normal
Enter an email subject: I neeed HELP
Urgent!
Enter an email subject: He loves peace
Normal
Enter an email subject: H!E!L!P!
Urgent!
Enter an email subject: H-E-L-P
Urgent!
Enter an email subject: HHHEEEEEEEEEEELLP
Urgent!
Enter an email subject: Please reply ASAP
Urgent!
Enter an email subject: URGENT!!!
Urgent!
"""

import re

def check_subject(subject):
    if subject == subject.upper():
        return True
    if subject[-3:] == "!!!":
        return True
    subject = subject.lower()
    if re.match(r".*h+\W*e+\W*l+\W*p+\W*.*", subject):
        return True
    if re.match(r".*a+\W*s+\W*a+\W*p+\W*.*", subject):
        return True
    if re.match(r".*u+\W*r+\W*g+\W*e+\Wn+\Wt+\W*.*", subject):
        return True
    return False

while True:
    subject = input("Enter an email subject: ").strip()
    if check_subject(subject):
        print("Urgent!")
    else:
        print("Normal")

