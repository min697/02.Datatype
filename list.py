minsang = ["박민상", "27", "010-9170-****"]
name = minsang[0]
age = minsang[1]
phone = minsang[2]

print(type(minsang))
print(name, age, phone)

names = [['강수경', '강혜나', '김민석'], ['20', '21', '22'], ['010-4643-3172', '010-8422-5473','010-6573-6413']]
#데이터는 9개지만 요소는 3개
print(names[0][0:2])

numbers=[1,2,3,4,5]
result = numbers[2] + numbers[-1]
print(result)

print(len(names[0]))

#리스트에 요소 추가하기
last = [1,2,3]
last.append(30)
print(last)
#빈리스트에 추가하고 싶을 때 이렇게 쓰면 됨
last = [1,2,3]
last.remove(3)
print(last)
print(type(last))




# 안전공학계산기 만들기 과제 있음(주제 선정 필요)
# 만들고 보고서도 만들어야 된다.


