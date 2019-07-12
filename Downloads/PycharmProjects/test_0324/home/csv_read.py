from CsvHelper  import CsvHelper


csv_helper = CsvHelper()
csv_data = csv_helper.read_data('../testFile/1.csv')


# 去掉首行标题

head = True

for i in csv_data:
    if head:
        head = False
        continue
    print(i[0])
# 去掉首行标题
cls = []
for i in range(1,len(csv_data)):
    cls.append(csv_data[i])
print(cls)
