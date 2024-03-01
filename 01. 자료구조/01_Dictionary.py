# dictionary �ǽ�
# �⺻ �ڷᱸ�� �� 1��
# dictionary �� �߰�ȣ('{}')�� �̿��Ͽ� �ʱ�ȭ �Ѵ�.

edu = {'�����':5,'�����':6}
# Dictionay�� ���� ����

edu['�����']

print(f"�̼� �ð� : {edu['�����']}")

edu['������'] = 3
# dictionary['key'] ������(=) value(3)
# value ���� : ���ο� Ű ���� ���ȣ �ȿ� �Է��ϰ� �Ҵ� �����ڸ� �̿��Ͽ� �����Ѵ�.

edu['������']

edu

edu['������'] = 5
# value ������Ʈ ��� -> ���� �ۼ�

edu

# value �� �ٸ� ������ ������Ʈ �ϴ� ��� :
# edu['�����']= edu['�����']+3
# edu['�����'] += 3
edu['�����'] += 3

edu

# dictionary �Լ� pop(), popitem()
# -> dictionary.pop('key')
# -> dictionary.popitem()
# pop() : ��ȣ�ȿ� ����(argument)�� �־��־�� �Ѵ�.
# popitem() : dictionary���� ������ key:value ���� delet�ȴ�.(��ȣ�� ����� �۵��Ѵ�.)

edu.pop('������')

edu

edu.popitem()

edu

# dictionary �� ��ġ�� ���
# dictionary + dictionary

new = {'������':33,'���θ�':22}
edu.update(new)
# dic.update(dic) : edu(dictionary)�� new(dictionary)�� �߰��� ��ɾ�

edu

new = {'�����':66, '���θ�':21, '������':23, '�����':55}
# new(dictionary) �缱��

new

edu

edu.update(new)
# ������ update�� dictionary�� key�� �ߺ��Ǿ� �ִٸ� overwriting �ȴ�.
# ������ dictionary�� ������ �ٸ� ��� update �ϴ� ������ �ٲ��� �ʰ� value �� update�ȴ�.

edu

# dictionary ���� for�ݺ���(loop) Ȱ���ϴ� ���
# forloop ���� dictionary ���� key, value �� �����ϰų� �����ϴ� ���

# for�������� �ݺ��� ���� edu(dic)���� key�� ���� �ݺ� �ϴ� ��ɾ�.
for key in edu:
  print(key)
  # key�� ������� ��µȴ�.

# items �޼��� ���
for key,val in edu.items():
  print(key, val)
# items �޼���� key, value ��� ��µȴ�.

# edu(dictionary)�� ����� value ���� += ���� ����
for key, val in edu.items():
  edu[key] = val + 200
  # ��� ���� -> edu[key] += 2
  # edu[] ��ȣ �ȿ� key���� �����ϸ� �ش� key���� ���� �ȴ�.

edu

# dictionary �����ϴ� ���

edu['�����'] = 1000
edu['������'] = 2000
edu

# key�� �������� ���� : sorted �޼��� ���(��������)
sorted_edu = sorted(edu.items())
sorted_edu
# key�� �������� �ѱ�:�����ټ�, ����:a-z, ����:������->ū��

# key�� �������� ���� : sorted �޼��� ���(��������) : key �� reverse �ɼ��� �߰��Ѵ�.
sorted_edu = sorted(edu.items(), key = lambda item: item[0], reverse=True)
sorted_edu
# key�� �������� ����(reverse)

# edu.item() : item �޼��� ���
# key = lambda item: item[0]  : (lambda ; �Լ� ��� ǥ��) ���� �� ������ ���ϴ� ���� => ���������� 0�� ° ���� key�� �������� �Ѵ�.
# -> edu(dic-)�� ���Ұ� itme �̶�� �� �� item�� 0��° ���� �������� ���� �Ѵ�.
#   -> items �޼��带 ����� ��, �Լ��� �Է��ϴ� '����(argument)' ������ ���� ��µǴ� ���� �޶�����.
# reverse=True : �������� �����Ͽ� �����Ѵ�.
sorted_edu = sorted(edu.items(), key = lambda item: item[1], reverse=True)
sorted_edu
# item �޼����� 1��° ���� value�� �������� ���� �Ѵ�.

