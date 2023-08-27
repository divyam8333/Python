t1=(22,12,34,36,16)
t2=(34,3,45,66,22)

#Sorting
res1=sorted(t1)
res2=sorted(t2)

#TypeCasting
res1=tuple(res1)
res2=tuple(res2)


print(res1)
print(res2)

res3=res1+res2

res4=sorted(res3)
res4=tuple(res4)
print(res4)