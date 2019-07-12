'''
23. 写一个小程序：控制台输入邮箱地址（格式为username@companyname.com），程序识别用户名和公司名后，将用户名和公司名输出到控制台。
要求：1. 校验输入内容是否符合规范（xx@yy.com）, 如是进入下一步，如否则抛出提示"incorrect email format"。注意必须以.com结尾
2. 可以循环“输入--输出判断结果”这整个过程
3. 按字母Q（不区分大小写）退出循环，结束程序
4.@和.com必须存在，而且前面的值不能为空
提示：用正则表达式的group()功能，一次取出username和companyname
'''
import re

print("Please enter Q to exit....")
while True:
    text = input("Please input your Email address：\n")
    matchObj = re.match(r'(^\S\w*)@(\S\w*)\.com', text)
    if matchObj:
        print(matchObj.group(1))
        print(matchObj.group(2))
    elif text == 'q' or text == 'Q':
        break
    else:
        print("incorrect email format")



# import re
#
# line = "Cats are smarter than dogs"
#
# matchObj = re.match(r'(.*) are (.*?) .*', line, re.M | re.I)
#
# if matchObj:
#     # print("matchObj.group() : ", matchObj.group())
#     print("matchObj.group(1) : ", matchObj.group(1))
#     print("matchObj.group(2) : ", matchObj.group(2))
# else:
#     print("No match!!")










