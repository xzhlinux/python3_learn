#!/usr/bin/python
#-*- coding: UTF-8 -*-
count = 0
age_1 = int(27)

while count < 3 :
    input_1 = int(input("请输入您的猜测的数字:"))
    if input_1 == age_1 :
        print("～_～恭喜您答对了！")
        break
    else :
        print("回答错误，请重新回答，您已使用了",1+count,"您还有", 2 - count, "次机会！")

    count += 1

    if count == 3 :
        choice = input("你个大傻逼还没猜对，是不是想继续？(Y/N)")
        if choice == 'y' or choice == 'Y' :
            count = 0
#count = 0 清空while循环对countd的纪录0