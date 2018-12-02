#!/usr/bin/python3
#encoding=utf-8

if __name__ == "__main__":
    totalday = 0
    for i in range(2000, 2018):
        if (i % 4 == 0 and i % 100 != 0) or (i % 400 == 0):  # 计算是不是闰年，闰年366天
            totalday = totalday + 366
        else:
            totalday = totalday + 365
    
    print(totalday)
    