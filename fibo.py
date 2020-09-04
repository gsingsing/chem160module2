Prev2 = 0
Prev1 = 1
for i in range(20):
    current = Prev2+Prev1
    print(current)
    Prev2, Prev1 = Prev1, current