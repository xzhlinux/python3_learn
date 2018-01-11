#!/usr/bin/python
#-*- coding: UTF-8 -*-



count = 0
age_1 = int(27)

while count <= 2:
    input_1 = int(input("请输入您的猜测的年龄:"))
    if input_1 == age_1 :
        print("恭喜您答对了！")
        break
    else :
        print("回答错误，请重新回答，您已使用了",1+count,"您还有", 2 - count, "次机会!")
    count += 1