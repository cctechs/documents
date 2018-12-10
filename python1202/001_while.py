#!/usr/bin/python3
#encoding=utf-8

print("\n=======99乘法表while==========")
i = 1
while i < 10:
    j = 1
    while j<=i:
        print("%d*%d=%d"%(i,j,i*j)),
        j = j + 1
    print
    i = i + 1
