import random


class gameNode:
    def __init__(self, number, p1, p2, nextTurn, left, right, staticValue, dynamicValue):      # p1 = player, p2 = computer
        self.number = number                                        # p1 | num | p2
        self.p1 = p1                                                #  0 | 999 | 0
        self.p2 = p2                                                
        self.nextTurn = nextTurn    
        self.left = left                                           
        self.right = right
        self.staticValue = staticValue
        self.dynamicValue = dynamicValue



class gameTree:
    def __init__(self, number):
        self.root = self.build(gameNode(number, 0, 0, "player", None, None, 0, -3621), 1)
        self.print_tree(self.root)
    

    def build(self, node, num):
        gameList = ["player","computer"]
                # ja bus svarigi
        nt = gameList[num]
        if (num == 0):
            num = 1
            if(node.number % 2 == 0):
                staticValue = node.p1 - node.p2 + 0
                node.left = gameNode(node.number//2, node.p1+2, node.p2, nt, None, None, staticValue, -3621)
                self.build(node.left, num)

            if(node.number % 3 == 0):
                staticValue = node.p1 - node.p2 + 1
                node.right = gameNode(node.number//3, node.p1, node.p2+3, nt, None, None, staticValue, -3621)
                self.build(node.right, num)
        else:
            num = 0
            if(node.number % 2 == 0):
                staticValue = node.p1 - node.p2 + 0
                node.left = gameNode(node.number//2, node.p1, node.p2+2, nt, None, None, staticValue, -3621)
                self.build(node.left, num)

            if(node.number % 3 == 0):
                staticValue = node.p1 - node.p2 + 1
                node.right = gameNode(node.number//3, node.p1+3, node.p2, nt, None, None, staticValue, -3621)
                self.build(node.right, num)
            
        return node
    

    # --- CHAT GPT
    def print_tree(self, node, level=0): 
        if node is not None:
            self.print_tree(node.right, level + 1)
            print(' ' * 4 * level + '->', node.number, node.nextTurn, node.p1, node.p2)
            self.print_tree(node.left, level + 1)
     # --- CHAT GPT

ERR_WRNG_INPUT = "Ludzu ievadiet pareizu ciparu"


# Game
def main():
    # speles uzsaksana
    num, ai_algorythm, isPlayerComputer = startGame()
    
    alg = gameTree(num)
    root = gameNode(num, 0, 0, "player", None, None, 0, -3621)  
    current = alg.root
    print(alg.root)
    print(current.number)

    
    

    while(current.number > 10 and (current.number % 2 == 0 or current.number % 3 == 0)):    # >10 , nevar sadalit ar 2 vai 3 
        print(f"Next turn : {current.nextTurn}")
        print(f"Number = {current.number}")
        
        dal = 0

        if (current.nextTurn == "computer"):
            if (ai_algorythm == 1):
                minimax(current, 4, False)
            else:
                alphaBeta(current, 4, False, -10000, 10000)


            try:
                if (current.left.dynamicValue != -3621):
                    if (current.dynamicValue == current.left.dynamicValue):
                        dal = 2
            except Exception as err:
                print(err)

            try:
                if (current.right.dynamicValue != -3621):
                    if (current.dynamicValue == current.right.dynamicValue):
                        dal = 3
            except Exception as err:
                print(err)

        else:
            if (not isPlayerComputer):
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
            
            else:
                if (ai_algorythm == 1):
                    minimax(current, 4, True)
                else:
                    alphaBeta(current, 4, True, -10000, 10000)
            
                try:
                    if (current.left.dynamicValue != -3621):
                        if (current.dynamicValue == current.left.dynamicValue):
                            dal = 2
                except Exception as err:
                    print(err)

                try:
                    if (current.right.dynamicValue != -3621):
                        if (current.dynamicValue == current.right.dynamicValue):
                            dal = 3
                except Exception as err:
                    print(err)


        
        current.number//=dal # samazina skaitli ar dalitaju
        match dal:
            case 2:                                                                               # skaitlis dalas ar 2
                current = current.left                                                                              # nakamais gajiens
            case 3:
                current = current.right


        print(f"Speletaja punkti : {current.p1}")
        print(f"Datora punkti : {current.p2}")

        

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
                #num = 19440#test
                #num = 13014#test2
                break
            else:
                print(ERR_WRNG_INPUT)
        except ValueError:
            continue

    
    print("""Ludzu, izvelaties datora algoritmu
MinMaks: 1
Alfa-Beta: 2""")
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

    print("""Cilveks pret Datoru: 1
Dators pret Datoru: 2""")
    while (True):
        try:
            izvele = int(input())
            
            if (izvele == 1 or izvele == 2):
                isPlayerComputer = izvele-1
                break
            else:
                print(ERR_WRNG_INPUT)
        except ValueError:
            continue

    return num, ai_algorythm, isPlayerComputer


# Nemts no interneta video
def minimax(node, depth, isMaximisingPlayer):
    if (depth == 0 or ((node.left == None and node.right == None))):
        node.dynamicValue = node.staticValue
        return node.staticValue
    
    if isMaximisingPlayer:
        maxEval = -10000
        if (node.left != None):
            eval = minimax(node.left, depth - 1, False)
            maxEval = max(maxEval, eval)
        
        if (node.right != None):
            eval = minimax(node.right, depth - 1, False)
            maxEval = max(maxEval, eval)
        node.dynamicValue = maxEval
        return maxEval
    
    else:
        minEval = 10000
        if (node.left != None):
            eval = minimax(node.left, depth - 1, True)
            minEval = min(minEval, eval)
        
        if (node.right != None):
            eval = minimax(node.right, depth - 1, True)
            minEval = min(minEval, eval)
        node.dynamicValue = minEval
        return minEval
    

def alphaBeta(node, depth, isMaximisingPlayer, alpha, beta):
    if (depth == 0 or ((node.left == None and node.right == None))):
            node.dynamicValue = node.staticValue
            return node.staticValue
        
    if isMaximisingPlayer:
        maxEval = -10000
        if (node.left != None):
            eval = alphaBeta(node.left, depth - 1, False, alpha, beta)
            maxEval = max(maxEval, eval)
            beta = max(beta, eval)
        
        if (not(beta <= alpha)):
            if (node.right != None):
                eval = alphaBeta(node.right, depth - 1, False, alpha, beta)
                maxEval = max(maxEval, eval)
        
        node.dynamicValue = maxEval
        return maxEval
    
    else:
        minEval = 10000
        if (node.left != None):
            eval = alphaBeta(node.left, depth - 1, True, alpha, beta)
            minEval = min(minEval, eval)
            beta = min(beta, eval)
        
        if (not(beta <= alpha)):
            if (node.right != None):
                eval = alphaBeta(node.right, depth - 1, True, alpha, beta)
                minEval = min(minEval, eval)
        
        node.dynamicValue = minEval
        return minEval


# Pievienotā GameEngine klase, lai varam apvienot loģiku ar GUI

# komentari šim un gui ir ģenerēti :)


class GameEngine:
    def __init__(self, start_number, algorithm=1, player_vs_ai=True):
        # Inicializē spēles dzinēju ar sākuma skaitli, algoritma izvēli un spēles režīmu (cilvēks pret datoru)
        # algorithm: 1 = minimax, 2 = alphaBeta
        self.tree = gameTree(start_number)  # Izveido spēles koku, izmantojot start_number kā sākuma vērtību
        self.current = self.tree.root       # Saglabā sākuma stāvokli no koka saknes
        self.player_vs_ai = player_vs_ai    # Saglabā informāciju par to, vai spēle ir cilvēks pret datoru
        self.algorithm = algorithm          # Saglabā izvēlēto algoritmu (1 vai 2)    

    def get_state(self):
        # Atgriež pašreizējo spēles stāvokli kā vārdnīcu, ko var izmantot GUI interfeisā
        return {
            "number": self.current.number,           # Pašreizējais skaitlis
            "player_score": self.current.p1,         # Spēlētāja punkti
            "computer_score": self.current.p2,       # Datora punkti
            "turn": self.current.nextTurn            # Kurš veic nākamo gājienu ("player" vai "computer")
        }

    def is_game_over(self):
        # Pārbauda, vai spēle ir beigusies:
        # Spēle beidzas, ja pašreizējais skaitlis ir mazāks vai vienāds ar 10 vai ja skaitli vairs nevar dalīt ar 2 vai 3.
        return self.current.number <= 10 or (self.current.number % 2 != 0 and self.current.number % 3 != 0)

    def make_player_move(self, divisor):
        
        # Veic spēlētāja gājienu, ja tas ir atļauts:
        # Pārbauda, vai nākamais gājiens ir spēlētājam un vai pašreizējais skaitlis dalās ar norādīto divisor (2 vai 3).
        if self.current.nextTurn == "player" and self.current.number % divisor == 0 :
            self.current.number //= divisor  # Dalās ar divisor, atjaunojot skaitli
            # Pāriet uz atbilstošo apakšmezglu (koka mezglu) atkarībā no izvēlētā dalītāja
            if divisor == 2 and self.current.left is not None:
                self.current = self.current.left
            elif divisor == 3 and self.current.right is not None:
                self.current = self.current.right
            return True  # Gājiens veiksmīgi izpildīts
      
        return False  # Ja nosacījumi netiek izpildīti, gājiens nav veiksmīgs

    def make_ai_move(self):
        # Veic datora (AI) gājienu, ja nākamais gājiens ir datoram
        #if self.current.nextTurn == "computer":
            # Izvēlas algoritmu atkarībā no izvēles (1 = minimax, 2 = alphaBeta)
        isMaximising = False
        if self.current.nextTurn == "computer":
            isMaximising = False
        else:
            isMaximising = True

        if self.algorithm == 1:
            minimax(self.current, 4, isMaximising)  # Izsauc minimax algoritmu ar dziļumu 4
        else:
            alphaBeta(self.current, 4, isMaximising, -10000, 10000)  # Izsauc alphaBeta algoritmu ar dziļumu 4 un sākotnējiem alpha, beta vērtībām
        
        # Pārbauda, kurš apakšmezgls atbilst aprēķinātajam vērtējumam:
        # Ja kreisais (dalīšana ar 2) apakšmezgls ir derīgs un tā dinamiskā vērtība sakrīt ar pašreizējo, tad veic gājienu
        if self.current.left is not None and self.current.left.dynamicValue == self.current.dynamicValue:
            self.current.number //= 2
            self.current = self.current.left
        # Pretējā gadījumā, ja labo (dalīšana ar 3) apakšmezgls atbilst, tad veic gājienu
        elif self.current.right is not None and self.current.right.dynamicValue == self.current.dynamicValue:
            self.current.number //= 3
            self.current = self.current.right
        
if __name__ == '__main__':
    main()
