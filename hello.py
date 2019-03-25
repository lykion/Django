# -*- coding:utf-8 -*-

print('=============================')
print('这是一个Django项目')
print('=============================')

list = ['a', 'b', 'c', 'd', 'e']
print(list[4:])


def addlist(var, list=[]):
    list.append(var)
    return list


list1 = addlist(1)
list2 = addlist(123, [])
list3 = addlist('a')

print("list1 = %s" % list1)
print("list2 = %s " % list2)
print("list3 = %s " % list3)
