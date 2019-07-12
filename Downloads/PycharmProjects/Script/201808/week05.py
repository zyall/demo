# # 9. 控制台输入多行（注意是一次性输入多行）英文字母，要求把输入内容转成大写字母，打印到控制台。（行数，内容顺序不变）
# # 如输入:
# # Hello world
# # Practice makes perfect
# # 函数输出:
# # HELLO WORLD
# # PRACTICE MAKES PERFECT
lines=[]

while True:
    s = input("")
    if s:
        lines.append(s.upper())
    else:
        break
for sentence in lines:
    print(sentence)

#10. 控制台输入以空格隔开的一串单词，要求把输入内容去重后，按字母表前后排序后，作为结果输出
# 如输入：hello world and practice makes perfect and hello world again
# 输出：again and hello makes perfect practice world

# def sr():
#     l1 = input("请输入：").split(" ")
#     l2 = []
#     l1.sort()
#     [l2.append(i) for i in l1 if not i in l2]
#     return ' '.join(list(l2))


# print(sr())
#
# # l1 = input("请输入：").split(" ")
# # l2=list(set(l1))
# # l2.sort()
# # print(' '.join(list(l2)))



#找出重复项

a = ['l', 'i', 'u', 'h', 'a', 'i', 'w', 'e', 'n']
# print([val for val in list(set(a)) if a.count(val)==2])

for val in list(set(a)):
    if a.count(val) == 2:
        print(val)
