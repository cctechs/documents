#!/usr/bin/python3
#encoding=utf-8

if __name__ == "__main__": #程序入口 
    b = True  #定义一个bool变量，
    a = 30    #定义一个整形变量
    if a > 30:   #如果a 大于 30，那么b=True, 否则 b = False
        b = True
    else:
        b = False

    #print函数的作用就是打印
    print(b)  #打印b的值   输出为 False
    print(int(True))   #输出为1
    print(int(False))  #输出为0

    print(float(True))
    print(float(False))