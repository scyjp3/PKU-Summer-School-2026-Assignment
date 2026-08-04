set1 = set()
set1.add('a')
set1.add('b')
set1.add('c')
set1.add('d')
set1.add('e')
add_order = ['a', 'b', 'c', 'd', 'e']
print(f"添加元素的顺序: {add_order}")
print("添加后的集合:", set1)
print("元素的打印顺序可能与添加顺序不同\n")

pop_order = []
while set1:
    elem = set1.pop()
    pop_order.append(elem)
    print(f"  pop() 删除: {elem}")
print(f"删除元素的顺序: {pop_order}")
if {add_order == pop_order} == True:
    print("添加元素的顺序与删除元素的顺序相同")
else:
    print("添加元素的顺序与删除元素的顺序不同")