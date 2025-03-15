import random


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

ERR_WRNG_INPUT = "Ludzu ievadiet pareizu ciparu"
ALGORITMA_IZVELE = """Ludzu, izvelaties datora algoritmu
MinMaks: 1
Alfa-Beta: 2"""

# Game
def main():
    # speles uzsaksana
    num, ai_algorythm = startGame()
    
    alg = Algorythm(num)
    root = gameNode(num, 0, 0, "player", None, None)  
    current = root


    while(current.number > 10 and (current.number % 2 == 0 or current.number % 3 == 0)):    # >10 , nevar sadalit ar 2 vai 3 
        print(f"Next turn : {current.nextTurn}")
        print(f"Number = {current.number}")
        
        
        dal = 0
        while (True):
            try:
                print("Izvēlaties dalītāju: ", end="")
                dal = int(input())
                
                if (dal == 2 or dal == 3):
                    if (current.number % dal == 0):
                        break
                else:
                    print(ERR_WRNG_INPUT)
            
            except ValueError:
                continue

        current.number//=dal # samazina skaitli ar dalitaju

        if(current.nextTurn == "player"):           # kas speles saja gajiena
            match dal:
                case 2:                                                                               # skaitlis dalas ar 2
                    current.left = gameNode(current.number, current.p1, current.p2+dal, "computer", None, None)           # jauns mezgls nakamajam gajienam
                    current = current.left                                                                              # nakamais gajiens
                case 3:
                    current.right = gameNode(current.number, current.p1+dal, current.p2, "computer", None, None)          # goes right
                    current = current.right

        else:
            match dal:
                case 2: 
                    current.left = gameNode(current.number, current.p1+dal, current.p2, "player", None, None)
                    current = current.left
                case 3:
                    current.right = gameNode(current.number, current.p1, current.p2+dal, "player", None, None)
                    current = current.right
        

    print("---END---")
    print("Numurs ir mazaks par 10 vai to nevar dalit ar 2 vai 3")
    print(f"Speletaja punkti : {current.p1}")
    print(f"Datora punkti : {current.p2}")


# Spēles sākumā spēles programmatūra gadījuma ceļā saģenerē 5 skaitļus diapazonā no 10000 līdz 20000, 
# bet tādus, kas sākotnēji dalās gan ar 3, gan ar 2.  
def startGame():
    start = []

    # izveido 5 ciparus kuri dalas ar 3 un 2
    for i in range(5):
        start.append(6*random.randint(1667, 3333))

    for i in range(len(start)):
        print(f"Sakuma skaitlis {i+1} = {start[i]}")

    # Cilvēks-spēlētājs izvēlas, ar kuru no saģenerētajiem skaitļiem viņš vēlas sākt spēli.    
    num = 0
    ai_algorythm = 0
    while (True):
        try:
            print("Izvēlaties skaitli: ", end="")
            izvele = int(input())
            
            if (izvele > 0 and izvele < 6):
                num = start[izvele-1] 
                break
            else:
                print(ERR_WRNG_INPUT)
        except ValueError:
            continue

    
    print(ALGORITMA_IZVELE)
    while (True):
        try:
            izvele = int(input())
            
            if (izvele == 1 or izvele == 2):
                ai_algorythm = izvele
                break
            else:
                print(ERR_WRNG_INPUT)
        except ValueError:
            continue

    return num, ai_algorythm



main()
