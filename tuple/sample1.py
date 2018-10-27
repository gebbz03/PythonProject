#TUPLE SYNTAX

tp=1,2,'Bill',4.4,False
print(tp,type(tp))

tp2=(1,2,'Bill',4.4,False)
print(tp2,type(tp2))

#NOT TUPLE
a,b=1,2
print(a)
s=('hi')
print(s,type(s))


#ACCESS TUPLE

tp3=1,2,'Bill',4.4,False
print(tp3[0],tp3[2],tp3[-1],sep='|')
