#!/usr/local/bin/python
# coding: ansi
import os, sys




# �ڸ�Ʈ(�ּ�)
print("hellow world") # ���̼� ����!

# ���⿡ �ڵ带 �ۼ��ϼ���.
kitkat = 190
oreos = 502
pringles = 292
twix = 135.9
cheetos = 485


# �پ��� ���� ����
print(kitkat + oreos * 2)
print(cheetos * 4)
print(pringles + oreos + twix)
print(pringles * 3 + oreos * 2)

# ���ο� �Լ� �����
def hellow():
    print("hellow!")
    print("welcome to codeit!")

hellow()


# ������ �Է��ϱ�
def cafe_mocha_recipe():
    print("1. �غ�� �ſ� ���� �ҽ��� �ִ´�.")
    print("2. ���������Ҹ� �����ϰ� �ܿ� �ξ� �ش�.")
    print("3. ���� �ҽ��� Ŀ�Ǹ� �� ���� �ش�.")
    print("4. ��ǰ��� ���� ��ǰ�� ����, �ܿ� �ξ� �ش�.")
    print("5. ��ũ���� ��� �ش�.")


# �׽�Ʈ �ڵ�
cafe_mocha_recipe()
cafe_mocha_recipe()

# �Ķ���� �н�
def hellow(name):
    print("hellow!")
    print(name)
    print("welcome to Codeit!")


hellow("Chris")
hellow("Michael")

# �������� �Ķ����
def print_sum(a, b, c):
    print(a + b + c)

print_sum(7, 3, 2)
print_sum(3, 1, 2 )

# ���� ���ϱ� ����!
def multiply_three_numbers(n1, n2, n3):
    print(n1+n2+n3)
# �׽�Ʈ �ڵ�
multiply_three_numbers(50, 50, 5)
multiply_three_numbers(700, 50, 6)
multiply_three_numbers(-200, 70, 4)
multiply_three_numbers(-201, 71, 5)