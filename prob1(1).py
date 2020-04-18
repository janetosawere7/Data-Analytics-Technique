import re 

p = re.compile(r'^\s*((?:\+|\-)?(?:[1-9]\d*|0)(?:\.\d+|(?:\.\d+)?(?:E|e)(?:\+|\-)?\d+))\s*((?:\+|\-)?[1-9]\d*|0)\s*([x|y|z])\s*$')

f = open('data.txt')
sum_float = 0.0
sum_int = 0
st = ''
for line in f:
    m = p.search(line)
    if m:
        sum_float += float(m.group(1))
        sum_int += int(m.group(2))
        st += m.group(3)
        # print m.group()
    else:
        print( "No match with " + line, end=' ' ) 
f.close()
print( "\n", sum_float, sum_int, st )
