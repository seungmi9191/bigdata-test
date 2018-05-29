'''
2018.05.29.화 -우승미-
pro01.
아래와 같이 은행 프로그램을 작성하세요.

1. "예금" 선택 후 금액을 입력하면 예금액이 합산됩니다.
2. "출금" 선택 후 금액을 입력하면 예금액이 차감됩니다.
3. "잔고" 선택 시 현재 잔고가 출력됩니다.
4. "종료" 선택 시 종료됩니다.
"1,2,3,4" 이외의 숫자 입력 시 "다시 입력해주세요" 메세지가 출력됩니다.
'''


#변수 초기화
num = 0 #번호선택
cash = 0 #입력액
sumcash = 0 #총 금액
balance = 0 #잔고

while True :
    print("-"*30)
    print("1.예금 | 2.출금 | 3.잔고 | 4.종료")
    print("-"*30)

    #사용자에게 입력금액 받음
    num = int(input("선택> "))

    #예금액
    if num == 1 :
        cash = int(input("예금액> "))
        sumcash += cash #sumcash = sumcash+cash

    elif num == 2 :
        cash = int(input("출금액> "))
        sumcash -= cash #sumcash = sumcash-cash

    elif num == 3 :
        balance = sumcash #sumcash를 balance에 담음
        print("잔고액> ", balance)

    elif num == 4 :
        print("프로그램 종료")
        break

    else :
        print("다시 입력해주세요.")