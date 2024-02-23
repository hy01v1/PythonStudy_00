#!/usr/local/bin/python
# coding: ansi
import os, sys




# 데이터를 저장하는 구조를 : 자료구조 라고 한다.
# list : 여러 객체를 한 묶음으로 관리할 때 사용
# list indexing : list안의 원소들에 접급하는 방식
# index 는 0부터 선언된다.
# teams[0] : teams list의 첫 번째 원소
# teams[-1] : teams list의 마지막 원소
# append : 리스트 마지막에 새로운 원소를 추가한다.

teams = ['1번팀','2번팀','3번팀','4번팀']
teams.append('마지막팀')
print(teams)

# list 안에 다른 자료구조를 삽입 할 수 있다.
# list in dictionaries
budget = [  {'판촉비' : 50, '소모품비' : 12},
                    {'소모품비' : 30, '외주용역비' : 30},
                    {'교육훈련비' : 40, '지급수수료' : 23}]
# list in lists
# list in dataframes
print(budget)

    # 리스트 관련 다른 함수들
# insert : 리스트 특정 위치에 신규 원소를 추가한다.
# pop : 리스트 마지막 원소를 제거하면서 return 한다.
# extend : 리스트와 리스트를 붙이는 함수

zzz = ['1', '2', '3']
print(len(zzz))
# list 길이 출력 함수

# 리스트에 원소 추가하기
zzz.append('4')
print(zzz)
print(len(zzz))


print(zzz[1:3])
# 0은 불포함 원소 3개 포함하여 표시 (0은 제외)
zzz.append('5')
print(len(zzz))
print(zzz)
print(zzz[2:4])
# 0,1은 불포함 원소 4개 포함하여 표시 (0은 제외)
# [x:y] : x까지 불포함, y갯수만큼 0에서 계산하여 표시
# : x <= y 를 선언

red_a =       ['r1', 'r2', 'r3']
black_b =   ['b1', 'b2', 'b3']
green_g =  ['g1', 'g2', 'g3']
c_num =     [1, 2, 3, 4]
color = [red_a, black_b, green_g, c_num]
print(len(color))
print(color)
# list 안에 list 입력