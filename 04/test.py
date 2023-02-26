import usecsv

a = [['국어','영어','수학'],[99,88,77]]
usecsv.writecsv('test.csv', a)

a = [['물리','화학','생물'],[70, 99, 100]]
usecsv.writecsv('test.csv', a)