#１　基礎的な技術
count = 0
total = 0

for i in range(1, 1001):
  if i % 7 == 0:
    count += 1
    total += i
print("合計:", total, "平均:", total/count)



#２　元号判定
import random as rnd
ad_year = rnd.randint(1926,2027) #1926～2027の乱数を発生

print(f"{ad_year}年")

if ad_year < 1989:
  print("昭和")
elif ad_year < 2019:
  print("平成")
else:
  print("令和")



#３ 令和年の変換
import random as rnd
ad_year=rnd.randint(2019,2027)

print(f"西暦{ad_year}年は令和{ad_year - 2018}年です")
