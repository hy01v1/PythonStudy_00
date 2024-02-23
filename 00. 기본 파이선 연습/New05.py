#!/usr/local/bin/python
# coding: ansi
import os, sys




# 코멘트(주석)
print("hellow world") # 파이선 시작!

# 여기에 코드를 작성하세요.
kitkat = 190
oreos = 502
pringles = 292
twix = 135.9
cheetos = 485


# 다양한 과자 조합
print(kitkat + oreos * 2)
print(cheetos * 4)
print(pringles + oreos + twix)
print(pringles * 3 + oreos * 2)

# 새로운 함수 만들기
def hellow():
    print("hellow!")
    print("welcome to codeit!")

hellow()


# 레시피 입력하기
def cafe_mocha_recipe():
    print("1. 준비된 컵에 초코 소스를 넣는다.")
    print("2. 에스프레소를 추출하고 잔에 부어 준다.")
    print("3. 초코 소스와 커피를 잘 섞어 준다.")
    print("4. 거품기로 우유 거품을 내고, 잔에 부어 준다.")
    print("5. 생크림을 얹어 준다.")


# 테스트 코드
cafe_mocha_recipe()
cafe_mocha_recipe()

# 파라미터 학습
def hellow(name):
    print("hellow!")
    print(name)
    print("welcome to Codeit!")


hellow("Chris")
hellow("Michael")

# 여러개의 파라미터
def print_sum(a, b, c):
    print(a + b + c)

print_sum(7, 3, 2)
print_sum(3, 1, 2 )

# 숫자 곱하기 연습!
def multiply_three_numbers(n1, n2, n3):
    print(n1+n2+n3)
# 테스트 코드
multiply_three_numbers(50, 50, 5)
multiply_three_numbers(700, 50, 6)
multiply_three_numbers(-200, 70, 4)
multiply_three_numbers(-201, 71, 5)