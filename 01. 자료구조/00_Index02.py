

 
# 따옴표 앞에 f를 입력하면, [변수명] 문자열 안에 다른 변수를 넣을 수 있다.

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

# 2. 자료구조 - dictionary
# key 로 값을 찾고 싶은 경우 주로 사용한다.
# key-value 쌍으로 이루어진 자료구조이다.
members = {
    '기획팀' : ['손흥민', '김민재'],
    '사업팀' : ['박지성', '이천수'],
    '개발팀' : ['안정환', '차두리']
    }
print(members['개발팀'])

# item(인자)을 추가하는 경우 함수명(ex. members)에 ['총무팀']=['김승규'] 로 key-velue 를 입력해주면 된다.
members['총무팀'] = ['김승규']
print(members)

# dictionary 관련 함수 : pop, popitem
# pop : velue를 return 하여 key-velue 쌍을 제거한다. 1개 이상의 argument(인자)를 입력해야 한다.
# aa.pop('인자')
# popitem : key-velue 쌍을 return 하여 제거한다. 가장 오른쪽의 인자를 제거한다. 인자를 입력하면 애러발생한다.
# aa.popitem()

# 3. 자료구조 - set
# set : 고유한 원소들의 묶음이다. 집합!
# list 와 다르게 순서에 상관하지 않는다. -> print시 무작위로 출력된다.
# add : 집합에 원소를 추가한다.
# remove :  집합에서 원소를 제거한다. 제거하려는 원소가 집합에 없는 경우 애러를 발생한다.
# discard :  집합에서 원소를 제거한다. 애러가 발생하지 않는다.

ss = set(['A', 'B', 'C'])
print(ss)
# 출력이 렌덤하다.

ss.add('D')
print(ss)
# ss(set 자료구조)에서 'D'원소를 추가한 명령 예시

ss.remove('C')
print(ss)
# ss에서 'C'를 remove로 제거

#ss.remove('X') # : 이 명령어의 경우 애러가 표시된다.
ss.discard('V')
print(ss)
# set자료구조에 없는 인자인 'V'를 제거한 명령어 : 애러가 표시 되지 않는다.







