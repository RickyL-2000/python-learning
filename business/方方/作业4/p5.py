import re
import datetime

t = "1.   abc  2016-10-31  \n2.   xyz   2016-9-4\n3.   aef   2016-10-aa\n4.    asasf asdf 10-14\n5.  2013-10-3  234234\n6.  1945-8-15 abc  1945\n7.  1972-01-30 asdf  1988-10-1"

text = input("输入一段文本:")
date_all = re.findall(r"(\d{4}-\d{1,2}-\d{1,2})", text)
idx = 1
for date in date_all:
    try:
        datetime.datetime.strptime(date, '%Y-%m-%d')
    except ValueError:
        continue
    yyyy, mm, dd = date.split("-")
    print(f"{idx}. {mm:>02}/{dd:>02}/{yyyy:>04}")
    idx += 1
