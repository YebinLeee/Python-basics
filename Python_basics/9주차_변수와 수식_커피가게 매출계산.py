americano_price = 2500
caffelatte_price = 3300
caffucino_price = 3500

x = int(input("아메리카노 판매 개수: "))
y = int(input("카푸라떼 판매 개수: "))
z = int(input("카푸치노 판매 개수: "))
sum = x*americano_price + y*caffelatte_price + z*caffucino_price

sales = americano_price*x
sales = sales + caffelatte_price*y
sales = sales + caffucino_price*z

print(" 총 매출은", sum, "입니다.")
print(" 총 매출은", sales, "입니다.")
