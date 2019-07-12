'''
24. 定义一个函数：入参为数字n，生成一串长度为n的随机字符串作为结果输出。
要求：1. 对入参校验，要求n为大于0的正整数，如不满足要求则抛出错误提示，结束程序
2. 随机字符串取值范围：大小写字母、数字、特殊字符@#$*
提示：random.choice()函数

ABCDE12345. / ^ &+指定长度的随机字符串
'''
#
# import random,string
#
# #
# def rand_str(n):
#     if n > 0:
#         # chars = string.ascii_letters + string.digits + '@#$*'
#         chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789@#$*'
#         ran_str = ''.join(random.sample(chars,n))
#         # ran_str = ''.join(random.choice(chars) for _ in range(n))
#         return ran_str
#     else:
#         return "incorrect  format"
#
#
# if __name__ == '__main__':
#     # print(rand_str(0))
#     print(rand_str(5))


import random
def rand_str(n):
    rand_str = ''
    if n > 0:
        for i in range(n):
            rand_str += random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890')
        return rand_str
    else:
        return "incorrect  format"

print(rand_str(0))
print(rand_str(13))




