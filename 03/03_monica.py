import re, os

os.chdir(r'C:\workspace\Doit_python\03\data')

f = open('friends101.txt', 'r', encoding='utf8')
script101 = f.read()
print(script101[:100])

# 'Monica:' 다음 아무 문자나 반복되는 (.+) 패턴을 찾아 리스트로 반환
Line = re.findall(r'Monica:.+', script101)
print(Line[:3])

for item in Line[:3] :
    print(item)

f = open('monica.txt', 'w', encoding='utf8')

monica = ''
for i in Line :
    monica += i + '\n'
f.write(monica)

