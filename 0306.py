# 1-15 取8個亂數不重複整數
import random
loto = []

for i in range(0, 8):
    result = random.randint(1, 15)
    while result in loto:
        result = random.randint(1, 15)
    loto.append(result)

print(loto)
