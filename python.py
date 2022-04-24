#! /usr/bin/python
# -*- coding: UTF-8 -*-
def a():
    def b():
        print('我是b函数的')
    return(b)
S=a()
S()

a = 1
print(a)
def two():
    global a
    a = 2
    print(a)
two()
b = a
print(b)

list2=["a","b","c"]

def P2(*s1):

    for v in s1:

        print("<"+str(v)+">")

    pass

P2(*list2)