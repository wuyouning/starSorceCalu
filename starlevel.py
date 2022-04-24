#! /usr/bin/python
# -*- coding: UTF-8 -*-
from lib2to3.pytree import NegatedPattern
import math
from random import choice
from re import I, X 
import numpy as np

# 请求输入
def inputStarNum(a):
    print("输入",a,"条数")
    astarnum = int(input())
    return(astarnum)

# 计算星星现有总分
def HowStarSore ():
    StarSumNum = sum(starNum)
    starSumSore = sum(starSore)
    fullSumsore = StarSumNum * 5
    starLevelnow = starSumSore / fullSumsore * 5
    print ("现有评分:",float('{:.1f}'.format(starLevelnow)))
    return (starLevelnow)

#计算想要增加的条数
def HowStarNum (choocestarLevel,wantStarLevel):
    #去除需要增加星星条数的数目组
    starNum2 = [i for i in starNum if i != starNum[choocestarLevel]]
    wantStarLevelR = sum(starNum2) * wantStarLevel
    #去除需要增加星星条数的分数组
    # 权计算
    Star5ScoreQ = Star4Score / 5 * Star5Num
    Star4ScoreQ = Star4Score / 5 * Star4Num
    Star3ScoreQ = Star3Score / 5 * Star3Num
    Star2ScoreQ = Star2Score / 5 * Star2Num
    Star1ScoreQ = Star1Score / 5 * Star1Num
    starSoreQ = [Star1ScoreQ,Star2ScoreQ,Star3ScoreQ,Star4ScoreQ,Star5ScoreQ]
    #去除需要增加星星条数的权
    starSoreQ = sum([i for i in starSoreQ if i != starSoreQ[choocestarLevel]])
    wantStarlevelP = wantStarLevel / 5
    wantStarlevelP2 = 1 - wantStarlevelP
    Star5NumPre = wantStarLevelR / 5 - starSoreQ
    choiceStarNum = Star5NumPre / wantStarlevelP2
    print("所需条数",math.ceil(choiceStarNum))
    return(math.ceil(choiceStarNum))

    #星星列表
def listStar(starLevelnow):
    # 控制范围
    starlist = np.arange(1, 5, .1)
    # 筛选 不拿小于现有分数的值和5，5 可能会有运算冲突
    newStarList = [i for i in starlist if i >= starLevelnow]
    # 取小数点
    newStarList = [float('{:.1f}'.format(i)) for i in newStarList]
    print("评星表",newStarList)
    return(newStarList)
    # 单独取值进入运算
#列出所有星级需要的条数
def allStarNum(starlist):
    #循环执行
    allStarNumlist = []
    for wantStarLevel in starlist:
        choiceStarNum = HowStarNum(4,wantStarLevel)
        print(wantStarLevel)
        allStarNumlist.append(choiceStarNum)
    pass
    print("数目表",allStarNumlist)
    return(allStarNumlist)

# 对比表
def addStarNum(choocestarLevel,allStarNumlist):
    #循环执行
    addStarNumlist = []
    choocestarLevelNum = starNum[choocestarLevel]
    for aStarNum in allStarNumlist:
        addStarNum = math.ceil(aStarNum - choocestarLevelNum)
        addStarNumlist.append(addStarNum)
    pass
    print("需要增加的条目表",addStarNumlist)

# 定义星级 5star 4star 3star 2star 1star分数
Star5Score = 5
Star4Score = 4
Star3Score = 3
Star2Score = 2
Star1Score = 1

# 输入星级条数
Star5Num = inputStarNum("五星")
Star4Num = inputStarNum("四星")    
Star3Num = inputStarNum("三星") 
Star2Num = inputStarNum("二星") 
Star1Num = inputStarNum("一星") 
# 计算总分
Star5SumScore = Star5Num * Star5Score
Star4SumScore = Star4Num * Star4Score
Star3SumScore = Star3Num * Star3Score
Star2SumScore = Star2Num * Star2Score
Star1SumScore = Star1Num * Star1Score

#数列整理
starNum = [Star1Num,Star2Num,Star3Num,Star4Num,Star5Num]
starSore = [Star1SumScore,Star2SumScore,Star3SumScore,Star4SumScore,Star5SumScore]
starLevel = 5

#主程
starLevelnow = HowStarSore()
choocestarLevel = int(input("输入你想要计算条数的星级")) - 1
wantStarLevel = float(input("输入你想要得到的分数，不超过5"))
HowStarNum(choocestarLevel,wantStarLevel)
StarList = listStar(starLevelnow)
allStarNumlist = allStarNum(StarList)
addStarNum(choocestarLevel,allStarNumlist)