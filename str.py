#str="n"
'''print(id(str))
str1="n"
print(id(str1))
print(type(str))

#print(list)
#r=reversed(list)
#r=list[::-1]'''
'''list=["MONICA","nagarjuna","soubin","rajini","bokkodu"]
print(list)
list.append("upendra")
print(list)
list.insert(4,"sruthihasaan")
print(list)
list.append("amirkhan")
print(list)
list.remove("nagarjuna")
print(list)'''
list=[]
n=int(input("enter the sizee of list"))
for d in range(1,n+1):
    data=input("enter the data")
    list.append(data)
for i in list:
    print(i)