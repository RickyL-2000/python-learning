1) """
2) HW12_1. 验证一个字符串是否为有效电子邮件地址. “有效”定义如下：
3) 1) 由“用户名@服务器域名”构成；
4) 2) 用户名：由字母a～z(不区分大小写)、数字0～9、点、减号或下划线组成。只能以数字或字母开头和结尾。
5) 如：Jack.s, Jack_s, Jack-s, Jack123均为合法的用户名，%Jack, Jack#s, Jack$均为无效用户名。
6) 3) 服务器域名：多个字符串之间用点分隔。其中，末尾字符串仅包含字母a～z(不区分大小写)，且由2~3个字母组成。其它字符串由字母a～z(不区分大小写)、数字0～9、减号组成，且以数字或字母开头和结尾。
7) 如：fudan.edu.cn, 163.com, abc-123.org均为合法域名，abc.123, abc.cncn, abc-.org, abc_123.org均为无效域名。

8) Enter an email address: huiliu@fudan.edu.cn
9) Valid
10) Enter an email address: 123456@fudan.edu.cn
11) Valid
12) Enter an email address: comet.1@163.com
13) Valid
14) Enter an email address: comet_1@163.com
15) Valid
16) Enter an email address: %hui@fudan.edu.cn
17) Invalid
18) Enter an email address: comet#1@163.com
19) Invalid
20) Enter an email address: comet%@163.com
21) Invalid
22) Enter an email address: alex-von-freud@icloud.com
23) Valid
24) Enter an email address: comet.1@163.cncn
25) Invalid
26) Enter an email address: comet@163.361
27) Invalid
28) Enter an email address: hui@abc_123.edu.it
29) Invalid
30) Enter an email address: hui@abc-123.edu.it
31) Valid
32) """
33) import re

# emmmm

34) while True:
35)     email = input("Enter an email address: ")
36)     if email == "":
37)         break
38)     email = email.strip()
39)     if re.match(r"^([A-Za-z0-9]+[-._])*[A-Za-z0-9]+@(([A-Za-z0-9]+[-])*[A-Za-z0-9]+\.)*[A-Za-z]{2,3}$", email):
40)         print("Valid")
41)     else:
42)         print("Invalid")
43)     continue
