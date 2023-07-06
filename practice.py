''' 
문자열 처리
url = "http://naver.com"
url = "http://daum.com"
url = "http://google.com"
url = "http://youtube.com"
pw = url.replace("http://", "")
print(pw)
pw = pw[:pw.find(".")] #index 사용 가능
print(pw)
pw = pw[:3] + str(len(pw)) + str(pw.count("e")) + "!"
print(pw)

print("{url}의 비밀번호는 {pw} 입니다." .format(url=url, pw=pw))
'''

''' 자료 구조
### 리스트
subway = [10, 20, 30]
print(subway)

subway = ["유재석", "조세호", "박명수"]
print(subway)

print(subway.index("조세호"))

subway.append("하하")
print(subway)

subway.insert(1, "정형돈")
print(subway)

# 지하철에 있는 사람을 한 명씩 뒤에서 꺼냄
print(subway.pop())
print(subway)

# print(subway.pop())
# print(subway)

# print(subway.pop())
# print(subway)

subway.append("유재석")
print(subway)

print(subway.count("유재석"))


num_list = [5, 2, 4, 3, 1]
num_list.sort()
print(num_list)

num_list.reverse()
print(num_list)

num_list.clear()
print(num_list)
num_list = [5, 2, 4, 3, 1]
mix_list = ["조세호", 20, True]
print(mix_list)

num_list.extend(mix_list)
print(num_list)

# TypeError: '<' not supported between instances of 'str' and 'int'
num_list.sort()
print(num_list)


### 사전
# cabinet = {3:"유재석", 100:"김태호"}
# print(cabinet[3])
# print(cabinet[100])

# print(cabinet.get(3))
# # print(cabinet[5]) # KeyError: 5
# print(cabinet.get(5))
# print(cabinet.get(5, "사용 가능")) # 사용 가능
# print("hi")

# print(3 in cabinet) # True
# print(5 in cabinet) # False

cabinet = {"A-3":"유재석", "B-100":"김태호"}
print(cabinet.get("A-3"))
print(cabinet.get("B-100"))

# 새 손님
print(cabinet)
cabinet["A-3"] = "김종국"
cabinet["C-20"] = "조세호"
print(cabinet)

# 간 손님
del cabinet["A-3"]
print(cabinet)

# key 들만 출력
print(cabinet.keys())

# value 들만 출력
print(cabinet.values())

# key, value 쌍으로 출력
print(cabinet.items())

# 목욕탕 폐점
cabinet.clear()
print(cabinet)


### 튜플(tuple) : 내용 변경 및 추가 불가능, 속도가 리스트 보다 빠름.
menu = ("돈까스", "치즈까스")

print(menu[0])
print(menu[1])
price = (1000, 2000)

shop = (menu, price)

print(shop)
print(shop[1][1])

# menu.add("생선까스") # AttributeError: 'tuple' object has no attribute 'add'

# name = "김종국"
# age = 20
# hobby = "코딩"
# print(name, age, hobby)

(name, age, hobby) = ("김종국", 20, "코딩")
print(menu, name, age, hobby)


### 세트(set) : 중복 안됨, 순서 없음
my_set = {1, 2, 3, 3, 3}

print(my_set)

java = {"유재석", "김태호", "양세형"}
python = set(["유재석", "박명수"]) # python = {"유재석", "박명수"}

# 교집합 (java 와 python 을 모두 할 수 있는 개발자)
print(java & python)
print(java.intersection(python))

# 합집합 (java 할 수 있거나 python 할 수 있는 개발자)   
print(java | python)
print(java.union(python)) 

# 차집합 (java 할 수 있지만 python 은 할 줄 모르는 개발자)
print(java - python)
print(java.difference(python))

# python 할 줄 아는 사람이 늘어남
python.add("김태호")
print(python)

# java 를 잊었어요
java.remove("김태호")
print(java)


### 자료구조의 변경
# 커피숍
menu = {"커피", "우유", "주스"}
print(menu, type(menu))  # <class 'set'>

menu = list(menu) # set -> list
print(menu, type(menu))

menu = tuple(menu) # list -> tuple
print(menu, type(menu))

menu = set(menu) # tuple -> set
print(menu, type(menu))


# 퀴즈 4
# 당신의 학교에서는 파이썬 코딩 대회를 주최합니다.
# 참석률을 높이기 위해 댓글 이벤트를 진행하기로 하였습니다.
# 댓글 작성자들 중에 추첨을 통해 1명은 치킨, 3명은 커피 쿠폰을 받게 됩니다.
# 추첨 프로그램을 작성하시오.

# 조건1 : 편의상 댓글은 20명이 작성하였고 아이디는 1~20 이라고 가정
# 조건2 : 댓글 내용과 상관 없이 무작위로 추첨하되 중복 불가
# 조건3 : random 모듈의 shuffle 과 sample 을 활용

#(출력 예제)
# -- 당첨자 발표 --
# 치킨 당첨자 : 1
# 커피 당첨자 : [2, 3, 4]
# -- 축하합니다 --

#(활용 예제)
# from random import *
# lst = [1, 2, 3, 4, 5]
# print(lst)
# shuffle(lst)
# print(lst)
# print(sample(lst, 1))

# from random import *

# lst = [1, 2, 3, 4, 5]
# print(lst)
# shuffle(lst)
# print(lst)
# print(sample(lst, 1))

from random import *

users = range(1, 21) # 1부터 20까지 숫자를 생성
users = list(users)
#print(lst)

shuffle(users)
#print(lst)

winner = sample(users, 4) # 4명 중에서 1명은 치킨, 3명은 커피
print(winner)

print("-- 당첨자 발표 --")
print("치킨 당첨자 : {0}".format(winner[0]))
print("커피 당첨자 : {0}".format(winner[1:]))
print("-- 축하합니다 --")


# winner_coffee = sample(users, 3)
# print(winner_coffee);
# users = set(users)
# winner_coffee = set(winner_coffee)
# newUsers = users.difference(winner_coffee)
# winner_coffee = list(winner_coffee)
# winner_coffee.sort()

# print(newUsers)
# newUsers = list(newUsers)
# winner_chicken = sample(newUsers, 1)

# print("-- 당첨자 발표 --")
# print("치킨 당첨자 : {0}".format(winner_chicken))
# print("커피 당첨자 : {0}".format(winner_coffee))몰라
# print("-- 축하합니다 --")
'''


'''
제어문
### if
# weather = input("오늘 날씨는 어때요? ")
# if weather == "비" or weather == "눈" :
#     print("우산을 챙기세요")   
# elif weather == "미세먼지" :
#     print("마스크를 챙기세요")
# else :
#     print("준비물 필요 없어요")

temp = int(input("기온은 어때요?"))
if 30 <= temp :
    print("너무 더워요. 나가지 마세요")
elif 10 <= temp and temp < 30 :
    print("괜찮은 날씨에요")
elif 0 <= temp < 10 :
    print("외투를 챙기세요")
else :
    print("너무 추워요. 나가지 마세요")

    
### for
# for waiting_no in range(1, 6) :
#     print("대기번호 : {0}".format(waiting_no))  

starbucks = ["아이언맨", "토르", "아이엠 그루트"]

for customer in starbucks :
    print("{0}님, 커피가 준비되었습니다.".format(customer))

    
### while
# customer = "토르"
# index = 5

# while index >= 1 :
#     print("{0}님, 커피가 준비되었습니다. {1}번 남았어요.".format(customer, index))
#     index -= 1
#     if index == 0 :
#         print("커피는 폐기처분되었습니다.")

# customer = "아이언맨"
# index = 1
# while True :
#     print("{0}님, 커피가 준비되었습니다. {1}번째 호출입니다.".format(customer, index))
#     index += 1

customer = "토르"
person = "Unknown"

while person != customer :
    print("{0}님, 커피가 준비되었습니다.".format(customer))
    person = input("이름이 어떻게 되세요?")
    
while person == customer :
    print("{0}님, 커피가 준비되었습니다. 맛있게 드세요.".format(customer))
    person = "Unknown"

### continue 와 break
absent = [2, 5] # 결석
no_book = [7] # 책을 깜빡했음
for student in range(1, 11) : # 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
    if student in absent :
        continue # 다음 반복으로 넘어감
    elif student in no_book :
        print("오늘 수업 여기까지. {0}번은 교무실로 따라와".format(student))
        break # 반복문을 끝냄

    print("{0}번, 책을 읽어봐".format(student))

### 한 줄 for
# 출석번호가 1 2 3 4, 앞에 100을 붙이기로 함 -> 101, 102, 103, 104
# students = [1, 2, 3, 4, 5]
# print(students)
# students = [i+100 for i in students]
# print(students)

# 학생 이름을 길이로 변환
# students = ["Iron man", "Thor", "I am groot"]
# students = [len(i) for i in students]
# print(students)

# 학생 이름을 대문자로 변환
# students = ["Iron man", "Thor", "I am groot"]
# students = [i.upper() for i in students]
# students = [i.capitalize() for i in students]
# print(students)

# Quiz) 당신은 Cocoa 서비스를 이용하는 택시 기사님입니다.
# 50명의 승객과 매칭 기회가 있을 때, 총 탑승 승객 수를 구하는 프로그램을 작성하시오.

# 조건 1 : 승객별 운행 소요 시간은 5분 ~ 50분 사이의 난수로 정해집니다.
# 조건 2 : 당신은 소요 시간 5분 ~ 15분 사이의 승객만 매칭해야 합니다.

# (출력문 예제)
# [0] 1번째 손님 (소요시간 : 15분)
# [ ] 2번째 손님 (소요시간 : 50분)
# [0] 3번째 손님 (소요시간 : 5분)
# ...
# [ ] 50번째 손님 (소요시간 : 16분)

# 총 탑승 승객 : 2분
import random

cnt = 0;
chk = " "
for i in range(1, 51) :
    totTime = random.randrange(5, 51)
    if (5 <= totTime <= 15) :
        chk = "O"
        cnt += 1
    else :
        chk = " "

    print("[{2}] {0}번째 손님 (소요시간 : {1}분)".format(i, totTime, chk))

print("총 탑승 승객 : {0}분".format(cnt))
'''

'''
함수
### 함수    

def open_account() :
    print("새로운 계좌가 생성되었습니다.")

open_account()

### 전달값과 반환값
def open_account(balance) :
    print("새로운 계좌가 생성되었습니다. 잔액은 {0}원입니다.".format(balance))
    return balance

def deposit(balance, money) : # 입금
    print("입금이 완료되었습니다. 잔액은 {0}원입니다.".format(balance + money))
    return balance + money

def withdraw (balance, money) : # 출금
    if balance >= money : # 잔액이 출금보다 많으면
        print("출금이 완료되었습니다. 잔액은 {0}원입니다.".format(balance - money))
        return balance - money
    else :
        print("출금이 완료되지 않았습니다. 잔액은 {0}원입니다.".format(balance))
        return balance

def withdraw_night (balance, money) : # 저녁에 출금
    commission = 100 # 수수료 100원
    return commission, balance - money - commission 

def withdraw_night2 (balance, money) : # 저녁에 출금
    commission = 100 # 수수료 100원
    rtn = [commission, balance - money - commission]
    return rtn


balance = open_account(10000)
balance = deposit(balance, 1000) # 잔액 1000원 
balance = withdraw(balance, 500) # 잔액 500원

commission, balance = withdraw_night(balance, 500) # 잔액 -100원
print("수수료 {0}원이며, 잔액은 {1}원입니다.".format(commission, balance))

res = withdraw_night2(balance, 500) # 잔액 -700원
print("수수료 {0}원이며, 잔액은 {1}원입니다.".format(res[0], res[1]))


### 기본값
# def profile(name, age, main_lang) :
#     print("이름 : {0}\t나이 : {1}\t주 사용 언어 : {2}"\
#         .format(name, age, main_lang))
    
# profile("유재석", 20, "파이썬")
# profile("김태호", 25, "자바")

# 같은 학교 같은 학년 같은 반 같은 수업
def profile(name, age = 17, main_lang = "파이썬") :
    print("이름 : {0}\t나이 : {1}\t주 사용 언어 : {2}"\
        .format(name, age, main_lang))
    
profile("유재석", 20)
profile("김태호")


### 키워드값
def profile(name, age=17, main_lang="파이썬") :
    print(name, age, main_lang)

profile("유재석", main_lang = "파이썬")
profile("김태호", main_lang = "자바", age = 25)


### 가변인자
# def profile(name, age, lang1, lang2, lang3, lang4, lang5) :
#     print("이름 : {0}\t나이 : {1}\t".format(name, age), end=" ")
#     print(lang1, lang2, lang3, lang4, lang5)

def profile(name, age, *language) :
    print("이름 : {0}\t나이 : {1}\t".format(name, age), end=" ")
    for lang in language :
        print(lang, end=" ")
    print()

profile("유재석", 20, "Python", "Java", "C", "C++", "C#", "JavaScript")
profile("김태호", 25, "Kotlin", "Swift")


### 지역변수와 전역변수
gun = 10

def checkpoint(soldiers) : # 경계근무
    global gun # 전역 공간에 있는 gun 사용
    gun = gun - soldiers
    print("[함수 내] 남은 총 : {0}".format(gun))

def checkpoint_ret(gun, soldiers) :
    gun = gun - soldiers
    print("[함수 내] 남은 총 : {0}".format(gun))
    return gun

print("전체 총 : {0}".format(gun))
gun = checkpoint_ret(gun, 2)
print("남은 총 : {0}".format(gun))

# quiz) 표준 체중을 구하는 프로그램을 작성하시오

# * 표준 체중 : 각 개인의 키에 적당한 체중

# (성별에 따른 공식)
# 남자 : 키(m) x 키(m) x 22
# 여자 : 키(m) x 키(m) x 21

# 조건 1 : 표준 체중은 별도의 함수 내에서 계산
#         * 함수명 : std_weight
#         * 전달값 : 키(height), 성별(gender)
# 조건 2 : 표준 체중은 소수점 둘째자리까지 표시

# (출력 예제)
# 키 175cm 남자의 표준 체중은 67.38kg 입니다.

def std_weight(height, gender) :
    weight = (height/100)**2  
    if (gender == "남자") :
        weight = weight * 22
    else :
        weight = weight * 21

    print("키 {0}Cm {1}의 표준 체중은 {2}Kg 입니다.".format(height, gender, round(weight, 2)))
    

std_weight(175, "남자")
'''


'''
입출력

### 표준 입출력 

# import sys

# print("python", "java", "Javascript", sep=" VS ", end="?")
# print("무엇이 더 재밌을까요?")

# print("python", "java", file=sys.stdout) # 표준 출력
# print("python", "java", file=sys.stderr) # 표준 에러

# scores = {"수학" : 0, "영어" : 50, "코딩" : 100}
# for subject, score in scores.items() :
#     # print(subject, score)
#     print(subject.ljust(8), str(score).rjust(4), sep=":")
#     # 수학      :   0
#     # 영어      :  50
#     # 코딩      : 100

# for num in range(1, 21) :
#     print("대기번호 : " + str(num).zfill(3))
#     # 001, 002, 003, ...    

# answer = input("아무 값이나 입력하세요 : ")
answer = 10
print(type(answer))
# print("입력하신 값은 " + answer + "입니다.")


### 다양한 출력 포맷
# 빈 자리는 빈공간으로 두고, 오른쪽 정렬을 하되, 총 10자리 공간을 확보
print("{0: >10}".format(500))

# 양수일 땐 +로 표시, 음수일 땐 -로 표시
print("{0: >+10}".format(500))
print("{0: >+10}".format(-500))

# 왼쪽 정렬하고, 빈칸을 _로 채움
print("{0:_<+10}".format(500))

# 3자리 마다 콤마를 찍어주기
print("{0:,}".format(100000000000))

# 3자리 마다 콤마를 찍어주기, +- 부호도 붙이기
print("{0:+,}".format(100000000000))
print("{0:+,}".format(-100000000000))

# 3자리 마다 콤마를 찍어주기, +- 부호도 붙이기, 자릿수 확보하기
# 돈이 많으면 행복하니까 빈 자리는 ^ 로 채워주기
print("{0:^<+30,}".format(100000000000))

# 소수점 출력
print("{0:f}".format(5/3))
print("{0:.2f}".format(5/3))


### 파일 입출력
# score_file = open("score.txt", "w", encoding="utf8") # w : 쓰기용도
# print("수학 : 0", file=score_file)
# print("영어 : 50", file=score_file)
# score_file.close()

# score_file = open("score.txt", "a", encoding="utf8") # a : append
# score_file.write("과학 : 80")
# score_file.write("\n코딩 : 100")
# score_file.close()

# score_file = open("score.txt", "r", encoding="utf8") # r : 읽기
# print(score_file.read())
# score_file.close()

# score_file = open("score.txt", "r", encoding="utf8") # r : 읽기
# print(score_file.readline(), end="") # 줄별로 읽기, 한 줄 읽고 커서는 다음 줄로 이동
# print(score_file.readline(), end="")
# print(score_file.readline(), end="")
# print(score_file.readline(), end="")
# score_file.close()

# score_file = open("score.txt", "r", encoding="utf8") # r : 읽기
# while True :
#     line = score_file.readline()
#     if not line :
#         break
#     print(line, end="")
# score_file.close()

score_file = open("score.txt", "r", encoding="utf8") # r : 읽기
lines = score_file.readlines() # list 형태로 저장
for line in lines :
    print(line, end="")
score_file.close()


### pickle 
# pickle 사용하려면 항상 B(binary)를 붙여줘야 함
# 인코딩 설정은 필요 없음

import pickle
# profile_file = open("profile.pickle", "wb") # w : 쓰기, b : binary
# profile = {"이름" : "박명수", "나이" : 30, "취미" : ["축구", "골프", "코딩"]}
# print(profile)
# pickle.dump(profile, profile_file) # profile 에 있는 정보를 file 에 저장
# profile_file.close()

profile_file = open("profile.pickle", "rb") # r : 읽기, b : binary
profile = pickle.load(profile_file) # file 에 있는 정보를 profile 에 불러오기
print(profile)
profile_file.close()


### with
import pickle

# with open("profile.pickle", "rb") as profile_file :
#     print(pickle.load(profile_file))

# with open("study.txt", "w", encoding="utf8") as study_file :
#     study_file.write("파이썬을 열심히 공부하고 있어요.")

with open("study.txt", "r", encoding="utf8") as study_file :
    print(study_file.read())

# quiz) 당신의 회사에서는 매주 1회 작성해야 하는 보고서가 있습니다.
# 보고서는 항상 아래와 같은 형태로 출력되어야 합니다.

# - X 주차 주간보고 -
# 부서 :
# 이름 :
# 업무 요약 :

# 1주차부터 50주차까지의 보고서 파일을 만드는 프로그램을 작성하시오.

# 조건 : 파일명은 '1주차.txt', '2주차.txt', ... 와 같이 만듭니다.

def report(week) :
    with open("{0}주차.txt".format(week), "w", encoding="utf8") as report_file :
        report_file.write("- {0}주차 주간보고 -".format(week))
        report_file.write("\n부서 : ")
        report_file.write("\n이름 : ")
        report_file.write("\n업무 요약 : ")

for i in range(1, 51) :
    report(i)
'''

'''
클래스 
### 클래스
# # 마린 : 공격 유닛, 군인. 총을 쏠 수 있음
# name = "마린" # 유닛의 이름
# hp = 40 # 유닛의 체력
# damage = 5 # 유닛의 공격력

# print("{0} 유닛이 생성되었습니다.".format(name))
# print("체력 {0}, 공격력 {1}\n".format(hp, damage))

# # 탱크 : 공격 유닛, 탱크. 포를 쏠 수 있는데, 일반 모드 / 시즈 모드
# tank_name = "탱크"
# tank_hp = 150
# tank_damage = 35

# print("{0} 유닛이 생성되었습니다.".format(tank_name))
# print("체력 {0}, 공격력 {1}\n".format(tank_hp, tank_damage))

# tank2_name = "탱크"
# tank2_hp = 150
# tank2_damage = 35

# def attack(name, location, damage) :
#     print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]".format(name, location, damage))  

# attack(name, "1시", damage)
# attack(tank_name, "1시", tank_damage)
# attack(tank2_name, "1시", tank2_damage)

class Unit :
    def __init__(self, name, hp, damage) :
        self.name = name
        self.hp = hp
        self.damage = damage
        print("{0} 유닛이 생성되었습니다.".format(self.name))
        print("체력 {0}, 공격력 {1}\n".format(self.hp, self.damage))

marine1 = Unit("마린", 40, 5)
marine2 = Unit("마린", 40, 5)
tank = Unit("탱크", 150, 35)

### __init__


### 멤버 변수
'''
class Unit :
    def __init__(self, name, hp, damage) :
        self.name = name
        self.hp = hp
        self.damage = damage
        print("{0} 유닛이 생성되었습니다.".format(self.name))
        print("체력 {0}, 공격력 {1}\n".format(self.hp, self.damage))

# marine1 = Unit("마린", 40, 5)
# marine2 = Unit("마린", 40, 5)
# tank = Unit("탱크", 150, 35)

wraith1 = Unit("레이스", 80, 5)
print("유닛 이름 : {0}, 공격력 : {1}".format(wraith1.name, wraith1.damage))

# 마인드 컨트롤 : 상대방 유닛을 내 것으로 만드는 것 (빼앗음)
wraith2 = Unit("빼앗은 레이스", 80, 5)
wraith2.clocking = True # 외부에서 변수 추가 가능

if wraith2.clocking == True :
    print("{0} 는 현재 클로킹 상태입니다.".format(wraith2.name))
    

pri