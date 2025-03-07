import random

# Spēles sākumā spēles programmatūra gadījuma ceļā saģenerē 5 skaitļus diapazonā no 10000 līdz 20000, 
# bet tādus, kas sākotnēji dalās gan ar 3, gan ar 2.  

start = []
for i in range(5):
    start.append(6*random.randint(1667, 3333))

for i in range(len(start)):
    print(f"Sakuma skaitlis {i+1} = {start[i]}")

num = start[int(input())-1] # Cilvēks-spēlētājs izvēlas, ar kuru no saģenerētajiem skaitļiem viņš vēlas sākt spēli.
print(num)

#

class algorythm:
    def __init__(self, num):
        self.num = num
        # self.root = tree(gameNode(num, 0, 0, "0", None, None))
        # building a tree
        

    def find(number):
        print("aaa")    


class gameNode:
    def __init__(self, number, p1, p2, nextTurn, left, right):      # p1 = player, p2 = computer
        self.number = number                                        # p1 | num | p2
        self.p1 = p1                                                #  0 | 999 | 0
        self.p2 = p2                                                
        self.nextTurn = nextTurn    
        self.left = left                                           
        self.right = right                                       

# Game
alg = algorythm(num)

root = gameNode(num, 0, 0, "player", None, None)

current = root
while(current.number > 10):        
    if(current.nextTurn == "player"):
        print(f"Number = {current.number}")
        print("Select 2 or 3 :")        # dalitajs
        dal = input()
        #if(num % dal != 0):             # Ceru ka nevajag apstradat kludas
        match dal:
            case "2": 
                current.number/=2
                current.left = gameNode(current.number, current.p1, current.p2+2, "computer", None, None)
                current = current.left
            case "3":
                current.number/=3
                current.right = gameNode(current.number, current.p1, current.p2+3, "computer", None, None)
                current = current.right
    else:
        # computer to answer
        # alg.find(current.number)
        #
        #
        # TEST CASE

        if(current.number % 2 == 0):
            current.number/=2
            current.left = gameNode(current.number, current.p1+2, current.p2, "player", None, None)
            current = current.left
        else:
            current.number/=3
            current.right = gameNode(current.number, current.p1+2, current.p2, "player", None, None)
            current = current.right
