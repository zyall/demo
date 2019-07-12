# 13. 控制台输入一串英文字母+数字混合的字符串，统计字符串中，字母和数字的个数，作为结果输出。
# 例如输入：hello world! 123
# 输出：数字：3
# 字母：10
# import re
#
# s = input("请输入一串字符：")
# s2=re.findall(r'[A-Za-z]', s)
# s3=re.findall(r'\d', s)
# print("字母:", len(s2))
# print("数字:", len(s3))


s = input("请输入一串字符：")
l =[]
a =[]
for i in s:
    if i.isdigit():
        l.append(i)
    elif i.isalpha():
        a.append(i)

# print(len(l),len(a))

print('数字:', len(l))
print('字母:', len(a))


# 14. 控制台输入一串英文大小写混合的字符串，统计字符串中，大小写字母的个数，作为结果输出。
# 例如输入：Hello world!
# 输出：大写字母：1
# 小写字母：9
# s = input("请输入一串字符：")
# s2 = re.findall(r'[A-Z]', s)
# s3 = re.findall(r'[a-z]', s)
# print("大写字母:", len(s2))
# print("小写字母:", len(s3))
s = input("请输入一串字符：")
l =[]
a =[]
for i in s:
    if i.isupper():
        l.append(i)
    elif i.islower():
        a.append(i)

# print(len(l),len(a))

print('大写字母:', len(l))
print('小写字母:', len(a))
