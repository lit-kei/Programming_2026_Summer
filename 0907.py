#(5)
okane = 1000
choco = 20
gum = 15
max = 0
min = okane // choco
max_c = max_g = min_c = min_g = 0

for c in range(okane // choco + 1):
  nokori = okane - choco * c
  g = nokori // gum
  p = c * choco + g * gum
  if p != okane: continue
  sum_tmp = c + g
  if max < sum_tmp:
    max = sum_tmp
    max_c = c
    max_g = g
  dif_tmp = abs(c - g)
  if min > dif_tmp:
    min = dif_tmp
    min_c = c
    min_g = g

print(f"和が最大　チョコ：{max_c}、ガム：{max_g}")
print(f"差が最小　チョコ：{min_c}、ガム：{min_g}")
