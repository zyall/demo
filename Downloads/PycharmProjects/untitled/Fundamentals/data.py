#coding=utf-8
class A:
    def __init__(self,filepath):
        self.filepath=filepath
    def load_dict_from_file(self):
        param={}
        try:
            with open(filepath, 'r') as f:
                for line in f:
                    (key, value) = line.strip().split(':')
                    param[key] = value
                return param
        except IOError as ioerr:\
            print("文件 %s 不存在" %filepath)


if __name__ == "__main__":
    filepath='param_file'
    a=A(filepath).load_dict_from_file()
    print(a)





