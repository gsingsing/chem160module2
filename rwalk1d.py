from random import choice
trials = 10000
steps = 100000
gothome = 0
for i in range(trials):
    point = 0
    for step in range(steps):
        point+=choice((-1,1))
        if point==0:
            gothome+=1
            break
print("fraction that got home=", gothome/trials)