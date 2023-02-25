f = open('a.txt', 'w')
f.write('abc')
f.close()

f = open('a.txt', 'w')
f.write('나는 오늘 학교에 갔다')
f.close()

f = open('a.txt','r')
diary = f.read()
print(diary[:5])

f = open('a.txt','a')
f.write('학교에 가지 않을 날이 올까?')
f.close()

f = open('a.txt','r')
print(f.read())

f = open('abcde.txt','w')
f.write('I went to school today.')

with open('test.txt','w') as f :
    f.write('오늘 나는 학교에 갔습니다.')