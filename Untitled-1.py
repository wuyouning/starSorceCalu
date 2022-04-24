#! /usr/bin/python
# -*- coding: UTF-8 -*-

# 定义星级 5star 4star 3star 2star 1star分数
Star5Score = 5
Star4Score = 4
Star3Score = 3
Star2Score = 2
Star1Score = 1

# 输入星级条数
Star5Num = 588
Star4Num = 7    
Star3Num = 4 
Star2Num = 6 
Star1Num = 165 
# 计算总分
Star5SumScore = Star5Num * Star5Score
Star4SumScore = Star4Num * Star4Score
Star3SumScore = Star3Num * Star3Score
Star2SumScore = Star2Num * Star2Score
Star1SumScore = Star1Num * Star1Score

# 计算星星总分
StarNum = sum([Star5Num,Star4Num,Star3Num,Star2Num,Star1Num])
starSumSore = sum([Star1SumScore,Star2SumScore,Star3SumScore,Star4SumScore,Star5SumScore])
fullSumsore = StarNum * 5
starLevel = starSumSore / fullSumsore * 5
print (starLevel)

# 计算需要的五星数量
wantStarLevel = input

