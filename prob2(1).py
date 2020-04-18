import re

f = open('data1.txt', 'r')
p = re.compile(r'\d+')
sm = 0
for line in f:
	sm += sum(map(int, p.findall(line)))
f.close()
print( sm )