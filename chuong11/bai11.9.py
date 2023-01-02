def party_late(customer,name):
    s=[]
    d=len(customer)
    for ch in customer:
        x=[ch]
        s+=x
        if(str(ch)==name[0])and(len(s)>((d//2)+1)):
            t=[True]
            break
        else:
            t=[False]
            return print(t[0])
L=['dung','phuong','hoang','vinh','tung','nguyet','an']
name=['dung']
party_late(L,name)