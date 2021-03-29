# '''파이썬 300제 101~120'''
# print(3==5)
# print(3<5)
# x=4
# print(1<x<5)
# # print(3 => 4) #지원하지 않는 연산자
# if 4< 3:
#     print("Hello World")
# else:
#     print("Hi,there.")

# if True :
#     print("1")
#     print("2")
# else : 
#     print("3")
# print("4")

# if True :
#     if False:
#         print("1")
#         print("2")
#     else:
#         print("3")
# else :
#     print("4")
# print("5")
# user = input("입력:")
# print(user * 2)
# number = input("숫자를 입력하세요:")
# print(10 +int(user))
# user = input("")
# if int(user)%2 == 0:
#     print("짝수")
# else:
#     print("홀수")
# user = input("입력값:")
# num = 20 + int(user)
# if num > 255:
#     print(255)
# else:
#     print(num)

# user = input("입력값:")
# num= int()
# 조건문
money = 20000 # 비교 연산자를 통한 조건문
if money >= 3000:
    print('차를 사지말고 저축을 해라.')
    print('저축해서 집을 사라')
else:
    print("버스를 좋아해라")

money = 2000
house = False
if money >= 30000 or house: #둘 중 하나라도 참이면 참
    print("차를 사도 된다")
else:
    print("걸어다녀도 된다")

life = ['family','work',]
if 'money' in life:
    pass # 아무것도 하지 않는다
else:
    print("카드를 꺼내라")

if 'money' in life:
    pass
else:
    print("최선을 다해라")
print('='*80)


# 구구단
'''
2 x 1 = 2
2 x 2 = 4
.........
2 x 9 = 18
'''
# dan = 2
# for i in range(1,10):
#     print(f"{dan} x {i} = {dan * i}")
# print('='*80)
# while True:
#     dan = int(input('몇 단?')) #'1' '2' (o)/ 'q'(x)
#     # if dan == 'q' or dan =='Q': # in
#     # if dan in['Q','q']:
#     #     break
#     # for i in range(1,10):
#     #     print(f"{dan} x {i} = {dan * i}")
    
 
    # 리스트 내포
a = [1,2,3,4]
result = [num * 10 for num in a]
print(result)

result =  [x*y for x in range(2,10) 
for y in range(1,10)]
print(result)
print('='*80)   
# 튜플 자료형
t1 = (1)
t2 = (1,)

print(t1, type(t1))
print(t1, type(t2))

t1 = (1,2,'a','b')
# del t1[0]         #튜플은 값 삭제 불가능
# t1[0] = 100       #튜플은 값 수정 불가능
print(t1)

# 튜플의 인덱싱
t1 = (1,2,'a','b')
print(t1[0])
print(t1[1])
print(t1[-1])
print(t1[-2])

# 튜플의 슬라이싱
t1 = (1,2,'a','b')
print(t1[1:3])
print(t1[:3])
print(t1[3:])
print(t1[:])

# 튜플 덧셈
t1 = (1,2,'a','b')
t2 = (3,4)
print(t1 + t2)

# 튜플 곱하기 숫자
t2 = (3,4)
print(t2 * 3)

# 튜플 길이 구하기
print(len(t1))
print('='*80)
#딕셔너리 자료형
dic = {'name':'pey', 'phone':'0119993323', 'birth': '1118'}
print(dic)
dic['gender'] = 'Male'
print(dic)
dic['face' ] = 'good' #딕셔너리 쌍 추가
print(dic)
del dic['phone'] # 딕셔너리 쌍 삭제
print(dic['name'])
# print(dic['weight']) # 없는 키 접근시 오류 방생
print(dic.get('weight')) #없는 키 접근시 기본값 설정 가능
print(dic.get('weight', '??'))

# key 또는 value 리스트 만들기
dic = {'name':'pey', 'phone':'0119993323', 'birth': '1118'}
print(dic.keys())
print(dic.values())
print(dic.items())

for i in dic.keys():
    print(i)

for i in dic.items():
    print(i[1]) #peym 0119993323,1128만 나오게 출력

# 딕셔너리 요소 모두 지우기
dic = {'name':'pey', 'phone':'0119993323', 'birth': '1118'}
dic.clear()
print(dic)
# 해당 key 가 딕셔너리 안에 있는지 조사하기
dic = {'name':'pey', 'phone':'0119993323', 'birth': '1128'}
print('name' in dic) # name 키가 존재하므로 True
print('pey' in dic)  # value는 조사 대상이 아니므로 False
print('gender' in dic) #gender 키가 없으므로 False


# 집합 자료형
s1 = set([1,2,3])
print(s1)

s1 = set([1,2,3,1,2,3])  #중복감 없음
print(s1)

s1 = set('Hello') # 순서를 보장하지 않음
print(s1)

a = ['a','b','c','a','b','c']
print(a)

#리스트 중복 제거용으로 활용 가능
print(set(a))
print(list(set(a)))

print('='* 80)

# 교집합
s1 = set([1,2,3,4,5,6])
s2 = set([4,5,6,7,8,9])
print(s1 & s2)
print(s2 & s1)
print(s1.intersection(s2))

# 합집합
print(s1 | s2)
print(s1 | s1)
print(s1.union(s2) )

# 차집합
print(s1 - s2)
print(s2 - s1)
print(s1.difference(s2))

s1 = set([1,2,3])
s1.add(4) # 값 1개 추가
print(s1)

s1.update([4,5,6,7]) # 값 여러개 추가, 업데이트할 때는 리스트함수로
print(s1)

s1= set([1,2,3])
s1.remove(2) # 값 제거
print(s1)

# 불 자료형
print(bool('python'))
print(bool(''))
print(bool(' '))
print(bool([1,2]))
print(bool([]))

print('='* 80)
print(bool(1))
print(bool(0)) #0만 False
print(bool(-1))
print(bool(1.232))
print(bool(None))
print(bool("0"))