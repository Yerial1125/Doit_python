import re
import usecsv

total = usecsv.opencsv('data/popSeoul.csv')

for i in total[:5]:
    print(i)

# 1. 문자형을 실수형으로 변경
j = '1,468,146'
float(re.sub(',','',j))
print(float(re.sub(',','',j)))
print(type(float(re.sub(',','',j))))

# 인구 자료 예시
# 숫자 원소만 골라서 쉼표 제거하기
i = total[2]
print(i)

k = []
for j in i :
    if re.search('\d', j) :
        k.append(float(re.sub(',','',j)))
    else:
        k.append(j)

print(k)

# 2. 문자와 숫자가 섞인 원소 골라내기

p = ['123강남','151,767','11,093','27,394']
k = []
# for j in p :
#     if re.search('\d', j) :
#         k.append(float(re.sub(',','',j)))
#     else:
#         k.append(j)

# --> Traceback (most recent call last):
#   File "C:\workspace\Doit_python\04\03.py", line 34, in <module>
#     k.append(float(re.sub(',','',j)))
#              ^^^^^^^^^^^^^^^^^^^^^^^
# ValueError: could not convert string to float: '123강남'

for j in p :
    if re.search('[a-z가-힣]', j):
        k.append(j)
    else :
        k.append(float(re.sub(',','',j)))

print(k)

# 3. 특수문자와 숫자가 섞인 원소 골라내기

i = ['123!!','151,767','11,093','27,394']
l = []
# for j in i :
#     if re.search('[a-z가-힣]', j):
#         k.append(j)
#     else:
#         k.append(float(re.sub(',', '', j)))

# --> Traceback (most recent call last):
#   File "C:\workspace\Doit_python\04\03.py", line 58, in <module>
#     k.append(float(re.sub(',', '', j)))
#              ^^^^^^^^^^^^^^^^^^^^^^^^^
# ValueError: could not convert string to float: '123!!'

for j in i :
    if re.search('[a-z가-힣!]', j):
        l.append(j)
    else:
        l.append(float(re.sub(',', '', j)))
print(l)

for j in i :
    if re.search('[a-z가-힣!]', j):
        i[i.index(j)] = j
    else:
        i[i.index(j)] = float(re.sub(',', '', j))

print(i)

# 4. 예외 처리
i =  ['123!!','151,767','11,093','27,394','','!!!$%']
for j in i :
    try :
        i[i.index(j)] = float(re.sub(',', '', j))
    except :
        pass

print(i)


# 5. 예외처리로 숫자만 골라서 숫자형으로 바꾸기
i = total[1]
for j in i :
    try :
        i[i.index(j)] = float(re.sub(',', '', j))
    except :
        pass
print(i)

for i in total :
    for j in i :
        try :
            i[i.index(j)] = float(re.sub(',', '', j))
        except :
            pass
print(total)