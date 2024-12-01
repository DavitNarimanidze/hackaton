# 15 აიღეთ რაიმე list'ი და დათვლეთ მასში მოცემული რიცხვების საშუალო არითმეტიკული.												

listn = [1, 4, 6, 8, 10]
middle = 0
for i in listn:
    middle += i
print(middle / len(listn))