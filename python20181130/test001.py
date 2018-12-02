#!/usr/bin/python3
# encoding=utf-8

if __name__ == "__main__":
    zhangsan = input("张三请输入 1:剪刀 2:石头 3:布\n")
    lisi = input("李四请输入 1:剪刀 2:石头 3:布\n")

    # 1 剪刀
    # 2 石头
    # 3 布

    if zhangsan == 1:  # 张三  剪刀
        if lisi == 1:
            print("一样")
        elif lisi == 2:  # 李四 石头
            print("李四赢")
        elif lisi == 3:  # 李四 布
            print("张三赢")
        else:
            print("输入错误")

    elif zhangsan == 2:  # 张三  石头
        if lisi == 1: #李四 剪刀
            print("张三赢")
        elif lisi == 2: 
            print("一样")
        elif lisi == 3:  # 李四 布
            print("李四赢")
        else:
            print("输入错误")
    elif zhangsan == 3:  # 张三 布
        if lisi == 1: #李四剪刀
            print("李四赢")
        elif lisi == 2:  # 李四 石头
            print("张三赢")
        elif lisi == 3:  # 李四 布
            print("一样")
        else:
            print("输入错误")
    else:
        print("输入错误")
