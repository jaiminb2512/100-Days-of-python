while True:
    import random
    
    a = input("Enter your choice : ")
    game = ["Snake", "snake","Water","water","Gun", "gun"]

    if a == game[0] or a == game[1]:
        a = 1
    elif a== game[2] or a == game[3]:
        a = 2
    elif a == game[4] or a==game[5]:
        a = 3

    lst = [1,2,3]
    c = int(random.choice(lst))

    if a == c:
        print("Mathch draw")
        
    elif a==1 and c==2:
        print("You Win")

    elif a==1 and c==3:
        print("You loss")
        
    elif a==2 and c==1:
        print("You Loss")
        
    elif a==2 and c==3:
        print("You win")
        
    elif a==3 and c==1:
        print("You Win")
        
    elif a==3 and c==2:
        print("You Loss")
        
    else :
        print("Invalid input")

    if c == lst[0]:
        c = game[0]
    elif c == lst[1]:
        c = game[2]
    else :
        c = game[2]

    if a == lst[0]:
        a = game[0]
    elif a == lst[1]:
        a = game[2]
    else:
        a = game[4]
    print(f"Computer choose {c} and you choose {a}")