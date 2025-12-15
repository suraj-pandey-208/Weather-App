d={'a':1, 'b':2, 'c':4}
max1=0
max2=0
for i in d:
    if d[i]>max1:
        max2=max1
        max1=d[i]
    
    elif d[i]>max2:
        max2=d[i]





print("max1 is ",max1)
print("max2 is ",max2)


    #Question--2  # wapp to check whether dictionary contains unique key &values

dic={1:'a',2:'b',3:'c',4:'a'}
dic1=dict()
flag=False
for i in in dic:

if dic[i] in dict:
        flag=True
        break

    else:
        dic1[dic[i]]=1

    if flag==alse:
        print("dictionary contains unique alues")
    else:
        print("dictionary contain dupli cate values")