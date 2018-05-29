'''
2018.05.29.화 -우승미-
pro03.
set을 사용하여 1~45까지의 숫자 중 임의의 6개의
숫자를 콤마(,)로 구분하여 출력하세요.
'''

#random 함수
import random

numbers = []

#1~45까지 반복
for num in range(1,46) :
    numbers.append(num) #numbers 리스트 안에 num(1~45) 넣어줌

#print(numbers)

#리스트를 set으로 변경 → set에서 random을 이용하여 6개의 숫자 출력
setNumbers = set(random.sample(numbers, 6))
print(setNumbers)

'''
#샘플링(sample)
random 모듈에서 유용한 기능은 리스트, set, 튜플 등과 같은 컬렉션으로부터 일부를 샘플링해서 뽑아내는 기능이다.
random 모듈에서 smaple(컬렉션, 샘플수) 함수는 지정된 컬렉션으로부터 샘플수만큼 랜덤 추출을 하는 함수다.
'''