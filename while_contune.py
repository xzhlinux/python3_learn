#!/usr/bin/python
#-*- coding: UTF-8 -*-
#
# age_1 = 26
# age_2 = int(input("请输入您的年龄>>:"))
#
# if age_2 == age_1:
#     print("您获得来一辆兰博基尼!")
# elif age_2 < age_2:
#     print("您输入的号码有误!")
# else :
#     print("你真够笨的!")
#
#
#打印50不打印，第60-90打印对应值的平方
# count = 0
# while count <= 100 :
#     if count == 50 :
#         pass
#
#     elif count >= 60 and count <= 80 :
#         print(count * count)
#     else :
#         print('loop',count)
#
#     count += 1
#
# print("---------- loop is ended ----------")


# count = 0
# while True  :
#     print ("你猜猜",count)
#     count += 1

# count = 0
# while count <= 100 :
#         print("loop",count)
#         if count == 5 :
#             continue
#         count += 1
#
# print("-------- out of while loop ----------")

count = 0
while count <= 100 :
    count += 1
    if count >5 and count < 95 :
        break
    print("loop",count)

print("-------- out of loop----------")
