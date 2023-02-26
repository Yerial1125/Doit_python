import re, usecsv

English = 'She is a vegetarian. She does not eat meat. She thinks that animals should not be killed.' \
          'It is hard for her to hang out with people. Many people like to eat meat. She told his parents not to eat meat. ' \
          'They laughed at her. She realized they couldn\'t give up meat.'

Korean = '그녀는 채식주의자입니다. 그녀는 고기를 먹지 않는다. 그녀는 동물들이 죽어서는 안된다고 생각한다. ' \
         '그녀는 사람들과 어울리는 것이 힘들다. 많은 사람들이 고기 먹는 것을 좋아한다. 그녀는 그의 부모님에게 고기를 먹지 말라고 말했다. ' \
         '그들은 그녀를 비웃었다. 그녀는 그들이 고기를 포기할 수 없다는 것을 깨달았다.'

Korean_list = re.split('\.', Korean)
English_list = re.split('\.', English)

print(Korean_list)

total = []

for i in range(len(English_list)) :
    total.append([English_list[i], Korean_list[i]])

usecsv.writecsv('English_Korean.csv', total)