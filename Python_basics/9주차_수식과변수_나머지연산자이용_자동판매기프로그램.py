#사용자로부터 투입한돈과 물건 값을 입력받는다.

get_money = int(input("투입한 돈: "))
price = int(input("물건값: "))
remainder = get_money - price
print("거스름돈:", remainder)
coin500 = remainder // 500 # 500원의 동전은 500으로 나눈 몫
coin100 = (remainder%500) // 100 # 100원의 동전은 500원으로 나눈 나머지를 100으로 나눈 몫
print("500원 동전의 개수: ", coin500)
print("100원 동전의 개수: ", coin100) 
