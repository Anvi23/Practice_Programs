lst1=[1,2,4,4]
lst2=[1,2,3,9]

for val in lst1:
    for i in range(len(lst2)):
            total=val+lst2[i]
if total==8:
    print('True')
else:
    print('False')

print

for i in range(len(lst1)):
    if lst1[i] + lst1[len(lst1)-1] < 8:
        print('False')
    else:
        print('True')
