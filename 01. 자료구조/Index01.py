#!/usr/local/bin/python
# coding: ansi
import os, sys

# 함수 = 인자를 받아 ouyput 해주는 것

a = 100
b = 40

c = a + b
print(c)

# 축약 표현 : a = a + b 로 업데이트
a = a + b
print(a)
print(c)

a /= b  #a를 b로 나눈 값으로 업데이트 = 변수 업데이트 용도로 사용한다.
#사칙연산 사용 가능
print(a)

f = 'programmers'
# a에 문자열 저장 가능 ", ' 쌍따옴표 사용 불가(코드 문제로 인코딩 따로 해주어야 함)
print(f)
# 리스트 도 변수에 저장 가능
l = ['기획팀', '개발팀', '사업팀']
print(l)

name = l[0] #  리스트 인덱싱 첫번째
print(name)
name = l[1] #  리스트 인덱싱 두번째
print(name)
name = l[2] #  리스트 인덱싱 세번째
print(name)

# 합쳐서 출력 가능
file_name  = f'{name}' + '_탬플릿.xlsx'
# f를 입력하고 {변수명}으로 작성하면 => 문자열 안에 다른 변수 입력 가능
print(file_name)
print(name + file_name)
z = f'{name} is hell!!'
print(z)
name = l[1]
z = f'{name}, '
z += f'{name} is hell!!!!!'
print(z)




