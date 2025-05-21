list1 = [101, 11, 12, 13, 40]
print("list1:", list1)

list2 = ['a', 'b', 'c']
print("list2:", list2)

list3 = [101, 'a', 'prop']
print("list3:", list3)


list4 = list1 + list2
print("list4 (list1 + list2):", list4)


list5 = [1, 2, 5, (101, 18, 'a', 'DSA')]
print("list5:", list5)


print("Slice of tuple in list5[3]:", list5[3][1:4])  

print("list5[:3]:", list5[:3])      
print("list5[3:]:", list5[3:])        
print("list5[-1]:", list5[-1])        
print("list5[-1][1:]:", list5[-1][1:])  
