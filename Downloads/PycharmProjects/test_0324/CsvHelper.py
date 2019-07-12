
import csv

class CsvHelper():
    def read_data(self,f,encoding = "utf-8-sig"):
        '''
        :param f:
        :param encoding:
        :return:列表方式的csv文件内容
        '''
        data_ret = []
        # cls = []
        with open(f,encoding=encoding,mode='r') as csv_file:
            csv_data = csv.reader(csv_file)
            for row in csv_data:
                data_ret.append(row)
        return data_ret
        # 去掉首行标题
        # for i in range(1,len(data_ret)):
        #     cls.append(data_ret[i])
        # return cls
    '''读取字典'''
    def read_dict(self,f,encoding = "utf-8-sig"):
        '''
        :param f:
        :param encoding:
        :return:列表方式的dict_file文件内容
        '''
        data_ret = []
        # cls = []
        with open(f,encoding=encoding,mode='r') as dict_file:
            csv_data = csv.DictReader(dict_file)
            for row in csv_data:
                data_ret.append(row)
        return data_ret
        # for i in range(1,len(data_ret)):
        #     cls.append(data_ret[i])
        # return cls

if __name__ =='__main__':
    A = CsvHelper()
    # C = A.read_data('./testFile/1.csv')
    C = A.read_dict('./testFile/1.csv')

    print(C)