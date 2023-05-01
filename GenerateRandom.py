import random

def gen_random():
    result = []
    num = [0,1,2,3,4,5,6,7,8,9]
    for i in range(4):
        rand = random.randrange(0, len(num))
        result.append(num[rand])
        num.remove(num[rand])
    return result

print(gen_random())
