import csv, os


# CSV 파일 읽기

os.chdir(r'C:\workspace\Doit_python\04')
f = open('a.csv', 'r')

new = csv.reader(f)
print(new)

for i in new:
    print(i)

a_list = []

# 처음 반복문을 수행하면서 커서가 맨 마지막으로 이동 -> 커서를 처음으로 이동!
f.seek(0)

for i in new:
    print(i)
    a_list.append(i)

print(a_list)

def opencsv(filename) :
    f = open(filename, 'r')
    reader = csv.reader(f)
    output = []
    for i in reader:
        output.append(i)
    return output

print(opencsv('example2.csv'))

# CSV 파일 쓰기

a = [['구','전체','내국인','외국인'],['관악구', 519864, 502089, 17775], ['강남구', 547602, 542498, 5104],
     ['송파구',686181, 679247, 6934], ['강동구', 428547, 424235, 4312]]

# newline을 입력하지 않으면 줄바꿈이 한번 더 일어남.
f = open('abc.csv', 'w', newline='')
csvobject = csv.writer(f, delimiter=',')
csvobject.writerows(a)