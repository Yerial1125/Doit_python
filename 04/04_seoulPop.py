import usecsv, re

# CSV형 리스트로 바꾸기
total = usecsv.opencsv('data/popSeoul.csv')
newPop = usecsv.switch(total)
print(newPop[:5])

# 등록외국인 비율 계산하기
i = newPop[1]
print(i)
print(i[2] / (i[1] + i[2]) * 100)

foreign = round(i[2] / (i[1] + i[2]) * 100 , 1)
print(foreign)

# 각 구의 외국인 비율 출력하기
for i in newPop :
    foreign = 0
    try :
        foreign = round(i[2] / (i[1] + i[2]) * 100, 1)
        print(i[0], foreign)
    except :
        pass

# 첫 행 지정하기
new = [['구', '한국인', '외국인', '외국인 비율(%)']]

for i in newPop :
    try:
        new.append([i[0], i[1], i[2], round(i[2] / (i[1] + i[2]) * 100, 1)])
    except :
        pass

print(new)

# 외국인 비율이 3% 초과일 때만 출력하기

new_3pct = [['구', '한국인', '외국인', '외국인 비율(%)']]
for i in newPop:
    foreign = 0
    try:
        foreign = round(i[2] / (i[1] + i[2]) * 100, 1)
        if foreign > 3 :
            new_3pct.append([i[0], i[1], i[2], foreign])
    except :
        pass

print(new_3pct)
usecsv.writecsv('newPop.csv', new_3pct)