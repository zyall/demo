class A:
    def __init__(self,list):
        self.list=list
    def Sort(self):
        lenth=len(list)
        for i in range(0,lenth):
            for j in range(i,lenth):
                if list[i] >= list[j]:
                    tmp=list[i]
                    list[i]=list[j]
                    list[j]=tmp
        return list

if __name__=='__main__':
    list=[9,3,5,6,8]
    s=A(list).Sort()
    print(s)