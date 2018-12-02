#!/usr/bin/python3
#encoding=utf-8

if __name__ == "__main__":
    y = input("请输出年份:\n")
    if y < 0:
        print("年份输入错误")
    else:
        m = input("请输出月份:\n")
        if m <= 0 or m > 12:
            print("月份输入错误")
        else:
            v = m % 2
            if m %2 == 0: # 偶数月 2 4 6 8 10 12
                if m == 2: # 如果是2月，需要判断是否是闰年
                    if (y % 4 == 0 and y % 100 != 0) or (y%400==0): 
                        day = 29
                    else:
                        day = 28
                else:
                    day = 30
            else:
                day = 31
            
            print(day)

