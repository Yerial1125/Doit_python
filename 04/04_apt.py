import usecsv, re

# 1. CSV형 리스트로 만들고 자료 가공하기
apt = usecsv.switch(usecsv.opencsv('data/apt_201910.csv'))
print(len(apt))

# 2. 슬라이싱으로 원하는 자료 출력하기
print(apt[0])

for i in apt[:6] :
    print(i[0])

for i in apt[:6] :
    print(i[0],i[4],i[8])

print()
for i in apt :
    try:
        if i[5] >= 120 and i[8] <= 30000 and re.match('강원', i[0]) :
            print(i[0], i[4], i[8])
    except:
        pass

# 4. 분석결과를 CSV 파일로 저장하기

new_list =[]

for i in apt :
    try:
        if i[5] >= 120 and i[8] <= 30000 and re.match('강원', i[0]) :
            new_list.append([i[0], i[4], i[8]])
    except:
        pass

usecsv.writecsv('over120_lower30000.csv', new_list)