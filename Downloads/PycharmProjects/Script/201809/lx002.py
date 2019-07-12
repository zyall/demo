'''
需求北京：
1. 调某个接口可以合并一段时间的数据。比如原来是0701-0703、0704-0708、0709-0710。
传参start_date = 20180701, end_date = 20180710, 接口就会将上述3个时间段的数据合成1个20180701-20180710数据段。
2. 然后发现如果传参的start_date比数据段最早的时间还早，比如start_date传20180601，实际数据是从20180701开始的，那接口就会报错。
所以需要获取数据段第一个时间first_date，和实际传参start_date对比大小。如果start_date比first_date早，就给接口传first_date作为合并的起始时间

如下是具体实现的函数，伪代码，从实际脚本中摘抄出来的
'''

cube_list = ["a", "b", "c", "d", "e"]
first_date_dict = {"a": "20180701", "b": "20180701", "c": "20180718", "d": "20180701", "e": "20180601"}


def batch_merge_segments(start_date, end_date):
    res_list = []
    for cube_name in cube_list:
        first_date = first_date_dict[cube_name]
        # 如果start_date比起始时间大，则取起始时间
        if int(start_date) <= int(first_date):
            real_start_date = first_date
        # 如果start_date比起始时间小，则取start_date
        else:
            real_start_date = start_date
        res = {"cube_name": "%s—%s—%s" %(cube_name, real_start_date, end_date)}
        res_list.append(res)
    return res_list

res = batch_merge_segments(20180701, 20180910)
print(res)