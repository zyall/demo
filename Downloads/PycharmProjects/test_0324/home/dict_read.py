from CsvHelper  import CsvHelper

csv_helper = CsvHelper()
csv_d = csv_helper.read_dict('../testFile/1.csv')


for i in csv_d:
    print(i['age'])