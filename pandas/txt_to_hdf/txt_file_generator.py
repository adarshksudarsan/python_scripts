import random
for i in range (0,5):
    randomlist = random.sample(range(1, 99), 50)
    print(randomlist)
    print(type(randomlist))
    with open(str(i)+'.txt', 'w') as f:
        for item in randomlist:
            f.write("%s" % item)
            f.write(",")
        f.write("1") 
for i in range (5,10):
    randomlist = random.sample(range(1, 99), 50)
    print(randomlist)
    print(type(randomlist))
    with open(str(i)+'.txt', 'w') as f:
        for item in randomlist:
            f.write("%s" % item)
            f.write(",")
        f.write("0") 
