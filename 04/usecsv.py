# CSV 파일 불러오기
import csv, os
import re


def opencsv(filename) :
    f = open(filename, 'r')
    reader = csv.reader(f)
    output = []
    for i in reader:
        output.append(i)
    return output


# CSV 파일 작성하기

def writecsv(filename, the_list) :
    with open(filename, 'w', newline='') as f :
        a = csv.writer(f, delimiter = ',')
        a.writerows(the_list)

# CSV형 리스트에서 숫자형 변환

def switch(list_name) :
    for i in list_name
        for j in i :
            try :
                i[i.index(j)] = float(re.sub(',','',j))
            except :
                pass
    return list_name