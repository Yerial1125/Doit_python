import os, re

os.chdir(r'C:\workspace\Doit_python\03\data')

f = open('friends101.txt', 'r', encoding='utf8')
script101 = f.read()

char = re.compile(r'[A-Z][a-z]+:')
print(re.findall(char, script101))

# set 키워드로 중복된 원소 지우기
y = set(re.findall(char, script101))
print(y)

z = list(y)
character = []
for i in z :
    character += [i[:-1]]

print(character)

#  list 컴프리헨션 사용
character2 = [x[:-1] for x in list(set(re.findall(r'[A-Z][a-z]+:', script101)))]
print(character2)