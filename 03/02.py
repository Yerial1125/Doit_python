import re

example = '이동민 교수님은 다음과 같이 설명했습니다(이동민, 2019). 그런데 다른 교수님은 이 문제에 대해서 다른 견해를 가지고 있었습니다.' \
          '(최재영, 2019). 또 다른 경해도 있었습니다(Lion, 2018)'

result = re.findall(r'\([A-Za-z가-힣]+, \d+\)', example)
print(result)

# match 메서드
# match 메서드
# 패턴 앞에는 r을 붙여준다.
pattern = r'life'
script = 'life'
print(re.match(pattern, script))

# group매서드를 사용해 매치된 내용을 반환
print(re.match(pattern, script).group())
print(re.match(r'life', 'life').group())

# 매칭되는 것이 없을 때는 오류 메시지
# print(re.match(r'life', 'animal').group())

# 함수 정의
def refinder (pattern, script) :
    if re.match(pattern, script) :
        print('Match!')
    else:
        print('Not a match!')

pattern = r'Life'
script = 'Life is so cool'
refinder(pattern, script)

pattern = r'life'
script = 'Life is so cool'
refinder(pattern, script)

# Not a Match -> match : 문자열의 시작부터 매칭되는지 찾는 함수
pattern = r'is'
script = 'Life is so cool'
refinder(pattern, script)

# search 메서드
print(re.search(pattern, script).group())
print(re.search(r'Life', script).group())
print(re.search(r'cool', script).group())
# is
# Life
# cool

# findall 메서드 : 패턴을 모두 찾아 리스트로 반환하기
number = 'My number is 511223-1****** and your is 521012-2******'
print(re.findall('\d{6}', number))
# -> ['511223', '521012']

example1 = '저는 91년에 태어났습니다. 97년에는 IMF가 있었습니다. 지금은 2020년입니다.'
# 숫자(\d)로 시작하고, 어떤 문자든(.) 반복(+)되며, '년'으로 끝나는 문자열 반환
print(re.findall(r'\d.+년',example1))
# -> ['91년에 태어났습니다. 97년에는 IMF가 있었습니다. 지금은 2020년']

print(re.findall(r'\d.+?년',example1)) # ? -> '년'이라는 글자를 찾으면 패턴 찾기를 멈춤
print(re.findall(r'\d+년',example1)) # 숫자를 반복시킨 후 '년으로 끝나는 문자를 찾기
# -> ['91년', '97년', '2020년']

result = re.findall(r'\(.+\)', example) # \를 안 붙이면 문자로 인식X.
print(result)
# ->['(이동민, 2019). 그런데 다른 교수님은 이 문제에 대해서 다른 견해를 가지고 있었습니다.(최재영, 2019). 또 다른 경해도 있었습니다(Lion, 2018)']/

result = re.findall(r'\(.+?\)', example)
print(result)
# -> ['(이동민, 2019)', '(최재영, 2019)', '(Lion, 2018)']

# split메서드 : 문장 나누는 패턴 만들기

sentence = 'I have a lovely dog, really. I am not telling a lie. What a pretty dog! I love this dog.'
print(re.split(r'[.?!]', sentence))
# ['I have a lovely dog, really', ' I am not telling a lie', ' What a pretty dog', ' I love this dog', '']

data = 'a:3; b:4; c:5'

for i in re.split(r'; ',data) :
    print(re.split(r':', i))

# sub 메서드 : 문자열 바꾸기
print(re.sub(r'dog', 'cat',sentence))

words = 'I am home now. \n\n\nI am with my cat.\n\n'
print(words)
print(re.sub(r'\n', '', words))

# ly로 끝나는 문장 찾기
print(re.findall(r'\w+ly', sentence))
# -> ['lovely', 'really']