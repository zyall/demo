# 11.控制台输入一组以逗号隔开的4位二进制数字，若该数字的的十进制数能被5整除，则将数字以逗号隔开输出。
# 例如输入：0100,0101, 0011,1010,1001
# 输出：0101,1010

def num():
    l = input("请输入：").split(',')
    a = []
    for i in l:
        if int(i, 2) % 5 == 0:
            a += [i]
    return ','.join(a)


print(num())

# 12.找出范围在1000-3000（包括左右边界），每一位都是偶数的数字
# （例如2236不满足范围，因为3不是偶数；2008满足范围，0是偶数；1286不满足，1不是偶数）
def get_num():
    num = ''
    for a in range(1000, 3001):
        a = str(a)
        if int(a[0]) % 2 == 0 and int(a[1]) % 2 == 0 and int(a[2]) % 2 == 0 and int(a[3]) % 2 == 0:
            num += str(a) + ','
    return num.strip(',')


print(get_num())