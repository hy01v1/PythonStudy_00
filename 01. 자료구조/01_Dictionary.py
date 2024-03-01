# dictionary 실습
# 기본 자료구조 중 1개
# dictionary 는 중괄호('{}')를 이용하여 초기화 한다.

edu = {'손흥민':5,'김민재':6}
# Dictionay에 값을 저장

edu['손흥민']

print(f"이수 시간 : {edu['손흥민']}")

edu['김진수'] = 3
# dictionary['key'] 연산자(=) value(3)
# value 변경 : 새로운 키 값을 대괄호 안에 입력하고 할당 연산자를 이용하여 수정한다.

edu['김진수']

edu

edu['김진수'] = 5
# value 업데이트 방법 -> 새로 작성

edu

# value 만 다른 값으로 업데이트 하는 방법 :
# edu['김민재']= edu['김민재']+3
# edu['김민재'] += 3
edu['김민재'] += 3

edu

# dictionary 함수 pop(), popitem()
# -> dictionary.pop('key')
# -> dictionary.popitem()
# pop() : 괄호안에 인자(argument)를 넣어주어야 한다.
# popitem() : dictionary에서 오른쪽 key:value 부터 delet된다.(괄호를 비워야 작동한다.)

edu.pop('김진수')

edu

edu.popitem()

edu

# dictionary 를 합치는 방법
# dictionary + dictionary

new = {'차범근':33,'차두리':22}
edu.update(new)
# dic.update(dic) : edu(dictionary)에 new(dictionary)를 추가한 명령어

edu

new = {'김범수':66, '차두리':21, '차범근':23, '손흥민':55}
# new(dictionary) 재선언

new

edu

edu.update(new)
# 기존에 update된 dictionary의 key가 중복되어 있다면 overwriting 된다.
# 각각의 dictionary의 순서가 다른 경우 update 하는 순서로 바뀌지 않고 value 만 update된다.

edu

# dictionary 에서 for반복문(loop) 활용하는 방법
# forloop 에서 dictionary 안의 key, value 를 변경하거나 연산하는 방법

# for구문으로 반복문 시작 edu(dic)안의 key에 대해 반복 하는 명령어.
for key in edu:
  print(key)
  # key가 순서대로 출력된다.

# items 메서드 사용
for key,val in edu.items():
  print(key, val)
# items 메서드는 key, value 모두 출력된다.

# edu(dictionary)에 저장된 value 값에 += 연산 적용
for key, val in edu.items():
  edu[key] = val + 200
  # 축약 가능 -> edu[key] += 2
  # edu[] 괄호 안에 key값을 지정하면 해당 key에만 적용 된다.

edu

# dictionary 정렬하는 방법

edu['손흥민'] = 1000
edu['차범근'] = 2000
edu

# key를 기준으로 정렬 : sorted 메서드 사용(오름차순)
sorted_edu = sorted(edu.items())
sorted_edu
# key를 기준으로 한글:가나다순, 영어:a-z, 숫자:작은수->큰수

# key를 기준으로 정렬 : sorted 메서드 사용(내림차순) : key 에 reverse 옵션을 추가한다.
sorted_edu = sorted(edu.items(), key = lambda item: item[0], reverse=True)
sorted_edu
# key를 기준으로 역순(reverse)

# edu.item() : item 메서드 사용
# key = lambda item: item[0]  : (lambda ; 함수 축약 표현) 정렬 할 기준을 정하는 인자 => 예문에서는 0번 째 값인 key를 기준으로 한다.
# -> edu(dic-)의 원소가 itme 이라고 할 때 item의 0번째 값을 기준으로 정렬 한다.
#   -> items 메서드를 사용할 때, 함수에 입력하는 '인자(argument)' 순서에 따라 출력되는 값이 달라진다.
# reverse=True : 논리적으로 반전하여 적용한다.
sorted_edu = sorted(edu.items(), key = lambda item: item[1], reverse=True)
sorted_edu
# item 메서드의 1번째 값인 value를 기준으로 정렬 한다.

