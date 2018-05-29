'''
2018.05.29.화 -우승미-
pro04.
다음 문자열을 모든 대문자를 소문자로 변환하고,
문자 콤마(,) 점(.) \n을 없앤 후에 각 단어를
카운트 수와 함께 오름차순으로 출력하세요.
'''

import re

str = {}

s = """We encourage everyone to contribute to Python. If you still have questions after reviewing the material
in this guide, then the Python Mentors group is available to help guide new 
contributors through the process."""

#모든 대문자를 소문자로 변환
s = s.lower()
#print(ss)

#문장의 , / . / \n 제거
s = s.replace(",","")
s = s.replace(".","")
s = s.replace("\n","")

#print(s)

#공백 기준으로 단어 자르기
list_s = s.split(" ")
#print(list_s)

#list_s를 dic str에 넣기
#중복된 단어 +1 , 하나인 단어는 1
for i in list_s :
    if i in str :
        str[i] += 1
    else :
        str[i] = 1

#print(str)

#알파벳 오름차순으로 정렬하기
sort_list = sorted(str)

for i in sorted(str) :
    print(i.upper(), ":", str[i])

