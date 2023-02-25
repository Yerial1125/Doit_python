import os, re

os.chdir(r'C:\workspace\Doit_python\03\data')

f = open('friends101.txt', 'r', encoding='utf8')
# 읽은 후 커서를 맨 앞으로 이동
f.seek(0)

# 객체 f 안의 모든 문장을 원소로 하는 리스트 형성
sentences = f.readlines()
print(sentences[:3])

# 대사만 출력
for i in sentences[:20]:
    if re.match(r'[A-Z][a-z]+:', i):
        print(i)

# 대사만 담긴 리스트 출력
lines = [i for i in sentences if re.match(r'[A-Z][a-z]+:', i)]
print(lines[:10])

# would가 들어간 문장만 추출
would = [i for i in sentences if re.match(r'[A-Z][a-z]+:', i) and re.search('would', i)]
print(would)

# 파일로 저장하기
newf = open('would.txt','w')
newf.writelines(would)

# take가 들어만 문장만 추출
take = [i for i in sentences if re.match(r'[A-Z][a-z]+:', i) and re.search('take', i)]
print(take)
for i in take:
    print(i)

newf2 = open('take.txt', 'w')
newf2.writelines(take)