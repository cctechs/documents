#!/usr/bin/python3
#encoding=utf-8

#99乘法表 for
print("\n=======99乘法表for==========")
for i in range(1, 10):
    for j in range(1, i+1):
        print("%d*%d=%d"%(i,j,i*j)),
    print


