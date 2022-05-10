"""
HW12_2. 从输入字符串中清除HTML标记。
如：对于字符串 <a href="index.htm">Welcom to Fudan University!</a> 处理后, 输出为Welcome to Fudan University!
<p class="chromeframe"> You are using an outdated browser. <a href="http://browsehappy.com/"> Upgrade your browser today </a> or <a href="">install Google Chrome Frame</a> to better experience this site </p>
"""
import re

while True:
    string = input("Enter a string: ").strip()
    ret = re.sub('<[^<]+?>', '', string).replace('\n', '').strip()
    print(ret)
