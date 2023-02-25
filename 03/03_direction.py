import os, re

os.chdir(r'C:\workspace\Doit_python\03\data')

f = open('friends101.txt', 'r', encoding='utf8')
script101 = f.read()


r'\([A-Za-z].+?[a-z:\.]\)'
# .+ : 문자/숫자/빈칸 등이 자유롭게 반복
#  ? : 탐욕 제어
# [a-z:\.] : 마지막 글자로 영어 소문자 또는 마침표

dir = re.findall(r'\([A-Za-z].+?[a-z:\.]\)', script101)
print(dir)