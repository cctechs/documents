#!/usr/bin/python3
# encoding=utf-8

if __name__ == "__main__":
    d = input("请输入距离:\n")

    if d < 0:
        print "输入错误"
    else:
        totalMoney = 0
        if d >= 1 and d <= 100:
            totalMoney = d * 5
        elif d > 100 and d <= 1000:
            totalMoney = d * 3
        else:
            totalMoney = d
        print(d, totalMoney)
