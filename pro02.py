'''
2018.05.29.화 -우승미-
pro02.
5개의 숫자를 키보드로 입력받아 평균을 구하는 프로그램을 작성하세요.
숫자는 콤마(,)로 구분하여 입력합니다.
'''

#숫자 입력받음
num = input("숫자 5개를 ,로 구분하여 입력하세요: ")
#print(num, type(num))

#평균을 담을 변수 초기화
sum = 0

#입력받은 문자열을 ,로 자르기
number = num.split(",")
#print(number)

#split는 문자열을 자르면 list를 반환한다.
#list는 str형이므로 int로 형변환
for i in number :
    sum += int(i)

#후에 number의 값이 가변적으로 변할 것을 대비하여 len메소드로 number의 길이를 지정해줌
avg = sum/len(number)

print("평균은 %3.1f 입니다." % avg)