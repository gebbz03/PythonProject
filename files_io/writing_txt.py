#write text in file
'''
w = write
a = append
r = read/default
OR
wt = write
at = append
rt = read
t is for text mode
'''

with open('number.txt','w') as fobj:
    fobj.write('1')
    fobj.write('\n')
    fobj.write('23435345')