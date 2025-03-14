import random

# Spēles sākumā spēles programmatūra gadījuma ceļā saģenerē 5 skaitļus diapazonā no 10000 līdz 20000, 
# bet tādus, kas sākotnēji dalās gan ar 3, gan ar 2.  

start = []
for i in range(5):
    start.append(6*random.randint(1667, 3333))

for i in range(len(start)):
    print(f"Sakuma skaitlis {i+1} = {start[i]}")

num = start[int(input("Kads skaitlis ? : "))-1] # Cilvēks-spēlētājs izvēlas, ar kuru no saģenerētajiem skaitļiem viņš vēlas sākt spēli.
#


class gameNode:
    def __init__(self, number, p1, p2, nextTurn, left, right):      # p1 = player, p2 = computer
        self.number = number                                        # p1 | num | p2
        self.p1 = p1                                                #  0 | 999 | 0
        self.p2 = p2                                                
        self.nextTurn = nextTurn    
        self.left = left                                           
        self.right = right                                       


class Algorythm:
    def __init__(self, number):
        self.root = self.build(gameNode(number, 0, 0, "player", None, None))
        self.print_tree(self.root)
        
    def build(self, node):
        nt = "computer"        # ja bus svarigi
        if(node.number % 2 == 0):
            node.left = gameNode(node.number//2, node.p1, node.p2, nt, None, None)
            self.build(node.left)
        if(node.number % 3 == 0):
            node.right = gameNode(node.number//3, node.p1, node.p2, nt, None, None)
            self.build(node.right)
        return node
    

    # --- CHAT GPT
    def print_tree(self, node, level=0): 
        if node is not None:
            self.print_tree(node.right, level + 1)
            print(' ' * 4 * level + '->', node.number)
            self.print_tree(node.left, level + 1)
     # --- CHAT GPT

# Game
alg = Algorythm(num)

root = gameNode(num, 0, 0, "player", None, None)  

current = root
while(current.number > 10 and (current.number % 2 == 0 or current.number % 3 == 0)):    # >10 , nevar sadalit ar 2 vai 3 
    print(f"Next turn : {current.nextTurn}")
    if(current.nextTurn == "player"):           # kas speles saja gajiena
        print(f"Number = {current.number}")     
        dal = input("Select 2 or 3 : ")         # dalitajs
        #if(num % dal != 0):                    # Ceru ka nevajag apstradat kludas
        match dal:
            case "2": 
                current.number//=2                                                                                  # skaitlis dalas ar 2
                current.left = gameNode(current.number, current.p1, current.p2+2, "computer", None, None)           # jauns mezgls nakamajam gajienam
                current = current.left                                                                              # nakamais gajiens
            case "3":
                current.number//=3
                current.right = gameNode(current.number, current.p1+3, current.p2, "computer", None, None)          # goes right
                current = current.right
    else:

        # computer to answer
        # !

        print(f"Number = {current.number}")
        dal = input("Select 2 or 3 : ")
        match dal:
            case "2": 
                current.number//=2
                current.left = gameNode(current.number, current.p1+2, current.p2, "player", None, None)
                current = current.left
            case "3":
                current.number//=3
                current.right = gameNode(current.number, current.p1, current.p2+3, "player", None, None)
                current = current.right


print("---END---")
print("Numurs ir mazaks par 10 vai to nevar dalit ar 2 vai 3")
print(f"Speletaja punkti : {current.p1}")
print(f"Datora punkti : {current.p2}")

