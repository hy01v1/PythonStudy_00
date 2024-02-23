#!/usr/local/bin/python
import os, sys



#https://www.edwith.org/basic-python/lecture/123694?isDesc=false
#강의용
#주석 => "#" 

# 표준출력 함수 : print(), ('')
# 한줄 연결 출력 : print('aa', end='as')


print('Hello World')
print('Hello')
print('Hellow', end=' World!!')
print('Hellow','World!!')
print('Hellow'+'World!!')
''
# 입력 함수 : input("메세지")
#x = input()
x = input('x 입력 :')
y = input('y 입력 :')
print('결과값 : ',x,'+',y,'=',x+y)

# 입력 -> 섭씨온도 (실수)
#정수입력 int
#실수입력 float
C = float(input("섭씨온도 입력 => "))
#화씨온도  변환
F = (C * (9/5)) + 32

print("결과) 섭씨온도 : ", C, "화씨온도 : ", F)

