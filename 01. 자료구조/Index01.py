#!/usr/local/bin/python
# coding: ansi
import os, sys

# �Լ� = ���ڸ� �޾� ouyput ���ִ� ��

a = 100
b = 40

c = a + b
print(c)

# ��� ǥ�� : a = a + b �� ������Ʈ
a = a + b
print(a)
print(c)

a /= b  #a�� b�� ���� ������ ������Ʈ = ���� ������Ʈ �뵵�� ����Ѵ�.
#��Ģ���� ��� ����
print(a)

f = 'programmers'
# a�� ���ڿ� ���� ���� ", ' �ֵ���ǥ ��� �Ұ�(�ڵ� ������ ���ڵ� ���� ���־�� ��)
print(f)
# ����Ʈ �� ������ ���� ����
l = ['��ȹ��', '������', '�����']
print(l)

name = l[0] #  ����Ʈ �ε��� ù��°
print(name)
name = l[1] #  ����Ʈ �ε��� �ι�°
print(name)
name = l[2] #  ����Ʈ �ε��� ����°
print(name)

# ���ļ� ��� ����
file_name  = f'{name}' + '_���ø�.xlsx'
# f�� �Է��ϰ� {������}���� �ۼ��ϸ� => ���ڿ� �ȿ� �ٸ� ���� �Է� ����
print(file_name)
print(name + file_name)
z = f'{name} is hell!!'
print(z)
name = l[1]
z = f'{name}, '
z += f'{name} is hell!!!!!'
print(z)




