import random
for l in range(1000):
    number_of_players = 100
    players = [0] * 101

    for i in range(0,101):
        players[i] = random.randint(1,100)

    check_false = False
    for i in range(1,101):
        check = 0
        for x in range(1,101):
            if (i == x):
                continue
            check += players[x]
        #print("player = {}, total = {}".format(i, check))

        check = check % 100

        #print("player = {}, moduled = {}".format(i, check))

        if (check >= i):
            check = (100 + i) - check
        else:
            check = i - check

        print("player = {}, completed = {}".format(i, check))

        if (check == players[i]):
            print("Good job player number {} -- given number {}\n \n".format(i, players[i]))
            check_false = True
            break;

    if (check_false == False):
        print("NAH")
        break;
