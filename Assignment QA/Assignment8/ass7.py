#Hectrogeneous Tuple
t=(12,11.33,"aman",111,3+4j,True,"anita",44,3.3,"itu",False)

#Creating List
t1,t2,t3,t4,t5=[],[],[],[],[]

for i in t:
    if type(i)==int:
        t1.append(i)

    elif type(i)==float:
        t2.append(i)
    
    elif type(i)==complex:
        t3.append(i)

    elif type(i)==str:
        t4.append(i)

    elif type(i)==bool:
        t5.append(i)


t1=tuple(t1)
t2=tuple(t2)
t3=tuple(t3)
t4=tuple(t4)
t5=tuple(t5)

print(t1,t2,t3,t4,t5,sep="\n")
